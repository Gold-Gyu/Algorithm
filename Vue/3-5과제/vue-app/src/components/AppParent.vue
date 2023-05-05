<template>
  <div id="parent">
    <h1>AppParent</h1>
    <!-- input데이터가 입력이 들어갔을 때 부모(appparent에 넘겨준다) -->
    <!-- input하면 parentChanged가 발생 method에 만들기-->
    <input type="text" v-model="parentData" @input="parentChanged">
    <div>appData: {{ appData }}</div>
    <div>parentData: {{parentData}}</div>
    <div>childData: {{childData}}</div>

    <!-- 이 곳에서 일어남 appchild(자식)으로부터 childChanged를 발생시킴 -->
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
        // 여기서 childData가 Appchild에서 보내줬던 this.childData임
        childChanged(childData) {
            // this.childData는 appParent 컴포넌트 안에 있는 childData 값
            // 우측 childData는 AppChild에서 받아온 인자
            this.childData = childData
            // 그리고 또 그 위 부모인 app에게 데이터를 보낸다.
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