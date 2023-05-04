<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div>
      <ul>

        <button @click="getUsers">유저 정보 가져오기</button>
        <UserComponent v-for="user in users" 
        :key="user.id" 
        :user="user">
          {{ user.username}}
        </UserComponent>
      </ul>
    </div>
      <!-- users는 store안에 있는 state에서 가져오기 때문에 computed속성으로 사용할 수 있도록해줘야한다 -->

  </div>
</template>

<script>
import UserComponent from '@/components/UserComponent'
export default {
  name: 'App',
  components: {
    UserComponent
  },
  created() {
    this.$store.dispatch("getUsers", 10)
  },
  methods : {
    // 클릭했을 때 action을 호출
    // getUsers는 store의 action 함수 명과 같음
    //dispatch를 통해 action 호출
    getUsers() {
      this.$store.dispatch("getUsers", 5)
    }
  },
  computed: {
    users() {
      // store 안에 state안에 users라는 데이터를 가져온다.
      return this.$store.state.users;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
ul {
  list-style-position :inside
}
</style>
