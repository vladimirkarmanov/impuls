import http from '../../common/http'


export default class AuthService {

    static async login(username, password) {
        const response = await http.post('token/', {
            username,
            password,
        })
        await this.setNewHeaders(response)
        return response.data
    }

    static async refreshToken(refresh) {
        const response = await http.post('token/refresh/', {
            refresh,
        })
        await this.setNewHeaders(response)
        return response
    }

    static async setNewHeaders(response) {
        http.defaults.headers['Authorization'] = 'Bearer ' + response.data.access
        localStorage.setItem('access_token', response.data.access)
        localStorage.setItem('refresh_token', response.data.refresh)
    }


    static async logout() {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
    }

    // TODO: сделать более безопасную проверку на авторизацию

    static isAuthorized() {
        const token = localStorage.getItem('access_token')
        return !!token
    }

    static async fetchJobPlaces() {
        const response = await http.get('job-places/')
        return response.data.results
    }

    static async fetchJobPositions() {
        const response = await http.get('job-positions/')
        return response.data.results
    }
}


