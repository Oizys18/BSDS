<template>
  <div>
    <h1>Admin Index</h1>
    <span @click="go('createFound')">
    <button-default :text="btn1" />
    </span>
    <span @click="go('lostList')">
    <button-default :text="btn2" />
    </span>
    <span @click="go('login')">
      <button-default :text="btn3" />
    </span>
  </div>
</template>

<script>
import buttonDefault from '@/components/common/button/buttonDefault'

export default {
  name: "adminIndex",
  components: {
    buttonDefault,
  },
  data() {
    return {
      btn1: "습득물 등록",
      btn2: "분실신고 목록",
      btn3: "로그인"
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