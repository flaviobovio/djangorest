import {
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
} from 'react-bootstrap'

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
                        <NavLink href="/swimmer">                           
                            <FontAwesomeIcon size={"xl"} icon={faPersonSwimming} /> Nadadores
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="/swimmerform">
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
                 </Nav>
             </Navbar>
         </div>
    );
}




