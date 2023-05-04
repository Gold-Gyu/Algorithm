<template>
    <div class="box2">
      <h2>AppParent</h2>
      <input v-model.number="app2_num" type="number" @input="gotoapp">
        <h3>appData : {{ app_num }}</h3>
        <h3>childData : {{ childnum }}</h3>
        <AppChild :app_num="app_num" :app2_num="app2_num" @childgo="childapply"/>
    </div>
</template>
  
<script>
  import AppChild from "@/components/AppChild.vue"
  
  export default {
    name: 'AppParent',
    components: {
      AppChild
    },
    data() {
        return {
            childnum : null,

            app2_num : null
        }
    },
    props: {
        app_num : Number
    },
    methods : {
        gotoapp() {
            this.$emit('gotoapp', this.app2_num)
        },
        
        childapply(childnum) {
            this.$emit('childapply', childnum)
            this.childnum = childnum
        } 
    }
  }
</script>
  
<style scoped>
    .box2 {
        border: 1px solid red;
    }
</style>