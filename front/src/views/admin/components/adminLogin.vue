<template>
  <div>
  <admin-navbar />
  <div class="login-form animated fadeIn faster">
    <form class="login-input" >
      <div class="login-box">
        <div class="user-input">
          <span class="login-header">로그인</span>
          <input
            v-model="credentials.username"
            type="text"
            class="login-input"
            id="username"
            placeholder="아이디를 입력하세요."
          >
          <input
            v-model="credentials.password"
            type="password"
            class="login-input"
            id="password"
            placeholder="비밀번호를 입력하세요."
          >
        </div>
        <div v-if="getErrors.length" class="error-list">
        <ul class="login-error" >
          <li v-for="(error, idx) in getErrors" :key="idx">
            {{ error }}
          </li>
        </ul>
        </div>
        <div @click="login(credentials) + go({name: 'adminIndex'})" >
          <button-default class="login-btn" :text="'로그인'" />
        </div>
      </div>
    </form>
  </div>
    </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import adminNavbar from "./adminNavbar";
  import buttonDefault from "@/components/common/button/buttonDefault";
  export default {
    name: 'adminLogin',
    components: {
      buttonDefault,
      adminNavbar
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
      }
    },
    methods: {
      ...mapActions(['login']),
      async go(path) {
        await this.$router.push(path)
      }
    },
    computed: {
      ...mapGetters(['getErrors', 'isLoading', 'isLoggedIn']),
    }
  }
</script>

<style>
  .login-form {
    /*position: relative;*/
    /*width: 20%;*/
    min-width: 250px;
    height: 350px;
    padding: 30px;
    margin: 10vh auto;
    background: #fff;
    border: 1px solid #404040;
    border-radius: 8px;
    /*box-shadow: 5px 5px 12px 0px #38618C;*/
  }
  .login-box {
    width: 100%;
    height: 100%;
  }
  .login-input, .login-header {
    text-align: center;
    display: block;
  }
  .login-header {
    color: #404040;
    font-weight: bold;
    font-size: 1.4rem;
    margin: 30px auto;
  }
  .login-input {
    width: 100%;
    min-width: 200px;
    height: 45px;
    border: none;
    font-size: 1rem;
    font-weight: lighter;
    margin-bottom: 30px;
  }
  .login-input input {
    border-style: solid;
    border-image: linear-gradient(to right, #38618C 60%, rgb(10, 149, 255) 100%);
    border-image-slice: 1;
    border-image-width: 0 0 0.8 0px;
  }
  .login-input::placeholder {
    color: #38618C;
  }
  .login-error {
    list-style-type: none;
    padding: 0;
    font-size: 0.8rem;
    color: #FB121D;
    margin-bottom: 30px;
  }
</style>