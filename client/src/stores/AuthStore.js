import { action, observable, runInAction } from 'mobx'
import AuthService from '../services/Auth/AuthService'

class AuthStore {
    @observable isAuthorized = AuthService.isAuthorized()
    @observable inProgress = false

    @action login(username, password) {
        this.inProgress = true
        return AuthService.login(username, password)
            .then(() => runInAction(() => {
                this.isAuthorized = true
            }))
            .finally(action(() => {
                this.inProgress = false
            }))
    }

    @action signup() {
        this.inProgress = true
        this.errors = undefined
        return AuthService.signup(this.values.username, this.values.email, this.values.password)
            .then(({user}) => commonStore.setToken(user.token))
            .then(() => userStore.pullUser())
            .catch(action((err) => {
                this.errors = err.response && err.response.body && err.response.body.errors
                throw err
            }))
            .finally(action(() => {
                this.inProgress = false
            }))
    }

    @action
    async logout() {
        await AuthService.logout()
        runInAction(() => {
            this.isAuthorized = false
        })
    }
}


export default AuthStore
