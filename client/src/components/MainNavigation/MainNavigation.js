import React from 'react'
import { Nav, Navbar, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const MainNavigation = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link>Администрирование</Nav.Link>
                    <Nav.Link>Деятельность</Nav.Link>
                    <Nav.Link>Олимпиады</Nav.Link>
                    <Nav.Link>Обучение</Nav.Link>
                    <Nav.Link>Объявления</Nav.Link>
                    <Nav.Link>Контакты</Nav.Link>
                    <Nav.Link>Диалоги</Nav.Link>

                    <NavDropdown title="Аккаунт" id="basic-nav-dropdown">
                        <LinkContainer to="/login">
                            <NavDropdown.Item>Вход</NavDropdown.Item>
                        </LinkContainer>
                        <LinkContainer to="/signup">
                            <NavDropdown.Item>Регистрация</NavDropdown.Item>
                        </LinkContainer>
                        <NavDropdown.Divider/>
                        <NavDropdown.Item>Выход</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default MainNavigation
