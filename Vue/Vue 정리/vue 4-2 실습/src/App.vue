<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="container">
      <div class="card">
        <h2>예약 페이지</h2>
        <h3>선생님 선택</h3>
        <div class="d-flex justify-content-ev">
          <div class="t-button justify-content-ev d-flex align-items-center" :class="{selected : selectedTeacher==='Eric'}" @click="selectTeacher('Eric')"><div>Eric</div></div>
          <div class="t-button justify-content-ev d-flex align-items-center" :class="{selected : selectedTeacher==='Tony'}" @click="selectTeacher('Tony')"><div>Tony</div></div>
        </div>
        <div class="hr-b"></div>
        <h2>시간 선택</h2>
        <div class="time-box" :class="{'selected' : isSelected(time)}" v-for="time in times" :key="time" @click="selectTime(time)">{{time}}</div>
      </div>
      <div class="card status">
        <h2>상담 신청 현황</h2>
        <h3>상담 선생님</h3>
        <div class="m-10">
        </div>
        <span>성함 : {{selectedTeacher}}</span>
        <div class="hr-b"></div>
        <h3>예약 현황</h3>
        {{this.selectedTimes}}
        <div class="hr-b"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      times : ["09:00","09:30","10:00","10:30","11:00","11:30",
      "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
      "16:00","16:30","17:00","17:30"]
      ,
      selectedTeacher : "",
      selectedTimes : []
    }
  },
  methods : {
    selectTeacher(name) {
      this.selectedTeacher = name
      this.selectedTimes = []
    },
    selectTime(time) {
      if (this.selectedTimes.includes(time)) {
        const t_idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(t_idx, 1)
        return
      } else {
        if (this.selectedTimes.length === 5) {
          alert("5타임까지만 신청할 수 있습니다.")
          return
        }
        this.selectedTimes.push(time)
      }
    },
    isSelected(time) {
      return this.selectedTimes.includes(time)
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
.container {
  border: 1px solid gray;
  border-radius: 10px 10px 10px 10px;
  width: 70%;
  height: 600px;
  margin: 0 auto;
  display : flex;
  box-shadow: -10px 10px 5px gray;
  overflow: hidden;
}

.m-10 {
  height: 40px;
}

.time-box {
  display: inline-block;
  width: 50px;
  padding: 5px;
}

.time-box:hover {
  background-color: lightskyblue;
}

.time-box-selected {
  background-color: lightskyblue;
}

.d-flex {
  display: flex;
}

.justify-content-ev {
  justify-content: space-evenly
}
.align-items-center {
  align-items: center;
}

.t-button {
  border: 1px solid black;
  width: 100px;
  height: 50px;
}

.t-button:hover {
  background-color: aliceblue;
}

.selected {
  background-color: lightskyblue;
}

.flex-wrap{
  flex-wrap: wrap;
}

.card {
  width: 50%;
  height: 100%;
}

.hr-b {
  width: 90%;
  margin: 30px auto;
  border: 1px solid cornflowerblue;
}

.status {
  background-color: aliceblue;
}
</style>
