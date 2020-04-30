<template>
<div>
  <admin-navbar />
  <div class="container">
    <p class="created-message">
      {{ createdMessage }}
    </p>
    <div class="go-index-button">
      <span @click="go('/admin')">
        <button-huge :text="'첫 페이지로'" />
      </span>
    </div>
  </div>  
</div>
</template>

<script>
import adminNavbar from '@/views/admin/components/adminNavbar'
import buttonHuge from '@/components/common/button/buttonHuge'
export default {
  name: 'created-page',
  components: {
    buttonHuge,
    adminNavbar
  },
  data() {
    return {
      createdMessage: '습득물 등록이 정상적으로 완료되었습니다.'
    }
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
    right: 20%;
  }
  .container {
    margin-top: 150px;
    display: flex;
  }
  .created-message {
    position: absolute;
    left: 20%;
    font-size: 1em;
  }
</style>