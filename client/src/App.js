import React from 'react'
import MainNavigation from './components/MainNavigation/MainNavigation'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Login from './components/Auth/Login/Login'
import Signup from './components/Auth/Signup/Signup'

function App() {
    return (
        <BrowserRouter>
            <MainNavigation/>
            <Switch>
                <Route path="/login">
                    <Login/>
                </Route>
                <Route path="/signup">
                    <Signup/>
                </Route>
            </Switch>
        </BrowserRouter>
    )
}

export default App
