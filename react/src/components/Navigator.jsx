import {
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPersonSwimming, faStopwatch, faTrophy } from '@fortawesome/free-solid-svg-icons'
import { faBuilding, faCalendar } from '@fortawesome/free-regular-svg-icons'




export function Navigator(args) {

    return (
        <div>
            <Navbar {...args} size="lg">
                <NavbarBrand href="/"><FontAwesomeIcon size={"2x"} icon={faTrophy} color={"gold"} /></NavbarBrand>
                <Nav className="me-auto">
                    {/* <Nav className="me-auto" navbar> */}
                    <NavItem>
                        <NavLink href="/pages/nadadors">
                            <FontAwesomeIcon size={"xl"} icon={faPersonSwimming} /> Nadadores
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="/pages/fechas">
                            <FontAwesomeIcon size={"xl"} icon={faCalendar} /> Fechas
                        </NavLink>
                    </NavItem>

                    <NavItem>
                        <NavLink href="/pages/prueba3">
                            <FontAwesomeIcon size={"xl"} icon={faBuilding} /> Sedes
                        </NavLink>
                    </NavItem>

                    <NavItem>
                        <NavLink href="/pages/medicions">
                            <FontAwesomeIcon size={"xl"} icon={faStopwatch} /> Mediciones
                        </NavLink>
                    </NavItem>






                    <UncontrolledDropdown nav inNavbar>
                        <DropdownToggle nav caret>
                            Options
                        </DropdownToggle>
                        <DropdownMenu end>
                            <DropdownItem>Option 1</DropdownItem>
                            <DropdownItem>Option 2</DropdownItem>
                            <DropdownItem divider />
                            <DropdownItem>Reset</DropdownItem>
                        </DropdownMenu>
                    </UncontrolledDropdown>
                </Nav>
            </Navbar>
        </div>
    );
}

