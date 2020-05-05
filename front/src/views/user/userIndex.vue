<template>
  <div class="user-index-wrapper">
    <navbar />
    <div class="user-index-container">
      <div class="title-container">
        <span class="selected">
          이미지 검색
        </span>
        <span class="unselected" @click="go('/keywordsearch')">
          상세검색
        </span>
      </div>
      <div class="file-bar">
        <div class="file-box">
          <label for="uploadfile">
            <span class="material-icons"> search </span>
            <span class="file-box-text" v-if="!file"
              >클릭하여 파일을 업로드해주세요.</span
            >
            <span class="file-box-text" v-else>{{ file.name }}</span>
          </label>
          <input type="file" id="uploadfile" @change="checkTitle()" />
        </div>
        <div @click="imgSearch()">
          <buttonHuge
            class="file-send"
            :text="btnText3"
            :bgColor="bgColor2"
            :txtColor="txtColor"
          />
        </div>
      </div>
      <div class="system-message">
        {{ message }}
      </div>
      <div class="user-index-result" v-if="searched">
        <div class="user-index-card-container" v-if="items[0]">
          <div
            class="user-index-card"
            v-for="(item, index) in items"
            :key="index.id"
            @click="showModal(item)"
          >
            <cardSmall :item="item" />
          </div>
        </div>
        <div class="keyword-button">
          <span @click="go('/keywordsearch')" id="keyword-search-button">
            찾으시는 물건이 없나요?
            <buttonHuge :text="btnText2" />
          </span>
        </div>
      </div>
      <div v-if="this.$store.state.showModal" class="user-index-modal">
        <modalProps :data="item" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import navbar from "@/views/user/components/navbar.vue";
import cardSmall from "@/components/common/card/cardSmall.vue";
import modalProps from "@/components/common/modal/modalProps.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
export default {
  name: "userIndex",
  components: {
    navbar,
    cardSmall,
    modalProps,
    buttonHuge,
  },
  data() {
    return {
      btnText: "다음",
      btnText2: "상세검색",
      btnText3: "검색",
      bgColor: "#0A95FF",
      bgColor2: "white",
      txtColor: "black",
      searched: false,
      message: "",
      file: "",
      items: {},
      baseurl: process.env.VUE_APP_BASE_URL,
    };
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
    showModal(item) {
      this.$store.state.showModal = true;
      this.item = item;
    },
    checkTitle() {
      this.searched = false;
      this.message = "";
      this.file = event.target.files[0];
    },
    imgSearch() {
      this.$store.state.loading = true;
      if (this.file) {
        this.message = "";
        let formData = new FormData();
        formData.append("image", this.file);
        axios
          .post(this.baseurl + "found/search/image/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((res) => {
            this.$store.state.loading = false;
            this.items = res.data.documents;
            this.searched = true;
          })
          .catch(err => {
            this.$store.state.loading = false;
            console.log(err);
          });
      } else {
        this.$store.state.loading = false;
        this.message = "파일이 없습니다.";
      }
    },
  },
  watch: {
    $route() {
      this.$store.state.showModal = false;
    },
  },
};
</script>

<style scoped>
.user-index-wrapper {
  margin-top: 250px;
  justify-content: center;
  align-items: center;
  display: flex;
}
.user-index-container {
  width: 40%;
}
.title-container {
  display: flex;
  justify-content: space-between;
}
.system-message {
  display: flex;
  justify-content: flex-start;
  color: red;
  padding-left: 5%;
  font-weight: bold;
}
.user-index-title {
  padding: 0.5em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
}
.selected {
  color: rgb(255, 255, 255);
  background-color: rgb(39, 39, 39);
  padding: 0.5em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
}
.unselected {
  padding: 0.5em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #ebebeb;
  border-radius: 20px;
  color: black;
  background-color: white;
}
.unselected:hover {
  box-shadow: 2px 2px 4px 0 grey;
  border: 1px solid #ebebeb;
  border-radius: 20px;
  outline: none;
}
.unselected:active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid #ebebeb;
  outline: none;
}
.user-index-select-container {
  display: flex;
  margin-top: 10px;
  justify-content: center;
}
.user-index-select {
  margin-left: 30px;
  font-size: 1.1rem;
  font-weight: bold;
}
.user-index-card-container {
  display: flex;
  margin-top: 30px;
  justify-content: center;
}
.keyword-button {
  display: flex;
  margin-top: 30px;
  align-items: center;
  justify-content: center;
}
.file-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
/* img upload */
.file-box {
  width: 85%;
}
.file-box label {
  height: 2em;
  display: flex;
  cursor: pointer;
  font-size: 1.3em;
  padding-left: 10px;
  align-items: center;
  justify-content: flex-start;
  color: rgb(100, 100, 100);
  background-color: #fdfdfd;
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
.file-send {
  margin: 0;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
  width: 10%;
  display: flex;
  justify-content: center;
}
/* file */
file-send :hover {
  box-shadow: 2px 2px 4px 0 grey;
  border: none;
  outline: none;
}
.file-send :active {
  box-shadow: inset 0 0 5px 0 grey;
  border: none;
  outline: none;
}

/* file */
.file-box :hover {
  box-shadow: 2px 2px 4px 0 grey;
  border: 1px solid #ebebeb;
  outline: none;
}
.file-box :active {
  box-shadow: inset 0 0 5px 0 grey;
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
</style>
