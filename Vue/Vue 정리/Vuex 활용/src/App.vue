<template>
  <div id="app">
    <!-- computed안에 있는 함수를 말한다. -->
    <h1>{{ message }}의 길이는 {{messageLength}}</h1>
    <h1>X2 : {{doubleLength}}</h1>
    <!-- 데이터 바꾸는법 -->
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
    <!-- 엔ㄷ터를 누르면  메소드 changeMessage 시작-->
    <!-- changeMessage는 newmessage를 담아서 dispach(action, newMessage)에서 action이라는 이름을 가진 -->
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    changeMessage() {
      // newMessage는 input에 입력한 값
      const newMessage = this.inputData
      // dispatch를 통해 index.js안의 action을 실행
      this.$store.dispatch('changeMessage', newMessage) // store안의 action에 changeMessage 발생
      // 다시 빈칸으로 비워주기
      this.inputData = null
    }
  },
  components: {

  },
  // computed를 통해 store안에 있는 state안에 있는 변수 값을 가져온다.
  computed: {
    message() {
      // store안에 stage안에 message
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
