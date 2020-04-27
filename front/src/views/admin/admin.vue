<template>
  <div>
    <h1>Admin Index</h1>
    <!-- 나중에 순서 뒤집을 것 -->
    <component :is="isLoggedIn ? 'admin-login' : 'admin-detail' "></component>
  </div>
</template>

<script>
import adminDetail from "./components/adminDetail";
import adminLogin from "./components/adminLogin";
import { mapGetters } from 'vuex'

export default {
  name: "adminIndex",
  components: {
    adminDetail,
    adminLogin,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style>

</style>