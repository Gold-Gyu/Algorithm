<template>
  <div>
    <h1> Article Page </h1>
    <router-link to="/create">[CREATE]</router-link>
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
    

}
</script>

<style>

</style>