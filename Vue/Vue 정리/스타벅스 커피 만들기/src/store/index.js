import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		optionList: [
			{
				type: "샷",
				price: 500,
				count: 0,
			},
			{
				type: "바닐라 시럽",
				price: 300,
				count: 0,
			},
			{
				type: "카라멜 시럽",
				price: 1000,
				count: 0,
			},
		],
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
		selectedOption: {},
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
		updateOptionList(state, selectedOption) {
			console.log(selectedOption)
            state.optionList = state.optionList.map((option) => {
                if (option.type == selectedOption.type && selectedOption.flag === 0) {
                    option.count ++;
                } else if (option.type == selectedOption.type && selectedOption.flag === 1 && option.count > 0) {
                    option.count --;
                }
                return option;
            });
        },


		addOrder(state) {
			
			state.orderList.push({
				menu: state.selectedMenu,
				size: state.selectedSize,
				option: state.selectedOption,
			})
	
			
		},

		updateMenuList(state, selectedMenu) {
			// console.log(selectedMenu)
			// console.log(state.menuList)
			state.menuList = state.menuList.map((menu) => {
				// console.log(menu.title)
				// console.log(selectedMenu.title)
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
		selectOption(context, county) {

			context.commit("updateOptionList", county)
		},
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
