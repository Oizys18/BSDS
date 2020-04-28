<template>
  <div class="search-wrapper">
    <div class="search-container">
      <span class="material-icons"> search </span>
      <input v-model="input" class="search-input" :placeholder="inputText" />
    </div>
            <buttonHuge
          class="search-button"
          @click="imgSearch()"
          v-if="!searched"
          :text="btnText3"
          :bgColor="bgColor2"
          :txtColor="txtColor"
        />
  </div>
</template>

<script>
import buttonHuge from "@/components/common/button/buttonHuge.vue";
export default {
  name: "searchBar",
  components:{
    buttonHuge,
  },
  data() {
    return {
      btnText3: "검색",
      bgColor2: "white",
      txtColor: "black",
      input: "",
    };
  },
  props: {
    inputText: {
      type: String,
      required: true,
      default: "No input",
    },
  },
  methods: {
    search() {},
  },
};
</script>

<style scoped>
.search-wrapper {
  height: 5vh;
  width: 100%;
  justify-content: space-around;
  align-items: center;
  display: flex;
}
.search-container {
  width: 100%;
  height: 2em;
  display: flex;
  color: rgb(100, 100, 100);
  font-size: 1.3em;
  padding-left: 10px;
  justify-content: flex-start;
  align-items: center;
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
}
input.search-input {
  border: none;
  width: 100%;
  height: 70%;
  font-size:1.3em;
  margin-right: 10%;
}

.search-icon {
  border: none;
  display: flex;
  justify-content: flex-start;
  background: none;
  position: relative;
}
.search-button {
  background-color: #fdfdfd;
  cursor: pointer;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
  width: 10%;
  display: flex;
  justify-content: center;
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
