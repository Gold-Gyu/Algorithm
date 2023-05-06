<template>
  <div id="child">
    <h1>AppChild</h1>
        <!-- input을 누르면 methods에서 childChanged가 발생 -->
        <!-- v-model은 data()안에 있는 childData와 바인딩됨 -->
        <!-- 즉, input에서 입력된 값이 data안의 childData로 넘어가서 수정함 -->
    <input type="text" v-model="childData" @input="childChanged">
    <div>appData: {{appData}}</div>
    <div>parentData: {{parentData}}</div>
    <div>childData: {{childData}}</div>

  </div>
</template>

<script>
export default {
    name : "AppChild",
    data() {
        return {
            childData: ""
        }
    },
    // 부모로부터 받는 데이터
    props: {
        appData : String,
        parentData: String
    },
    // 이제 부모에게 데이터를 넘겨주는 것
    methods : {
        childChanged() {
            // this.childData는 input에서 입력한 값
            // childChanged는 이제 부모인 (appParent)에서 childChanged라는 이벤트를 발생시킴
            this.$emit("childChanged", this.childData)
        }
    }
}
</script>

<style>
#child {
    border: 1px solid blue;
}
</style>