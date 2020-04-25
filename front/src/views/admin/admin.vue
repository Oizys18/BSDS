<template>
  <div>
    <h1>Admin Index</h1>
    <span @click="go('createFound')">
    <button-default :text="btn1" />
    </span>
    <span @click="go('lostList')">
    <button-default :text="btn2" />
    </span>
  </div>
</template>

<script>
import buttonDefault from '@/components/common/button/buttonDefault'
export default {
  name: "adminIndex",
  components: {
    buttonDefault
  },
  data() {
    return {
      btn1: "습득물 등록",
      btn2: "분실신고 목록"
    }
  },
  methods: {
    go(path) {
      this.$router.push({name: path})
    }
  }
}
</script>

<style>

</style>