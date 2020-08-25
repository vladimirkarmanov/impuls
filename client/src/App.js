import React from 'react'
import MainNavigation from './components/MainNavigation/MainNavigation'
import { Route, BrowserRouter, Switch } from 'react-router-dom'
import Login from './components/Auth/Login/Login'

function App() {
    return (
        <BrowserRouter>
            <MainNavigation/>
            <Switch>
                <Route path="/login">
                    <Login/>
                </Route>
            </Switch>
        </BrowserRouter>
    )
}

export default App
