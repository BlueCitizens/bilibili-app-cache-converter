// import Index from "@/components/HelloWorld.vue";

const routes = [
    {
        path: '/',
        redirect: '/index',
    },
    {
        path: '/index',
        component:()=> import('@renderer/components/Index.vue')
    },

]

export default routes
