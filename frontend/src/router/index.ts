import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/input",
      name: "input",
      component: () => import("../views/InputView.vue"),
    },
    {
      path: "/odp",
      name: "odp",
      component: () => import("../views/ODPView.vue"),
    }
    // {
    //   path: "/search",
    //   name: "search",
    //   component: () => import("../views/SearchView.vue"),
    // },
  ],
});

export default router;
