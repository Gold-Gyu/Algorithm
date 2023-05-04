<template>
  <div>
    <h2>산출세액 : {{ allTaxPrice }} 만원</h2>
    <h2>세액감면 : (-) {{ minusNum }} 만원</h2>
    <hr>
    <Finaltax :minus-num="minusNum" :total-num="allTaxPrice"/>
  </div>
  
</template>

<script>
import Finaltax from '@/components/Finaltax'

export default {
  name : 'Taxrate',
  components : {
    Finaltax,
  },
  props: {
    minusNum:{
      type: Number,
    },
    totalNum:{
      type : Number,
    },
  },
  computed:{
    allTaxPrice() {
      if (this.totalNum <= 1200) {
        return Math.round(this.totalNum*0.06)
      } else if (1200 < this.totalNum <= 4600) {
        return Math.round(this.totalNum*0.15) - 108
      } else if (4600 < this.totalNum <= 8800) {
        return Math.round(this.totalNum*0.24 - 522)
      } else if (8800 < this.totalNum <= 15000) {
        return Math.round(this.totalNum*0.35 - 1490)
      } else if (15000 < this.totalNum <= 30000) {
        return Math.round(this.totalNum*0.38 - 1940)
      } else if (30000 < this.totalNum <= 50000) {
        return Math.round(this.totalNum*0.40 - 2540)
      } else if (50000 < this.totalNum <= 100000) {
        return Math.round(this.totalNum*0.42 - 3540)
      } else {
        return Math.round(this.totalNum*0.45 - 6540)
      }
    }
  }
}
</script>

<style>

</style>