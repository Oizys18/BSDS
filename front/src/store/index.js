import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import image from "./modules/image";
import admin from "./modules/admin";
import posting from "./modules/posting";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    showModal:false,
    baseURL: process.env.VUE_APP_BASE_URL,
    loading: false,
    documents: Object,
    locationX: "",
    locationY: "",
    items: {},
    categories: {
      1: "가방",
      2: "귀금속",
      3: "도서용품",
      4: "산업용품",
      5: "서류",
      6: "쇼핑백",
      7: "스포츠용품",
      8: "악기",
      9: "유가증권",
      10: "의류",
      11: "자동차",
      12: "전자기기",
      13: "증명서",
      14: "지갑",
      15: "카드",
      16: "컴퓨터",
      17: "현금",
      18: "휴대폰",
      19: "기타",
    },
    colors: {
      1: "빨강",
      2: "주황",
      3: "노랑",
      4: "파랑",
      5: "초록",
      6: "분홍",
      7: "보라",
      8: "갈색",
      9: "회색",
      10: "흰색",
      11: "검정",
    },
    lostname: ''
  },
  mutations: {},
  actions: {},
  modules: {
    auth,
    image,
    admin,
    posting,
  },
});
