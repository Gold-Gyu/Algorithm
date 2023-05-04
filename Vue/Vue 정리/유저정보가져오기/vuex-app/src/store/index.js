import Vue from 'vue'
import Vuex from 'vuex'

import axios from "axios"
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 1. 받아올 데이터
    users: [],
  },
  getters: {
  },
  mutations: {
    CHANGE_USERS(state, payload){
      state.users = payload
    }
  },
  actions: {
    // 여기서 비동기 요청을 보낸다.
    // 인자 두개 context, payload 기억
    // 
    getUsers(context, num) {
      //axios 불러오기
      //axios로 요청하기
      axios.get(`https://random-data-api.com/api/v2/users?size=${num}`)
      // 요청이 성공하면
      .then((res) => {
        // 이때 mutation을 요청한다
        // mutation에가서 뮤테이션 먼저 작성후 돌아온다
        console.log(res.data)
        const users = res.data
        // mutation으로 보내주기
        context.commit("CHANGE_USERS", users)
      })
    }
  },
  modules: {
  }
})
