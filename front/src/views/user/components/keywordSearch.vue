<template>
  <div class="keyword-search-wrapper">
    <navbar />
    <div class="keyword-search-container">
      <div class="title-container">
        <span class="unselected" @click="go('/')">
          이미지 검색
        </span>
        <span class="selected">
          상세검색
        </span>
      </div>
      <div class="keyword-search-card">
        <div class="keyword-search-select-container">
          <span class="keyword-search-select-category">
            분류
            <selectOne :items="categories" :default="categoryDefault" @input="updateInput"/>
          </span>
          <span class="keyword-search-select-color">
            색상
            <selectOne :items="colors" :default="colorDefault" @input="updateInput"/>
          </span>
          <span class="keyword-search-select-location">
            예상분실위치
            <span @click="showModal()">
              <buttonDefault
                :text="btnText2"
                :bgColor="white"
                :txtColor="txtColor"
              />
            </span>
          </span>
        </div>
        <div class="keyword-search-button">
          <span @click="go('test')">
            <buttonHuge
              :text="btnText"
              :bgColor="bgColor"
              :txtColor="txtColor"
            />
          </span>
        </div>
      </div>
      <div v-if="isClicked" class="keyword-search-modal">
        <modalMap @exit_Clicked="exit_Modal" />
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar.vue";
import selectOne from "@/components/common/dropdown/selectOne.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
import modalMap from "@/components/common/modal/modalMap.vue";
import buttonDefault from "@/components/common/button/buttonDefault.vue";
export default {
  name: "keywordSearch",
  components: {
    navbar,
    selectOne,
    buttonHuge,
    modalMap,
    buttonDefault,
  },
  data() {
    return {
      categoryDefault: "분류를 선택해주세요",
      colorDefault: "색상을 선택해주세요",
      btnText: "검색",
      btnText2: "클릭하여 지도확인",
      bgColor: "#0A95FF",
      txtColor: "black",
      isClicked: false,
      inputColor:'',
    };
  },
  computed: {
    categories() {
      return this.$store.state.categories;
    },
    colors() {
      return this.$store.state.colors;
    },
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
    showModal(index) {
      console.log(index+'게시글 모달 띄우기')
      this.isClicked = true;
    },
    exit_Modal(flag) {
      this.isClicked = !flag;
    },
  },
};
</script>

<style scoped>
.keyword-search-wrapper {
  margin-top: 250px;
  justify-content: center;
  align-items: center;
  display: flex;
}
.keyword-search-card {
  height: 2em;
  margin-top: 10px;
  border: 1px solid black;
  height: 300px;
  border-radius: 40px;
}
.keyword-search-container {
  width: 40%;
}
.keyword-search-select-container {
  margin: 10%;
  display: grid;
  height: 100%;
  align-items: center;
  grid-template-rows: repeat(6, 15%);
  grid-template-columns: repeat(4, 25%);
}
.keyword-search-select-category {
  grid-column: 1/3;
  grid-row: 1/1;
  font-size: 1.5rem;
  font-weight: bold;
}
.keyword-search-select-color {
  grid-column: 1/3;
  grid-row: 3/3;
  font-size: 1.5rem;
  font-weight: bold;
}
.keyword-search-select-location {
  grid-column: 3/5;
  grid-row: 1/1;
  font-size: 1.5rem;
  font-weight: bold;
}

.keyword-search-button {
  position: absolute;
  bottom: 5%;
  right: 20%;
}
.keyword-search-card-container {
  /* margin-top: 100px; */
  justify-content: space-between;
  display: flex;
}

/* searchbar */
.custom-select {
  height: 2.5rem;
  width: 80%;
}

.title-container {
  display: flex;
  justify-content: space-between;
}

.selected {
  color: rgb(255, 255, 255);
  background-color: rgb(39, 39, 39);
  padding: 0.5em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
}
.unselected {
  padding: 0.5em;
  margin-bottom: 1em;
  font-size: 1.25em;
  border: 1px solid #ebebeb;
  /* border-bottom-color: #e2e2e2; */
  border-radius: 20px;
  color: black;
  background-color: white;
}

.unselected:hover {
  box-shadow: 2px 2px 10px 0 grey;
  border: 1px solid #ebebeb;
  border-radius: 20px;
  outline: none;
}
.unselected:active {
  box-shadow: inset 0 0 5px grey;
  border: 1px solid #ebebeb;
  outline: none;
}
</style>
