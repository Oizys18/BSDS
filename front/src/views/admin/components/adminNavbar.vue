<template>
  <div class="navbar-container">
    <h1 @click="go('/')">분실둥실</h1>
    <div class="navbtn-wrapper">
      <span @click="go('create')">
        <buttonDefault :text="btnText" />
      </span>
      <span @click="go('/found')">
        <buttonDefault :text="btnText2" />
      </span>
      <span @click="go('/searchlost')">
        <buttonDefault :text="btnText3" />
      </span>
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
      btnText2: "습득물 목록",
      btnText3: "분실신고조회",
    };
  },
  components: {
    buttonDefault,
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
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

.navbtn-wrapper {
  position: absolute;
  right: 0;
}
</style>
