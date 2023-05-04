import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: "message in store"
  },
  getters: {
    // state의 원본데이터를 건들지않고 활용해서 계산된 값을 얻을 수 있음
    // 즉, state 원본 데이터에 영향을 미치지 않음
    // getters인자는 getters안에서 계산된 내용을 가져다 사용할 때 사용한다. 다른 getters를 사용할 때

    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    // 여기서 state의 데이터를 바꿔준다.

    // mutations에서 직접 데이터를 변경해줌
    CHANGE_MESSAGE(state, payload) {
      // console.log(state)
      // console.log(payload)

      state.message = payload

    }
  },
  actions: {
    // state 변경외 모든 로직 진행
    // actions에서는 비동기식 작업을 할 수 있다.(외부 API와의 소통)
    //여기서 message는 App에서 보내준 newMessage이다.
    changeMessage(context, message) {
      console.log(context)
      console.log(context.state.message)
      console.log(message)
      // CHANGE_MESSAGE라는 이름의 뮤테이션을쓴다.
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
