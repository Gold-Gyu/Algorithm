<template>
  <div>
    <h2>결정세액 : {{ last_cal }} 만원</h2>
  </div>
</template>

<script>


export default {
  name : 'Finaltax',
  props: {
    minusNum:{
      type: Number,
    },
    totalNum:{
      type : Number,
    },
  },
  data() {
    return {
      final_num : 0,
    }
  },
  computed : {
    last_cal() {
      this.final_num = this.totalNum - this.minusNum
      return `${this.final_num}`
    }
  }
}
</script>

<style>

</style>