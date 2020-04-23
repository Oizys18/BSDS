<template>
<div id="container">
  <navbar/>
  <div id="create-form">
    <form @submit.prevent="createContent">
      <div id=left-wrapper>
        <div id="img-wrapper">
          <label for="file-input" id="image-label">
            <img id="image-upload" src="@/assets/images/camera.png">
          </label>
          <input
            id="file-input"
            ref="imageInput"
            type="file"
            accept="image/*"
            @change="onChangeImages"
          >
          <img v-if="imageUrl" :src="imageUrl"/>
        </div>

        <div id="date-wrapper">
          분실 추정 일자
          <select-one
            id="select-year"
            :items="yItems"
            @input="onTimeSelectStart"
          />
          <select-one
            id="select-month"
            :items="mItems"
            @input="onTimeSelectStart"
          />
          <select-one
            id="select-day"
            :items="dItems"
            @input="onTimeSelectStart"
          />
        </div>
        <div id="time-wrapper">
          분실 추정 시각
          <select-one
            id="select-time"
            :items="timeList"
            @input="onTimeSelectStart"
          /> ~
          <select-one
            id="select-time"
            :items="timeList"
            @input="onTimeSelectEnd"
          />
        </div>
        <div id="input-wrapper">
            <textarea
              id="content-area"
              v-model="contents"
              type="textarea"
              placeholder="필요한 내용이 있다면 입력해주세요."
              @input="onChangeInput"
            />
        </div>
      </div>
      <div id="right-wrapper">
        <!-- 비밀번호 자리 -->
        <div>
          <form>
            <input type="password">
          </form>
        </div>
      <button type="submit">등록하기</button>
      </div>
    </form>
  </div>
</div>
</template>

<script>
// import router from '../router'
import selectOne from '@/components/common/dropdown/selectOne'
import navbar from '@/views/user/components/navbar'
const axios = require('axios')

export default {
  name: 'create-form',
  components: {
    selectOne,
    navbar
  },
  data () {
    return {
      image: '',
      contents: '',
      imageUrl: null,
      yItems: [],
      mItems: ['1 월', '2 월', '3 월','4 월','5 월','6 월','7 월','8 월','9 월','10 월','11 월','12 월'],
      dItems: [],
      timeList: [],
      startTime: '',
      endTime: '',
    }
  },
  created () {
    for (let i=0; i<25; i++) {
      if (i<10) {
          this.timeList.push('0' + i.toString() + ':00') 
      } else {
          this.timeList.push(i.toString() + ':00') 
      }
    }
    for (let y=2020; y>1920; y--) {
      this.yItems.push(y.toString() + ' 년')
    }
    for (let d=1; d<32; d++) {
      this.dItems.push(d.toString() + ' 일')
    }
  },
  methods: {
    createContent () {
      const formdata = {
        "contents": this.contents,
        "imageFile": this.image,
        // "date": this.picker.replace(/-/g, ""),
        "time": this.startTime.replace(":", "") + this.endTime.replace(":", "")
      }
      console.log(this.startTime)
      axios.post('http://localhost:3001/board', this.formdata, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
      })
      .then(res => {
        console.log(res)
        console.log(formdata)
        // router.push({
        //     path:'/'
        // })
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
    onChangeInput() {
      console.log(this.contents)
      console.log(this.picker)
    },
    onTimeSelectStart(value) {
      this.startTime = this.timeList[value]
      console.log(this.startTime)
    },
    onTimeSelectEnd(value) {
      this.endTime = this.timeList[value]
    }
  }
}
</script>

<style scoped>
  #content-area {
    width: 80%;
    height: 100px;
    margin: 5px;
    padding: 10px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }
  #file-input {
    display: none;
  }
  #select-year {
    width: 100px;
    margin: 3px 5px 5px;
  }
  #select-month {
    width: 80px;
    margin: 3px 5px 5px;
  }
  #select-day {
    width: 80px;
    margin: 3px 5px 5px;
    padding: 2px;
  }
  #select-time {
    width: 80px;
    margin-left: 5px;
    padding: 2px;
  }
  #container {
    margin-top: 150px;
    /* display: table; */
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #create-form {
    overflow: hidden;
  }
  #left-wrapper {
    float: left;
    width: 900px;
    border: 1px solid black;
    margin-right: 50px;
    display: table-cell;

  }
  #right-wrapper {
    border: 1px solid black;
    float: left;
    width: 250px;
    display: table-cell;
  }
  #img-wrapper {
    margin: 5px; 
  }
  #date-wrapper, #img-wrapper, #time-wrapper, #input-wrapper {
    display: flex;
  }
  #image-label {
    display: inline;
  }
</style>