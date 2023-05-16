<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signup">
      <div>
        <label for=""> Username </label>
        <input type="text" v-model="username">
      </div>
      <div>
        <label for="password1"> Password </label>
        <input type="password" id="password1" v-model="password1">
      </div>
      <div>
        <label for="password2"> Password check </label>
        <input type="password" id="password2" v-model="password2">
      </div>
      <button type="submit"> 회원가입하기 </button>
    </form>

  </div>
</template>

<script>
// import axios from 'axios'
// const Server_URL = "http://127.0.0.1:8000/accounts/signup/"
export default {
  name: 'Signup',
  data: function () {
    return {
      username : null,
      password1 : null,
      password2 : null
    }
  },
  methods: {
    signup: function () {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      
      this.$store.dispatch("SignUp", payload)
      this.$router.push({ name : "CreateTodo"})

    }
  }
}
</script>