// import store from '../index'
const HOST = process.env.VUE_APP_BASE_URL
const axios = require('axios')

const state = {
  meta: {
    total: null
  },
  documents: [
    {
      id: null,
      color: null,
      category: null,
      created: null,
      modified: null,
      status: true,
      thumbnail: [
        ''
      ]
    },
  ]
};

const getters = {
  getItemSize: state => state.meta.total,
  getItems: state => state.documents
};

const mutations = {
  setMeta: (state, data) => state.meta = data,
  setDoc: (state, data) => state.documents = data
};

const actions = {
  getCreatedList: ({ commit }) => {
    commit('setLoading', true)
    axios.get(`${HOST}found/posting/admin/list/`, {
      headers: {
      'Authorization': `JWT ${sessionStorage.getItem('jwt')}`
    }
    })
      .then(res => {
        const data = res.data
        commit('setMeta', data.meta)
        commit('setDoc', data.documents)
        commit('setLoading', false)

      })
      .catch(err => console.log(err))
  },

  getLostList: ({ commit }) => {
    commit('setLoading', true)
    axios.get(`${HOST}lost/admin/`, {
      headers: {
        'Authorization': `JWT ${sessionStorage.getItem('jwt')}`
      }
    })
      .then(res => {
        const data = res.data
        commit('setMeta', data.meta)
        commit('setDoc', data.documents)
        commit('setLoading', false)

      })
      .catch(err => console.log(err))
  }
};

export default {
  state,
  mutations,
  getters,
  actions
}