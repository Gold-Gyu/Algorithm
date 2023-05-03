<template>
  <div class="wid">
    <div class="card status">
        <h2>상담 신청 현황</h2>
        <h3>상담 선생님</h3>
        <div class="m-10">
        </div>
            <span>
                성함 : 
                {{selectedTeacher}}
            </span>
        <div class="hr-b"></div>
        <h3>예약 현황</h3>
          <span>
            시간들 : {{this.selectedTimes}}
          </span>
        <div class="hr-b"></div>
      </div>
  </div>
</template>

<script>
export default {
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
    }

}
</script>

<style scoped>
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
  width: 100%;
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

.wid {
    width: 50%;
}
</style>