<template>
  <div class="search-lost-wrapper">
    <navbar />
    <div class="search-lost-container">
      <div class="search-lost-title">신고 번호를 입력해주세요</div>
      <div class="search-container">
        <span class="search-header">아이디</span>
        <input v-model="lostname" class="search-input" :type="idType" />
      </div>
      <div class="search-container">
        <span class="search-header">비밀번호</span>
        <input v-model="password" class="search-input" :type="pwType" />
      </div>
      <div class="search-button" @click="search">
        <buttonHuge :text="btnText" />
      </div>
    </div>
    <div v-if="this.$store.state.showModal" class="user-index-modal">
      <modalProps :data="item" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import navbar from "@/views/user/components/navbar.vue";
import modalProps from "@/components/common/modal/modalProps.vue";
import buttonHuge from "@/components/common/button/buttonHuge.vue";
export default {
  name: "searchLost",
  components: {
    navbar,
    buttonHuge,
    modalProps
  },
  data() {
    return {
      idType: "id",
      pwType: "password",
      btnText: "조회",
      lostname: "",
      password: "",
      item: Object,
      baseurl: process.env.VUE_APP_BASE_URL
    };
  },
  watch: {
    $route() {
      this.$store.state.showModal = false;
    }
  },
  methods: {
    search() {
      this.$store.state.loading = true;
      let data = { lostname: this.lostname, password: this.password };
      axios
        .post(this.baseurl + "lost/", data)
        .then(res => {
          this.$store.state.loading = false;
          this.item = res.data;
          this.$store.state.showModal = true;
        })
        .catch(err => {
          this.$store.state.loading = false;
          console.log(err);
        });
    }
  }
};
</script>

<style scoped>
.search-lost-wrapper {
  justify-content: center;
  align-items: center;
  display: flex;
  margin-top: 25vh;
}
.search-lost-title {
  font-size: 1.5em;
  margin: 0.5em;
}
.search-lost-container {
  width: 35%;
  color: rgb(37, 37, 37);
  font-size: 1em;
  background-color: #fdfdfd;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}
.search-header {
  justify-content: flex-start;
  display: flex;
  width: 50%;
}
.search-container {
  margin: 15px;
  height: 2em;
  width: 60%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: rgb(36, 36, 36);
  font-weight: bold;
  font-size: 1.3em;
  padding-left: 10px;
  background-color: #fdfdfd;
  border: 1px solid #ebebeb;
  border-bottom-color: #e2e2e2;
  border-radius: 20px;
  overflow: hidden;
}

input.search-input {
  border: none;
  width: 60%;
  height: 70%;
  align-items: center;
  font-size: 0.8em;
  margin-right: 10%;
  outline: none;
}
.search-button {
  margin: 15px;
}
</style>
