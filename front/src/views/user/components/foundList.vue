<template>
  <div id="found-wrapper">
    <navbar />
    <!-- <breadcrumb/> -->
    <!-- <selecter/> -->
    <div id="found-card-container">
      <div
        @click="go(index)"
        v-for="(item, index) in items"
        :key="index.id"
        class="found-card"
      >
        <cardBig :image="item[0]" :title="item[1]" :content="item[2]" />
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar";
import cardBig from "@/components/common/card/cardBig.vue";
export default {
  name: "foundList",
  components: {
    cardBig,
    navbar,
  },
  data() {
    return {
      items: {
        1: ["image1", "title1", "content1"],
        2: ["image2", "title2", "content2"],
        3: ["image3", "title3", "content3"],
        4: ["image4", "title4", "content4"],
        5: ["image3", "title3", "content3"],
        6: ["image4", "title4", "content4"],
        7: ["image3", "title3", "content3"],
        8: ["image4", "title4", "content4"],
      },
    };
  },
  methods: {
    go(index) {
      // this.$router.push("/found/" + index + "/");
      console.log(index + "로 갑니다!");
      
    },
  },
  mounted: {},
};
</script>

<style scoped>
#found-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 100px;
  justify-content: space-around;
  align-items: center;
  display: flex;
  flex-wrap: wrap;
}
#found-card-container {
  display: grid;
  width: 40%;
  grid-template-rows: repeat(4, 210px);
  grid-template-columns: repeat(2, 360px);
  justify-content: space-around;
  align-items: center;
  /* align-content: center; */
}
.found-card {
  margin: auto;
  display: flex;
  box-sizing: border-box;
}
</style>
