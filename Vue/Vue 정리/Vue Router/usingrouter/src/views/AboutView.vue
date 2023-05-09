<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h1>UserName</h1>
    <input type="text" v-model="user.name">
    <h1>email</h1>
    <input type="text" v-model="user.email">
    <button @click="movePage">move!</button>
  </div>
</template>

<script>
export default {
  name : "AboutView",
  data() {
    return {
      user : {
        name : "",
        email : "",
      }
    }
  },
  methods : {
    movePage() {
      console.log(this.user)
      this.$router.push({
        name : "hello",
        params : {
          user: this.user,
        },
      })
    }
  }
}
</script>
