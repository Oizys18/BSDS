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
            @change="postImageUser"
          >
          <img class="image-preview" v-if="getImgUrl" :src="getImgUrl"/>
        </div>
        <div class="category-wrapper">
          <span class="select">물품 분류</span>
          <select-one
            class="select-category"
            :items="Object.values($store.state.categories)"
            :default="this.getCategory === null ? '분류' : this.getCategoryName"
            @input="onSelectCategory"
          />
          <span class="error" v-if="!checkForm(this.category)">* 필수 입력란입니다.</span>
        </div>
        <div class="category-wrapper">
          <span class="select">색상</span>
          <select-one
            class="select-category"
            :items="Object.values($store.state.colors)"
            :default="this.getColor  === null ? '색상' : this.getColor"
            @input="onSelectColor"
          />
          <span class="error" v-if="!checkForm(this.color)">* 필수 입력란입니다.</span>
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
            :default="'시각'"
            :items="timeList"
            @input="onTimeSelect"
          />
          <span class="error" v-if="!checkForm(this.time)">* 필수 입력란입니다.</span>
        </div>
        <div class="category-wrapper">
          <span class="select-location">
            분실 추정 위치
            <span @click="showModal()">
              <buttonDefault
                :text="'지도에서 위치 선택'"
                :bgColor="'white'"
                :txtColor="'txtColor'"
              />
            </span>
          </span>
          <div v-if="isClicked" class="keyword-search-modal">
            <modalMap @exit_Clicked="exit_Modal" />
          </div>
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
      <div class="right-wrapper">
        <div class="description-wrapper">
          <div class="password">
            <label for="password" class="select">비밀번호</label>
            <p class="description">등록한 비밀번호는 내용 수정 및 분실상태 변경 시 사용됩니다.</p>
            <input id="password" class="input-password-email" type="password" v-model="password">
            <span class="error" v-if="!checkPassword(this.password)">* 비밀번호는 네 글자 이상 입력해주세요.</span>
          </div>
          <div class="email">
            <label for="email" class="select">이메일</label>
            <input id="email" class="input-password-email" type="email" v-model="email" >
            <span class="error" v-if="!validEmail(this.email)">* 이메일 형식에 맞게 입력해주세요.</span>
          </div>
          <div class="email">
            <label class="select">알림 제공 동의</label>
            <p class="description">유사한 습득물 등록 시 이메일로 알림을 보내드립니다.</p>
              <div class="email-radio" data-toggle="buttons">
                <label class="box-radio-input">
                  <input type="radio" name="cp_item" value="true" v-model="do_notice">
                  <span class="check">V</span>
                  <span class="description">동의</span>
                </label>
                <label class="box-radio-input">
                  <input type="radio" name="cp_item" value="false" v-model="do_notice">
                  <span class="check">V</span>
                  <span class="description">비동의</span>
                </label>
              </div>
          </div>
        </div>
        <div class="button-wrapper">
          <div class="submit-btn" @click="createContent">
            <button-default class="user-btn" :text="'등록하기'"/>
          </div>
          <div @click="go('/')">
            <button-default class="user-btn btn-option" :text="'취소'"/>
          </div>
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
import modalMap from "@/components/common/modal/modalMap";
import {mapActions, mapGetters, mapState} from "vuex";
const axios = require('axios')

export default {
  name: 'create-lost',
  components: {
    selectOne,
    navbar,
    buttonDefault,
    modalMap
  },
  data() {
    return {
      content: '',
      category: this.getCategory,
      color: this.getColor,
      yItems: [],
      mItems: ['1 월', '2 월', '3 월', '4 월', '5 월', '6 월', '7 월', '8 월', '9 월', '10 월', '11 월', '12 월'],
      dItems: [],
      date: ['2020', '-', '01', '-', '01'],
      timeList: [],
      time: '',
      password: '',
      email: '',
      isClicked: false,
      do_notice: true,
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
    for (let y = 2020; y > 2018; y--) {
      this.yItems.push(y.toString() + ' 년')
    }
    for (let d = 1; d < 32; d++) {
      this.dItems.push(d.toString() + ' 일')
    }
  },
  methods: {
    createContent() {
      const data = {
        "image_id": this.getId,
        "category": this.getCategory,
        "color": this.getColor,
        "content": this.content,
        "lost_time":
          `${this.date.reduce(function (accumulator, currentValue) {
          return accumulator + currentValue;
          })} ${this.time}:00`,
        "email": this.email,
        "password": this.password,
        "do_notice": this.do_notice,
        "x": '',
        "y": ''
      }
      console.log(data)
      axios.post(`${this.$store.state.baseURL}lost/posting/`, data)
        .then(res => {
          console.log(res)
          this.$router.push('created')
          console.log(this.image_id)
        })
        .catch(err => {
          console.log(err)
        })

    },
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onSelectCategory(value) {
      console.log(value)
      this.category = value
    },
    onSelectColor(value) {
      this.color = value
    },
    onTimeSelect(value) {
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
    showModal(index) {
      this.isClicked = true;
      console.log(index + "번 게시글 모달 생성");
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
    validEmail(email) {
        if (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
          return true
        } else if (email.length === 0) {
          return true
        }
    },
    checkForm(value) {
      if (value) {
        return true
      }
    },
    checkPassword(password) {
      if (password.length > 3) {
        return true
      }
    },
    changeDonotice(value) {
      this.do_notice = value
    }
  ,
    ...mapActions(['postImageUser']),
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
  .select-year {
    width: 100px;
    margin-right: 10px;
  }
  .select-month, .select-day, .select-time {
    width: 80px;
    margin-right: 10px;
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
    border-radius: 2%;
    margin-right: 45px;
    margin-bottom: 30px;
    padding: 1rem;
  }
  .right-wrapper {
    float: left;
    width: 320px;

    text-align: initial;
  }
  .description-wrapper {
    border: 1px solid black;
    border-radius: 2%;
    float: left;
    width: 320px;
    padding: 10px;
    text-align: initial;
  }
  .button-wrapper {
    border: none;
    width: 320px;
    padding: 0px 10px 10px 10px;
    text-align: center;
  }
  .img-wrapper {
    margin: 5px; 
  }
  .category-wrapper, .date-wrapper, .img-wrapper, .input-wrapper {
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
  .select, .select-location {
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
  input[type="password"], input[type="email"] {
    height: 1.5rem;
  }
  .description {
    font-size: 1rem;
    margin: 5px 15px 0px 10px;
    line-height: 1.4rem;
    word-break: keep-all;
  }
  .submit-btn {
    text-align: center;
  }
  .user-btn {
    width: 300px;
    margin-top: 15px;
  }
  .btn-option {
    margin: 3px;
  }
  .error {
    font-size: 0.8rem;
    color: #FB121D;
    padding-top: 2px;
    margin: 0 15px 0px 10px;
  }
  .email-radio{
    display: flex;
    padding: 10px;
    justify-content: space-around;
  }
  .box-radio-input input[type="radio"]{
    display:none;
  }
  .box-radio-input input[type="radio"] + span{
    display:inline-block;
    background:none;
    border:1px solid #dfdfdf;
    border-radius: 10px;
    padding:0px 10px;
    text-align:center;
    height:35px;
    line-height:33px;
    font-weight:500;
    cursor:pointer;
    margin: 10px 10px 0 10px
  }
  .box-radio-input input[type="radio"]:checked + span{
    border:1px solid #0A95FF;
    background:#0A95FF;
    color:#fff;
  }


</style>