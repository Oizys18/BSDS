<template>
  <div class="user-index-wrapper">
    <navbar />
    <div class="user-index-container">
      <h1 class="user-index-title">이미지검색</h1>
      <searchBar />
      <div class="user-index-select-container">
        <span class="user-index-select">
          분류
        </span>
        <span class="user-index-select">
          <selectOne :items="categories" :default="categoryDefault" />
        </span>
        <span class="user-index-select">
          색상
        </span>
        <span class="user-index-select">
          <selectOne :items="colors" :default="colorDefault" />
        </span>
      </div>
      <div class="user-index-result">
        <div class="user-index-card-container">
          <div
            class="user-index-card"
            v-for="(item, index) in items"
            :key="index.id"
          >
            <cardBig :image="item[0]" :title="item[1]" :content="item[2]" />
          </div>
        </div>
      </div>
      <div class="user-index-button">
        사진이 없다면
        <span @click="go('test')">
          <buttonDefault
            :text="btnText"
            :bgColor="bgColor"
            :txtColor="txtColor"
          />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar";
import buttonDefault from "@/components/common/button/buttonDefault.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
import searchBar from "@/components/common/search/searchBar.vue";
import cardBig from "@/components/common/card/cardBig.vue";
export default {
  name: "userIndex",
  components: {
    navbar,
    cardBig,
    searchBar,
    selectOne,
    buttonDefault,
  },
  data() {
    return {
      categoryDefault: "분류를 선택해주세요",
      categories: ["의류", "전자기기", "식품"],
      colorDefault: "색상을 선택해주세요",
      colors: ["검정", "노랑", "빨강", "주황"],
      btnText: "다음",
      bgColor: "#0A95FF",
      txtColor: "black",
      items: {
        // 1: ["image1", "title1", "content1"],
        // 2: ["image2", "title2", "content2"],
        // 3: ["image3", "title3", "content3"],
      },
    };
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
.user-index-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 150px;
  justify-content: center;
  align-items: center;
  display: flex;
}
.user-index-container {
  width: 60%;
}
.user-index-title {
  justify-content: flex-start;
  display: flex;
  padding: 0;
  margin-top: 100px;
  margin-bottom: 5px;
}
.user-index-select-container {
  margin-top: 20px;
  justify-content: flex-end;
  display: flex;
}
.user-index-select {
  margin-left: 15px;
  font-size: 1.1rem;
  font-weight: bold;
}

.user-index-button {
  position: absolute;
  bottom: 5%;
  right: 20%;
}

/* searchbar */
.search-container {
  height: 70px;
  border-radius: 50px;
}
.custom-select {
  height: 1.5rem;
}
</style>
