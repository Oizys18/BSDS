<template>
  <div id="admin-detail-wrapper">
    <div class="user-info">
      <span>{{ getUserInfo.parent_department }}</span>
      <span>{{ getUserInfo.center_name + getUserInfo.role }}</span>

    </div>
    <div class="page-link-button">
    <span @click="go('createFound')">
    <button-default :text="btn1" />
    </span>
    <span @click="go('createdList')">
    <button-default :text="btn2" />
    </span>
    <span @click="go('lostList')">
    <button-default :text="btn3" />
    </span>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import buttonDefault from "../../../components/common/button/buttonDefault";
export default {
  name: "adminDetail",
  components: {
    buttonDefault
  },
  data() {
    return {
      btn1: "습득물 등록",
      btn2: "작성한 글 목록",
      btn3: "분실 신고 목록"
    }
  },
  methods: {
    go(path) {
      this.$router.push({name: path})
    },
  },
  computed: {
    ...mapGetters(['getUserInfo'])
  }
}
</script>

<style scoped>


</style>