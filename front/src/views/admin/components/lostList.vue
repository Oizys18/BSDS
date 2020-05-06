<template>
  <div>
    <admin-navbar />
    <div v-if="getItemSize > 0" class="animated fadeIn faster">
      <paginated-list
        :pageHead="'분실신고 목록'"
        :items="getItems"
        :page-size="9"
      />
    </div>
    <div v-else></div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import adminNavbar from "./adminNavbar";
import paginatedList from "./paginatedList";
export default {
  name: "lostList",
  components: {
    paginatedList,
    adminNavbar,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["getItemSize", "getItems"]),
    ...mapState(["documents"]),
  },
  mounted() {
    this.$store.dispatch("getLostList");
  },
};
</script>

<style scoped></style>
