import React from 'react'
import { Nav, Navbar, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { observer } from 'mobx-react'
import { useStore } from '../../stores/store'

const MainNavigation = observer(() => {
    const {authStore} = useStore()

    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    {authStore.isAuthorized && <Nav.Link>Администрирование</Nav.Link>}
                    <Nav.Link>Деятельность</Nav.Link>
                    <Nav.Link>Олимпиады</Nav.Link>
                    <Nav.Link>Обучение</Nav.Link>
                    <Nav.Link>Объявления</Nav.Link>
                    <Nav.Link>Контакты</Nav.Link>
                    {authStore.isAuthorized && <Nav.Link>Диалоги</Nav.Link>}

                    <NavDropdown title="Аккаунт" id="basic-nav-dropdown">
                        {authStore.isAuthorized ?
                            <>
                                <LinkContainer to="/lk">
                                    <NavDropdown.Item>Личный кабинет</NavDropdown.Item>
                                </LinkContainer>
                                <NavDropdown.Divider/>
                                <LinkContainer to="/" onClick={() => authStore.logout()}>
                                    <NavDropdown.Item>Выход</NavDropdown.Item>
                                </LinkContainer>
                            </> : <>
                                <LinkContainer to="/login">
                                    <NavDropdown.Item>Вход</NavDropdown.Item>
                                </LinkContainer>
                                <LinkContainer to="/signup">
                                    <NavDropdown.Item>Регистрация</NavDropdown.Item>
                                </LinkContainer>
                            </>
                        }
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
})

export default MainNavigation
