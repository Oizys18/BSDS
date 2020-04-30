// import store from '../index'
import router from '../../router';
const HOST = process.env.VUE_APP_BASE_URL
const axios = require('axios');
const decoded = require('jwt-decode');

const state = {
  token: null,
  errors: [],
  loading: false,
  user_id: '',
  user_info: {
    username: '',
    parent_department: '',
    center_name: '',
    role: '',
    phone_number: '',
    address: [
      {
        address_name: '',
        x: '',
        y: ''
      }
    ]
  },
  detail_key: 0
};

// Vuex 에서는 Arrow Function
const getters = {
  isLoggedIn: () => sessionStorage.jwt ? true : false, // 특정 값을 true/false 로 바꾸는 구문
  getErrors: state => state.errors,
  isLoading: state => state.loading,
  getUserId: state => state.token ? decoded(state.token).user_id : '',
  getUserInfo: () => JSON.parse(sessionStorage.getItem(`info`)),
  getInfo: state => state.user_info,
  getToken: state => state.token,
  getDetailKey: state => state.detail_key
};

const mutations = {
  setLoading: (state, flag) => state.loading = flag,
  setToken: (state, token) => {
    state.token = token;
    sessionStorage.setItem('jwt', token);
  },
  pushError: (state, error) => state.errors.push(error),
  clearErrors: state => state.errors = [],
  setUserInfo: (state, data) => {
    state.user_info = data
    sessionStorage.setItem('info', JSON.stringify(data))
  }
};

const actions = {
  setInitialToken: ({ commit }) => {
    commit('setToken', sessionStorage.getItem('jwt'));
  },

  logout: ({ commit }) => {
    commit('setToken', null);
    sessionStorage.removeItem('jwt');
    router.push('/login');
  },

  pushError: ({ commit }, error) => {
    commit('pushError', error)
  },

  login: ({ commit, getters, dispatch }, credentials) => {
    if (getters.isLoggedIn)  {
      state.detail_key = 0
      // router.go()
    }
    // 로그인 안했다면
    else {
      commit('clearErrors');
      // username 없음
      // 요청 start
      axios.post(`${HOST}api-token/`, credentials)
        .then(token => {
          commit('setToken', token.data.token);
          dispatch('userInfo')
          commit('setLoading', false)
          .then(
            state.detail_key = 1,
        )
        })
        .catch(err => {
          if (!err.response) { // no reponse
            // commit('pushError', '* 서버 상태가 좋지 않네요.')
          } else if (err.response.status === 400) {
            commit('pushError', '* 아이디와 비밀번호를 확인하세요.');
          } else if (err.response.status === 500) {
            commit('pushError', '* 잠시 후에 다시 시도해주세요.');
          } else {
            commit('pushError', '* Some error occured');
          }
        })

    }
  },

  async userInfo ({commit}) {
    const token = sessionStorage.getItem('jwt')
    const admin_id = decoded(token).user_id
    axios.get(`${HOST}user/${admin_id}/`)
      .then(res => {
        commit('setUserInfo', res.data)
        state.detail_key = 3
        router.go()
      })
      .catch(err => console.log(err))
  },
};

export default {
  state,
  getters,
  mutations,
  actions
}