<template>
  <div class="menu-list">
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItem
      v-for="size in sizeList"
      :key="size.name"
      :size="size"
    ></SizeListItem>
  </div>
</template>

<script>
import SizeListItem from "@/components/SizeListItem";

export default {
  name: "SizeList",
  methods: {
    onSelectMenu() {},
  },
  computed: {
    sizeList() {
      return this.$store.state.sizeList;
    },
  },
  components: {
    SizeListItem,
  },
};
</script>

<style>
</style>