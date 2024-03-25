// import Index from "@/components/HelloWorld.vue";

const routes = [
    {
        path: '/',
        redirect: '/index/android',
    },
    {
        path: '/index',
        component: () => import('@renderer/components/Index.vue'),
        children: [
            {
                path: "android",
                name: "android",
                component: () => import('@renderer/components/Android.vue')
            },
            {
                path: "windows",
                name: "windows",
                component: () => import('@renderer/components/Windows.vue')
            },
            {
                path: "settings",
                name: "settings",
                component: () => import('@renderer/components/Settings.vue')
            },
        ]
    },


]

export default routes
