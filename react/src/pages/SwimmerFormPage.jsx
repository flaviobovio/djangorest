import React, { useState } from 'react';
import { Button, Form, Modal, Table } from 'react-bootstrap';

export function SwimmerFormPage() {
    const [Swimmers, setSwimmers] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [SwimmerName, setSwimmerName] = useState('');
    const [editingSwimmerId, setEditingSwimmerId] = useState(null);

    const handleClose = () => {
        setShowModal(false);
        setSwimmerName('');
        setEditingSwimmerId(null);
    };

    const handleShow = () => setShowModal(true);

    const addSwimmer = () => {
        setSwimmers([...Swimmers, { id: Date.now(), name: SwimmerName }]);
        handleClose();
    };

    const editSwimmer = (id) => {
        const SwimmerToEdit = Swimmers.find((Swimmer) => Swimmer.id === id);
        setSwimmerName(SwimmerToEdit.name);
        setEditingSwimmerId(id);
        handleShow();
    };

    const updateSwimmer = () => {
        setSwimmers(
            Swimmers.map((Swimmer) =>
                Swimmer.id === editingSwimmerId ? { ...Swimmer, name: SwimmerName } : Swimmer
            )
        );
        handleClose();
    };

    const deleteSwimmer = (id) => {
        setSwimmers(Swimmers.filter((Swimmer) => Swimmer.id !== id));
    };

    return (
        <div>
            <Button variant="primary" onClick={handleShow}>
                Add Swimmer
            </Button>

            <Modal show={showModal} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>{editingSwimmerId ? 'Edit Swimmer' : 'Add Swimmer'}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form>
                        <Form.Group controlId="name">
                            <Form.Label>Name</Form.Label>
                            <Form.Control
                                type="text"
                                name="name"
                                value={Swimmers.name}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>
                        <Form.Group controlId="age">
                            <Form.Label>Age</Form.Label>
                            <Form.Control
                                type="number"
                                name="age"
                                value={Swimmers.age}
                                onChange={handleChange}
                                min={0}
                                required
                            />
                        </Form.Group>
                        <Form.Group controlId="club">
                            <Form.Label>Club</Form.Label>
                            <Form.Control
                                type="text"
                                name="club"
                                value={Swimmers.club}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>
                        <Form.Group controlId="city">
                            <Form.Label>City</Form.Label>
                            <Form.Control
                                type="text"
                                name="city"
                                value={Swimmers.city}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>
                    </Form>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={editingSwimmerId ? updateSwimmer : addSwimmer}>
                        {editingSwimmerId ? 'Update' : 'Add'}
                    </Button>
                </Modal.Footer>
            </Modal>

            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {Swimmers.map((Swimmer) => (
                        <tr key={Swimmer.id}>
                            <td>{Swimmer.id}</td>
                            <td>{Swimmer.name}</td>
                            <td>
                                <Button variant="primary" onClick={() => editSwimmer(Swimmer.id)}>
                                    Edit
                                </Button>{' '}
                                <Button variant="danger" onClick={() => deleteSwimmer(Swimmer.id)}>
                                    Delete
                                </Button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    );
};

