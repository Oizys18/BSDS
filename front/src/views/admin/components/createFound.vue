<template>
  <div class="container">
    <admin-navbar />
    <div class="create-lost">
      <form>
        <div class="left-wrapper">
          <span class="error">{{ fileDescription }}</span>
          <div class="img-wrapper">
            <div class="file-input-btn">
              <label for="file-input" class="image-label">
                <img class="image-upload" src="@/assets/images/camera.png" />
              </label>
            </div>
            <input
              class="file-input"
              id="file-input"
              ref="imageInput"
              type="file"
              accept="image/jpg, image/jpeg"
              @change="getColorData"
            />
            <img class="image-preview" v-if="getImgUrl" :src="getImgUrl" />
            <span class="image-button"  @click="postImageAdmin">
              <button-default :text="'이미지 등록'" />
            </span>
          </div>
          <div class="category-wrapper">
            <span class="select">물품 분류</span>
            <select-one
              class="select-category"
              :default="getCategory === null ? '분류' : getCategoryName"
              :items="Object.values($store.state.categories)"
              @input="onSelectCategory"
            />
            <span class="error" v-if="getCategory === null"
              >* 필수 입력란입니다.</span
            >
          </div>
          <div class="category-wrapper">
            <span class="select">색상</span>
            <select-one
              class="select-category"
              :default="getColor === null ? '색상' : getColorName"
              :items="Object.values($store.state.colors)"
              @input="onSelectColor"
            />
            <span class="error" v-if="getColor === null"
              >* 필수 입력란입니다.</span
            >
          </div>
          <div class="input-wrapper">
            <textarea
              class="content-area"
              v-model="content"
              type="textarea"
              placeholder="필요한 내용이 있다면 입력해주세요."
            />
          </div>
        </div>
        <div class="right-wrapper">
          <div class="button-wrapper">
            <div @click="createContent">
              <button-default class="admin-btn" :text="'등록하기'" />
            </div>
            <div @click="go({ name: 'adminIndex' })">
              <button-default class="admin-btn" :text="'취소'" />
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from "vuex";
import adminNavbar from "./adminNavbar";
import selectOne from "@/components/common/dropdown/selectOne";
import buttonDefault from "@/components/common/button/buttonDefault";
const axios = require("axios");

export default {
  name: "create-found",
  components: {
    selectOne,
    buttonDefault,
    adminNavbar,
  },
  data() {
    return {
      content: "",
      category: this.getCategory,
      color: this.getColor,
      fileDescription: "* 카메라 아이콘을 눌러 사진을 업로드한 뒤 등록 버튼을 눌러주세요."
    };
  },
  methods: {
    createContent() {
      const data = {
        image_id: this.getId,
        content: this.content,
        category: this.getCategory,
        color: this.getColor,
      };
      axios
        .post(`${this.$store.state.baseURL}found/posting/`, data, {
          headers: {
            Authorization: `JWT ${sessionStorage.getItem("jwt")}`,
          },
        })
        .then((res) => {
          console.log(res);
          this.$router.push("created");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onSelectCategory(value) {
      this.category = value;
    },
    onSelectColor(value) {
      this.color = value;
    },
    checkForm(value) {
      if (value) {
        return true;
      }
    },
    go(path) {
      this.$router.push(path);
    },
    ...mapActions(["postImageAdmin", "getColorData"]),
  },
  computed: {
    ...mapGetters([
      "getId",
      "getCategory",
      "getColor",
      "getImgUrl",
      "getCategoryName",
      "getColorName",
    ]),
    ...mapState(["image_id"]),
  },
};
</script>

<style scoped>
.content-area {
  width: 100%;
  height: 100px;
  margin: 5px;
  padding: 10px;
  border: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  resize: none;
}
.file-input {
  display: none;
}
.container {
  margin-top: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.create-form {
  overflow: hidden;
}
.left-wrapper {
  float: left;
  width: 60%;
  border: 1px solid black;
  border-radius: 2%;
  margin-right: 45px;
  margin-bottom: 30px;
  padding: 1rem;
}
.right-wrapper {
  float: left;
  width: 30%;
  text-align: initial;
}
.button-wrapper {
  border: none;
  width: 100%;
  padding: 0px 10px 10px 10px;
  text-align: center;
}
.img-wrapper {
  margin: 5px;
}
.category-wrapper,
.img-wrapper,
.input-wrapper {
  display: flex;
  margin-bottom: 15px;
}
.image-preview {
  width: 200px;
  height: 150px;
}
.image-upload {
  margin-right: 20px;
}
.select {
  font-size: 1.1rem;
  font-weight: bold;
  margin: 0 15px 0px 10px;
}
.admin-btn {
  width: 300px;
}
.error {
  font-size: 0.8rem;
  color: #fb121d;
  padding-top: 2px;
  margin: 0 15px 0px 10px;
}
.file-input-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.image-button{
  position: relative;
  display: flex;
  justify-self: center;
  align-items: center;
}
</style>
