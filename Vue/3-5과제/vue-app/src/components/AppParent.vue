<template>
  <div id="parent">
    <h1>AppParent</h1>
    <!-- input데이터가 입력이 들어갔을 때 부모(appparent에 넘겨준다) -->
    <!-- input하면 parentChanged가 발생 method에 만들기-->
    <input type="text" v-model="parentData" @input="parentChanged">
    <div>appData: {{ appData }}</div>
    <div>parentData: {{parentData}}</div>
    <div>childData: {{childData}}</div>
    <AppChild :app-data="appData" 
    :parentData="parentData" 
    @childChanged="childChanged"/>
  </div>
</template>

<script>
import AppChild from "@/components/AppChild"
export default {
    name : "AppParent",
    data() {
        return {
            // parentData를 appChild로 내려다준다
            parentData: "",
            childData:""
        }
    },
    components :{
        AppChild
    },
    // 부모로부터 받을 때 props
    // props는 읽기 전용 여기서 수정하려고하면 안된다.
    props: {
        // 부모로부터 받을 데이터 이름과 타입
        appData: String,
    },
    methods : {
        parentChanged() {
            // parentChanged를 발생시킨다. thisparentData를 가지고
            this.$emit("parentChanged", this.parentData)
        },
        childChanged(childData) {
            this.childData = childData
            this.$emit("childChanged", childData)
        }
    }
}
</script>

<style>
#parent {
    border: 1px solid red
}

</style>