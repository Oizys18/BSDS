<template>
  <div>
    <div>분실신고 목록</div>
    <div id="lost-table-wrapper">
    <table class="lost-table">
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
          <td class="img-cell">{{item.image}}</td>
          <td>{{item.category}}</td>
          <td>{{item.date}}</td>
          <td>{{item.time}}</td>
          <td><button-default :text="'조회'" /></td>
        </tr>
      </tbody>
    </table>
    </div>
    <div class="list-page-btn">
      <span @click="prevPage" :key="btnPrev">
        <button-default :text="'prev'" :bgColor="btnPrev" />
      </span>
      <span v-for="num in numOfPages" :key="num" @click="onClickPage(num)">
        <button-default :text="num" />
      </span>
      <span @click="nextPage" :key="btnNext">
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
      pageSize: 3,
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

<style scoped>
  #lost-table-wrapper {
    width: 100%;
    height: 100%;
    margin-top: 150px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  .lost-table {
    width: 60%;
    margin: 15px
  }
  th {
    height: 3em;
  }
  td {
    height: 200px;
  }
  td.img-cell {
    width: 200px;
  }
  .list-page-btn {
    position: absolute;
    bottom: 5%;
    left: 50%;
    transform:translateX(-50%);
  }
</style>