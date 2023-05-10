<template>
  <div class="wrap">
    <h2>시작</h2>
    <div class="detail d-flex">
        <div class="prev d-flex align-items-center" @click="toHome"><span class="btn">이전</span></div>
        <div><img src="../assets/happeed.png" alt="" class="image"></div>
        <div class="next d-flex align-items-center" @click="toHafling"><span class="btn">다음</span></div>
    </div>
    <h2>해피드</h2>
  </div>
</template>

<script>
export default {
    name : 'Happend',
    methods:{
        toHome() {
            // 홈으로 이동하는 방법
            // 프로그램 방식으로
            this.$router.push({name : 'home'})
        },
        toHafling() {
            this.$router.push({name : 'hafling'})
        }
    }
}
</script>

<style>
.wrap {
    margin-top: 50px;
    text-align: center;
    border: 1px solid gray;
    padding: 20px;
    box-shadow: lightgray 6px 6px 12px 12px;
    border-radius: 10px;
}


.image {
    width: 200px;
}
.d-flex {
    display: flex;
}
.btn {
    border: 1px solid black;
    border-radius: 10px;
    cursor: pointer;
    background-color: skyblue;
    padding: 10px;
}
.align-items-center {
    align-items: center;
}
</style>