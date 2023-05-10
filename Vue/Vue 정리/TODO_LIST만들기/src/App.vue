<template>
  <div id="app">
    <!-- <nav> -->
    <div class="d-flex justify-content-ev">
      <SideBar/>
      <div class="box2">
        <router-view/>
      </div>
      
    </div>
      

  </div>
</template>

<script>
import SideBar from "@/components/SideBar.vue"
export default {
  name : "app",
  components : {
    SideBar
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
}

.justify-content-ev {
  justify-content: space-evenly;
}

.big {
  width: 100%;
  height: 500px;
}

.box {
  width: 20%;
  border: 1px solid black;
  border-radius: 10px;
  
}

.box2 {
  width: 70%;
  border: 1px solid black;
  border-radius: 10px;
}

.justify-content-center {
  justify-content: center;
}

.leftbox {
  width: 20%;
  height: 600px;
}

.rightbox {
  width: 70%;
  height: 90%;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.d-flex{
  display:flex;
}
.heightbox {
  width: auto;
  height: 600px;
}
.elementbox {
  border: 1px solid black;
  height: 80px;
  width: 90%;
  border-radius: 20px;
  margin: 20px;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
