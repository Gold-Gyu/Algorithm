<template>
  <div>
    <div class="todo d-flex align-items-center justify-content-bw">
      <div class="d-flex align-items-center">
        <span
          class="material-icons"
          :class="{ 'green-check': todo.isCompleted }"
          @click="toggleComplete(todo.id)"
          >{{
            todo.isCompleted ? "check_circle_outline" : "radio_button_unchecked"
          }}</span
        >
        <span>
          {{ todo.content }} :
          {{ new Date(todo.dueDateTime).toLocaleString() }}
        </span>
      </div>
      <div>
        <span class="material-icons" @click="toggleForm">edit_note</span>
        <span
          class="material-icons-round gold-star"
          @click="toggleImportant(todo.id)"
          >{{ todo.isImportant ? "star" : "star_border" }}</span
        >
      </div>
    </div>
    <todo-update-form
      v-if="editMode"
      :todo="todo"
      @updateComplete="toggleForm"
    ></todo-update-form>
  </div>
</template>

<script>
import TodoUpdateForm from "@/components/TodoUpdateForm";
import { mapActions } from "vuex";

export default {
  name: "TodoListItemComponent",
  components: {
    TodoUpdateForm,
  },
  props: {
    todo: Object,
  },
  data() {
    return {
      editMode: false,
    };
  },
  methods: {
    ...mapActions(["toggleComplete", "toggleImportant"]),
    toggleForm() {
      this.editMode = !this.editMode;
    },
  },
};
</script>

<style>
</style>