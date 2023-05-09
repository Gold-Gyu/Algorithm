<template>
  <div class="todo todoForm">
    <div class="d-flex">
      <button
        class="updateBtn d-flex align-items-center"
        @click="emitUpdate({ id: todo.id, content, dueDateTime })"
      >
        수정하기
      </button>
    </div>
    <div class="d-flex my-10">
      <input type="text" class="flex-auto todo-input" v-model="content" />
    </div>
    <div class="d-flex">
      <input
        type="datetime-local"
        class="flex-auto todo-input"
        v-model="dueDateTime"
      />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "TodoUpdateForm",
  props: {
    todo: Object,
  },
  data() {
    return {
      content: "",
      dueDateTime: null,
    };
  },
  created() {
    this.content = this.todo.content;
    this.dueDateTime = this.todo.dueDateTime;
  },
  methods: {
    ...mapActions(["updateTodo"]),
    emitUpdate(payload) {
      this.$emit("updateComplete");
      this.updateTodo(payload);
    },
  },
};
</script>

<style>
.todoForm {
  background-color: azure;
}

.updateBtn {
  height: 40px;
  padding: 20px;
  background-color: forestgreen;
  color: white;
  font-weight: bold;
  font-size: 18px;
  border: 0px;
  border-radius: 3px;
}

.updateBtn:hover {
  cursor: pointer;
}

.my-10 {
  margin: 20px 0px;
}

.align-items-stretch {
  align-items: stretch;
}
</style>