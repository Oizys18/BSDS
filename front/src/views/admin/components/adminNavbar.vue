<template>
  <div class="navbar-container">
    <img @click="go({name: 'adminIndex'})" src="@/assets/images/mainlogo.png">
<!--    <div class="logo-shadow">-->
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: "adminNavbar",
  methods: {
    go(path) {
      this.$router.push(path)
    }
  },
};
</script>

<style scoped>
  .navbar-container {
    /* position */
    position: absolute;
    top: 4vh;
    left: 15vw;

    /* shape and style */
    height: 10%;
    width: 70%;
  }
  img {
    max-height: 100%;
  }
  .logo-shadow {
    height: 100%;
    width: 40%;
    border-style: solid;
    border-image: linear-gradient(to right, #FF5F7A 0%, #3AB795 100%);
    border-image-slice: 1;
    border-image-width: 0 0 0.3 0px;
    margin-bottom: 5px;
  }
</style>
