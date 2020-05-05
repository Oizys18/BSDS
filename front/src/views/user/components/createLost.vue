<template>
  <div class="container">
    <navbar />
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
            <span class="image-button" @click="postImageUser">
              <button-default :text="'이미지 등록'" />
            </span>
          </div>
          <div class="category-wrapper">
            <span class="select">물품 분류</span>
            <select-one
              class="select-category"
              :items="Object.values($store.state.categories)"
              :default="getCategory === null ? '분류' : getCategoryName"
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
              :items="Object.values($store.state.colors)"
              :default="getColor === null ? '색상' : getColorName"
              @input="onSelectColor"
            />
            <span class="error" v-if="getColor === null"
              >* 필수 입력란입니다.</span
            >
          </div>
          <div class="date-wrapper">
            <span class="select">분실 추정 일자</span>
            <input
              class="select-year"
              type="date"
              min="2019-01-01"
              v-model="date"
            />
            <select-one
              class="select-time"
              :default="'시각'"
              :items="timeList"
              @input="onTimeSelect"
            />
            <span class="error" v-if="!checkForm(this.time)"
              >* 필수 입력란입니다.</span
            >
          </div>
          <span class="category-wrapper">
            <span class="select-location">
              <div class="select-location-container">
                <div class="location-wrapper">
                  <label class="location-title" for="addressinput"
                    >예상 분실위치</label
                  >
                  <div>
                    <input
                      id="addressinput"
                      type="text"
                      v-model="addressInput"
                    />
                    <span @click="searchAddress">
                      <buttonDefault
                        :text="btnText2"
                        :bgColor="bgColor"
                        :txtColor="txtColor"
                      />
                    </span>
                  </div>
                </div>
                <div class="search-results">
                  <span
                    class="results"
                    v-for="result in results"
                    :key="result.id"
                  >
                    <span @click="showModal(result)">
                      {{ result.address.address_name }}</span
                    >
                  </span>
                </div>
              </div>
            </span>
          </span>
          <div v-if="this.$store.state.showModal" class="keyword-search-modal">
            <modalMap @exit_Clicked="exit_Modal" />
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
          <div class="description-wrapper">
            <div class="password">
              <label for="password" class="select">비밀번호</label>
              <p class="description">
                등록한 비밀번호는 내용 수정 및 분실상태 변경 시 사용됩니다.
              </p>
              <input
                id="password"
                class="input-password-email"
                type="password"
                v-model="password"
              />
              <span class="error" v-if="!checkPassword(this.password)"
                >* 비밀번호는 네 글자 이상 입력해주세요.</span
              >
            </div>
            <div class="email">
              <label for="email" class="select">이메일</label>
              <input
                id="email"
                class="input-password-email"
                type="email"
                v-model="email"
              />
              <span class="error" v-if="!validEmail(this.email)"
                >* 이메일 형식에 맞게 입력해주세요.</span
              >
            </div>
            <div class="email">
              <label class="select">알림 제공 동의</label>
              <p class="description">
                유사한 습득물 등록 시 이메일로 알림을 보내드립니다.
              </p>
              <div class="email-radio" data-toggle="buttons">
                <label class="box-radio-input">
                  <input
                    type="radio"
                    name="cp_item"
                    value="true"
                    v-model="do_notice"
                  />
                  <span class="check">V</span>
                  <span class="description">동의</span>
                </label>
                <label class="box-radio-input">
                  <input
                    type="radio"
                    name="cp_item"
                    value="false"
                    v-model="do_notice"
                  />
                  <span class="check">V</span>
                  <span class="description">비동의</span>
                </label>
              </div>
            </div>
          </div>
          <div class="button-wrapper">
            <div class="submit-btn" @click="createContent">
              <button-default class="user-btn" :text="'등록하기'" />
            </div>
            <div @click="go('/')">
              <button-default class="user-btn btn-option" :text="'취소'" />
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// import router from '../router'
import selectOne from "@/components/common/dropdown/selectOne";
import navbar from "@/views/user/components/navbar";
import buttonDefault from "@/components/common/button/buttonDefault";
import modalMap from "@/components/common/modal/modalMap";
import { mapActions, mapGetters, mapState } from "vuex";
const axios = require("axios");

export default {
  name: "create-lost",
  components: {
    selectOne,
    navbar,
    buttonDefault,
    modalMap,
  },
  data() {
    return {
      content: "",
      category: this.getCategory,
      color: this.getColor,
      date: null,
      timeList: [],
      time: "",
      password: "",
      email: "",
      do_notice: true,
      btnText2: "주소검색",
      bgColor: "white",
      txtColor: "black",
      addressInput: "",
      results: "",
      showing: "",
      fileDescription:
        "* 카메라 아이콘을 눌러 사진을 업로드한 뒤 등록 버튼을 눌러주세요.",
    };
  },
  mounted() {
    for (let i = 0; i < 25; i++) {
      if (i < 10) {
        this.timeList.push("0" + i.toString() + ":00");
      } else {
        this.timeList.push(i.toString() + ":00");
      }
    }
  },
  methods: {
    searchAddress() {
      axios
        .get("https://dapi.kakao.com/v2/local/search/address.json", {
          params: {
            query: this.addressInput,
          },
          headers: {
            Authorization: "KakaoAK f8d38a34b065785c71e6beed1528657f",
          },
        })
        .then((res) => {
          this.results = res.data.documents.slice(0, 3);
        });
    },
    categorySearch() {
      this.$store.state.loading = true;
      axios
        .get(this.baseurl + "found/search/", {
          params: {
            category: this.inputCategory,
            color: this.inputColor,
            created: this.inputDate,
            x: this.$store.state.locationX,
            y: this.$store.state.locationY,
          },
        })
        .then((res) => {
          this.$store.state.loading = false;
          this.$store.state.documents = res.data.documents;
          this.go("/found");
        })
        .catch((err) => {
          this.$store.state.loading = false;
          console.log(err);
        });
    },
    go(path) {
      this.$router.push(path);
    },
    checkModal() {
      if (this.$store.state.showModal) {
        this.$store.state.showModal = false;
      } else {
        this.$store.state.showModal = true;
      }
    },
    showModal(e) {
      if (this.showing != e) {
        this.$store.state.locationX = e.x;
        this.$store.state.locationY = e.y;
      }
      this.showing = e;
      this.checkModal().then((this.$store.state.showModal = true));
    },
    exit_Modal() {
      this.$store.state.showModal = false;
    },

    createContent() {
      const data = {
        image_id: this.getId,
        category: this.category ? this.category : this.getCategory,
        color: this.color ? this.color : this.getColor,
        content: this.content,
        lost_time: this.date + " " + this.time,
        email: this.email,
        password: this.password,
        do_notice: this.do_notice,
        x: this.$store.state.locationX,
        y: this.$store.state.locationY,
      };
      console.log(data)
      axios
        .post(`${this.$store.state.baseURL}lost/posting/`, data)
        .then((res) => {
          this.$store.state.lostname = res.data.lostname;
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
    onTimeSelect(value) {
      this.time = this.timeList[value];
    },
    validEmail(email) {
      if (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        return true;
      } else if (email.length === 0) {
        return true;
      }
    },
    checkForm(value) {
      if (value) {
        return true;
      }
    },
    checkPassword(password) {
      if (password.length > 3) {
        return true;
      }
    },
    ...mapActions(["postImageUser", "getColorData"]),
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
.image-button {
  position: relative;
  display: flex;
  justify-self: center;
  align-items: center;
}
.select-location {
  width: 100%;
  justify-content: space-around;
  align-items: center;
  display: flex;
  flex-direction: column;
}
.location-wrapper {
  width: 50%;
}
.select-location-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.search-address label {
  padding: 0.1em;
  font-size: 1.3em;
}
.search-address input {
  font-size: 1em;
}
.search-results {
  margin: 5px;
  width: 50%;
  height: 80px;
  background: white;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  padding: 5px;
}
#addressinput {
  border: 1px solid black;
  border-radius: 15px;
  padding: 0.25em;
  width: 60%;
  outline: none;
}
#addressinput label {
  margin: 15px;
}
.modal-map-wrapper {
  /* position */
  position: fixed;
  top: 25%;
  right: 1%;

  /* modal shape */
  height: 40%;
  width: 20%;
  border: 1px solid black;

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;

  justify-content: space-between;
  align-items: center;
  display: flex;
  flex-direction: column;
}

.search-results span {
  font-size: 1em;
  color: rgb(70, 70, 255);
}
.search-results span:hover {
  font-weight: bold;
  color: blue;
}
.content-area {
  width: 100%;
  height: 100px;
  margin: 5px;
  padding: 10px;
  border: 1px solid black;
  border-radius: 15px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  resize: none;
}
.content-area:hover {
  outline: none;
}
.content-area:active {
  outline: none;
}

.file-input {
  display: none;
}
.select-year {
  width: 25%;
  margin-right: 10px;
  padding-left: 8px;
}
.select-year:hover {
  outline: none;
}
.select-year:active {
  outline: none;
}
.select-time {
  width: 15%;
  margin-right: 10px;
}
.container {
  margin-top: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
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
.description-wrapper {
  border: 1px solid black;
  border-radius: 2%;
  float: left;
  width: 100%;
  padding: 10px;
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
.date-wrapper,
.img-wrapper,
.input-wrapper {
  display: flex;
  margin-bottom: 15px;
  outline: none;
}

.input-wrapper:hover {
  outline: none;
}
.input-wrapper:active {
  outline: none;
}
.date-select-wrapper select {
  height: 1.5rem;
}
.image-preview {
  max-width: 200px;
  height: 150px;
}
.image-upload {
  margin-right: 20px;
}
.select,
.select-location {
  font-size: 1.1rem;
  font-weight: bold;
  margin: 0 15px 0px 10px;
}
.password,
.email {
  margin: 15px;
}
.input-password-email {
  border: none;
  width: 90%;
  border-bottom: black 1px solid;
  margin: 10px;
}
input[type="password"],
input[type="email"] {
  height: 1.5rem;
}
.description {
  font-size: 1rem;
  margin: 5px 15px 0px 10px;
  line-height: 1.4rem;
  word-break: keep-all;
}
.submit-btn {
  text-align: center;
}
.user-btn {
  width: 300px;
  margin-top: 15px;
}
.btn-option {
  margin: 3px;
}
.error {
  font-size: 0.8rem;
  color: #fb121d;
  padding-top: 2px;
  margin: 0 15px 0px 10px;
}
.email-radio {
  display: flex;
  padding: 10px;
  justify-content: space-around;
}
.box-radio-input input[type="radio"] {
  display: none;
}
.box-radio-input input[type="radio"] + span {
  display: inline-block;
  background: none;
  border: 1px solid #dfdfdf;
  border-radius: 10px;
  padding: 0px 10px;
  text-align: center;
  height: 35px;
  line-height: 33px;
  font-weight: 500;
  cursor: pointer;
  margin: 10px 10px 0 10px;
}
.box-radio-input input[type="radio"]:checked + span {
  border: 1px solid #0a95ff;
  background: #0a95ff;
  color: #fff;
}
.file-input-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
input[type="date"] {
  border-radius: 10px;
  border: 1px solid black;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
