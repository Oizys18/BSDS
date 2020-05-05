<template>
  <div>
    <div class="collider" v-on:click="exitModal"></div>
    <div class="modal-huge-wrapper">
      <div class="modal-huge-left">
        <div class="modal-huge-image">
          <img
            :src="
              data.thumbnail.length
                ? `${baseurl}${data.thumbnail}`
                : `${baseurl}${imagesrc}`
            "
          />
        </div>
        <div class="modal-huge-info">
          <div class="info">
            <span class="grid-title">분류</span>
            <span>{{ categories[data.category] }}</span>
          </div>
          <div class="info">
            <span class="grid-title">색상</span>
            <span>{{ colors[data.color] }}</span>
          </div>
          <div class="info" v-if="data.user">
            <span class="grid-title">습득물 등록 일자</span>
            <span>{{ data.created.slice(0, 10) }}</span>
          </div>
          <div class="info" v-else>
            <span class="grid-title">분실 추정 일자</span>
            <span>{{ data.lost_time.slice(0, 10) }}</span>
          </div>
          <div class="info" v-if="data.user">
            <span class="grid-title">보관 장소</span>
            <span>{{
              data.user.parent_department +
                " " +
                data.user.center_name +
                data.user.role
            }}</span>
          </div>
        </div>
        <div class="modal-huge-content">
          <span class="grid-title">내용</span>
          <span v-if="data.content" class="grid-content">
            {{ data.content }}
          </span>
          <span v-else class="grid-content">
            내용없음
          </span>
        </div>
      </div>
      <div class="modal-huge-right">
        <div class="modal-huge-status">
          <span class="grid-title">물품 상태</span>
          <span class="description" v-if="isLoggedIn"
            >물품이 주인을 찾았다면 체크해주세요.</span
          >
          <span class="description" v-else style="color:red"
            >수령 확인은 작성자 본인과 관리자만 가능합니다.</span
          >

          <div class="switch-check">
            <span class="switch-text">보관</span>
            <label class="switch">
              <input type="checkbox" v-model="nxtStatus" />
              <span class="slider round"></span>
            </label>
            <span class="switch-text">수령</span>
          </div>

          <span
            class="modal-button-container"
            @click="isLoggedIn ? onChangeStatusAdmin() : onChangeStatusUser()"
          >
            <span v-on:click="exitModal">
              <button-default :text="'저장 후 닫기'" />
            </span>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
import ButtonDefault from "../button/buttonDefault";
export default {
  name: "modalProps",
  components: { ButtonDefault },
  data() {
    return {
      status: null,
      imagesrc: `media/no_image.png`,
      nxtStatus: this.data.status,
    };
  },
  props: {
    data: {
      type: Object,
      default: null,
    },
  },
  methods: {
    exitModal() {
      this.$store.state.showModal = false;
    },
    onChangeStatusAdmin() {
      if (this.data.status != this.nxtStatus) {
        axios
          .patch(
            `${this.baseurl}found/posting/${this.data.id}/status/`,
            {},
            {
              headers: {
                Authorization: `JWT ${sessionStorage.getItem("jwt")}`,
              },
            }
          )
          .then()
          .catch((err) => console.log(err));
      }
    },
    onChangeStatusUser() {
      if (this.data.status != this.nxtStatus) {
        axios
          .patch(
            `${this.baseurl}lost/posting/${this.$store.state.lostname}/status/`,
            {}
          )
          .then((res) => console.log(res))
          .catch((err) => console.log(err));
      }
    },
  },
  computed: {
    baseurl() {
      return this.$store.state.baseURL;
    },
    categories() {
      return this.$store.state.categories;
    },
    colors() {
      return this.$store.state.colors;
    },
    ...mapGetters(["getStatus", "isLoggedIn"]),
  },
};
</script>

<style scoped>
.switch-text {
  padding: 0.5em;
}
.switch-check {
  display: flex;
  justify-content: center;
  margin: 15px;
  align-items: center;
  padding: 0.5em;
}
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196f3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196f3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

.collider {
  position: absolute;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  top: 0;
  left: 0;
  background: #2c3e50;
  opacity: 20%;
}
.modal-button-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
.modal-huge-wrapper {
  /* position */
  position: fixed;
  top: 15%;
  left: 25%;

  /* modal shape */
  width: 50%;

  /* content */
  color: black;
  font-size: 1rem;
}

.modal-huge-container {
  width: 100%;
  height: 100%;
  display: flex;
}

.modal-huge-left {
  float: left;
  width: 61%;
  height: 50vh;
  border-radius: 15px;
  border: 1px solid rgb(170, 170, 170);
  background-color: #ffffff;
}

.modal-huge-right {
  width: 30%;
  float: left;
  margin-left: 20px;
}

.modal-huge-image {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 25px;
}
.modal-huge-info {
  /*grid-area: info;*/
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 25px 15px 10px 15px;
}
.modal-huge-content {
  /*grid-area: content;*/
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 25px 15px 10px 15px;
}
.grid-title {
  font-size: 1.1rem;
  font-weight: bold;
  margin: 0px 10px 5px 10px;
}
.grid-content {
  font-size: 1rem;
  margin: 5px 0px 0px 12px;
  overflow: hidden;
}
.modal-huge-status {
  /*grid-area: status;*/
  display: flex;
  padding: 10px 15px 10px 15px;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  word-break: keep-all;
  border-radius: 15px;
  border: 1px solid rgb(170, 170, 170);
  background-color: #ffffff;
}
.modal-huge-radio {
  /*grid-area: radio;*/
  display: flex;
  padding: 10px;
  align-items: center;
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
.info {
  display: flex;
  justify-content: center;
}
.description {
  font-size: 1rem;
}
</style>
