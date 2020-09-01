import React from 'react'
import MainNavigation from './components/MainNavigation/MainNavigation'
import { Route, Switch } from 'react-router-dom'
import Login from './components/Auth/Login/Login'
import Signup from './components/Auth/Signup/Signup'

function App() {
    return (
        <>
            <MainNavigation/>
            <Switch>
                <Route path="/login" component={Login}/>
                <Route path="/signup">
                    <Signup/>
                </Route>
            </Switch>
        </>
    )
}

export default App
