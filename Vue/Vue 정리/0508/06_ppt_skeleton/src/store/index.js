import Vue from 'vue'
import Vuex from 'vuex'
import createPersitedState from 'vuex-persistedstate'
import myModule from "./modules/myModule"
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersitedState(),
  ],
  state: {
    message: 'message in state',
    age : 30,
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // messageLength를 이용해서 새로운 값을 계산
    doubleLength(state, getters) {
      return getters.messageLength * 2
    },
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      // console.log(state)
      // console.log(message)
      state.message = message
    },

  },
  actions: {
    changeMessage(context, message){
      // console.log(context)
      // console.log(message)
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
    myModule
  }
})
