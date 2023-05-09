<template>
  <div>
    <h1>오늘 할일</h1>
    <create-todo @create-todo="createNotImportant"></create-todo>
    <hr />
    <todo-list :todoList="todoList"></todo-list>
  </div>
</template>

<script>
import CreateTodo from "../components/CreateTodo.vue";
import TodoList from "../components/TodoListComponent.vue";

import { mapGetters, mapActions } from "vuex";
export default {
  name: "TodayTodoList",
  components: { CreateTodo, TodoList },
  computed: {
    ...mapGetters({
      todoList: "todayList",
    }),
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