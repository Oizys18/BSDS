import Vue from "vue";
import VueRouter from "vue-router";
import pnf from "@/views/pnf.vue";
import userIndex from "@/views/user/userIndex.vue";
import adminIndex from "@/views/admin/admin.vue";
import foundList from "@/views/user/components/foundList.vue";
import keywordSearch from "@/views/user/components/keywordSearch.vue";
import createLost from "@/views/user/components/createLost.vue";
import searchLost from "@/views/user/components/searchLost.vue";
import createdUser from "@/views/user/components/createdUser.vue";
import createFound from "@/views/admin/components/createFound.vue";
import createdAdmin from "@/views/admin/components/createdAdmin.vue";
import createdList from "@/views/admin/components/createdList";
import lostList from "@/views/admin/components/lostList";
import adminLogin from "@/views/admin/components/adminLogin";


Vue.use(VueRouter);

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
    path: "/admin/createdList",
    name: "createdList",
    component: createdList,
  },
  {
    path: "/admin/lostList",
    name: "lostList",
    component: lostList,
  },
  {
    path: "/admin/login",
    name: "login",
    component: adminLogin
  },
  {
    path: "*",
    name: "pnf",
    component: pnf
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
