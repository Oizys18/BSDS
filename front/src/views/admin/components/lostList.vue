<template>
  <div>
      분실신고 목록 즈림
    <table id="lost-table">
      <thead>
        <tr>
          <th>관리번호</th>
          <th>사진</th>
          <th>분류</th>
          <th>추정 분실일</th>
          <th>추정 분실 시각</th>
          <th>조회</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in calData" :key="item.id">
          <td>{{item.id}}</td>
          <td>{{item.image}}</td>
          <td>{{item.category}}</td>
          <td>{{item.date}}</td>
          <td>{{item.time}}</td>
          <td><button-default :text="'조회'" /></td>
        </tr>
      </tbody>
    </table>
    <div>
      <span @click="prevPage">
        <button-default :text="'prev'" :bgColor="btnPrev" />
      </span>
      <span v-for="num in numOfPages" :key="num" @click="onClickPage(num)">
        <button-default :text="num" />
      </span>
      <span @click="nextPage">
        <button-default :text="'next'" :bgColor="btnNext" />
      </span>
    </div>
  </div>
</template>

<script>
import buttonDefault from "@/components/common/button/buttonDefault"
export default {
  name: "lostList",
  components: {
    buttonDefault
  },
  data() {
    return {
      pageNum: 1,
      pageSize: 5,
      items: [{
          "id": 1,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 2,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 3,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 4,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 5,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 6,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 7,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 8,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 9,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
        }, {
          "id": 10,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
          "time": "13001500"
      }]
    }
  },
  created() {
    console.log(this.pageNum)
  },
  methods: {
    nextPage() {
      if (this.pageNum < this.numOfPages) {
        this.pageNum += 1
      }
    },
    prevPage() {
      if (this.pageNum > 1) {
        this.pageNum -= 1
      }
    },
    onClickPage(num) {
      this.pageNum = num
    }
  },
  computed: {
    startPage() {
      return (this.pageNum - 1)*this.pageSize
    },
    endPage() {
      return (this.startPage + this.pageSize)
    },
    numOfPages() {
      return Math.ceil(this.items.length / this.pageSize)
    },
    calData() {
      return this.items.slice(this.startPage, this.endPage)
    },
    btnPrev() {
      return (this.pageNum > 1) ? "default" : "grey"
    },
    btnNext() {
      return (this.pageNum < this.numOfPages) ? "default" : "grey"
    }
  }
}
</script>