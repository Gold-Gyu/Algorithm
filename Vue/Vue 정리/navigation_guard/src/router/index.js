import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from "@/views/LoginView.vue"
import NotFound404 from "@/views/NotFound404.vue"
// import NotFound404 from "@/views/NotFound404.vue"
import DogView from "@/views/DogView.vue"

Vue.use(VueRouter)
const isLoggedIn = true
// const isLoggedIn = false

const routes = [
  {
    path : '/404',
    name : "NotFound404",
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: "/login",
    name : "login",
    component : LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({ name : 'home'})
      } else {
        next() // 원래 가야할 곳으로 되돌려 준다.
        // 로그인이 안되어 있으면 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/dog/:breed',
    name : 'dog',
    component: DogView
  },



  {
    path: "*", // 위에가 해당하지 않는 모든 것들 .......
    redirect: "/404"
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js
// router.beforeEach((to, from, next) => {
//   // CODE HERE

//   // 로그인 여부
//   const isLoggedIn = true // 로그인 됨
//   // const isLoggedIn = false // 로그인 x
  
//   // 로그인이 필요한 페이지 지정
//   // const authPages= ['hello', 'about', 'home']
//   const allowAuthPages = ['login']
//   // 로그인이 필요하지 않은 곳만 지정하는 방법


//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAuthPages.includes(to.name)
  
//   if (isAuthRequired && !isLoggedIn) {
//     console.log("move to Login")
//     next({ name : 'login'})
//   } else {
//     console.log("move to to")
//     next()
//   }


// })


export default router
