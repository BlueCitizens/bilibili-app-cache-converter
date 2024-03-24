import axios from 'axios'

// 设置headers的方式不同，vue3在拦截器中
// axios.defaults.headers['Content-Type'] = 'application/json;charset=utf-8';
// 创建axios实例
const service = axios.create({
    // axios中请求配置有baseURL选项，表示请求URL公共部分
    // build后生产环境只能使用真实地址
    // baseURL: "/api",
    baseURL: "http://127.0.0.1:5001",
    // 超时
    timeout: 120000
});
// request拦截器
service.interceptors.request.use(
    config => {
        config.headers['Content-Type'] = 'application/json;charset=utf-8';
        return config;
    },
    (error) => {
        console.log(error);
        Promise.reject(error)
    }
);

export default service
