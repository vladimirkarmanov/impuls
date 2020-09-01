import React, { useEffect, useState } from 'react'
import { Button, Container, Form, NavLink, Row } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import AuthService from '../services/authService'

const Signup = () => {
    const [jobPlaces, setJobPlaces] = useState([])
    const [jobPositions, setJobPositions] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            const jobPlaces = await AuthService.fetchJobPlaces()
            setJobPlaces(jobPlaces)
            const jobPositions = await AuthService.fetchJobPositions()
            setJobPositions(jobPositions)
        }
        fetchData()
    }, [])

    return (
        <Container className="mt-5">
            <Row className="justify-content-center">
                <Form>
                    <h2 className="text-center">Регистрация</h2>
                    <Form.Group controlId="login">
                        <Form.Label>Имя<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="login">
                        <Form.Label>Фамилия<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="login">
                        <Form.Label>Отчество</Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="login">
                        <Form.Label>Логин<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="login">
                        <Form.Label>Email<span style={{color: 'red'}}>*</span></Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="login">
                        <Form.Label>Стаж</Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>

                    <Form.Group controlId="jobPlace">
                        <Form.Label>Место работы</Form.Label>
                        <Form.Control as="select">
                            {jobPlaces.map((jobPlace, index) => {
                                return <option key={index}>{jobPlace.name}</option>
                            })}
                        </Form.Control>
                    </Form.Group>

                    <Form.Group controlId="jobPlace">
                        <Form.Label>Должность</Form.Label>
                        <Form.Control as="select">
                            {jobPositions.map((jobPosition, index) => {
                                return <option key={index}>{jobPosition.name}</option>
                            })}
                        </Form.Control>
                    </Form.Group>

                    <Form.Group className="text-center">
                        <Button variant="primary" type="submit">Зарегестрироваться</Button>
                    </Form.Group>

                    <div className="text-center">
                        Уже есть аккаунт? <LinkContainer to="/login"><NavLink>Войти</NavLink></LinkContainer>
                    </div>
                </Form>
            </Row>
        </Container>
    )
}

export default Signup
