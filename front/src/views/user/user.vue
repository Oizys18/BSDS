<template>
  <div id="user-index-wrapper">
    <navbar />
    <div id="user-index-container">
      <h2 id="hello">이미지검색</h2>
      <searchBar/>
    </div>
  </div>
</template>

<script>
import navbar from "./components/navbar";
import searchBar from "@/components/common/search/searchBar.vue";
export default {
  name: "userIndex",
  components: {
    navbar,
    searchBar
  },
};
</script>

<style>
#user-index-wrapper {
  width: 100%;
  height: 100%;
  margin-top: 50px;
  justify-content: center;
  align-items: center;
  display: flex;
}
#user-index-container{
  justify-content: flex-start;
}
#hello{
  justify-content: flex-start;
  display: flex;
  padding:0;
  margin-top:100px;
  margin-bottom:5px;
}
</style>
