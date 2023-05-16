<template>
  <b-container role="group" class="p-5 login-form">
    <b-row>
      <label for="input-username">아이디</label>
      <b-form-input 
        id="input-username"
        placeholder="ID"
        v-model="username"
        :state="nameState"
        aria-describedby="input-live-help input-live-feedback"
        trim
        ></b-form-input>

        <b-form-invalid-feedback id="input-username-feedback" class="text-right">
          알파벳/숫자 3글자 이상
        </b-form-invalid-feedback>
    </b-row>
    <b-row>
        <label for="input-password">비밀번호</label>
        <b-form-input 
        id="input-password" 
        placeholder="PASSWORD" 
        trim 
        v-model="password" 
        type="password"
        :state="passwordState" 
        aria-describedby="input-live-help input-live-feedback"
        autocompleted="false"
        ></b-form-input>
        <b-form-invalid-feedback id="input-password-feedback" class="text-right">
            비밀번호는 최소 5글자 이상
        </b-form-invalid-feedback>
    </b-row>
    <b-button variant="success" @click="login">로그인</b-button>

  </b-container>
</template>

<script>
// import axios from 'axios'

export default {
  name: "LoginView",
  data() {
    return {
      username : "",
      password : "",
    }
  },
  computed: {
    nameState() {
      return this.username.length >= 3 ? true: false
    },
    passwordState() {
      return this.password.length >= 5 ? true: false
    }
  },
  methods : {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>
.login-form {
    background-color:  rgb(214, 228, 240);
    box-shadow: 20px 20px 10px 0px lightslategray;
}
</style>