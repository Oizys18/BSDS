<template>
  <div>
    <login-form />
  </div>
</template>

<script>
  import loginForm from "./loginForm";
  export default {
    name: 'adminLogin',
    components: {
      loginForm
    }
  }
</script>