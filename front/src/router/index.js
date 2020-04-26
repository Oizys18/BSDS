import Vue from 'vue'
import VueRouter from 'vue-router'
import userIndex from '@/views/user/userIndex.vue'
import adminIndex from '@/views/admin/admin.vue'
import componentTest from '@/views/componentTest.vue'
import foundList from '@/views/user/components/foundList.vue'
import createLost from '@/views/user/components/createLost.vue'
import createdUser from '@/views/user/components/createdUser.vue'
import createFound from '@/views/admin/components/createFound.vue'
import createdAdmin from '@/views/admin/components/createdAdmin.vue'
import lostList from '@/views/admin/components/lostList.vue'
import adminLogin from "@/views/admin/components/adminLogin";

// 로그인 여부
// import getters from "@/store/modules/auth.js";

Vue.use(VueRouter)

// 로그인 여부
// const requireAuth = () => (to, from, next) => {
//   if (getters.isLoggedIn) {
//     return next();
//   } else {
//     return next({ name: 'login' });
//   }
// }

const routes = [
  {
    path: "/",
    name: "userIndex",
    component: userIndex
  },
  {
    path: "/admin",
    name: "adminIndex",
    component: adminIndex,
    // beforeEnter: requireAuth()
  },
  {
    path: "/test",
    name: "componentTest",
    component: componentTest
  },
  {
    path: "/found",
    name: "foundList",
    component: foundList
  },
  {
    path: "/create",
    name: "createLost",
    component: createLost
  },
  {
    path: "/created",
    name: "createdUser",
    component: createdUser
  },
  {
    path: "/admin/create",
    name: "createFound",
    component: createFound
  },
  {
    path: "/admin/created",
    name: "createdAdmin",
    component: createdAdmin
  },
  {
    path: "/admin/lost",
    name: "lostList",
    component: lostList
  },
  {
    path: "/admin/login",
    name: "login",
    component: adminLogin
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
