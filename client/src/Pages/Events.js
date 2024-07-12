import React, { useState } from 'react';
import './Events.css';

const Events = () => {
    const [events, setEvents] = useState([]);
    const [formData, setFormData] = useState({
        name: '',
        location: '',
        date: ''
    });

    const handleChange = (e) => {
        const { id, value } = e.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [id]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const newEvent = {
            id: events.length + 1,
            ...formData
        };
        setEvents([...events, newEvent]);
        setFormData({ name: '', location: '', date: '' });
    };

    const handleDelete = (eventId) => {
        const updatedEvents = events.filter(event => event.id !== eventId);
        setEvents(updatedEvents);
    };

    return (
        <div className="events-container">
            <div className="form-container">
                <div className="div-container">
                    <label ><b>Add Event</b></label>
                    <form onSubmit={handleSubmit}>
                        <div>
                            <label htmlFor="name">Name:</label>
                            <input type="text" id="name" value={formData.name} onChange={handleChange} required />
                        </div>
                        <div>
                            <label htmlFor="location">Location:</label>
                            <input type="text" id="location" value={formData.location} onChange={handleChange} required />
                        </div>
                        <div>
                            <label htmlFor="date">Date:</label>
                            <input type="date" id="date" value={formData.date} onChange={handleChange} required />
                        </div>
                        <button type="submit">Add Event</button>
                    </form>
                </div>
            </div>
            <div className="events-list">
                <h3>Events List:</h3>
                <ul>
                    {events.map((event) => (
                        <li key={event.id}>
                            <strong>{event.name}</strong> - {event.location} ({event.date}){' '}
                            <button className="delete-button" onClick={() => handleDelete(event.id)}>Delete</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Events;
