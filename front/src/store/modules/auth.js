// const HOST = process.env.VUE_APP_SERVER_HOST;
const HOST = 'http://141f9f8b.ngrok.io'

const axios = require('axios');
const decoded = require('jwt-decode');
import router from '../../router';
// auth.js  인증관련 모든 State 를 작성.
// State 에 접근/변경 하는 모든 로직은 여기로.

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
  isLoggedIn: state => !!state.token , // 특정 값을 true/false 로 바꾸는 구문
  getErrors: state => state.errors,
  isLoading: state => state.loading,
  getUserId: state => state.token ? decoded(state.token).id : '',
  getUserInfo: state => state.user_info
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
  // sendLoginRequest: (credentials) => {
  //   axios.then(token => {
  //     commit('setToken', token.data.token);
  //     commit('setLoading', false)
  //     router.push('/');
  //   })
  //     .catch(err => {
  //       if (!err.response) { // no reponse
  //         commit('pushError', 'Network Error..')
  //       } else if (err.response.status === 400) {
  //         commit('pushError', 'Invalid username or password');
  //       } else if (err.response.status === 500) {
  //         commit('pushError', 'Internal Server error. Please try again later');
  //       } else {
  //         commit('pushError', 'Some error occured');
  //       }
  //       commit('setLoading', false);
  //     })
  // },

  login: ({ commit, getters }, credentials) => {
    // 이미 로그인 했다면,
    // module 안에서는, getters 함수들은 computed 처럼, 리턴 값으로 존재한다. 실행 불가능 (getters.isLoggedIn() 은 Error)
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
        axios.post(HOST + '/api-token/', credentials)
          .then(token => {
            commit('setToken', token.data.token);
            commit('setLoading', false)
            console.log(token)
            const admin_id = decoded(token).id
            axios.get(`http://localhost:3001/user/${admin_id}`)
              .then(res=> {
                commit('setUserInfo', res.data)
                console.log(res)
                console.log(state.user_info)
              })
              .catch(err => console.log(err))
            router.push({name: 'adminIndex'})
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

  // signup: ({ commit, getters, dispatch }, userInput) => {
  signup: ({ commit, getters }, userInput) => {
    if (getters.isLoggedIn) {
      router.push('/');
    } else {
      commit('clearErrors');
      commit('setLoading', true);
      if (userInput.password !== userInput.passwordConfirmation) {
        commit('pushError', 'Password & Password Confirmation did not match');
        commit('setLoading', false);
      } else {
        axios.post(HOST + '/signup/', userInput)
          .then(res => {
            if (res.data.status == 200){
              axios.post(HOST + '/api-token-auth/', {username: userInput.username, password: userInput.password })
                .then(token => {
                  commit('setToken', token.data.token);
                  commit('setLoading', false)
                  router.push('/');
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
          })
          .catch(err => {
            commit('pushError', err.response)
          })
      }
    }
  },
  }
;

export default {
  state,
  getters,
  mutations,
  actions
}