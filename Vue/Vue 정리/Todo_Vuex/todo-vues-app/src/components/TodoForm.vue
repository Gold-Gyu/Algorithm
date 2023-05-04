<template>
  <div>
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
</template>

<script>

export default {
    name: "TodoForm",
    data() {
        return {
            todoTitle: null
        }
    },
    methods: {
        createTodo() {
            if (this.todoTitle) {
                this.$store.dispatch('createTodo', this.todoTitle)
                
            } else {
                alert("할 일을 입력하세요!!")
            }
            // index.js안에있는 action부르기
            // createTodo라는 action을 this.todoTitle이라는 데이터를 가지고 실행

            // 입력칸 초기화
            this.todoTitle = null
            
        }
    }
}
</script>

<style>

</style>