<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>APP</h1>
    <input type="text" v-model="appData"/>
    <!-- v-bind는 data값을 input으로 가져오는 것이고 -->
    <!-- v-model은 input 값을 수정해서 data로 가는 것 -->
    <!-- input 데이터를 appData를 수정해주기 위한 바인딩을 사용하려면 v-model -->
    <div>appData : {{ appData}}</div>
    <div>parentData :{{ parentData }}</div>
    <div>childData : {{childData }}</div>
    <!-- appAaprent로 내려주기 위해서 -->
    <!-- : 안붙이면 문자열 값 그대로 넘어간다 -->
    <!-- AppParent emit에서 발생시킨 이벤트 명과 같아야한다 == parentChanged-->
    <AppParent :app-data="appData" @parentChanged="parentChanged" @childChanged="childChanged"/>
  </div>
</template>

<script>
import AppParent from "@/components/AppParent"
export default {
  name: 'App',
  components: {
    AppParent
  },
  // data 선언
  data () {
    return {
      appData : "",
      parentData : "",
      childData : "",
    }
  },
  methods:{
    //여기서 인자 parentData는 AppParent에서 emit으로 this.parentData 값을 넘겨준 것을 받은것
    // 즉 parentData == appParent에서 emit의 this.parentData 
    parentChanged(parentData){
      this.parentData = parentData
    },
    childChanged(childData) {
      this.childData = childData
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
  border: 1px solid black;
}
</style>
