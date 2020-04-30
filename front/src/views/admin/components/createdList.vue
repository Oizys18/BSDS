<template>
  <div>
    <admin-navbar />
    <div v-if="getItemSize">
    <paginated-card :pageHead="'작성한 글 목록'" :items="getItems" :page-size="6"/>
    </div>
    <div v-else>로딩중</div>
  </div>
</template>

<script>
import  { mapState, mapGetters } from 'vuex'
import adminNavbar from "./adminNavbar";
import paginatedCard from "./paginatedCard";
export default {
  name: "createdList",
  components: {
    paginatedCard,
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