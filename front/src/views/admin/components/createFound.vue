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
            @change="onChangeImages"
          >
          <img class="image-preview" v-if="imageUrl" :src="imageUrl"/>
        </div>
        <div class="category-wrapper">
          <span class="select">물품 분류</span>
          <select-one
            class="select-category"
            :default="'분류'"
          />
        </div>
        <div class="input-wrapper">
            <textarea
              class="content-area"
              v-model="contents"
              type="textarea"
              placeholder="필요한 내용이 있다면 입력해주세요."
              @input="onChangeInput"
            />
        </div>
      </div>
      <div class="right-wrapper">
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
      image: '',
      contents: '',
      imageUrl: null,
      category: '',
    }
  },
  methods: {
    createContent () {
      const formdata = {
        "contents": this.contents,
        "imageFile": this.image,
        "category": this.category
      }
      axios.post('http://localhost:3001/board', this.formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
      })
      .then(res => {
        console.log(res)
        console.log(formdata)
        this.$router.push('created')
      })
      .catch(err => {
        console.log(err)
      })
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      console.log(e.target.files)
      const file = e.target.files[0] 
      this.image = file
      this.imageUrl = URL.createObjectURL(file) 
      console.log(this.image)
      // 이미지 post 한번 더 보내서 분류 추가할것
    },
    go(path) {
      this.$router.push(path)
    }
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
  .right-wrapper {
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
    width: 20em;
  }
</style>