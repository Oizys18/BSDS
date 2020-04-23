<template>
  <div class="search-container">
    <input class="search-input" placeholder="검색어 즈려주세요 ex)가방,모자" />
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
  height: 2rem;
  border: 1px solid black;
  padding: 0px 0px 0px 15px;
  border-radius: 17px;
  justify-content: space-between;
  align-items: center;
  display: flex;
  font-size: 1.5rem;
}
.search-input {
  border: none;
  width: 80%;
  height: 70%;
}
.search-button {
  width: 15%;
  height: 100%;
  border: none;
  position: relative;
  border-left: 1px solid black;
  background: none;
  justify-content: space-evenly;
  display: flex;
}
.material-icons {
  font-size: 1rem;
}

</style>
