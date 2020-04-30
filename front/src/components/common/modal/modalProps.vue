<template>
  <div>
    <div class="collider" v-on:click="exitModal"></div>
    <div class="modal-huge-wrapper">
      <div class="modal-huge-container">
        <button class="modal-huge-collide" v-on:click="exitModal">
          <span>✖</span>
        </button>
        <div class="modal-huge-image">
          <img :src="this.baseurl + data.thumbnail[0]" />
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
            <span>{{ data.user.center_name + data.user.role }}</span>
          </div>
          <!--          <div class="info" v-else>-->
          <!--            <span class="grid-title">분실 추정 위치</span>-->
          <!--            <span>{{ data.x }}</span>-->
          <!--          </div>-->
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
        <div class="modal-huge-status">
          <span class="grid-title">물품 상태</span>
          <span>물품이 주인을 찾았다면 체크해주세요.</span>
          <div class="modal-huge-radio" data-toggle="buttons">
            <label class="box-radio-input">
              <input
                type="radio"
                name="cp_item"
                value="true"
                v-model="data.status"
              />
              <span class="check">V</span>
              <span class="description">수령</span>
            </label>
            <label class="box-radio-input">
              <input
                type="radio"
                name="cp_item"
                value="false"
                v-model="data.status"
              />
              <span class="check">V</span>
              <span class="description">보관</span>
            </label>
          </div>
          <span @click="onChangeStatus">
            <button-default :text="'저장'" />
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
    onChangeStatus() {
      this.status ? (this.status = false) : (this.status = true);
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
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
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
    ...mapGetters(["getStatus"]),
  },
};
</script>

<style scoped>
.collider {
  position: absolute;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  top: 0;
  left: 0;
  background: transparent;
}
.modal-huge-wrapper {
  /* position */
  position: fixed;
  top: 15%;
  left: 25%;

  /* modal shape */
  height: 60%;
  width: 50%;
  border: 1px solid black;
  border-radius: 15px;

  /* content */
  background-color: white;
  color: black;
  font-size: 1rem;

  /* justify-content: center;
    align-items: center; */
}

.modal-huge-container {
  width: 100%;
  height: 100%;
  /* contents align */
  display: grid;
  grid-template-rows: repeat(7, 14.5%);
  grid-template-columns: repeat(4, 25%);
  grid-template-areas:
    "image image status status"
    "image image status status"
    "image image status status"
    "image image status status"
    "info info content content"
    "info info content content"
    "info info content content";
}

.modal-huge-collide {
  position: absolute;
  right: 0;
  border: none;
  z-index: 10;
  font-size: 25px;
  background-color: transparent;
}
.modal-huge-image {
  width: 100%;
  height: 100%;
  border-radius: 15px;
  grid-area: image;
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-huge-info {
  grid-area: info;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 25px 15px 10px 15px;
}
.modal-huge-content {
  grid-area: content;
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
  grid-area: status;
  display: flex;
  padding: 25px 15px 10px 15px;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  word-break: keep-all;
}
.modal-huge-radio {
  grid-area: radio;
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
</style>
