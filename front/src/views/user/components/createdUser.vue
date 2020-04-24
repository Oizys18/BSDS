<template>
<div>
  <navbar />
  <div class="container">
    완료 웅앵
    <div class="go-index-button">
      <span @click="go('/')">
        <button-huge :text="'첫 페이지로'" />
      </span>
    </div>
  </div>  
</div>
</template>

<script>
import buttonHuge from '@/components/common/button/buttonHuge'
import navbar from '@/views/user/components/navbar'

export default {
  name: 'created-user',
  components: {
    buttonHuge,
    navbar
  },
  methods: {
    go(path) {
      this.$router.push(path);
    },
  },
}
</script>

<style scoped>
  .go-index-button {
    position: absolute;
    bottom: 5%;
    right: 5%;
  }
  .container {
    margin-top: 150px;
    display: flex;
  }
</style>