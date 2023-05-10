import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		// todo 리스트 Array
		list: [
			// 개별 todo Object
			{
				id: 1638771553377, // nowDateObj.getTime()
				content: "Vue", // Todo 내용
				dueDateTime: "2021-12-09T00:00", // 마감일
				isCompleted: false, // 완료된 할 일
				isImportant: true, // 중요 할 일
			},
			{
				id: 1638771553378,
				content: "Vue Router",
				dueDateTime: "2021-12-10T00:00",
				isCompleted: false,
				isImportant: true,
			},
			{
				id: 16387715533779,
				content: "Vuex",
				dueDateTime: "2021-12-11T00:00",
				isCompleted: true,
				isImportant: false,
			},
		],
	},
	getters: {
		todayList(state) {
			return state.list.filter((todo) => {
				const today_month = new Date().getMonth();
				const today_date = new Date().getDate();

				const todo_dueTime = new Date(todo.dueDateTime);

				// console.log(today_month, today_date);
				// console.log(todo_dueTime);

				return (
					todo_dueTime.getMonth() === today_month &&
					todo_dueTime.getDate() === today_date &&
					!todo.isCompleted
				);
			});
		},
		importantList(state) {
			return state.list.filter((todo) => {
				return todo.isImportant && !todo.isCompleted;
			});
		},
	},
	mutations: {
		CREATE_TODO(state, payload) {
			const today = new Date();
			today.setHours(0);
			today.setMinutes(0);

			const newTodo = {
				id: new Date().getTime(),
				content: payload.content,
				dueDateTime: today.toString(),
				isCompleted: false,
				isImportant: payload.isImportant,
			};

			state.list.push(newTodo);
			console.log(newTodo);
		},
		TOGGLE_COMPLETE(state, id) {
			const todo = state.list.find((todo) => todo.id === id);
			Vue.set(todo, "isCompleted", !todo.isCompleted);
		},
		TOGGLE_IMPORTANT(state, id) {
			const todo = state.list.find((todo) => todo.id === id);
			Vue.set(todo, "isImportant", !todo.isImportant);
		},
		UPDATE_TODO(state, payload) {
			const todo = state.list.find((todo) => todo.id === payload.id);
			Vue.set(todo, "content", payload.content);
			Vue.set(todo, "dueDateTime", payload.dueDateTime);
		},
	},
	actions: {
		createTodo(context, payload) {
			context.commit("CREATE_TODO", payload);
		},
		toggleComplete(context, id) {
			context.commit("TOGGLE_COMPLETE", id);
		},
		toggleImportant(context, id) {
			context.commit("TOGGLE_IMPORTANT", id);
		},
		updateTodo(context, payload) {
			context.commit("UPDATE_TODO", payload);
		},
	},
	modules: {},
});
