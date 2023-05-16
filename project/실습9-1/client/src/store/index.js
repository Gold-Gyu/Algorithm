import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false

    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'home'})
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method : 'post',
        url : `${API_URL}/auth/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        // console.log(res.data)
        context.commit('SAVE_TOKEN', res.data.access)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method : 'post',
        url : `${API_URL}/auth/login/`,
        data : {
          username, password
        }
      })
      .then((res) => {
        // console.log(res.data.access)
        context.commit('SAVE_TOKEN', res.data.access)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
