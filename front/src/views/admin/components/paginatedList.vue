<template>
  <div id="paginatedList-wrapper" class="animated fadeIn faster">
    <div class="list-page-btn">
      <span @click="prevPage" :key="btnPrev">
        <button-default :text="'이전'" :bgColor="btnPrev" />
      </span>
      <span class="list-page-btns" :key="btnPage">
        <span v-for="num in pageNumLi" :key="num" @click="onClickPage(num)">
          <span v-if="pageNum === num">
            <button-default
              :text="num.toString()"
              :bgColor="bgColor"
              :txtColor="txtColor"
            />
          </span>
          <span v-else>
            <button-default :text="num.toString()" />
          </span>
        </span>
        <span @click="nextPage" :key="btnNext">
          <button-default :text="'다음'" :bgColor="btnNext" />
        </span>
      </span>
    </div>
    <div id="card-container" :key="cardKey">
      <div
        @click="showModal() + getPresentUrl(item.id)"
        v-for="(item, index) in calData"
        :key="index.id"
      >
        <card-small
          :item="item"
          class="card-list animated delay-0.1s zoomIn faster"
        />
      </div>
    </div>
    <div v-if="this.$store.state.showModal" class="index-modal">
      <modal-props :data="getData" />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import buttonDefault from "@/components/common/button/buttonDefault";
import cardSmall from "@/components/common/card/cardSmall";
import modalProps from "@/components/common/modal/modalProps";
export default {
  name: "paginatedList",
  components: {
    buttonDefault,
    cardSmall,
    modalProps,
  },
  props: {
    items: Array,
    pageSize: {
      type: Number,
      default: 9,
    },
  },
  data() {
    return {
      cardKey: 0,
      pageNum: 1,
      btnPage: 0,
      imagesrc: `media/no_image.png`,
      isClicked: false,
      bgColor: "grey",
      txtColor: "white",
      pageNumLi: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    };
  },
  methods: {
    nextPage() {
      if (this.pageNum < this.numOfPages) {
        this.pageNum += 1;
        if (this.pageNum > 5 && this.pageNumLi[8] < this.numOfPages) {
          let result = [];
          this.pageNumLi.forEach((x) => result.push(x + 1));
          this.pageNumLi = result;
        }
        this.cardKey += 1;
        this.btnPage += 1;
      }
    },
    prevPage() {
      if (this.pageNum > 1) {
        this.pageNum -= 1;
        if (this.pageNum >= 5 && this.pageNumLi[0] > 1) {
          if (this.pageNum + 5 > this.numOfPages) {
            let max = this.numOfPages;
            this.pageNumLi = [
              max - 8,
              max - 7,
              max - 6,
              max - 5,
              max - 4,
              max - 3,
              max - 2,
              max - 1,
              max,
            ];
          } else {
            this.pageNumLi = [
              this.pageNum - 4,
              this.pageNum - 3,
              this.pageNum - 2,
              this.pageNum - 1,
              this.pageNum,
              this.pageNum + 1,
              this.pageNum + 2,
              this.pageNum + 3,
              this.pageNum + 4,
            ];
          }
        }
        this.cardKey += 1;
        this.btnPage += 1;
      }
    },
    onClickPage(num) {
      if (num < 6) {
        this.pageNumLi = [1, 2, 3, 4, 5, 6, 7, 8, 9];
      } else if (num + 5 > this.numOfPages) {
        let max = this.numOfPages;
        this.pageNumLi = [
          max - 8,
          max - 7,
          max - 6,
          max - 5,
          max - 4,
          max - 3,
          max - 2,
          max - 1,
          max,
        ];
      } else {
        this.pageNumLi = [
          num - 4,
          num - 3,
          num - 2,
          num - 1,
          num,
          num + 1,
          num + 2,
          num + 3,
          num + 4,
        ];
      }
      this.pageNum = num;
      this.cardKey += 1;
      this.btnPage += 1;
    },
    showModal() {
      this.$store.state.showModal = true;
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
    getPresentUrl(id) {
      if (window.location.href.includes("created")) {
        this.$store.dispatch("getDetailFound", id);
      } else {
        this.$store.dispatch("getDetailLost", id);
      }
    },
    ...mapActions(["getDetailFound", "getDetailLost"]),
  },
  computed: {
    startPage() {
      return (this.pageNum - 1) * this.pageSize;
    },
    endPage() {
      return this.startPage + this.pageSize;
    },
    numOfPages() {
      return Math.ceil(this.items.length / this.pageSize);
    },
    calData() {
      if (this.items.length > this.pageSize) {
        return this.items.slice(this.startPage, this.endPage);
      } else {
        return this.items;
      }
    },
    btnPrev() {
      return this.pageNum > 1 ? "default" : "grey";
    },
    btnNext() {
      return this.pageNum < this.numOfPages ? "default" : "grey";
    },
    baseurl() {
      return this.$store.state.baseURL;
    },
    ...mapGetters(["getData", "getUserInfo"]),
  },
};
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
  margin-top: 14vh;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  display: flex;
  flex-wrap: wrap;
}
.list-page-btn {
  position: fixed;
  top: 20%;
  left: 22%;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}
.list-page-btns {
  display: flex;
  flex-direction: column;
  cursor: pointer;
}
.card-list {
  margin: auto;
  display: flex;
  box-sizing: border-box;
}
</style>
