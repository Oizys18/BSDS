<template>
  <div>
    <admin-navbar />
    <div v-if="getItemSize">
    <paginated-list :pageHead="'작성한 글 목록'" :items="getItems" :page-size="9"/>
    </div>
    <div v-else></div>
  </div>
</template>

<script>
import  { mapState, mapGetters } from 'vuex'
import adminNavbar from "./adminNavbar";
import paginatedList from "./paginatedList";
export default {
  name: "createdList",
  components: {
    paginatedList,
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
    this.$store.dispatch('getCreatedList')
  }
}
</script>

<style scoped>

</style>