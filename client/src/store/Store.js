import { action, observable, runInAction } from 'mobx'

class Store {

    @observable isAuthorized = false
}

const store = new Store()

export default store
