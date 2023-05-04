<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <child-component name="이금규" @money="sayHello"/>
    <child-component2/>
  </div>
</template>

<script>
// 자식 불러오기
import ChildComponent from './components/ChildComponent.vue';
import ChildComponent2 from './components/ChildComponent2.vue'

export default {
  name: 'App',
  components: {
    // 자식 입력하기
    ChildComponent,
    ChildComponent2,

  },
  methods: {
    sayHello (morning) {
      console.log(morning)
      alert(`good, ${morning}원`)
    }
  },
  created() {
    console.log("App created")
  },
  mounted() {
    console.log("App mounted")
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
