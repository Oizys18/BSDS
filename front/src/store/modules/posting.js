const HOST = process.env.VUE_APP_BASE_URL
const axios = require('axios');

const state = {
  data: {
    id: null,
    color: null,
    category: null,
    postTime: null,
    content: null,
    status: null,
    thumbnail: [
      null
    ],
    x: null,
    y: null,
    user: {
      id: null,
      username: null,
      role: null,
      center_name: null,
      phone_number: null,
      address: [
        {
          address_name: null,
          x: null,
          y: null
        }
      ]
    }
  }
}

const getters = {
  getData: state => state.data,
  getStatus: state => state.status,
  getPostingId: state => state.id,
  getPostingColor: state => state.color,
  getPostingCategory: state => state.category,
  getPostTime: state => state.postTime,
  getPostContent: state => state.content,
  getThumbnail: state => state.thumbnail,
  getLocation: state => [state.x, state.y],
  getUser: state => state.user
}

const mutations = {
  setData: (state, data) => state.data = data,
  setPostingId: (state, id) => state.id = id,
  setPostingColor: (state, color) => state.color = color,
  setPostingCategory: (state, category) => state.category = category,
  setPostTime: (state, time) => state.postTime = time,
  setPostContent: (state, content) => state.content = content,
  setThumbnail: (state, image) => state.thumbnail = image,
  setLocation: (state, x, y) => {
    state.x = x
    state.y = y
  },
  setUser: (state, user) => state.user = user
}

const actions = {
  getDetailFound: ({commit}, id) => {
    commit('setPostingId', id)
    axios.get(`${HOST}found/posting/list/${id}/`)
      .then(res => {
        const data = res.data
        commit('setData', data)
        commit('setPostingCategory', data.category)
        commit('setPostingColor', data.color)
        commit('setPostContent', data.content)
        commit('setPostTime', data.created)
        commit('setThumbnail', data.thumbnail[0])
        commit('setUser', data.user)
      })
      .catch(err => console.log(err))
  },
  getDetailLost:  ({commit}, id) => {
    commit('setPostingId', id)
    axios.get(`${HOST}lost/admin/${id}/`, {
      headers: {
        'Authorization': `JWT ${sessionStorage.getItem('jwt')}`
      }
    })
      .then(res => {
        const data = res.data
        commit('setData', data)
        commit('setPostingCategory', data.category)
        commit('setPostingColor', data.color)
        commit('setPostContent', data.content)
        commit('setPostTime', data.created)
        commit('setThumbnail', data.thumbnail[0])
        commit('setUser', data.user)
      })
      .catch(err => console.log(err))
  },
}

export default {
  state,
  getters,
  mutations,
  actions
}