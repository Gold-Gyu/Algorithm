<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name : 'CreateView'}">[CREATE]</router-link>
    <ArticleList/>
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue';
import { RouterLink } from 'vue-router';
export default {
  name: 'ArticleView',
  components: {
    ArticleList,
    RouterLink
},
  computed:{
  },
  created() {
    // 데이터를 준비할 때 시행
    this.getArticles()
  },
  methods: {
    getArticles() {
      // 실행시 장고로 부터 데이터 불러와지기 때문에
      this.$store.dispatch("getArticles")
    }
  }
}
</script>

<style>

</style>
