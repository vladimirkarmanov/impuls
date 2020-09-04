import axios from 'axios'
import AuthService  from '../services/Auth/AuthService'

const http = axios.create({
    baseURL: '/api',
    headers: {
        'Content-type': 'application/json'
    }
})


http.interceptors.response.use(response => {
    return response
}, err => {
    return new Promise((resolve, reject) => {
        const originalReq = err.config
        if (err.response.status === 401 && err.config && !err.config.__isRetryRequest) {
            originalReq._retry = true

            let res = http.post('token/refresh/', {
                token: localStorage.getItem('access_token'),
                refresh_token: localStorage.getItem('refresh_token')
            }).then(r => r.json())
                .then(r => {
                    console.log(r)
                    AuthService.setNewHeaders(r)
                    return axios(originalReq)
                })
            resolve(res)
        }
        return Promise.reject(err)
    })
})

export default http
