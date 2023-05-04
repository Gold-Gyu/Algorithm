<template>
  <div id="child">
    <h1>AppChild</h1>
        <!--  -->
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
    props: {
        appData : String,
        parentData: String
    },
    methods : {
        childChanged() {
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