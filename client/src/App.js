import React, { useEffect, useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import BookShelves from './Pages/BookShelves';
import Navbar from './Components/Navbar';
import Footer from './Components/Footer';
import FormData from './Pages/Form';
import BookInfo from './Pages/BookInfo';
import Events from './Pages/Events';
import axios from 'axios';
import './App.css';

const App = () => {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/books");
      setBooks(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handlePost = async (data) => {
    if (Object.keys(data).length > 0) {
      try {
        const response = await axios.post("http://127.0.0.1:5000/books", data, {
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response.status !== 201) {
          throw new Error('Failed to add book');
        }

        fetchBooks();
      } catch (error) {
        console.error("Error adding book:", error);
      }
    }
  };

  const handleBuy = async (bookId, bookDetails) => {
    try {
      const bookData = {
        id: bookDetails.id,
        title: bookDetails.title,
        category: bookDetails.category,
        picture: bookDetails.picture,
        description: bookDetails.description,
        price: bookDetails.price,
      };

      await axios.post("http://localhost:5000/books", bookData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      await axios.delete(`http://localhost:5000/books`);

      alert('You have added the book to your shelf');
      fetchBooks();
    } catch (error) {
      console.error('Error buying book:', error);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage books={books} handleBuy={handleBuy} />} />
          <Route path="/form" element={<FormData handlePost={handlePost} />} />
          <Route path="/MyShelves" element={<BookShelves />} />
          <Route path="/bookinfo/:id" element={<BookInfo handleBuyNow={handleBuy} />} />
          <Route path="/events" element={<Events />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
};

export default App;
