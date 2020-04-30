<template>
  <div id="paginatedList-wrapper">
    <div id="card-container">
      <div
        @click="showModal(index) + getDetailFound(item.id)"
        v-for="(item, index) in calData"
        :key="index.id"
        class="card-list"
      >
        <card-big
          :image="item.thumbnail.length ? `${baseurl}${item.thumbnail}` : `${baseurl}${imagesrc}`"
          :content="item.created.slice(0, 10)"
          :title="getUserInfo.parent_department + ' ' + getUserInfo.center_name + getUserInfo.role"
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
      <modal-props @exit_Clicked="exit_Modal" :data="getData"/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"
import buttonDefault from "@/components/common/button/buttonDefault"
import cardBig from "@/components/common/card/cardBig";
import modalProps from "@/components/common/modal/modalProps";
export default {
  name: "paginatedCard",
  components: {
    buttonDefault,
    cardBig,
    modalProps
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
      imagesrc: `media/no_image.png`,
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
    ...mapActions(["getDetailFound"])
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
    ...mapGetters(["getData", "getUserInfo"])
  }
}
</script>

<style scoped>
  #card-container {
    display: grid;
    width: 40%;
    grid-template-rows: repeat(3, 210px);
    grid-template-columns: repeat(2, 360px);
    justify-content: space-around;
    align-items: center;
    margin: 10px;
  }
  #paginatedList-wrapper {
    width: 100%;
    height: 100%;
    margin-top: 150px;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    display: flex;
    flex-wrap: wrap;
  }
  .list-page-btn {
    /*position: absolute;*/
    /*bottom: 5%;*/
    /*left: 50%;*/
    /*transform:translateX(-50%);*/
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