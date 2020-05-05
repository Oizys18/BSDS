<template>
  <div id="paginatedList-wrapper">
    <div id="card-container">
      <div
        @click="showModal() + getDetailFound(item.id)"
        v-for="(item, index) in calData"
        :key="index.id"
        class="card-list"
      >
        <card-small
          :item="item"
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
    <div v-if="this.$store.state.showModal" class="index-modal">
      <modal-props :data="getData"/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"
import buttonDefault from "@/components/common/button/buttonDefault"
import cardSmall from "@/components/common/card/cardSmall";
import modalProps from "@/components/common/modal/modalProps";
export default {
  name: "paginatedCard",
  components: {
    buttonDefault,
    cardSmall,
    modalProps
  },
  props: {
    items: Array,
    pageSize: {
      type: Number,
      default: 9
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
    showModal() {
      this.$store.state.showModal = true;
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
      if (this.items.length > this.pageSize) {
        return this.items.slice(this.startPage, this.endPage)
      } else {
        return this.items
      }
    },
    btnPrev() {
      return (this.pageNum > 1) ? "default" : "grey"
    },
    btnNext() {
      return (this.pageNum < this.numOfPages) ? "default" : "grey"
    },
    baseurl() {
      return this.$store.state.baseURL;
    },
    ...mapGetters(["getData", "getUserInfo"])
  }
}
</script>

<style scoped>
  #card-container {
    display: grid;

    grid-template-rows: repeat(3, 230px);
    grid-template-columns: repeat(3, 230px);
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