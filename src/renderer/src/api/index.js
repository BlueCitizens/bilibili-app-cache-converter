import request from '@renderer/axios'

// 请求转换
export function hello(query) {
    return request({
        url: '/hello',
        method: 'get',
        params: query
    })
}

// 请求转换
export function convert(form) {
    return request({
        url: '/convert',
        method: 'post',
        data: form
    })
}
