<template>
  <div id="user-index-wrapper">
    <navbar />
    <div id="user-index-container">
      <h1 id="user-index-title">이미지검색</h1>
      <searchBar />
      <div id="user-index-select-container">
        분류 <selectOne :items="categories" :default="categoryDefault" /> 색상
        <selectOne :items="colors" :default="colorDefault" />
      </div>
      <div id="user-index-button">
        사진이 없다면<buttonDefault
          :text="btnText"
          :bgColor="bgColor"
          :txtColor="txtColor"
        />
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "./components/navbar";
import buttonDefault from "@/components/common/button/buttonDefault.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
import searchBar from "@/components/common/search/searchBar.vue";
export default {
  name: "userIndex",
  components: {
    navbar,
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
    };
  },
  mounted: {},
};
</script>

<style>
#user-index-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 150px;
  justify-content: center;
  align-items: center;
  display: flex;
}
#user-index-container {
  justify-content: flex-start;
}
#user-index-title {
  justify-content: flex-start;
  display: flex;
  padding: 0;
  margin-top: 100px;
  margin-bottom: 5px;
}
#user-index-select-container {
  margin-top: 20px;
  justify-content: space-between;
  display: flex;
}
#user-index-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  top: 200px;
}
</style>
