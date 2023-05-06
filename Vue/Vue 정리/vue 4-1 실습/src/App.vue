<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div class="container">
    <h1>버튼 박스 제작</h1>
    <hr>
    <div class="d-flex justify-content-center">      
    <div class="card col-8">
      <div class="m-3">
        <h2>예약 페이지</h2>
      </div>
      <h3>시간 선택</h3>
      <div class="card-body">
        <div class="btn btm-sm" :class="{'btn-primary' : isSelected(time) , 'btn-outline-primary' : !isSelected(time)}" v-for="time in times" :key="time" @click="selectBtn(time)">{{time}}</div>
        <div class="border border-3 border-primary mt-1"></div>
        <h4>선택 시간 : {{selectedTimes}}</h4>
      </div>
    </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      times: [
      "00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30",
      "04:00","04:30","05:00","05:30","06:00","06:30","07:00","07:30",
      "08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30",
      "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
      "16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30",
      "20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",],
      selectedTimes : ["00:00"]
    }
  },
  methods: {
    isSelected(time) {
      return this.selectedTimes.includes(time)
    },
    selectBtn(time) {
      if (!this.selectedTimes.includes(time)) {
        if (this.selectedTimes.length == 5) {
          alert("5타임까지만 신청할 수 있습니다.")
          return
        }
        this.selectedTimes.push(time)
      } else {

        const t_idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(t_idx, 1)
      }
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
