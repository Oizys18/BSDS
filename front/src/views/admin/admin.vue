<template>
  <div :key="getDetailKey">
    <admin-navbar />
    <div id="admin-index-wrapper">
      <!-- 나중에 순서 뒤집을 것 -->
      <component :is="isLoggedIn ? 'admin-detail' : 'admin-login'" />
    </div>
  </div>
</template>

<script>
import adminDetail from "./components/adminDetail";
import adminLogin from "./components/adminLogin";
import adminNavbar from "./components/adminNavbar";
import { mapGetters } from 'vuex'

export default {
  name: "adminIndex",
  components: {
    adminDetail,
    adminLogin,
    adminNavbar
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'getDetailKey'])
  }
}
</script>

<style scoped>
  #admin-index-wrapper {
    margin-top: 150px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
</style>