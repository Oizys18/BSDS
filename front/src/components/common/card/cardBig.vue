<template>
  <div class="card-big-container">
    <div class="card-big-image" >
      <img :src="this.image" alt="No image">
    </div>
    <div class="card-big-text">
      <div class="card-big-title">
        보관기관:{{ this.title }}
      </div>
      <div class="card-big-content">
        습득일:{{ this.content }}
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
  font-size:13px;
  margin: 5px;
  border: 1px solid black;
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
}
.card-big-text {
  border-left: 1px solid black;
  width: 150px;
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card-big-title {
  width: 150px;
  height: 20px;
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
