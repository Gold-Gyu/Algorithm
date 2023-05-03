<template>
    <div>
        <h2>산출세액 : {{  }} 만원</h2>
        <h2>세액감면 : (-) 50 만원 </h2>
        <p>{{ staticProps }}</p>
        <hr>
        <Finaltax/>
    </div>
  </template>
  
  <script>
    import Finaltax from '@/components/Finaltax.vue';
  
  export default {
    name: 'Taxrate',
    data () {
        return {
            
        }
    },
    components: {
      Finaltax
    },
    props:['staticProps'],
    computed: {
        calculator() {

        }
    }

  }
  </script>
  
  <style>
  
  </style>
  