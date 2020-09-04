import { action, observable, reaction } from 'mobx'

class CommonStore {

    @observable token = window.localStorage.getItem('access_token')

    constructor() {
        reaction(
            () => this.token,
            token => {
                if (token) {
                    window.localStorage.setItem('access_token', token)
                } else {
                    window.localStorage.removeItem('access_token')
                }
            }
        )
    }

    @action setToken(token) {
        this.token = token
    }
}

export default CommonStore
