<template>
  <div class="side-bar border2">
    <ul class="router-list">
      <li>
        <router-link :to="{ name: 'all' }"><h2>모든</h2></router-link>
      </li>
      <li>
        <router-link :to="{ name: 'today' }"><h2>오늘</h2></router-link>
      </li>
      <li>
        <router-link :to="{ name: 'important' }"><h2>중요</h2></router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SideBar",
};
</script>

<style>
.router-list {
  list-style: none;
  padding-inline-start: 0;
}

.router-list a {
  text-decoration: none;
}

a.router-link-exact-active {
  color: #42b983;
}

.router-list a:not(.router-link-exact-active) {
  color: #2c3e50;
}

.side-bar {
  width: 20%;
  text-align: center;
}
.border2 {
  border: 2px solid black;
  border-radius: 5px;
}
</style>