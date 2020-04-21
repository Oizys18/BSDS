<template>
  <div class="search-container">
    <input class="search-input" placeholder="검색어 즈려주세요 ex)솔지하투" />
    <button class="search-button">
      <span class="material-icons"> search </span>검색
    </button>
  </div>
</template>

<script>
export default {
  name: "searchBar",
};
</script>

<style scoped>
.search-container {
  width: 80%;
  border: 1px solid black;
  padding: 0px 0px 0px 15px;
  border-radius: 17px;
  height: 2rem;
  justify-content: space-between;
  align-items: center;
  display: flex;
}
.search-input {
  border: none;
  width: 65%;
  height: 1.5rem;
}
.search-button {
  border: none;
  position: relative;
  height: 2rem;
  border-left: 1px solid black;
  background: none;
  display:flex;
  font-size: 1rem;
  width:15%;
}
.material-icons {
  font-size: 1.1rem;
}
</style>
