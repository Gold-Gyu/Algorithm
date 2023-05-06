<template>
  <div
    class="menu-item d-flex justify-content-bw align-items-center"
    :class="{ selected: menu.selected }"
    @click="selectMenu"
  >
    <img class="menu-img" :src="menu.image" alt="" />
    <p>{{ menu.title }}</p>
    <p>{{ menu.price }}원</p>
  </div>
</template>

<script>
export default {
  name: "MenuListItem",
  props: {
    menu: Object,
  },
  methods: {
    selectMenu() {
      this.$store.dispatch("selectMenu", this.menu);
    },
  },
};
</script>

<style>
.selected {
  background-color: forestgreen;
  color: white;
}
.d-flex {
  display: flex;
}
.justify-content-bw {
  justify-content: space-between;
}
.menu-img {
  width: 50px;
  height: 50px;
  border-radius: 10px;
}
.align-items-center {
  align-items: center;
}
.menu-item {
  border: 1px solid black;
  border-radius: 10px;
  padding: 5px;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>