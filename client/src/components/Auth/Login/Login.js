import React, { useState } from 'react'
import { Button, Container, Form, NavLink, Row } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import AuthService from '../services/authService'
import PropTypes from 'prop-types'

const Login = ({history}) => {
    const [state, setState] = useState({
        username: '',
        password: '',
    })

    const handleChange = (event) => {
        const {name, value} = event.target
        setState({...state, [name]: value})
    }

    const handleLogin = async (event) => {
        event.preventDefault()
        const {username, password} = state

        await AuthService.login(username, password)
        history.push('/')
    }

    return (
        <Container className="mt-5">
            <Row className="justify-content-center">
                <Form onSubmit={handleLogin}>
                    <h2 className="text-center">Вход</h2>
                    <Form.Group controlId="login">
                        <Form.Label>Логин<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text" name="username" onChange={handleChange}/>
                    </Form.Group>

                    <Form.Group controlId="password">
                        <Form.Label>Пароль<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="password" name="password" onChange={handleChange}/>
                    </Form.Group>

                    <Form.Group className="text-center">
                        <Button variant="primary" type="submit">Войти</Button>
                    </Form.Group>

                    <div className="text-center">
                        Нет аккаунта? <LinkContainer to="/signup"><NavLink>Регистрация</NavLink></LinkContainer>
                    </div>
                    <div className="text-center">
                        Забыли пароль? <LinkContainer to="/password-reset"><NavLink>Сброс</NavLink></LinkContainer>
                    </div>
                </Form>
            </Row>
        </Container>
    )
}

Login.propTypes = {
    history: PropTypes.object.isRequired,
}

export default Login
