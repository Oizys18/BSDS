<template>
  <div class="card-big-container">
    <div class="card-big-image">
      {{ this.image }}
    </div>
    <div class="card-big-text">
      <div class="card-big-title">
        {{ this.title }}
      </div>
      <div class="card-big-content">
        {{ this.content }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cardBig",
  data() {
    return {};
  },
  props: {
    image: {
      type: String,
      required: true,
      defalut: "이미지없음!",
    },
    title: {
      type: String,
      required: true,
      defalut: "타이틀없음!",
    },
    content: {
      type: String,
      required: true,
      defalut: "내용없음!",
    },
  },
};
</script>

<style scoped>
.card-big-container {
  margin: 5px;
  border: 1.5px solid black;
  border-radius: 15px;
  width: 350px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 2px 2px 4px 0 grey;
}
.card-big-container:active {
  box-shadow: 3px 3px 8px 0 grey;
}
.card-big-image {
  width: 200px;
  height: 200px;

  border-radius: 15px;
}
.card-big-text {
  border-left: 1.5px solid black;
  width: 150px;
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card-big-title {
  width: 150px;
  height: 20px;
  border-radius: 15px;
}
.card-big-content {
  height: 180px;
  width: 150px;
  border-radius: 15px;
  justify-content: center;
  align-content: center;
  display: flex;
  flex-direction: column;
}
</style>
