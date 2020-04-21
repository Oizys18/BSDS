<template>
  <div>
    <navbar/>
    <div id="user-index-container">
      <h1>hello</h1>
    </div>
  </div>
</template>

<script>
import navbar from "./components/navbar";
export default {
  name:'userIndex',
  components:{
    navbar
  }
}
</script>

<style>
#user-index-container{
  width:100%;
  margin:50px, 10%, 0, 10%;
}
</style>