<template>
  <div>
    <h1> 게시물 목록 </h1>
    <ArticleListItem
    v-for="article in articles" :key="article.id"
    :article="article"/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
export default {
    name : 'ArticleList',
    components : {
        ArticleListItem
    },
    computed: {
        articles() {
            return this.$store.state.articles
        }
    }
}
</script>

<style>

</style>