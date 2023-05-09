<template>
  <div class="todo-list-box">
    <todo-list-item-component
      v-for="todo in todoList"
      :key="todo.id"
      :todo="todo"
    ></todo-list-item-component>
  </div>
</template>

<script>
import TodoListItemComponent from "./TodoListItemComponent.vue";

export default {
  components: { TodoListItemComponent },
  name: "TodoListComponent",
  props: {
    todoList: Array,
  },
};
</script>

<style>
.justify-content-bw {
  justify-content: space-between;
}

.gold-star {
  color: gold;
}

.green-check {
  color: forestgreen;
}

span.material-icons,
span.material-icons-round {
  font-size: 30px;
}

span.material-icons:hover,
span.material-icons-round:hover {
  cursor: pointer;
  color: orangered;
}

.fill-green:hover {
  color: forestgreen;
}

.todo span {
  margin-right: 10px;
}

.align-items-center {
  align-items: center;
}

.todo {
  border: 1px solid gray;
  border-radius: 5px;
  padding: 20px;
  margin: 20px;
}

.todo-list-box {
  overflow-y: auto;
}
</style>