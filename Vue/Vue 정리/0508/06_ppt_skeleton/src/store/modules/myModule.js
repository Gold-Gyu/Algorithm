const myModule = {
    state: {
        level : 20,
    },
    mutations :{
        INCREMENT_LEVEL(state) {
            state.level += 1
        }
    },
    actions: {
        incrementLevel(context) {
            context.commit('INCREMENT_LEVEL')
        }
    },
}

export default myModule