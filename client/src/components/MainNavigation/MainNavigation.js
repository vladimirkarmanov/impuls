import React from 'react'
import { Nav, Navbar, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import AuthService from '../Auth/services/authService'

const MainNavigation = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    {AuthService.isAuthenticated() && <Nav.Link>Администрирование</Nav.Link>}
                    <Nav.Link>Деятельность</Nav.Link>
                    <Nav.Link>Олимпиады</Nav.Link>
                    <Nav.Link>Обучение</Nav.Link>
                    <Nav.Link>Объявления</Nav.Link>
                    <Nav.Link>Контакты</Nav.Link>
                    {AuthService.isAuthenticated() && <Nav.Link>Диалоги</Nav.Link>}

                    <NavDropdown title="Аккаунт" id="basic-nav-dropdown">
                        <LinkContainer to="/login">
                            <NavDropdown.Item>Вход</NavDropdown.Item>
                        </LinkContainer>
                        <LinkContainer to="/signup">
                            <NavDropdown.Item>Регистрация</NavDropdown.Item>
                        </LinkContainer>
                        {AuthService.isAuthenticated() &&
                        <>
                            <LinkContainer to="/lk">
                                <NavDropdown.Item>Личный кабинет</NavDropdown.Item>
                            </LinkContainer>
                            <NavDropdown.Divider/>
                            <LinkContainer to="/logout" onClick={AuthService.logout}>
                                <NavDropdown.Item>Выход</NavDropdown.Item>
                            </LinkContainer>
                        </>
                        }
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default MainNavigation
