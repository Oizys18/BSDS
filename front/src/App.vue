<template>
  <div id="app">
    <fade-loader
    class="spinner"
      :loading="this.$store.state.loading"
      :height="height"
      :width="width"
    ></fade-loader>
    <router-view />
  </div>
</template>
<script>
import FadeLoader from "vue-spinner/src/FadeLoader.vue";
export default {
  name: "app",
  components: {
    FadeLoader,
  },
  data(){
    return{
      width:"10px",
      height:"10px",
    }
  }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow: hidden;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.spinner {
  width:100%;
  height:100%;
  top: 40vh;
  left: 50vw;
}
</style>
