import { createRouter, createWebHashHistory } from 'vue-router'
import routes from "./routers";

const router = createRouter({
    // 指定路由的模式
    history: createWebHashHistory(),
    routes
})
export default router
