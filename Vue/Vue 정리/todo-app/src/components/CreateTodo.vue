<template>
  <div class="todo-input-box d-flex align-items-center">
    <span class="material-icons add-btn" @click="createTodo(inputTodo)"
      >add_circle_outline</span
    >
    <input
      class="flex-auto todo-input"
      type="text"
      placeholder="할 일을 작성해주세요!"
      v-model="inputTodo"
      @keyup.enter="createTodo"
    />
  </div>
</template>

<script>
export default {
  name: "CreateTodo",
  data() {
    return {
      inputTodo: "",
    };
  },
  methods: {
    createTodo() {
      this.$emit("create-todo", this.inputTodo);
      this.inputTodo = "";
    },
  },
};
</script>

<style>
.add-btn {
  padding: 10px;
}

.todo-input {
  height: 50px;
  font-size: 30px;
}

.todo-input-box {
  padding: 20px;
}

.flex-auto {
  flex: auto;
}
</style>