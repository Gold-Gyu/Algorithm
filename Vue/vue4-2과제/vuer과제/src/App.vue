<template>
<div class="app">
  <div class="container">
    <br>
    <h1>SSAFY 상담 예약 시스템</h1>
    <br>
    <div class="total_page mx-auto">
        <div class="page">
          <div class="container">
            <br>
            <h2>예약 페이지</h2>
            <br>
            <h3>선생님 선택</h3>
            <br>
            <div class="row">
              <div class="col d-flex justify-content-center" v-for="(name, index) in names" :key="index">
                <button class="selected teach_btn" :class = "{ choose : temp_name.includes(name)}" @click = "changeTeacher(name)">{{ name }}</button>
              </div>
            </div>
            <hr>
            <br>
            <h5>시간 선택</h5>
            <div class="row">
              <div class="col" v-for="(time, index) in times" :key="index">
                <button class="reser_btn" :class = "{ choose : temp.includes(time)}" @click = "changeColor(time)">{{ time }}</button>
              </div>
            </div>
          </div>
        </div>
          
        <div class="page choose">
          <div class="container">
            <br>
            <h2>상담 신청 현황</h2>
            <br>
            <h3>상담 선생님</h3>
            <br>
            <div class="row mx-auto d-flex justify-content-center">선택 시간 :
              <div class="col-2" v-for="(select, index) in temp_name" :key="index">
                <h6 :class="chooseteacher(select)">{{ select }}</h6>
              </div>
            </div>
            <hr>
            <br>
            <h5>예약 현황</h5>
            <br>
            <div class="row mx-auto d-flex justify-content-center">선택 시간 :
              <div class="col" v-for="(select, index) in temp" :key="index">
                <h6 :class="choosecolor(select)">{{ select }}</h6>
              </div>
            </div>
            <hr>
            <img src="./assets/ssafy-logo.png" alt="">
          </div>
        </div>
      
    </div>
  </div>
    
</div>
  
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      temp : [],
      temp_name : [],
      names : ["Eric", "Tony"],
      times: [
    "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
    "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
    "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
  ]}
  },
  methods: {
    changeColor(time) {
      if (this.temp.includes(time)){
        for(let i = 0; i < this.temp.length; i++){
          if(this.temp[i] === time){
            this.temp.splice(i, 1)
            break
          }
        }
        
      }
      else{
        this.temp.push(time)
      }
      console.log(this.temp)
    },
  choosecolor(){
    if (this.temp.length > 5){
      this.temp.pop()
      return alert("5타임까지만 신청할 수 있습니다.")
    }
  },
  changeTeacher(name){
    if (this.temp_name.includes(name)){
        for(let i = 0; i < this.temp_name.length; i++){
          if(this.temp_name[i] === name){
            this.temp_name.splice(i, 1)
            break
          }
        }
        
      }
    else{
      this.temp_name.push(name)
    }
    console.log(this.temp_name)
  },
  chooseteacher(){
    if (this.temp_name.length > 5){
      this.temp_name.pop()
      return alert("선생님은 한 분만 선택 가능합니다")
    }
  },
}
}
</script>

<style>
h1 {
  text-align : center;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.total_page {
  width : 900px;
  height : 500px;
  border : 1px black solid;
  display: flex;
  justify-content : center;
}
.page {
  width: 450px;
  text-align : center;
  
}

.choose {
  background-color: #dae4f1;
  color: #0F4C81;
}
button:hover {
  background-color: #dae4f1;
  color: #0F4C81;
}

button {
  background-color : white;
  border : none;
  text-align : center;
}

.teach_btn {
  width : 150px;
  height : 40px;
  border : 1px solid navy;
}

</style>
