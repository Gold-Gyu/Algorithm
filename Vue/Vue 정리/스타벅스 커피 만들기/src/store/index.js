import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		orderList: [],
		menuList: [
			{
				title: "아메리카노",
				price: 3000,
				selected: false,
				image: "https://source.unsplash.com/featured/?americano",
			},
			{
				title: "라떼",
				price: 4000,
				selected: false,
				image: "https://source.unsplash.com/featured/?latte",
			},
			{
				title: "카푸치노",
				price: 4500,
				selected: false,
				image: "https://source.unsplash.com/featured/?capucchino",
			},
		],
		sizeList: [
			{
				name: "small",
				price: 0,
				selected: false,
			},
			{
				name: "medium",
				price: 500,
				selected: false,
			},
			{
				name: "large",
				price: 1000,
				selected: false,
			},
		],
		selectedMenu: {},
		selectedSize: {},
	},
	getters: {
		totalOrderCount(state) {
			return state.orderList.length;
		},
		totalOrderPrice(state) {
			return state.orderList.reduce((sum, order) => {
				sum += order.menu.price + order.size.price;
				return sum;
			}, 0);
		},
	},
	mutations: {
		addOrder(state) {
			state.orderList.push({
				menu: state.selectedMenu,
				size: state.selectedSize,
			});
		},
		updateMenuList(state, selectedMenu) {
			state.menuList = state.menuList.map((menu) => {
				if (menu.title === selectedMenu.title) {
					menu.selected = true;
					state.selectedMenu = selectedMenu;
				} else {
					menu.selected = false;
				}
				return menu;
			});
		},
		updateSizeList(state, selectedSize) {
			state.sizeList = state.sizeList.map((size) => {
				if (size.name === selectedSize.name) {
					size.selected = true;
					state.selectedSize = selectedSize;
				} else {
					size.selected = false;
				}
				return size;
			});
		},
	},
	actions: {
		selectMenu(context, selectedMenu) {
			context.commit("updateMenuList", selectedMenu);
		},
		selectSize(context, selectedSize) {
			context.commit("updateSizeList", selectedSize);
		},
		addOrder(context) {
			context.commit("addOrder");
		},
	},
	modules: {},
});
