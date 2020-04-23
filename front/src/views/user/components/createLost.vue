<template>
<div id="wrapper">
  <div class="create-form">
    <form @submit.prevent="createContent">
      <div>
      <select-one
        id="select-year"
        :items="yItems"
        @select="onTimeSelectStart"
      />
      <select-one
        id="select-month"
        :items="mItems"
        @select="onTimeSelectStart"
      />
      <select-one
        id="select-day"
        :items="dItems"
        @select="onTimeSelectStart"
      />
      </div>
      <select-one
        id="select-time"
        :items="startTimeList"
        @select="onTimeSelectStart"
      /> ~
      <select-one
        id="select-time"
        :items="endTimeList"
        @select="onTimeSelectEnd"
      />
      <div>
      <label for="file-input">
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
      <textarea
        class="content-area"
        v-model="contents"
        type="textarea"
        placeholder="필요한 내용이 있다면 입력해주세요."
        @input="onChangeInput"
      />
      <br>
      <button type="submit">등록하기</button>
    </form>
  </div>
</div>
</template>

<script>
// import router from '../router'
import selectOne from '@/components/common/dropdown/selectOne'
const axios = require('axios')

export default {
  name: 'create-form',
  components: {
    selectOne,
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
        "date": this.picker.replace(/-/g, ""),
        "time": this.startTime.replace(":", "") + this.endTime.replace(":", "")
      }
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
    },
    onChangeInput() {
      console.log(this.contents)
      console.log(this.picker)
    },
    onTimeSelectStart(value) {
      this.startTime = this.timeList[value]
    },
    onTimeSelectEnd(value) {
      this.endTime = this.timeList[value]
      console.log(this.endTime)
    }
  }
}
</script>

<style scoped>
  .content-area {
    width: 80%;
    height: 100px;
  }
  #file-input {
    display: none;
  }
  #image-upload {
    width: 10%
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
  }
  #select-time {
    width: 80px;
    margin-left: 3px;
  }
  #container {
    display: flex;
    align-items: center;
    flex-direction: column;
  }
  #wrapper {
    padding: 10px;
    width: 50%;
    border: 1px solid black;
    border-style: dotted;
    display: flex;
    flex-direction: column;
    /* align-items: center; */
    justify-content: center;
    padding: 5px 30px 30px 30px;
    margin: 10px;
  }
</style>