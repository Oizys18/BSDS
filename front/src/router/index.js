import Vue from "vue";
import VueRouter from "vue-router";
import userIndex from "@/views/user/userIndex.vue";
import adminIndex from "@/views/admin/admin.vue";
import componentTest from "@/views/componentTest.vue";
import foundList from "@/views/user/components/foundList.vue";
import keywordSearch from "@/views/user/components/keywordSearch.vue";
import createLost from "@/views/user/components/createLost.vue";
import searchLost from "@/views/user/components/searchLost.vue";
import createdUser from "@/views/user/components/createdUser.vue";
import createFound from "@/views/admin/components/createFound.vue";
import createdAdmin from "@/views/admin/components/createdAdmin.vue";
import createdList from "@/views/admin/components/createdList";
import lostList from "@/views/admin/components/lostList";

// 로그인 여부
// import getters from "@/store/modules/auth.js";

Vue.use(VueRouter);

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
    component: userIndex,
  },
  {
    path: "/keywordsearch",
    name: "keywordSearch",
    component: keywordSearch,
  },
  {
    path: "/searchlost",
    name: "searchLost",
    component: searchLost,
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
    component: componentTest,
  },
  {
    path: "/found",
    name: "foundList",
    component: foundList,
  },
  {
    path: "/create",
    name: "createLost",
    component: createLost,
  },
  {
    path: "/created",
    name: "createdUser",
    component: createdUser,
  },
  {
    path: "/admin/create",
    name: "createFound",
    component: createFound,
  },
  {
    path: "/admin/created",
    name: "createdAdmin",
    component: createdAdmin,
  },
  {
    // 이걸 나중에 어케 바꾸지...
    path: "/admin/createdList",
    name: "createdList",
    component: createdList,
  },
  {
    path: "/admin/lostList",
    name: "lostList",
    component: lostList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
