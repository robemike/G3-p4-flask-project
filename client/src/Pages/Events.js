import React, { useState, useEffect } from 'react';
import './Events.css';

const Events = () => {
  const [events, setEvents] = useState([]);
  const [books, setBooks] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    location: 'Nairobi', // The default location
    date: '',
    book_id: ''
  });

  useEffect(() => {
    fetchEvents();
    fetchBooks();
  }, []);

  const fetchEvents = async () => {
    try {
      const response = await fetch("http://localhost:5000/events");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setEvents(data);
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  };

  const fetchBooks = async () => {
    try {
      const response = await fetch("http://localhost:5000/books");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setBooks(data);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  };

  const handleAddEvent = async (data) => {
    try {
      const response = await fetch("http://localhost:5000/events", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to add event');
      }

      await response.json();
      fetchEvents(); // Refreshes events after adding
    } catch (error) {
      console.error("Error adding event:", error);
    }
  };

  const handleDelete = async (eventId) => {
    try {
      const response = await fetch(`http://localhost:5000/events/${eventId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete event');
      }

      fetchEvents(); // Refresh events after deletion
    } catch (error) {
      console.error("Error deleting event:", error);
    }
  };

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [id]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleAddEvent(formData);
    setFormData({ name: '', location: 'Nairobi', date: '', book_id: '' });
  };

  return (
    <div className="events-container">
      <div className="form-container">
        <div className="div-container">
          <h2>Add Event</h2>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor="name">Name:</label>
              <input type="text" id="name" value={formData.name} onChange={handleChange} required />
            </div>
            <div>
              <label htmlFor="location">Location:</label>
              <select id="location" value={formData.location} onChange={handleChange} required>
                <option value="Nairobi">Nairobi</option>
                <option value="Mombasa">Mombasa</option>
                <option value="Machakos">Machakos</option>
                <option value="Nakuru">Nakuru</option>
              </select>
            </div>
            <div>
              <label htmlFor="date">Date:</label>
              <input type="date" id="date" value={formData.date} onChange={handleChange} required />
            </div>
            <div>
              <label htmlFor="book_id">Book:</label>
              <select id="book_id" value={formData.book_id} onChange={handleChange} required>
                <option value="">Select a book</option>
                {books.map((book) => (
                  <option key={book.id} value={book.id}>{book.title}</option>
                ))}
              </select>
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
              <em>Book: {event.book_id}</em>{' '}
              <br></br>
              <button className="delete-button" onClick={() => handleDelete(event.id)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Events;
