<template>
  <div class="navbar-container">
    <div class="logo-shadow">
    <img @click="go({name: 'adminIndex'})" src="@/assets/images/mainlogo.png">
    </div>
  </div>
</template>

<script>
export default {
  name: "adminNavbar",
  methods: {
    go(path) {
      this.$router.push(path)
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
    height: 130px;
    width: 100%;
    /*background-color: whitesmoke;*/
    /*box-shadow: 0 0 5px;*/

    /* content align */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  img {
    max-height: 80%;
  }
  .logo-shadow {
    height: 90%;
    width: 40%;
    /*border-bottom: 1px solid #3AB795;*/
    border-style: solid;
    border-image: linear-gradient(to right, #FF5F7A 0%, #3AB795 100%);
    border-image-slice: 1;
    border-image-width: 0 0 0.3 0px;
    margin-bottom: 5px;
  }
</style>
