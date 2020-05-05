<template>
  <div class="navbar-container">
    <img class="logo" @click="go('/')" src="@/assets/images/mainlogo.png" />
    <div class="navbtn-wrapper">
      <span @click="go('/')" class="nav-btn">
        <buttonDefault :text="btnText4" />
      </span>
      <span @click="go('create')" class="nav-btn">
        <buttonDefault :text="btnText" />
      </span>
      <span @click="go('/searchlost')" class="nav-btn">
        <buttonDefault :text="btnText3" />
      </span>
      <span @click="go('/found')" class="nav-btn">
        <buttonDefault :text="btnText2" />
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
      btnText4: "분실물 검색",
      btnText: "분실물 등록",
      btnText3: "내 글 보기",
      btnText2: "습득물 조회",
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
  top: 8vh;
  left: 40vw;

  /* shape and style */
  height: 10%;
  width: 20%;
}

img {
  max-height: 100%;
}
.navbtn-wrapper {
  padding: 0.7em;
  border-radius: 15px;
  position: fixed;
  top: 30%;
  left: 10%;
  display: flex;
  flex-direction: column;
  border: 2px solid #c2c2c2;
}
.nav-btn {
  border: 1px solid grey;
  border: none;
  color: #606060;
  font-size: 1rem;
  font-weight: bold;
  margin: 3px 10px 10px 10px;
}

</style>
