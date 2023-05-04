<template>
  <div>
    <h2>여기는 child2</h2>


  </div>
</template>

<script>
import EventBus from "@/EventBus"

export default {
    name : "ChildComponent2",
    methods : {

    },

    // 생성되자마자
    created() {
        // v-on:
        EventBus.$on("fromC1", (message) => {
            alert(`C1에서 온 메세지 : ${message}`)
            

        })
        console.log('c2 Created')
    },
    
    mounted() {
        console.log('c2 mounted')
    },
}
</script>

<style>

</style>