<template>
    <div>
        <li @click="updateTodo">{{todoitem.title}}</li>
        <button @click="deleteTodo" :class=" {'is-completed' : todo.isCompleted}">DELETE</button>
    </div>
</template>

<script>
export default {
    name : "TodoListItem",
    props: {
        todoitem: Object,
    },
    methods: {
        deleteTodo() {
            this.$store.dispatch('deleteTodo', this.todo)
        },
        updateTodo() {
            this.$store.dispatch('updateTodo', this.todo)
        }
    }
}
</script>

<style>

</style>