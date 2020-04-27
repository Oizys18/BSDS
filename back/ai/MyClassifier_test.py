#!/usr/bin/env python
# coding: utf-8

# In[2]:


# utility
import os
import numpy as np
os.environ["CUDA_VISIBLE_DEVICES"]="3"

# keras tensorflow wrapper
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.applications import InceptionV3, Xception
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.python.keras.metrics import top_k_categorical_accuracy
from tensorflow.python.keras.callbacks import ModelCheckpoint, CSVLogger
from tensorflow.keras.optimizers import Adam

# scikit-learn helper function
from sklearn.utils.class_weight import compute_class_weight


# In[3]:


def top_3_accuracy(true, pred):
    return top_k_categorical_accuracy(true, pred, k=3)

def path_join(dirname, img_paths):
    return [os.path.join(dirname, img_path) for img_path in img_paths]


# In[4]:


TRAIN_PATH = './dataset/train'
# 샘플링 몇 개만 해보기 

datagen = ImageDataGenerator(rescale=1./255,
                             validation_split=0.9)

batch_size = 32
input_shape = (224,224)

generator_train = datagen.flow_from_directory(directory=TRAIN_PATH,
                                              target_size=input_shape,
                                              shuffle=True,
                                              subset="training"
                                              )

generator_validate = datagen.flow_from_directory(directory=TRAIN_PATH,
                                                 target_size=input_shape,
                                                 shuffle=False,
                                                 subset="validation"
                                                 )
steps_train = generator_train.n / batch_size
steps_validate = generator_validate.n / batch_size

cls_train = generator_train.classes
cls_validate = generator_validate.classes

num_classes = generator_train.num_classes

class_weight = compute_class_weight(class_weight='balanced',
                                    classes=np.unique(cls_train),
                                    y=cls_train)


# In[5]:


class Model():
    def __init__(self, name, class_weight, params):
        assert name != '', "Model name needs to be specified"
        self.name = name
        self.trained = False  
        
    def construct_model(self):
        if self.name == 'inceptionv3':
            print('{:=^75}'.format('Downloading {}'.format(self.name)))
            self.base_model = InceptionV3(**params['network_params'])
            print('{:=^75}'.format('Download Complete'))
            
        elif self.name == 'xception':
            print('{:=^75}'.format('Downloading {}'.format(self.name)))
            self.base_model = Xception(**params['network_params'])
            print('{:=^75}'.format('Download Complete'))
            
            
        # 모델 구조  base model -> global average pooling -> dense
        print('{:=^75}'.format('Adding layers'))
        self.model = Sequential()
        self.model.add(self.base_model)
        self.model.add(GlobalAveragePooling2D())
        self.model.add(Dense(params['num_classes'], activation='softmax'))
        print('{:=^75}'.format('Added layers'))
    
        # 지정 경로에 저장
        if not os.path.exists('weight_path/'):
            os.mkdir('weight_path/')
        self.weight_save_path = os.path.join('weight_path/', self.name + "_weights.h5")
        
        print('{:=^75}'.format('Saving weights to {}'.format(self.weight_save_path)))
        self.model.save_weights(self.weight_save_path)
        print('{:=^75}'.format('Saved weights'))
    
    
    # train with feature extraction
    def train(self):
        if self.trained == True:
            self.model.load_weights(self.weight_save_path)
            self.trained = False
        
        # parma validation
        assert params['mode'] in ['fe', 'ft'], "mode must be either 'fe' or 'ft'"
        
        # 레이어 trainable 지정
        # feature extraction
        if params['mode'] == 'fe':
            self.model.layers[0].trainable = False
            
        # finetuning
        elif params['mode'] == 'ft':
            self.model.layers[0].trainable = True
    
            
        # compile the model with designated parameters    
        self.model.compile(optimizer=Adam(lr=params['lr']),
                           loss='categorical_crossentropy',
                           metrics=['categorical_accuracy', top_3_accuracy])
        
        if not os.path.exists(params['log_path']):
            os.mkdir(params['log_path'])
        
        if not os.path.exists(params['cp_path']):
            os.mkdir(params['cp_path'])
        
        # csv logger callback 
        log_path = os.path.join(params['log_path'], self.name + '_' + params['mode'] + '.log')
        csvlog_callback = CSVLogger(log_path)
        
        # checkpoint callback 
        cp_path = os.path.join(params['cp_path'], self.name + '_' + params['mode'] + '-{epoch:04d}-{val_loss:.2f}.h5')
        cp_callback = ModelCheckpoint(cp_path,
                                      mode="max",
                                      save_best_only=True)
        
        print('{:=^75}'.format('training {} with {}'.format(self.name, params['mode'])))
        # actual data fitting
        self.model.fit_generator(generator=generator_train,
                                  epochs=params['epoch'],
                                  class_weight=class_weight,
                                  validation_data=generator_validate,
                                  validation_steps=steps_validate,
                                  callbacks=[cp_callback, csvlog_callback])
        
        # save model once done training    
        if not os.path.exists(params['model_path']):
            os.mkdir(params['model_path'])
            
        model_save_path = os.path.join(params['model_path'], self.model.name + '_' + params['mode'] + '.h5')
        self.model.save(model_save_path)
        self.trained = True


# In[6]:


params = {
    'num_classes': num_classes,
    'log_path': 'log/',
    'cp_path': 'checkpoint/',
    'model_path': 'model/',
    'mode': 'ft',
    'lr': 0.0001,
    'epoch': 1,
    'network_params': {
    'include_top' : False,  
    'weights' : 'imagenet', 
    'input_shape' : input_shape + (3,)
    }
}


# In[7]:


# inception = Model(name='inceptionv3', class_weight=class_weight, params=params)
xception = Model(name='xception', class_weight=class_weight, params=params)


# In[8]:


# inception.construct_model()
xception.construct_model()
# inception.model.summary()
xception.model.summary()


# In[ ]:


# 모델 훈련
##### feature extraction 
# inception.train()
# inception.save()


# In[ ]:


# Fine tuning 
# params.update({
#     'mode': 'ft',
#     'lr': 0.0001
# })


# In[ ]:


# inception.train()
# inception.save()


# In[ ]:


xception.train()
# xception.save()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

headers = [
    'epoch',
    'categorical_accuracy',
    'loss',
    'top_3_accuracy',
    'val_categorical_accuracy',
    'val_loss',
    'val_top_3_accuracy'
]

# inceptionv3_fe_log = 'log/inceptionv3_fe.log'
# inceptionv3_ft_log = 'log/inceptionv3_ft.log'
# xception_fe_log = 'log/xception_fe.log'
xception_ft_log = 'log/xception_ft.log'

# logs = [inceptionv3_fe_log, inceptionv3_ft_log, xception_fe_log, xception_ft_log]
logs = [xception_ft_log]


legends = [log.split('/')[1].split('.log')[0] for log in logs]

fig = plt.figure(figsize=(20,10))
for log in logs:
    df = pd.read_csv(log)
    # val loss subplot
    plt.subplot(2,2,1)
    plt.title('Validation Loss')
    plt.plot(df.epoch, df.val_loss)
    plt.legend(legends)
    
    # val accuracy subplot
    plt.subplot(2,2,2)
    plt.title('Validation Accuracy')
    plt.plot(df.epoch, df.val_categorical_accuracy)
    plt.legend(legends)
    
    # val top 3 accuracy subplot
    plt.subplot(2,2,3)
    plt.title('Validation Top 3 Accuracy')
    plt.plot(df.epoch, df.val_top_3_accuracy)
    plt.legend(legends)

plt.show()

