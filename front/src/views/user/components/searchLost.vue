<template>
  <div class="search-lost-wrapper">
    <navbar />
    <div class="search-lost-container">
      <h1 class="search-lost-title">신고 번호를 입력해주세요</h1>
      <searchBar />
    </div>
  </div>
</template>

<script>
import navbar from "@/views/user/components/navbar.vue";
import searchBar from "@/components/common/search/searchBar.vue";
export default {
  name: "searchLost",
  components: {
    navbar,
    searchBar,
  },
};
</script>

<style scoped>
.search-lost-wrapper {
  justify-content: center;
  align-items: center;
  display: flex;
  margin-top: 25vh;
}
.search-lost-title{
  justify-content: flex-start;
  display: flex;
  padding: 0;
  margin-bottom: 5px;
}
.search-lost-container {
  width: 40%;
}
</style>
