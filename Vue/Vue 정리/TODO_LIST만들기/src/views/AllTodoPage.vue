<template>
  <div class="heightbox">
    <div class="">

      <h1 > 모든 할 일 </h1>
      <button @click="goToList">+</button>
      <input type="text" v-model="inputData" placeholder="할 일을 입력하세요">
      <hr>
      <div class="justify-content-ev">

        <div v-for="todo in todolist" :key="todo.id">
          <div class="">

            <div class="elementbox container justify-content-space">
              <div class="d-flex">
                <input v-if="todo.isCompleted" v-model="todo.isCompleted" checked type="checkbox" @click="changeCompleted">
                <input v-else type="checkbox" @click="changeCompleted2">
                <div>
                  {{ todo.content }}

                </div>
              </div>
              <div>
                <span
                v-if="todo.isImportant"
                style="color: yellow; font-size:1.5rem"
                @click="changeImportant"
                >★</span>
                <span v-else
                style="color: yellow; font-size:1.5rem"
                @click="changeImportant2"
                >☆</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'AllTodoPage',
  data() {
    return {
      inputData : ""

    }
  },
  components: {
    // HelloWorld
  },
  methods : {
    important () {
      
      console.log(value)
    },
    changeImportant() {
      const todo = this.$store.state.todo.list

      console.log(todo)
    },
    changeImportant2() {

    },
    changeCompleted() {

    },
    changeCompleted2() {

    },
    goToList() {
      console.log(this.inputData)
      this.$store.dispatch("goToList", this.inputData)
      this.inputData = ""
    }
  },
  computed: {
    todolist() {
      return this.$store.state.todo.list
    },

  }

}
</script>

<style>
.justify-content-space {
  justify-content: space-between;
}
.flex-direction {
  flex-direction: column;
}


.justify-content-left {
  justify-content: left;
}
/* .d-flex{
  display:flex;
} */
</style>