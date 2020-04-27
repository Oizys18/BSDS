import store from '../index'
const HOST = 'http://141f9f8b.ngrok.io'

const axios = require('axios');

const state = {
  image_id: null,
  color: null,
  category: null,
  imageUrl: null,
};

const getters = {
  getId: state => state.Id,
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
  }
};

const actions= {
  postImage: ({ commit }, e) => {
    console.log(e)
    console.log(e.target.files)
    const file = e.target.files[0]
    const formdata = new FormData();
    commit('setImgUrl', URL.createObjectURL(file))
    let pageUrl = ''
    if (window.location.href.includes('admin')) {
      pageUrl = 'found'
    } else {
      pageUrl = 'lost'
    }
    formdata.append('image', file)
    axios.post(`${HOST}/${pageUrl}/posting/image/`, formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
      })
      .then(res => {
        commit('setId', res.data.image_id)
        commit('setCategory', res.data.category)
        commit('setColor', res.data.color)
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