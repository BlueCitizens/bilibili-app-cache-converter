import { createRouter, createWebHistory } from 'vue-router'
import routes from "./routers";

const router = createRouter({
    // 指定路由的模式
    history: createWebHistory(),
    routes
})
export default router
