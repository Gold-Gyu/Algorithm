<template>
  <div class="sidebar box justify-content-center">

      <nav>
        <div>
          <router-link to="/" class="fonts">모든</router-link>
        </div>
        <div>
          <router-link :to="{ name : 'today'}" class="fonts">오늘</router-link>
        </div>      
        <div>
          <router-link :to="{ name : 'important'}" class="fonts">중요</router-link>
        </div>
      </nav>

    
  </div>
</template>

<script>
export default {
  name : "SideBar"
}
</script>

<style scoped>
  .box1 {
    width: 20%;
    border : 1px black solid;

  }

  .fonts {
    font-size: 30px;
  }



</style>
