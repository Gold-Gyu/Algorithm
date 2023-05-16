<template>
  <b-container>
    <h1>게시물 작성</h1>
    <b-row class="my-1">
    <b-col sm="2">
      <label for="input-default">제목 :</label>
    </b-col>
    <b-col sm="10">
      <b-form-input id="input-default" placeholder="제목을 작성하세요." v-model="title"></b-form-input>
    </b-col>
  </b-row>

    <b-row class="mt-2">
    <b-col sm="2">
      <label for="textarea-default">내용 :</label>
    </b-col>
    <b-col sm="10">
      <b-form-textarea
        id="textarea-default"
        placeholder="내용을 입력하세요."
        v-model="content"
      ></b-form-textarea>
    </b-col>
    </b-row>

    <b-button variant="success" @click="create_article">작성하기</b-button>
  </b-container>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
    name : "ClientView",
    computed : {
        isLogin() {
            return this.$store.getters.isLogin
        }
    },
    created() {
        this.getArticles()
    },
    data() {
        return {
            title : "",
            content : ""
        }
    },
    methods : {
      getArticles() {

            

        },
        create_article() {
            const title = this.title
            const content = this.content
            if (this.isLogin) {
                this.$store.dispatch('getArticles')
            }

            else {
                alert('로그인이 필요한 페이지')
                this.$router.push({ name : 'login'})
            }
            if (!title) {
                alert('제목 입력해주세요')
                return
            } else if (!content){
                alert('내용 입력해주세요')
                return
            }
            axios({
                method: 'post',
                url : 'http://127.0.0.1:8000/articles/',
                data : { title, content },
                headers : {
                    Authorization : `Bearer ${this.$store.state.token}` 
                }
                })
                .then(() => {
                    this.$router.push({name : 'ArticleView'})
                })
                .catch((err) => {
                    console.log(err)
                })
            
           
    }
}
}
</script>

<style>

</style>