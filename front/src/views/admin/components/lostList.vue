<template>
  <div>
    <admin-navbar />
    <div v-if="getItemSize > 0">
      <paginated-lost :pageHead="'분실신고 목록'" :items="getItems" :page-size="9"/>
    </div>
    <div v-else></div>
  </div>
</template>

<script>
  import  { mapState, mapGetters } from 'vuex'
  import adminNavbar from "./adminNavbar";
  import paginatedLost from "./paginatedLost";
  export default {
    name: "lostList",
    components: {
      paginatedLost,
      adminNavbar
    },
    data() {
      return {
      }
    },
    computed: {
      ...mapGetters(["getItemSize", "getItems"]),
      ...mapState(["documents"])
    },
    mounted() {
      this.$store.dispatch('getLostList')
    }
  }
</script>

<style scoped>

</style>