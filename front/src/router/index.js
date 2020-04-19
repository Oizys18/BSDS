import Vue from 'vue'
import VueRouter from 'vue-router'
import userIndex from '@/views/user/user.vue'
import adminIndex from '@/views/admin/admin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "userIndex",
    component: userIndex
  },
  {
    path: "/admin",
    name: "adminIndex",
    component: adminIndex
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
