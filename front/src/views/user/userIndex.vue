<template>
  <div class="user-index-wrapper">
    <navbar />
    <div class="user-index-container">
      <h1 class="user-index-title">이미지 검색</h1>
      <form class="search-container">
        <div class="search-icon">
          <span class="material-icons"> search </span>
        </div>

        <div class="filebox">
          <label for="uploadfile">클릭하여 파일을 업로드해주세요.</label>
          <input type="file" id="uploadfile" />
        </div>

        <!-- <div class="search-img-title">
          <span v-if="!searched">
            <input class="search-img-inner-title" type="file">
          </span>
          <span v-else>
            <span class="search-img-inner-title">
              {{ imgTitle }}
            </span>
          </span>
        </div> -->
      </form>
      <div class="user-index-select-container" v-if="searched">
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
      <div class="user-index-result" v-if="searched">
        <div class="user-index-card-container" v-if="items[0]">
          <div
            class="user-index-card"
            v-for="(item, index) in items"
            :key="index.id"
            @click="showModal(index)"
          >
            <cardBig :image="item[0]" :title="item[1]" :content="item[2]" />
          </div>
        </div>
        <div style="margin-top: 100px;" v-else>
          <h1>띠용! 검색결과가 하나도 없어요!</h1>
          <span @click="go('/keywordsearch')">
            <buttonHuge
              :text="btnText2"
              :bgColor="bgColor"
              :txtColor="txtColor"
            />
          </span>
        </div>
      </div>
      <div class="user-index-button" v-else>
        <h2>사진이 없다면</h2>
        <span @click="go('/keywordsearch')">
          <buttonHuge :text="btnText" :bgColor="bgColor" :txtColor="txtColor" />
        </span>
        <modal v-if="isClicked" class="user-index-modal">
          <modalHuge @exit_Clicked="exit_Modal" />
        </modal>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios"
import navbar from "@/views/user/components/navbar.vue";
import cardBig from "@/components/common/card/cardBig.vue";
import modalHuge from "@/components/common/modal/modalHuge.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
// import buttonDefault from "@/components/common/button/buttonDefault.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
export default {
  name: "userIndex",
  components: {
    navbar,
    cardBig,
    selectOne,
    modalHuge,
    buttonHuge,
  },
  data() {
    return {
      categoryDefault: "분류를 선택해주세요",
      categories: ["의류", "전자기기", "식품"],
      colorDefault: "색상을 선택해주세요",
      colors: ["검정", "노랑", "빨강", "주황"],
      btnText: "다음",
      btnText2: "상세검색",
      bgColor: "#0A95FF",
      txtColor: "black",
      isClicked: false,
      searched: false,
      imgTitle: "클릭하여 이미지를 업로드해주세요",
      file: "",
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
    showModal(index) {
      this.isClicked = true;
      console.log(index + "번 게시글 모달 생성");
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
    uploadFile() {
      this.file = this.$refs.file.files[0];
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
  width: 57%;
}
.user-index-title {
  justify-content: flex-start;
  display: flex;
  padding: 0;
  margin-top: 100px;
  margin-bottom: 5px;
}
.user-index-select-container {
  margin-top: 10px;
  justify-content: flex-start;
  display: flex;
}
.user-index-select {
  margin-left: 15px;
  font-size: 1.1rem;
  font-weight: bold;
}
.user-index-button {
  position: fixed;
  align-items: center;
  display: flex;
  top: 370px;
  right: 22%;
}
.user-index-card-container {
  margin-top: 10px;
  justify-content: space-between;
  display: flex;
}

/* img upload */
.filebox label {
  margin-left:10%;
  width:max-content;
  display: inline-block;
  padding: 0.5em 0.75em;
  color: #999;
  font-size: inherit;
  line-height: normal;
  vertical-align: middle;
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 0.25em;
}
.filebox input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

/* searchbar */
.search-container {
  width: 100%;
  border: 1px solid rgb(194, 194, 194);
  border-radius: 20px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  background-color: white;
  outline: none;
}
.search-container:hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: none;
  outline: none;
}

.search-container:active {
  box-shadow: inset 0 0 5px grey;
  border: none;
  outline: none;
}

.search-img-title {
  border: none;
  width: 100%;
  height: 70%;
  font-size: 1.5em;
  margin-left: 5%;
  justify-content: flex-start;
  display: flex;
  color: rgb(90, 90, 90);
}
.search-img-inner-title {
  font-size: 1.5rem;
}
.search-icon {
  border: none;
  display: flex;
  justify-content: flex-start;
  background: none;
  position: relative;
}

.material-icons {
  font-size: 50px;
}
</style>
