import request from '@renderer/axios'

// 获取网站信息
export function hello(query) {
    return request({
        url: '/hello',
        method: 'get',
        params: query
    })
}
