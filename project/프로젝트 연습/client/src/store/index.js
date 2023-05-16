import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins : [
    createPersistedState(),
],
  state: {
    token : null
  },
  getters: {
  },
  mutations: {
    // SIGN_UP(state, token) {
    //   state.token = token
    // },
    SAVE_TOKEN(state, token) {
      state.token = token
    }


  },
  actions: {
    SignUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: "post",
        url : "http://127.0.0.1:8000/accounts/signup/",
        data : {
          username : username,
          password1 : password1,
          password2 : password2,
        }
      })
      .then((res)=> {
        console.log(res)
        context.commit("SAVE_TOKEN", res.data.access)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    Login(context,payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: "post",
        url : "http://127.0.0.1:8000/accounts/login/",
        data : {
          username : username,
          password : password

        }
      })
      .then((res)=> {
        console.log(res.data.access)
        context.commit("SAVE_TOKEN", res.data.access)
      })
      .catch((err) => {
        console.log(err)
      })


    }
  },
  modules: {
  }
})
