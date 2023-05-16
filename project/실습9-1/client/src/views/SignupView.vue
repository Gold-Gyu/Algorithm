<template>
  <b-container role="group" class="p-5">
    <h1>Sign Up</h1>

    <b-form  @submit.stop.prevent>
      <label for="feedback-user">User ID</label>
      <b-form-input v-model="username" :state="id_check" id="feedback-user"></b-form-input>
      <b-form-invalid-feedback :state="id_check">
        Your user ID must be 5-12 characters long.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="id_check">
        Looks Good.
      </b-form-valid-feedback>
    </b-form>

    <b-form @submit.stop.prevent>
      <label for="text-password">Password</label>
      <b-form-input v-model="password" type="password" id="input-password" :state="pw_check" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        Your password must be 8-20 characters long, contain letters and numbers, and must not
        contain spaces, special characters, or emoji.
      </b-form-text>
      <b-form-invalid-feedback id="input-password-feedback">
        Your user Password must be 8-20 characters long.
      </b-form-invalid-feedback>
    </b-form>

    <b-form @submit.stop.prevent>
      <label for="text-password">Password-Check</label>
      <b-form-input v-model="password_check" type="password" :state="repw_check" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        Check your password again please
      </b-form-text>
      <b-form-invalid-feedback id="input-password-feedback">
        Incorrect!
      </b-form-invalid-feedback>
      <b-form-valid-feedback>
        Correct!
      </b-form-valid-feedback>
    </b-form>
    <br>
    <b-button variant="success" @click="signup">회원가입</b-button>
  </b-container>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      username : "",
      password : "",
      password_check : ""
    }
  },
  computed: {
    id_check() {
      if ((this.username.length >= 5) && (this.username.length <= 12)){
        return true
      } else {
        return false
      }
    },
    pw_check() {
      if ((this.password.length >= 8) && (this.password.length <= 20)){
        return true
      } else {
        return false
      }
    },
    repw_check() {
      if(this.password_check === '' || this.password != this.password_check){
        return false
      }
      else {
        return true
      } 
    },

  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password
      const password2 = this.password_check

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

</style>