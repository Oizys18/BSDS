<template>
<div class="container">
  <navbar/>
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
            @change="postImage"
          >
          <img class="image-preview" v-if="getImgUrl" :src="getImgUrl"/>
        </div>
        <div class="category-wrapper">
          <span class="select">물품 분류</span>
          <select-one
            class="select-category"
            :default="getCategory ? getCategory : '분류'"
          />
        </div>
        <div class="category-wrapper">
          <span class="select">색상</span>
          <select-one
            class="select-category"
            :default="getColor ? getColor : '색상'"
          />
        </div>
        <div class="date-wrapper">
          <span class="select">분실 추정 일자</span>
          <select-one
            class="select-year"
            :default="'연'"
            :items="yItems"
            @input="onDateSelectY"
          />
          <select-one
            class="select-month"
            :default="'월'"
            :items="mItems"
            @input="onDateSelectM"
          />
          <select-one
            class="select-day"
            :default="'일'"
            :items="dItems"
            @input="onDateSelectD"
          />
          <select-one
            class="select-time"
            :default="'선택'"
            :items="timeList"
            @input="onTimeSelectStart"
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
        <div class="password">
        <span class="select">비밀번호</span>
        <p class="description">등록한 비밀번호는 내용 수정 및 분실상태 변경 시 사용됩니다.</p>
        <input class="input-password-email" type="password" v-model="password">
        </div>
        <div class="email">
        <span class="select">이메일</span>
        <p class="description">유사한 습득물 등록 시 이메일로 알림을 보내드립니다.</p>
        <input class="input-password-email" type="text" v-model="email">
        </div>
        <div class="submit-btn" @click="createContent">
          <button-default :text="'등록하기'"/>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
// import router from '../router'
import selectOne from '@/components/common/dropdown/selectOne'
import navbar from '@/views/user/components/navbar'
import buttonDefault from '@/components/common/button/buttonDefault'
import {mapActions, mapGetters} from "vuex";
const axios = require('axios')

export default {
  name: 'create-lost',
  components: {
    selectOne,
    navbar,
    buttonDefault
  },
  data() {
    return {
      content: '',
      category: '',
      yItems: [],
      mItems: ['1 월', '2 월', '3 월', '4 월', '5 월', '6 월', '7 월', '8 월', '9 월', '10 월', '11 월', '12 월'],
      dItems: [],
      date: ['2020', '-', '00', '-', '00'],
      timeList: [],
      time: '',
      password: '',
      email: ''
    }
  },
  mounted() {
    for (let i = 0; i < 25; i++) {
      if (i < 10) {
        this.timeList.push('0' + i.toString() + ':00')
      } else {
        this.timeList.push(i.toString() + ':00')
      }
    }
    for (let y = 2020; y > 1920; y--) {
      this.yItems.push(y.toString() + ' 년')
    }
    for (let d = 1; d < 32; d++) {
      this.dItems.push(d.toString() + ' 일')
    }
  },
  methods: {
    createContent() {
      const formdata = {
        "content": this.contents,
        "lost_time": this.date.reduce(function (accumulator, currentValue) {
          return accumulator + currentValue;
        }),
        "time": this.startTime.replace(":", "") + this.endTime.replace(":", ""),
        "email": this.email,
        "password": this.password
      }
      axios.post('http://localhost:3001/board', this.formdata, {
        headers: {
          "Content-Type": "multipart/form-data",
        }
      })
        .then(res => {
          console.log(res)
          console.log(formdata)
          this.$router.push('/created')
        })
        .catch(err => {
          console.log(err)
        })
    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeInput() {
      console.log(this.contents)
    },
    onTimeSelectStart(value) {
      this.time = this.timeList[value]
      console.log(this.time)
    },
    onDateSelectY(value) {
      this.date[0] = this.yItems[value].slice(0, -2)
      console.log(this.date)
    },
    onDateSelectM(value) {
      const temp = this.mItems[value].slice(0, -2)
      if (temp < 10) {
        this.date[2] = '0' + temp
      } else {
        this.date[2] = temp
      }
      console.log(this.date)
    },
    onDateSelectD(value) {
      const temp = this.dItems[value].slice(0, -2)
      if (temp < 10) {
        this.date[4] = '0' + temp
      } else {
        this.date[4] = temp
      }
      console.log(this.date)
    },
    ...mapActions(['postImage']),
  },
  computed: {
    ...mapGetters(['getId', 'getCategory', 'getColor', 'getImgUrl'])
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
  .select-year {
    width: 100px;
    margin: 3px 5px 5px;
    height: 1.5rem;
  }
  .select-month, .select-day, .select-time {
    width: 80px;
    margin: 3px 5px 5px;
    height: 1.5rem;
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
  }
  .right-wrapper {
    border: 1px solid black;
    float: left;
    width: 20em;
    padding: 10px;
    text-align: initial;
  }
  .img-wrapper {
    margin: 5px; 
  }
  .category-wrapper, .date-wrapper, .img-wrapper, .time-wrapper, .input-wrapper {
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
  .password, .email{
    margin: 15px;
  }
  .input-password-email {
    border: none;
    width: 90%;
    border-bottom: black 1px solid;
    margin: 10px;
  }
  .description {
    font-size: 1rem;
    margin: 0 15px 0px 10px;
    word-break: keep-all;
  }
  .submit-btn {
    text-align: center;
  }
</style>