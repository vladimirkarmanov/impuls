import React from 'react'
import ReactDOM from 'react-dom'
import './index.scss'
import App from './App'
import * as serviceWorker from './serviceWorker'
import { BrowserRouter } from 'react-router-dom'
import { rootStore, StoreContext } from './stores/store'

ReactDOM.render(
    <React.StrictMode>
        <StoreContext.Provider value={rootStore}>
            <BrowserRouter>
                <App/>
            </BrowserRouter>
        </StoreContext.Provider>

    </React.StrictMode>,
    document.getElementById('root')
)

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister()
