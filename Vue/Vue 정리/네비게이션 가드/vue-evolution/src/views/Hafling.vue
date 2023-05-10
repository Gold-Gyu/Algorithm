<template>
  
  <div class="wrap">
    <h2>1단계</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center" @click="notGo"><span class="btn">이전</span></div>
        <div><img src="../assets/happling.png" alt="" class="image"></div>
        <div class="next d-flex align-items-center" @click="toHafleaf"><span class="btn">다음</span></div>
    </div>
    <h2>해플링</h2>
  </div>
</template>

<script>
export default {
    name : 'Hafling',
    methods: {
        toHafleaf() {
            this.$router.push({name : 'hafleaf'})
        },
        notGo() {
            this.$router.push({name : 'happend'})
        }
    }
}
</script>

<style>

</style>