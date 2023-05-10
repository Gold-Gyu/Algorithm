<template>
  <div id="app">
    <h1> 캐릭터 진화 단계 가이드</h1>
    <nav>
      <router-link :to="{name : 'home'}">Home</router-link> |
      <router-link :to="{ name : 'happend'}">Start</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin : 0, auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* width: 700px; */
}

nav {

}

nav a {

}

nav a.router-link-exact-active {
}
</style>
