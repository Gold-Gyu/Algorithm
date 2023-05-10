<template>
  
  <div class="wrap">
    <h2>2단계</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center" @click="checking"><span class="btn">이전</span></div>
        <div><img src="../assets/happlossome.png" alt="" class="image"></div>
        <div class="next d-flex align-items-center" @click="toHapplower"><span class="btn">다음</span></div>
    </div>
    <h2>해플라썸</h2>
  </div>
</template>

<script>
export default {
    name : 'Hafleaf',
    methods:{
        checking() {
            this.$router.push({name : 'hafling'})
        },
        toHapplower() {
            this.$router.push({name : 'happlower'})
        }

    }

}
</script>

<style>

</style>