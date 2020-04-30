<template>
  <div class="navbar-container">
    <div class="logo-shadow">
    <img class="logo" @click="go('/')" src="@/assets/images/mainlogo.png">
      </div>
    <div class="navbtn-wrapper">
      <span @click="go('create')">
        <buttonDefault class="nav-btn" :text="btnText" />
      </span>
      <span @click="go('/found')">
        <buttonDefault class="nav-btn" :text="btnText2" />
      </span>
      <span @click="go('/searchlost')">
        <buttonDefault class="nav-btn" :text="btnText3" />
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
  margin-top: 20px;
  top: 0;
  left: 0;

  /* shape and style */
  height: 10%;
  width: 100%;
  /*background-color: whitesmoke;*/
  /*box-shadow: 0 0 5px;*/

  /* content align */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 20px;
}

/*.navbtn-wrapper {*/
/*  position: absolute;*/
/*  right: 20%;*/
/*}*/

.logo {
  margin-bottom: 15px;
  /*align-self: center;*/
  /*justify-self: baseline;*/
  /*border-bottom: white;*/

}
.logo-shadow {
  height: 100%;
  width: 40%;
  border-style: solid;
  border-image: linear-gradient(to right, #FF5F7A 0%, #3AB795 100%);
  border-image-slice: 1;
  border-image-width: 0 0 0.3 0px;
  /*border-bottom: 1px solid #ffccd5;*/
  margin-bottom: 5px;
}
  img {
    max-height: 90%;
  }
  .nav-btn {
    border: none;
    color: #3AB795;
    font-size: 1rem;
    font-weight: bold;
    margin: 3px 10px 10px 10px;
  }
  .nav-btn:hover {
    box-shadow: 2px 2px 10px 0 #3AB795;
  }
</style>
