import AuthStore from './AuthStore'
import CommonStore from './CommonStore'
import { createContext, useContext } from 'react'

class RootStore {
    constructor() {
        this.authStore = new AuthStore()
        this.commonStore = new CommonStore()
    }
}

export const rootStore = new RootStore()

export const StoreContext = createContext(rootStore)

export const useStore = () => {
    return useContext(StoreContext)
}
