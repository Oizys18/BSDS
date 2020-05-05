<template>
    <div>
    <admin-navbar />
        <div id="admin-index-wrapper">
            <!-- 나중에 순서 뒤집을 것 -->
            <admin-login />
        </div>
    </div>
</template>

<script>
import adminLogin from "../components/adminLogin";
import adminNavbar from "../components/adminNavbar";
import { mapGetters } from 'vuex'
export default {
    name: "loginPage",
    components: {
      adminLogin,
      adminNavbar
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
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