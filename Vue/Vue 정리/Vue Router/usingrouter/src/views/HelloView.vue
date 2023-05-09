<template>
  <div>
    <h1>hello</h1>
    <h1>{{ user.name }}</h1>
    <h1>{{ user.email}}</h1>
    <button @click="back2">back 2칸</button>
    <button @click="replacePage">페이지 교체</button>
  </div>
</template>

<script>
export default {
    name : "HelloView",
    data() {
        return {
            user : this.$route.params.user
        }
    },
    methods: {
        back2(){

            this.$router.go(-2)
        },
        replacePage() {
            this.$router.replace({ name : "about"})
        }
    }
}
</script>

<style>

</style>