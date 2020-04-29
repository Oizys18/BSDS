<template>
  <div id="paginatedList-wrapper">
    <div id="card-container">
      <div
        @click="showModal(index)"
        v-for="(item, index) in calData"
        :key="index.id"
        class="card-list"
      >
        <card-big
          :image="item.thumbnail.length ? `${baseurl}${item.thumbnail}` : imagesrc"
          :content="item.created"
          />
      </div>
    </div>
    <div class="list-page-btn">
      <span @click="prevPage" :key="btnPrev">
        <button-default :text="'prev'" :bgColor="btnPrev" />
      </span>
      <span v-for="num in numOfPages" :key="num" @click="onClickPage(num)">
        <button-default :text="num.toString()" />
      </span>
      <span @click="nextPage" :key="btnNext">
        <button-default :text="'next'" :bgColor="btnNext" />
      </span>
    </div>
    <div v-if="isClicked" class="index-modal">
      <modalHuge @exit_Clicked="exit_Modal" />
    </div>
  </div>
</template>

<script>
import buttonDefault from "@/components/common/button/buttonDefault"
import cardBig from "@/components/common/card/cardBig";
import modalHuge from "@/components/common/modal/modalHuge";
export default {
  name: "paginatedCard",
  components: {
    buttonDefault,
    cardBig,
    modalHuge
  },
  props: {
    items: Array,
    pageSize: {
      type: Number,
      default: 6
    }
  },
  data() {
    return {
      pageNum: 1,
      imagesrc: `${this.baseurl}media/no_image.png`,
      isClicked: false
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
    },
    showModal(index) {
      this.isClicked = true;
      console.log(index + "번 게시글 모달 생성");
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
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
    },
    baseurl() {
      console.log(this.$store.state.baseURL);
      return this.$store.state.baseURL;
    },
  }
}
</script>

<style scoped>
  #card-container {
    display: grid;
    width: 40%;
    grid-template-rows: repeat(4, 210px);
    grid-template-columns: repeat(2, 360px);
    justify-content: space-around;
    align-items: center;
    margin: 10px;
  }
  #paginatedList-wrapper {
    width: 100%;
    height: 100%;
    margin-top: 60px;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    display: flex;
    flex-wrap: wrap;
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
  .card-list {
    margin: auto;
    display: flex;
    box-sizing: border-box;
  }
</style>