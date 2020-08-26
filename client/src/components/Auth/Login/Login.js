import React from 'react'
import { Button, Container, Form, NavLink, Row } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const Login = () => {
    return (
        <Container className="mt-5">
            <Row className="justify-content-center">
                <Form>
                    <h2 className="text-center">Вход</h2>
                    <Form.Group controlId="login">
                        <Form.Label>Логин<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="password">
                        <Form.Label>Пароль<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="password"/>
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

export default Login
