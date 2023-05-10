import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Happend from '../views/Happend.vue'
import Hafling from '../views/Hafling.vue'
import Hafleaf from '../views/Hafleaf.vue'
import Happlower from '../views/Happlower.vue'
import NotFound404 from '../views/NotFound404.vue'
Vue.use(VueRouter)

const routes = [
  {
    path : "/404",
    name : "NotFound404",
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/happend',
    name : 'happend',
    component: Happend,
    beforeEnter(to, from, next) {
      if (from.name === "hafling") {
        alert("이전 진화 단계로 돌아갈 수 없습니다.")
        return
      } next ()
    }

  },
  {
    path: '/hafling',
    name : 'hafling',
    component: Hafling,
    beforeEnter(to, from, next) {
      if (from.name === "hafleaf") {
        alert("이전 진화 단계로 돌아갈 수 없습니다.")
        return
      } next()
    }
  },
  {
    path: '/hafleaf',
    name : 'hafleaf',
    component: Hafleaf,
    beforeEnter(to, from, next) {
      if (from.name === "happlower") {
        alert("이전 진화 단계로 돌아갈 수 없습니다.")
        return
      } next()
    }

  },
  {
    path: '/happlower',
    name : 'happlower',
    component: Happlower,
    
  },
  {
    path: "*",
    redirect: "/404"
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
