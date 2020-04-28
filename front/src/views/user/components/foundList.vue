<template>
  <div id="found-wrapper">
    <navbar />
    <!-- <breadcrumb/> -->
    <!-- <selecter/> -->
    <div id="found-card-container">
      <div
        @click="showModal(index)"
        v-for="(item, index) in items"
        :key="index.id"
        class="found-card"
      >
        <cardBig :image="item[0]" :title="item[1]" :content="item[2]" />
      </div>
    </div>
    <!-- <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button
        :disabled="pageNum >= pageCount - 1"
        @click="nextPage"
        class="page-btn"
      >
        다음
      </button>
    </div> -->
    <div v-if="isClicked" class="user-index-modal">
      <modalHuge @exit_Clicked="exit_Modal" />
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar";
import cardBig from "@/components/common/card/cardBig.vue";
import modalHuge from "@/components/common/modal/modalHuge.vue";
export default {
  name: "foundList",
  components: {
    cardBig,
    navbar,
    modalHuge,
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
      isClicked: false,
    };
  },
  methods: {
    showModal(index) {
      this.isClicked = true;
      console.log(index + "번 게시글 모달 생성");
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
  },
  mounted: {},
};
</script>

<style scoped>
#found-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 60px;
  justify-content: center;
  align-items: center;
  flex-direction: column;
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
  margin: 10px;
}
.found-card {
  margin: auto;
  display: flex;
  box-sizing: border-box;
}
</style>
