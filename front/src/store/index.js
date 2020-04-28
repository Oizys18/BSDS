import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import image from './modules/image'
import admin from './modules/admin';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    categories: [
      { id: 1, name: '가방' },
      { id: 2, name: '귀금속' },
      { id: 3, name: '도서류' },
      { id: 4, name: '의류' },
      { id: 5, name: '지갑' },
      { id: 6, name: '전자제품' },
      { id: 7, name: '휴대폰' },
      { id: 8, name: '카드' },
      { id: 9, name: '열쇠' },
      { id: 10, name: '기타' },
    ],
    colors: [
      { id: 1, name: '빨강' },
      { id: 2, name: '주황' },
      { id: 3, name: '노랑' },
      { id: 4, name: '파랑' },
      { id: 5, name: '초록' },
      { id: 6, name: '분홍' },
      { id: 7, name: '보라' },
      { id: 8, name: '갈색' },
      { id: 9, name: '회색' },
      { id: 10, name: '흰색' },
      { id: 11, name: '검정' },
    ]
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    image,
    admin
  }
})
