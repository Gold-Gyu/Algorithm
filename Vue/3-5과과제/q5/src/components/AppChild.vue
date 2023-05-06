<template>
    <div class="box2">
      <h2>AppChild</h2>
      <input v-model.number="app3_num" type="text" @input="childgo">
        <h3>appData : {{ app_num }}</h3>
        <h3>parentData : {{ app2_num }}</h3>
        <h3>childData : {{ app3_num }}</h3>
    </div>
  </template>
  
  <script>
  
  
  export default {
    name: 'AppChild',
    components: {
      
    },
    data() {
        return {
            app3_num : null
        }
    },
    props: {
        app_num : Number,
        app2_num : Number
    },
    methods : {
        childgo () {
            this.$emit("childgo", this.app3_num)
        }   
    }
  }
  </script>
  
  <style scoped>
    .box2 {
        border: 1px solid blue;
    }
  </style>