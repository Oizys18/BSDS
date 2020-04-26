<template>
  <div>
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
</template>

<script>
  import buttonDefault from "../../../components/common/button/buttonDefault";
  export default {
    name: "adminDdiyong",
    components: {
      buttonDefault
    },
    data() {
      return {
        btn1: "습득물 등록",
        btn2: "작성한 글 목록",
        btn3: "분실신고 목록"
      }
    },
    methods: {
    go(path) {
      this.$router.push({name: path})
    }
  }
  }
</script>