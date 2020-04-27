<template>
  <div class="keyword-search-wrapper">
    <navbar />
    <div class="keyword-search-container">
      <h1 class="keyword-search-title">무엇을 잃어버리셨나요?</h1>
      <searchBar :inputText="inputText" />
      <div class="keyword-search-card">
        <div class="keyword-search-select-container">
          <span class="keyword-search-select-category">
            분류
            <selectOne :items="categories" :default="categoryDefault" />
          </span>
          <span class="keyword-search-select-color">
            색상
            <selectOne :items="colors" :default="colorDefault" />
          </span>
          <span class="keyword-search-select-location">
            예상분실위치
            <span @click="showModal()">
              <buttonDefault
                :text="btnText2"
                :bgColor="white"
                :txtColor="txtColor"
              />
            </span>
          </span>
        </div>
        <div class="keyword-search-button">
          <span @click="go('test')">
            <buttonHuge
              :text="btnText"
              :bgColor="bgColor"
              :txtColor="txtColor"
            />
          </span>
        </div>
      </div>
      <div v-if="isClicked" class="keyword-search-modal">
        <modalMap @exit_Clicked="exit_Modal" />
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar.vue";
import searchBar from "@/components/common/search/searchBar.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
import modalMap from "@/components/common/modal/modalMap.vue";
import buttonDefault from "@/components/common/button/buttonDefault.vue";
export default {
  name: "keywordSearch",
  components: {
    navbar,
    searchBar,
    selectOne,
    buttonHuge,
    modalMap,
    buttonDefault,
  },
  data() {
    return {
      categoryDefault: "분류를 선택해주세요",
      categories: ["의류", "전자기기", "식품"],
      colorDefault: "색상을 선택해주세요",
      colors: ["검정", "노랑", "빨강", "주황"],
      btnText: "검색",
      btnText2: "클릭하여 지도확인",
      bgColor: "#0A95FF",
      txtColor: "black",
      isClicked: false,
      inputText:"검색어를 입력해주세요 ex)가방,신발",
      items: {
        1: ["image1", "title1", "content1"],
        2: ["image2", "title2", "content2"],
        3: ["image3", "title3", "content3"],
      },
    };
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
    showModal(index) {
      this.isClicked = true;
      console.log(index + "번 게시글 모달 생성");
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
  },
};
</script>

<style scoped>
.keyword-search-wrapper {
  margin-top: 150px;
  justify-content: center;
  align-items: center;
  display: flex;
}
.keyword-search-card {
  margin-top: 50px;
  border: 1px solid black;
  height: 500px;
  border-radius: 40px;
}
.keyword-search-container {
  width: 60%;
}
.keyword-search-title {
  justify-content: flex-start;
  display: flex;
  padding: 0;
  margin-bottom: 5px;
}
.keyword-search-select-container {
  margin: 5%;
  display: grid;
  height: 70%;
  align-items: center;
  grid-template-rows: repeat(4, 25%);
  grid-template-columns: repeat(4, 25%);
}
.keyword-search-select-category {
  grid-column: 1/3;
  grid-row: 1/1;
  font-size: 1.5rem;
  font-weight: bold;
}
.keyword-search-select-color {
  grid-column: 1/3;
  grid-row: 3/3;
  font-size: 1.5rem;
  font-weight: bold;
}
.keyword-search-select-location {
  grid-column: 3/5;
  grid-row: 1/1;
  font-size: 1.5rem;
  font-weight: bold;
}

.keyword-search-button {
  position: absolute;
  bottom: 5%;
  right: 20%;
}
.keyword-search-card-container {
  margin-top: 100px;
  justify-content: space-between;
  display: flex;
}

/* searchbar */
.search-container {
  height: 70px;
  border: 1px solid black;
  border-radius: 50px;
}
.custom-select {
  height: 2.5rem;
  width: 80%;
}
</style>
