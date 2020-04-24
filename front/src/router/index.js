import Vue from 'vue'
import VueRouter from 'vue-router'
import userIndex from '@/views/user/user.vue'
import adminIndex from '@/views/admin/admin.vue'
import componentTest from '@/views/componentTest.vue'
import foundList from '@/views/user/components/foundList.vue'
import createLost from '@/views/user/components/createLost.vue'
import createdUser from '@/views/user/components/createdUser.vue'
import createFound from '@/views/admin/components/createFound.vue'
import createdAdmin from '@/views/admin/components/createdAdmin.vue'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
