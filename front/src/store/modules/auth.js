// import store from '../index'
import router from '../../router';

const HOST = "http://f66b6c33.ngrok.io/"
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
};

// Vuex 에서는 Arrow Function
const getters = {
  isLoggedIn: () => !!sessionStorage.jwt, // 특정 값을 true/false 로 바꾸는 구문
  getErrors: state => state.errors,
  isLoading: state => state.loading,
  getUserId: state => state.token ? decoded(state.token).user_id : '',
  getUserInfo: state => state.user_info,
  getToken: state => state.token
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
    console.log(state.user_info)
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
      router.push('/');
    }
    // 로그인 안했다면
    else {
      commit('clearErrors');
      commit('setLoading', true);
      // username 없음
      if (!credentials.username) {
        commit('pushError', 'username can not be empty');
        commit('setLoading', false);
      }
      // password < 8
      if (credentials.password < 8) {
        commit('pushError', 'password too short');
        commit('setLoading', false);
      }
      // 요청 start
      else {
        axios.post(`${HOST}api-token/`, credentials)
          .then(token => {
            commit('setToken', token.data.token);
            commit('setLoading', false)
            dispatch('userInfo')
            console.log(token)
          router.replace({name: 'adminIndex'})
            .catch(error => {
              if (error.name === "NavigationsDuplicated") {
                throw error
              }
            })
          })
          .catch(err => {
            if (!err.response) { // no reponse
              commit('pushError', 'Network Error..')
            } else if (err.response.status === 400) {
              commit('pushError', 'Invalid username or password');
            } else if (err.response.status === 500) {
              commit('pushError', 'Internal Server error. Please try again later');
            } else {
              commit('pushError', 'Some error occured');
            }
            commit('setLoading', false);
          })
      }
    }
  },

  userInfo: ({commit}) => {
    const token = sessionStorage.getItem('jwt')
    const admin_id = decoded(token).user_id
    axios.get(`${HOST}user/${admin_id}/`)
      .then(res => {
        commit('setUserInfo', res.data)
        console.log(res)
        console.log(state.user_info)
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