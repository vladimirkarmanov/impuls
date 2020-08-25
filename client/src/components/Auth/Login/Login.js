import React from 'react'
import { Button, Col, Container, Form, Row } from 'react-bootstrap'

const Login = () => {
    return (
        <Container className="mt-5">
            <Row className="justify-content-center">
                <Form>
                    <Col>
                        <h2 className="text-center">Вход</h2>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Label>Логин*</Form.Label>
                            <Form.Control type="email" placeholder="Enter email"/>
                            <Form.Text className="text-muted">
                            </Form.Text>
                        </Form.Group>

                        <Form.Group controlId="formBasicPassword">
                            <Form.Label>Пароль*</Form.Label>
                            <Form.Control type="password" placeholder="Password"/>
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                        <p className="text-center">Нет аккаунта? <a>Регистрация</a></p>
                        <p className="text-center">Забыли пароль? <a>Сбросить</a></p>
                    </Col>
                </Form>
            </Row>
        </Container>
    )
}

export default Login
