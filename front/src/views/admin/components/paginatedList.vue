<template>
  <div>
    <div>{{ pageHead }}</div>
    <div id="table-wrapper">
    <table class="table">
      <thead>
        <tr>
          <th
            v-for="(header, idx) in itemHeader"
            :key="idx">
            {{ header }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in calData" :key="item.id">
          <td>{{item.id}}</td>
          <td class="img-cell" >
            <img
              :src="item.thumbnail.length > 0
              ? `http://8c6a607d.ngrok.io/${item.thumbnail}`
              : 'http://8c6a607d.ngrok.io/media/no_image.png'">
          </td>
          <td>{{ item.category }}</td>
          <td>{{ item.created }}</td>
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
  name: "paginatedList",
  components: {
    buttonDefault
  },
  props: {
    items: Array,
    itemHeader: Array,
    pageHead: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      pageNum: 1,
      pageSize: 3,
      imagesrc: 'media/no_image.png',
    }
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
  #table-wrapper {
    width: 100%;
    height: 100%;
    margin-top: 150px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  .table {
    width: 60%;
    margin: 15px
  }
  th {
    height: 50px;
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
  .list-page-btn > span {
    /*pointer-events: none;*/
  }
</style>