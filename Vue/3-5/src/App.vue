<template>
  <div id="app" class="box">
    <div class=""><h1>App</h1>
      <input v-model.number="app_num" type="number">
      <h3>parentData : {{ number2 }}</h3>
      <h3>childData : {{ endnum }}</h3></div>
    <div><AppParent :app_num="app_num" @gotoapp="applyapp" @childapply="endgame"/></div>


    
  </div>
</template>

<script>
import AppParent from "./components/AppParent.vue"

export default {
  name: 'App',
  components: {
    AppParent,

  },
  data() {
    return {
      app_num : null,
      number2 : "",
      endnum : null

    }
  },
  methods :{
    applyapp(number2) {
      this.number2 = number2
    },
    lastgo(lastnum) {
      this.lastnum = lastnum
    },
    endgame(endnum) {
      this.endnum = endnum
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
.box {
  border: 1px solid black;
}
</style>
