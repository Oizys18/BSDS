import Vue from 'vue'
import VueRouter from 'vue-router'
import userIndex from '@/views/user/user.vue'
import adminIndex from '@/views/admin/admin.vue'
import componentTest from '@/views/componentTest.vue'
import foundList from '@/views/user/components/foundList.vue'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
