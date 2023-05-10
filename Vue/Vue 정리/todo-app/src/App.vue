<template>
  <div id="app" class="d-flex">
    <side-bar></side-bar>
    <div class="border2 view-box">
      <router-view />
    </div>
  </div>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
export default {
  components: { SideBar },
  name: "App",
};
</script>

<style>
.d-flex {
  display: flex;
}

.view-box {
  width: 80%;
  padding: 20px;
  margin-left: 20px;
}

#app {
  width: 1400px;
  padding: 50px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
