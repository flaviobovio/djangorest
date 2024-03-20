import React, { useState, useEffect } from 'react';
import { Form, Button, Modal } from 'react-bootstrap';


export function SwimmerFormPage({ initialData = {}, onSubmit, isEdit = false }) {

    const [formData, setFormData] = useState({
        name: initialData.name || '',
        age: initialData.age || 0,
        club: initialData.club || '',
        city: initialData.city || '',
    });

    const handleChange = (event) => {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        onSubmit(formData);
    };

    useEffect(() => {
        // Optional: Reset form for create operation
        if (!isEdit) {
            setFormData({ name: '', age: 0, club: '', city: '' });
        }
    }, [isEdit]);

    return (
        <Modal show={true}>
            <Modal.Header>
                <Modal.Title>{isEdit ? 'Edit Swimmer' : 'Create Swimmer'}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form onSubmit={handleSubmit}>
                    <Form.Group controlId="name">
                        <Form.Label>Name</Form.Label>
                        <Form.Control
                            type="text"
                            name="name"
                            placeholder="Enter swimmer name"
                            value={formData.name}
                            onChange={handleChange}
                            required
                        />
                    </Form.Group>
                    <Form.Group controlId="age">
                        <Form.Label>Age</Form.Label>
                        <Form.Control
                            type="number"
                            name="age"
                            placeholder="Enter swimmer age"
                            value={formData.age}
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
                            placeholder="Enter swimmer club"
                            value={formData.club}
                            onChange={handleChange}
                            required
                        />
                    </Form.Group>
                    <Form.Group controlId="city">
                        <Form.Label>City</Form.Label>
                        <Form.Control
                            type="text"
                            name="city"
                            placeholder="Enter swimmer city"
                            value={formData.city}
                            onChange={handleChange}
                            required
                        />
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        {isEdit ? 'Save Changes' : 'Create Swimmer'}
                    </Button>
                </Form>
            </Modal.Body>
        </Modal>
    );
};
