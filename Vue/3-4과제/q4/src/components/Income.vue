<template>
  <div>
    <br>
    <p>연봉 입력 (만원): <input v-model.number="year_num" type="number"></p>
    <p>세액감면액 (만원): <input v-model.number="minus_num" type="number"></p>
    <hr>
    <h2>종합소득금액 : {{ year_num }} 만원</h2>
    <h2>종합소득공제 : (-) 150 만원 </h2>
    <h2>과세표준 : {{ calculator }} 만원</h2>
    <hr>
    <Taxrate :minus-num="minus_num" :total-num="total_num"/>
  </div>
  
</template>

<script>
import Taxrate from '@/components/Taxrate'

export default {
  name : 'Income',
  components : {
    Taxrate,
  },
  data() {
    return {
      year_num : 0,
      minus_num : 0,
      total_num : 0,
    }
  },
  computed: {
    calculator() {
      this.total_num = this.year_num - 150

      if (this.total_num < 150){
        this.total_num = 0
      }

      return `${this.total_num}`
    }
  }
}
</script>

<style>

</style>