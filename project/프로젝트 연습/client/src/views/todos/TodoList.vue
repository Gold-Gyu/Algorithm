<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  created() {
    //데이터가 생성되기 전에
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          // console.log(res.data)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
  },

  methods: {
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          // console.log(res.data)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      // 3번 문제
      // console.log(todo.id)
      const todo_pk = todo.id
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo_pk}/`,
        data : {todo_pk}
      })
      .then(() => {
        this.getTodos()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateTodoStatus: function (todo) {
      // 4번 문제
      // console.log(todo)
      const todo_pk = todo.id
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/todos/${todo_pk}/`,
        data : todo
      })
      .then(() => {
        if (todo.is_completed === true) {
          todo.is_completed = false
        } else if (todo.is_completed === false) {
          todo.is_completed = true
        }

      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
