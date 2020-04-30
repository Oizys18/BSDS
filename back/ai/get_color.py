from firebase import firebase
import json
import json
import numpy as np
import json
from random import randint
import numpy as np
import tensorflow as tf
import os


# Get Data
db = firebase.FirebaseApplication(
    "https://color-classification.firebaseio.com", None)
jsonData = db.get("/colors", None)
data = []

for user in jsonData.keys():
    entry = {}
    entry['r'] = jsonData[user]['r']
    entry['g'] = jsonData[user]['g']
    entry['b'] = jsonData[user]['b']
    entry['label'] = jsonData[user]['label']
    data.append(entry)

json.dump({"data": data}, open("data.json", "w"))


# 데이터 전처리
data = json.load(open("data.json"))['data']
cols = []
lbls = []
labelsValues = [
    "red-ish",
    "green-ish",
    "blue-ish",
    "orange-ish",
    "yellow-ish",
    "pink-ish",
    "purple-ish",
    "brown-ish",
    "grey-ish"
]
for submission in data:
    color = []
    color.append(submission["r"] / 255)
    color.append(submission["g"] / 255)
    color.append(submission["b"] / 255)
    cols.append(color)
    lbls.append(labelsValues.index(submission["label"]))

colors = np.array(cols, dtype=np.float32)
labels = np.array(lbls, dtype=np.uint8)
np.savez_compressed("processedData", colors=colors, labels=labels)


# train
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


colors = None
labels = None
data_size = 0


with tf.device("/cpu:0"):
    with np.load("processedData.npz") as savedData:
        colors = np.array(savedData['colors'], dtype=np.float32)
        labels = tf.one_hot(savedData['labels'], 9, dtype=tf.uint8).numpy()
        data_size = len(savedData['colors'])


train_size = int(data_size*0.8)
test_size = validation_size = int((data_size - train_size)/2)

indexes = [randint(0, data_size-1) for i in range(train_size)]
colors_train = tf.constant([colors[i] for i in indexes])
labels_train = tf.constant([labels[i] for i in indexes])
test_indexes = []
for i in range(0, data_size):
    if not (i in indexes):
        test_indexes.append(i)
test_indexes = [test_indexes[randint(0, test_size-1)]
                for i in range(test_size)]
colors_test = tf.constant([colors[i] for i in test_indexes])
labels_test = tf.constant([labels[i] for i in test_indexes])
validation_indexes = []
for i in range(0, data_size):
    if not (i in test_indexes) and not (i in indexes):
        validation_indexes.append(i)
validation_indexes = [validation_indexes[randint(
    0, validation_size-1)] for i in range(validation_size)]
colors_validation = tf.constant([colors[i] for i in validation_indexes])
labels_validation = tf.constant([labels[i] for i in validation_indexes])

np.savez_compressed("dataset", train_x=colors_train.numpy(), train_y=labels_train.numpy(), test_x=colors_test.numpy(),
                    test_y=labels_test.numpy(), validation_x=colors_validation.numpy(), validation_y=labels_validation.numpy())

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=(3,), activation=tf.nn.relu),
    tf.keras.layers.Dense(9, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.compat.v1.train.AdamOptimizer(0.002),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("Training:")
model.fit(colors_train, tf.cast(labels_train,
                                tf.float32), epochs=15, batch_size=32)
print("Training ended. Validating:")
model.fit(colors_validation, tf.cast(
    labels_validation, tf.float32), epochs=15, batch_size=32)

json.dump({'model': model.to_json()}, open("model.json", "w"))
model.save_weights("model_weights.h5")
