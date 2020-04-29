<template>
  <div class="navbar-container">
    <img @click="go('admin')" src="@/assets/images/mainlogo.png">
  </div>
</template>

<script>
export default {
  name: "adminNavbar",
  data() {
  },
  components: {

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
    position: absolute;
    left: 15%;
  }
</style>
