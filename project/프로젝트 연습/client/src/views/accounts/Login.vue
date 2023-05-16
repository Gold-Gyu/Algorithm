<template>
  <div>
    <form @submit.prevent="login">
        <label for="username">username</label>
        <input type="text" id="username" v-model="username"><br>

        <label for="username"> password : </label>
        <input type="password" id="password" v-model="password"><br>

        <input type="submit" id="login" value="Login">
    </form>

  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username : null,
      password : null
    }
  },
  methods: {
    login: function () {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch("Login", payload)
      this.username = ""
      this.password = ""
    }
  }
}
</script>
