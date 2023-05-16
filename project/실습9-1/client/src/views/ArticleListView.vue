<template>
  <div>
    <h1> Article Page </h1>
    <router-link :to="{name : 'create'}">[CREATE]</router-link>
    <ArticleList></ArticleList>
  </div>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue"

export default {
    name : 'ArticleListView',
    components : {
        ArticleList
    },
    computed : {
        isLogin() {
            return this.$store.getters.isLogin
        }
    },
    created(){
        this.getArticles()
    },
    methods : {
        getArticles() {

            if (this.isLogin) {
                this.$store.dispatch('getArticles')
            }

            else {
                alert('로그인이 필요한 페이지')
                this.$router.push({ name : 'login'})
            }

        }
    }

}
</script>

<style>

</style>