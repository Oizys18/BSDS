<template>
  <div class="keyword-search-wrapper">
    <navbar />
    <div class="keyword-search-container">
      <div class="title-container">
        <span class="unselected" @click="go('/')">이미지 검색</span>
        <span class="selected">상세 검색</span>
      </div>
      <div class="search-card">
        <div class="selectors">
          <span class="selector">
            <label for="selectcategory">분류</label>
            <span id="selectcategory">
              <selectOne
                :items="categories"
                :default="categoryDefault"
                @input="updateCategory"
              />
            </span>
          </span>
          <span class="selector">
            <label for="selectcolor">색상</label>
            <span id="selectcolor">
              <selectOne
                :items="colors"
                :default="colorDefault"
                @input="updateColor"
              />
            </span>
          </span>
          <span class="selector">
            <label for="selectdate">날짜</label>
            <span id="selectdate">
              <input
                type="date"
                name="lostdate"
                id="lostdate"
                v-model="inputDate"
              />
            </span>
          </span>
        </div>
        <div class="search-address">
          <label for="addressinput">예상 분실위치</label>
          <div>
            <input id="addressinput" type="text" v-model="addressInput" />
            <span @click="searchAddress">
              <buttonDefault
                :text="btnText2"
                :bgColor="bgColor"
                :txtColor="txtColor"
              />
            </span>
          </div>
          <div class="search-results">
            <span class="results" v-for="result in results" :key="result.id">
              <span @click="showModal(result)">{{
                result.address.address_name
              }}</span>
            </span>
          </div>
        </div>
      </div>
      <div class="keyword-search-button">
        <span @click="categorySearch">
          <buttonHuge :text="btnText" :bgColor="bgColor" :txtColor="txtColor" />
        </span>
        <br />
        <span class="errorMsg" v-if="errorMSG"
          >결과물이 없습니다! <br />더 자세한 정보를 입력하거나 분류를
          확인해주세요.</span
        >
      </div>

      <div v-if="this.$store.state.showModal" class="keyword-search-modal">
        <modalMap @exit_Clicked="exit_Modal" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
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
      btnText2: "주소검색",
      bgColor: "white",
      txtColor: "black",
      inputColor: "",
      inputDate: "",
      addressInput: "",
      results: "",
      showing: "",
      errorMSG: false,
      baseurl: process.env.VUE_APP_BASE_URL,
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
  mounted() {
    this.$store.state.showModal = false;
  },
  methods: {
    searchAddress() {
      axios
        .get("https://dapi.kakao.com/v2/local/search/address.json", {
          params: {
            query: this.addressInput,
          },
          headers: {
            Authorization: "KakaoAK f8d38a34b065785c71e6beed1528657f",
          },
        })
        .then((res) => {
          this.results = res.data.documents.slice(0, 5);
        });
    },
    categorySearch() {
      this.$store.state.loading = true;
      axios
        .get(this.baseurl + "found/search/", {
          params: {
            category: this.inputCategory,
            color: this.inputColor,
            created: this.inputDate,
            x: this.$store.state.locationX,
            y: this.$store.state.locationY,
          },
        })
        .then((res) => {
          this.$store.state.loading = false;
          if (res.data.documents[0]) {
            this.$store.state.documents = res.data.documents;
            this.go("/found");
          } else {
            this.errorMSG = true;
          }
        });
    },
    go(path) {
      this.$router.push(path);
    },
    checkModal() {
      if (this.$store.state.showModal) {
        this.$store.state.showModal = false;
      } else {
        this.$store.state.showModal = true;
      }
    },
    showModal(e) {
      if (this.showing != e) {
        this.$store.state.locationX = e.x;
        this.$store.state.locationY = e.y;
      }
      this.showing = e;
      this.checkModal().then((this.$store.state.showModal = true));
    },
    exit_Modal() {
      this.$store.state.showModal = false;
    },
    updateCategory(e) {
      this.inputCategory = e;
    },
    updateColor(e) {
      this.inputColor = e;
    },
  },
  watch: {
    $route() {
      this.$store.state.showModal = false;
    },
  },
};
</script>

<style scoped>
#addressinput{
  border:1px solid black;
  border-radius: 15px;
  padding:0.25em;
  width:60%;
  outline:none;
}
.navbar-container {
  /* position */
  position: absolute;
  top: 160px;
  left: 40vw;

  /* shape and style */
  height: 20%;
  width: 20%;
}
.errorMsg {
  color: red;
}
.keyword-search-wrapper {
  margin-top: 300px;
  justify-content: center;
  align-items: center;
  display: flex;
}
.search-card {
  border: 1px solid #b4b4b4;
  height: 300px;
  border-radius: 40px;
  justify-content: space-around;
  align-items: center;
  display: flex;
}
.selectors {
  width: 50%;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}
.selector {
  padding: 0.5em;
  align-items: center;
  width: 100%;
  justify-content: center;
  display: flex;
  flex-direction: row;
}
.selector label {
  padding: 1em;
  font-size: 1.3em;
}
.selector input {
  padding: 0.7em;
  border-radius: 15px;
  border: 1px solid black;
}
.keyword-search-container {
  width: 40%;
  justify-content: center;
}
.search-address {
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 50%;
}
.selector #selectdate input{
  width:150px;
}
.search-address label {
  padding: 0.1em;
  font-size: 1.3em;
}
.search-address input {
  font-size: 1em;
}
.search-results {
  margin: 5px;
  width: 65%;
  height: 130px;
  background: white;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  padding: 5px;
}
.search-results span {
  font-size: 1em;
  color: rgb(70, 70, 255);
}
.search-results span:hover {
  font-weight: bold;
  color: blue;
}
.keyword-search-button {
  position: relative;
}

/* searchbar */
.custom-select {
  height: 2.5rem;
  width: 100%;
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
