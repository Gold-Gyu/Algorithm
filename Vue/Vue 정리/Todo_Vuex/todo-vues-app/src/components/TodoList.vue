<template>
    <div>
        <TodoListItem v-for="(todo, index) in todos" :key="index" :todoitem="todo"/>
    </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'

export default {
    name:"TodoList",
    components: {
        TodoListItem
    },
    computed: {
        todos() {
            // state에서 todos의 []배열안에서 하나씩 꺼내온다.
            return this.$store.state.todos
        }
    }
}
</script>

<style>

</style>