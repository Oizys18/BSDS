<template>
  <div class="login-form">
    <div v-if="isLoading" class="spinner-border" role="status">
      <span class="sr-only">Loading</span>
    </div>

    <form v-else class="login-input" >
      <div v-if="getErrors.length" class="error-list alert alert-danger">
        <p>아래의 오류를 해결해 주세요</p>
        <ul>
          <li v-for="(error, idx) in getErrors" :key="idx">
            {{ error }}
          </li>
        </ul>
      </div>
      <div class="login-box">
        <div class="user-input">
          <label for="username">아이디</label>
          <input v-model="credentials.username" type="text" class="form-control" id="username">
        </div>

        <div class="user-input">
          <label for="password">비밀번호</label>
          <input v-model="credentials.password" type="password" class="form-control" id="password">
        </div>
        <div @click="login(credentials)" >
          <button-default :text="'로그인'" />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import buttonDefault from "@/components/common/button/buttonDefault";
  export default {
    name: 'LoginForm',
    components: {
      buttonDefault
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
    },
    computed: {
      ...mapGetters(['getErrors', 'isLoading', 'isLoggedIn']),
    }
  }
</script>

<style>
  .login-box {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 400px;
    padding: 40px;
    transform: translate(-50%, -50%);
    background: none;
    box-sizing: border-box;
    border: 1px solid black;
    border-radius: 10px;
  }
  .user-input {
    position: relative;
  }
  .user-input input {
    width: 100%;
    padding: 10px 0;
    font-size: 1em;
    color: black;
    margin-bottom: 30px;
    border: none;
    border-bottom: 1px solid black;
    outline: none;
    background: transparent;
  }
  .user-input label {
    padding: 10px 0;
    font-size: 1.1em;
    color: black;
    pointer-events: none;
  }
</style>