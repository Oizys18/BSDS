<template>
  <div id="found-wrapper">
    <navbar />
    <div
      id="found-card-container"
      v-for="(item, index) in items"
      :key="index.id"
    >
      <cardBig :image="item[0]" :title="item[1]" :content="item[2]" />
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
      },
    };
  },
  methods: {},
  mounted: {},
};
</script>

<style>
#found-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 150px;
  justify-content:space-around;
  align-items: center;
  display: flex;
  flex-wrap:wrap;
}
#found-card-container{
  margin-left:100px;
  margin-right:100px;
  /* flex-basis: 30%; */
}
</style>
