<template>
  <div>
    <h1>중요 할일</h1>
    <create-todo @create-todo="createImportant"></create-todo>
    <hr />
    <todo-list :todoList="todoList"></todo-list>
  </div>
</template>

<script>
import CreateTodo from "../components/CreateTodo.vue";
import TodoList from "@/components/TodoListComponent";
import { mapGetters, mapActions } from "vuex";

export default {
  components: { CreateTodo, TodoList },
  name: "ImportantTodo",
  computed: {
    ...mapGetters({
      todoList: "importantList",
    }),
  },
  methods: {
    ...mapActions(["createTodo"]),
    createImportant(content) {
      this.createTodo({ content, isImportant: true });
    },
  },
};
</script>

<style>
</style>