<template>
  <form class="search-wrapper" action="">
    <div class="search-container">
      <div class="search-icon">
        <span class="material-icons"> search </span>
      </div>
      <input v-model="input" class="search-input" :placeholder="inputText" />
    </div>
    <button class="search-button">검색</button>
  </form>
</template>

<script>
export default {
  name: "searchBar",
  data() {
    return {
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
  width: 90%;
  height: 100%;
  border: 1px solid black;
  padding: 0px 0px 0px 15px;
  border-radius: 20px;
  justify-content: space-around;
  align-items: center;
  display: flex;
}
.search-input {
  border: none; 
  width: 70%;
  height: 70%;
  font-size: 2rem;
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
  width: 9%;
  height: 100%;
  justify-content: center;
  align-items: center;
  display: flex;
  font-size: 1.5rem;
  border: 1px solid black;
  margin-left: 1%;
  border-radius: 20px;
  background-color: white;
}
.material-icons {
  font-size: 50px;
}
</style>
