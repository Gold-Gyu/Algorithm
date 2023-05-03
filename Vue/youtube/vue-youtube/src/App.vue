<template>
  <div id="app">
    <h1 class="text-primary font-weight-bold">SSAFY TUBE</h1>
    <iframe id="player" type="text/html" width="640" height="360" :src="videoSrc" frameborder="0"></iframe>
    <div>
      {{videoTitle}}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: "App",
  components: {
  },
  data : function () {
    return {
      videoId : '',
      title : ''
    }
  },
  computed : {
    videoSrc () {
      return `https://www.youtube.com/embed/${this.videoId}`
    },
    videoTitle (){
      return _.unescape(this.title)
    }
  },
  created () {
    console.log('created')
    // AIzaSyBckE3e0n36_5DY3AuRggRXGby5jgdrmSk
    axios.get("https://www.googleapis.com/youtube/v3/search/?part=snippet&key=AIzaSyBckE3e0n36_5DY3AuRggRXGby5jgdrmSk&type=video&q=%EC%BD%94%EB%94%A9%EB%85%B8%EB%9E%98")
    .then((result) => {
      console.log(result.data.items[0].id.videoId)
      console.log(result.data.items[0].snippet.title)
      this.title = result.data.items[0].snippet.title
      this.videoId = result.data.items[0].id.videoId
    })
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");
#app {
  font-family: "Noto Sans KR", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
