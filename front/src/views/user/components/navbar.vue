<template>
  <div class="navbar-container">
    <h1>분실둥실</h1>
    <div id="navbtn-wrapper">
      <buttonDefault :text="btnText" />
      <buttonDefault :text="btnText2" />
      <buttonDefault :text="btnText3" />
    </div>
  </div>
</template>

<script>
import buttonDefault from "@/components/common/button/buttonDefault.vue";
export default {
  name: "navbar",
  data() {
    return {
      btnText: "분실물 등록",
      btnText2: "분실물 목록",
      btnText3: "분실신고조회",
    };
  },
  components: {
    buttonDefault,
  },
};
</script>

<style scoped>
.navbar-container {
  /* position */
  position: absolute;
  top: 0;
  left: 0;

  /* shape and style */
  height: 50px;
  width: 100%;
  background-color: whitesmoke;
  box-shadow: 0 0 5px;

  /* content align */
  display: flex;
  justify-content: center;
  align-items: center;
}

#navbtn-wrapper{
    position: absolute;
    right:0;
}
</style>
