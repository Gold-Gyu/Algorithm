<template>
  <div class="wrap">
    <h2>3단계</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center" @click="checking"><span class="btn">이전</span></div>
        <div><img src="../assets/happlower.png" alt="" class="image"></div>
        <div class="next d-flex align-items-center" @click="backToHome"><span class="btn">다음</span></div>
    </div>
    <h2>해플라워</h2>
  </div>
</template>

<script>
export default {
    name : "Happlower",
    data() {
        return {

        }
    },
    methods: {
        backToHome() {
            alert("Home으로 돌아갑니다!")
            this.$router.push({ name : 'home'})
        },
        checking() {
            this.$router.push({ name: 'hafleaf'})
        }
    }
}
</script>

<style>

</style>