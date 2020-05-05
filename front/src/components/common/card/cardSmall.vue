<template>
  <div class="card-small-container">
    <div class="card-small-image">
      <img
        :src="
          item.thumbnail.length
            ? `${baseurl}${item.thumbnail}`
            : `${baseurl}${imagesrc}`
        "
        alt="ㅠ사진이 없어요ㅠ"
      />
    </div>
    <div class="card-small-text">
      <div class="itemCategory">
        분류: {{ this.$store.state.categories[item.category] }}
      </div>
      <div class="itemColor">
        색상: {{ this.$store.state.colors[item.color] }}
      </div>
      <div v-if="item.created" class="itemDate">습득일: {{ item.created.slice(2, 10) }}</div>
      <div v-else class="itemDate">분실일: {{ item.lost_time.slice(2, 10) }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cardSmall",
  data() {
    return {
      baseurl: process.env.VUE_APP_BASE_URL,
      imagesrc: `media/no_image.png`,
    };
  },
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.card-small-container {
  font-size: 13px;
  margin: 5px;
  width: 200px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 4px 4px 10px 0 grey;
}
.card-small-container:active {
  box-shadow: 3px 3px 8px 0 grey;
}
.card-small-image {
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
}
.card-small-text {
  color: transparent;
  opacity: 0;
  font-size: 1.5em;
  position: absolute;
  justify-content: center;
  box-shadow: inset 0 0 5px rgb(238, 238, 238);
  width: 200px;
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card-small-text:hover {
  opacity: 0.8;
  color: white;
  background-color: #472222;
}
</style>
