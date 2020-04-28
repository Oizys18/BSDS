<template>
<div class="container">
  <div class="create-lost">
    <form>
      <div class=left-wrapper>
        <div class="img-wrapper">
          <label for="file-input" class="image-label">
            <img class="image-upload" src="@/assets/images/camera.png">
          </label>
          <input
            class="file-input"
            id="file-input"
            ref="imageInput"
            type="file"
            accept="image/*"
            @change="postImageAdmin"
          >
          <img class="image-preview" v-if="getImgUrl" :src="getImgUrl"/>
        </div>
        <div class="category-wrapper">
          <span class="select">물품 분류</span>
          <select-one
            class="select-category"
            :default="this.getCategory === null ? '분류' : this.getCategoryName"
            :items="Object.values($store.state.categories)"
            @input="onSelectCategory"
          />
          <span class="error" v-if="!checkForm(this.category)">* 필수 입력란입니다.</span>
        </div>
        <div class="category-wrapper">
          <span class="select">색상</span>
          <select-one
            class="select-category"
            :default="this.getColor  === null ? '색상' : this.getColor"
            :items="Object.values($store.state.colors)"
            @input="onSelectColor"
          />
          <span class="error" v-if="!checkForm(this.color)">* 필수 입력란입니다.</span>
        </div>
        <div class="input-wrapper">
            <textarea
              class="content-area"
              v-model="content"
              type="textarea"
              placeholder="필요한 내용이 있다면 입력해주세요."
            />
        </div>
      </div>
      <div class="button-wrapper">
        <div @click="createContent">
          <button-default class="admin-btn" :text="'등록하기'"/>
        </div>
        <div @click="go('/admin')">
          <button-default class="admin-btn" :text="'취소'"/>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
  import {mapGetters, mapActions, mapState} from 'vuex'
import selectOne from '@/components/common/dropdown/selectOne'
import buttonDefault from '@/components/common/button/buttonDefault'
const axios = require('axios')

export default {
  name: 'create-lost',
  components: {
    selectOne,
    buttonDefault
  },
  data () {
    return {
      content: '',
      category: this.getCategory,
      color: this.getColor
    }
  },
  methods: {
    createContent () {
      const data = {
        "image_id": this.getId,
        "content": this.content,
        "category": this.category,
        "color": this.color,
      }
      axios.post(`${this.$store.state.baseURL}found/posting/`, data, {
        headers: {
          "Authorization": `JWT ${sessionStorage.getItem('jwt')}`
        }
      })
      .then(res => {
        console.log(res)
        console.log(data)
        this.$router.push('created')
      })
      .catch(err => {
        console.log(err)
      })
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onSelectCategory(value) {
      this.category = value
    },
    onSelectColor(value) {
      this.color = value
    },
    checkForm(value) {
      if (value) {
        return true
      }
    },
    go(path) {
      this.$router.push(path)
      this.$store._mutations.clearState()
    },
    ...mapActions(['postImageAdmin'])
  },
  computed: {
    ...mapGetters(['getId', 'getCategory', 'getColor', 'getImgUrl', 'getCategoryName']),
    ...mapState(['image_id'])
  }
}
</script>

<style scoped>
  .content-area {
    width: 100%;
    height: 100px;
    margin: 5px;
    padding: 10px;
    border: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    resize: none;
  }
  .file-input {
    display: none;
  }
  .container {
    margin-top: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .create-form {
    overflow: hidden;
  }
  .left-wrapper {
    float: left;
    width: 50em;
    border: 1px solid black;
    margin-right: 3em;
    margin-bottom: 2em;
    padding: 1rem;
    border-radius: 10px;
  }
  .button-wrapper {
    border: none;
    float: left;
    width: 20em;
    padding: 0px 10px 10px 10px;
    text-align: center;
  }
  .img-wrapper {
    margin: 5px; 
  }
  .category-wrapper, .img-wrapper, .input-wrapper {
    display: flex;
    margin-bottom: 15px;
  }
  .image-preview {
    width: 200px;
    height: 150px;
  }
  .image-upload {
    margin-right: 20px;
  }
  .select {
    font-size: 1.1rem;
    font-weight: bold;
    margin: 0 15px 0px 10px;
  }
  .admin-btn {
    width: 300px;
  }
  .error {
    font-size: 0.8em;
    color: #FB121D;
    padding-top: 2px;
    margin: 0 15px 0px 10px;
  }
</style>