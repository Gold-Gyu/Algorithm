<template>
  <div
    class="menu-item d-flex justify-content-bw"
    :class="{ selected: size.selected }"
    @click="selectSize"
  >
    <p class="size-item d-flex align-items-center justify-content-center">
      {{ size.name }}
    </p>
    <div class="size-item d-flex align-items-center justify-content-center">
      {{ size.price }}원
    </div>
  </div>
</template>

<script>
export default {
  name: "SizeListItem",
  props: {
    size: Object,
  },
  methods: {
    selectSize() {
      this.$store.dispatch("selectSize", this.size);
    },
  },
};
</script>

<style>
.size-item {
  text-align: center;
  height: 50px;
  width: 50px;
}
</style>