<template>
  <div>
    <h1>모든 할일</h1>
    <create-todo @create-todo="createNotImportant"></create-todo>
    <hr />
    <todo-list :todoList="todoList"></todo-list>
  </div>
</template>

<script>
import CreateTodo from "@/components/CreateTodo";
import { mapActions } from "vuex";
import TodoList from "../components/TodoListComponent.vue";

export default {
  name: "AllTodoPage",
  components: {
    CreateTodo,
    TodoList,
  },
  data() {
    return {};
  },
  computed: {
    todoList() {
      return this.$store.state.list;
    },
  },
  methods: {
    ...mapActions(["createTodo"]),
    createNotImportant(content) {
      this.createTodo({ content, isImportant: false });
    },
  },
};
</script>

<style>
</style>