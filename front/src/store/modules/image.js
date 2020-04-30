import store from '../index'
import * as Vibrant from 'node-vibrant'
const HOST = process.env.VUE_APP_BASE_URL

const axios = require('axios');

const state = {
  image_id: null,
  color: null,
  category: null,
  imageUrl: null,
  colorData: [],
  file: null
};

const getters = {
  getId: state => state.image_id,
  getCategory: state => state.category,
  getCategoryName: state => store.state.categories[state.category],
  getColor: state => state.color,
  getColorName: state => store.state.colors[state.color],
  getImgUrl: state => state.imageUrl,
};

const mutations = {
  setId: (state, img_id) => state.image_id = img_id,
  setCategory: (state, ctgr) => {
    state.category = ctgr
  },
  setColor: (state, clr) => {
    state.color = clr
  },
  setImgUrl: (state, imageUrl) => {
    state.imageUrl = imageUrl
  },
  clearState: (state) => {
    state.image_id = null,
    state.category = null,
    state.color = null
    state.imageUrl = null
  },
  setColorData: (state, colordata) => {
    state.colorData = colordata
  },
  setFile: (state, file) => {
    state.file = file
  }
};

const actions= {
  getColorData: ({ commit }, e) => {
    const colorDataArray = [];
    const file = e.target.files[0]
    const imgUrl = URL.createObjectURL(file)
    commit('setFile', file)
    commit('setImgUrl', imgUrl)
    Vibrant.from(state.imageUrl)
        .getPalette()
        .then((palette) => {
          colorDataArray.push(palette.Vibrant.hex);
          colorDataArray.push(palette.Muted.hex);
          colorDataArray.push(palette.DarkVibrant.hex);
          colorDataArray.push(palette.DarkMuted.hex);
          colorDataArray.push(palette.LightVibrant.hex);
          colorDataArray.push(palette.LightMuted.hex);
          colorDataArray.push(palette.Vibrant.population);
          colorDataArray.push(palette.Muted.population);
          colorDataArray.push(palette.DarkVibrant.population);
          colorDataArray.push(palette.DarkMuted.population);
          colorDataArray.push(palette.LightVibrant.population);
          colorDataArray.push(palette.LightMuted.population);
        });
    commit('setColorData', colorDataArray);
  },

  postImageUser: ({ commit }) => {
    const formdata = new FormData();
    formdata.append('image', state.file)
    formdata.append('colorData', state.colorData)
    axios.post(`${HOST}lost/posting/image/`, formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
      })
      .then(res => {
        commit('setId', res.data.image_id)
        commit('setCategory', res.data.category)
        commit('setColor', res.data.color)
      })
      .catch(err => console.log(err))
  },

  postImageAdmin: ({ commit }) => {
    const formdata = new FormData();
    formdata.append('image', state.file)
    formdata.append('colorData', state.colorData)
    axios.post(`${HOST}found/posting/image/`, formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
            'Authorization': `JWT ${sessionStorage.getItem('jwt')}`
        }
      })
      .then(res => {
        commit('setId', res.data.image_id)
        commit('setCategory', res.data.category)
        commit('setColor', res.data.color)
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