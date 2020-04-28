import store from '../index'
const HOST = 'http://8c6a607d.ngrok.io'

const axios = require('axios');

const state = {
  image_id: null,
  color: null,
  category: null,
  imageUrl: null,
};

const getters = {
  getId: state => state.image_id,
  getCategory: state => state.category,
  getColor: state => state.color,
  getImgUrl: state => state.imageUrl,
};

const mutations = {
  setId: (state, img_id) => state.image_id = img_id,
  setCategory: (state, ctgr) => {
    state.category = store.state.categories[ctgr].name
    console.log(store.state.categories)
  },
  setColor: (state, clr) => {
    state.color = store.state.colors[clr].name
  },
  setImgUrl: (state, imageUrl) => {
    state.imageUrl = imageUrl
  },
  clearState: (state) => {
    state.image_id = null,
    state.category = null,
    state.color = null
    state.imageUrl = null
  }
};

const actions= {
  postImageUser: ({ commit }, e) => {
    console.log(e)
    console.log(e.target.files)
    const file = e.target.files[0]
    const formdata = new FormData();
    commit('setImgUrl', URL.createObjectURL(file))
    formdata.append('image', file)
    axios.post(`${HOST}/lost/posting/image/`, formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
      })
      .then(res => {
        commit('setId', res.data.image_id)
        commit('setCategory', res.data.category)
        console.log(res)
        console.log(state)
      })
      .catch(err => console.log(err))
  },
  postImageAdmin: ({ commit }, e) => {
    console.log(e)
    console.log(e.target.files)
    const file = e.target.files[0]
    const formdata = new FormData();
    commit('setImgUrl', URL.createObjectURL(file))
    formdata.append('image', file)
    axios.post(`${HOST}/found/posting/image/`, formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
            'Authorization': `JWT ${sessionStorage.getItem('jwt')}`
        }
      })
      .then(res => {
        commit('setId', res.data.image_id)
        commit('setCategory', res.data.category)
        console.log(res)
        console.log(state)
      })
      .catch(err => console.log(err))
  }
};

export default {
  state,
  getters,
  mutations,
  actions
}