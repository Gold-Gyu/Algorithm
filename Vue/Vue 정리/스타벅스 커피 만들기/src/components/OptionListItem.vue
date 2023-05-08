<template>
  <div class="menu-item d-flex justify-content-bw">
    
      <div class="size-item d-flex align-items-center justify-content-center">

        <p>{{option.type}}</p>
      </div>

      <div class="size-item d-flex align-items-center justify-content-center">

        <button class="btn" @click="decrease">-</button>
        <p>{{option.count}}</p>
        <button class="btn" @click="increase">+</button>
      </div>


  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch("selectOption", {type : this.option.type, flag : 0})
    },
    decrease() {
      this.$store.dispatch("selectOption", {type : this.option.type, flag : 1})

    },
  },
}
</script>

<style>
.btn {

  width: 50px;
  height: 30px;
  border-radius: 30px;
}
</style>