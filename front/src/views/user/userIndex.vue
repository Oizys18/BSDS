<template>
  <div class="user-index-wrapper">
    <navbar />
    <div class="user-index-container">
      <h1 class="user-index-title">이미지 검색</h1>

      <div class="file-box">
        <label for="uploadfile">
          <span class="material-icons"> search </span>
          <span class="file-box-text" v-if="!file"
            >클릭하여 파일을 업로드해주세요.</span
          >
          <span class="file-box-text" v-else>{{ imgTitle }}</span>
        </label>
        <input type="file" id="uploadfile" @change="checkTitle()" />
      </div>
      <div class="file-send" @click="imgSearch()">
        <buttonHuge :text="btnText3" :bgColor="bgColor2" :txtColor="txtColor" />
      </div>

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
import axios from "axios";
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
      btnText3: "검색",
      bgColor: "#0A95FF",
      bgColor2: "white",
      txtColor: "black",
      isClicked: false,
      searched: false,
      imgTitle: "이미지가 없어요!",
      file: "",
      items: {
        // 0: ["image1", "title1", "content1"],
        // 1: ["image2", "title2", "content2"],
        // 2: ["image3", "title3", "content3"],
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
    checkTitle() {
      this.imgTitle = event.target.files[0].name;
      this.file = event.target.files[0];
      console.log(event.target.files[0].name);
    },
    imgSearch() {
      let formData = new FormData();
      let url = "";
      formData.append("file", this.file);
      axios
        .post(url + "/found/search/image/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          console.log(res);
        })
        .catch(function() {
          console.log("FAILURE!!");
        });
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
  width: 40%;
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
  justify-content: center;
  display: flex;
}
.user-index-select {
  margin-left: 30px;
  font-size: 1.1rem;
  font-weight: bold;
}
.user-index-card-container {
  margin-top: 30px;
  justify-content: center;
  display: flex;
}
.user-index-button {
  position: absolute;
  width: inherit;
  bottom: 10vh;
  align-items: center;
  justify-content: flex-end;
  display: flex;
}

/* img upload */
.file-box label {
  width: 100%;
  height: 2em;
  display: flex;
  color: rgb(100, 100, 100);
  font-size: 1.7em;
  justify-content: flex-start;
  align-items: center;
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
}
.file-box input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

/* file */
.file-box :hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: 1px solid #ebebeb;
  outline: none;
}
.file-box :active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid #ebebeb;
  outline: none;
}
.material-icons,
.file-box-text:hover {
  box-shadow: none;
  border: none;
  outline: none;
}
.material-icons,
.file-box-text:active {
  box-shadow: none;
  border: none;
  outline: none;
}

.file-send {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
</style>
