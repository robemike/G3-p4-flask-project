import React, { useEffect, useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import BookShelves from './Pages/BookShelves';
import Navbar from './Components/Navbar';
import Footer from './Components/Footer';
import FormData from './Pages/Form';
import BookInfo from './Pages/BookInfo';
import Events from './Pages/Events';
import './App.css';

//Display books on the home page
const App = () => {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    try {
      const response = await fetch("http://localhost:5000/books");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setBooks(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
//posts book on the home page array
  const handlePost = async (data) => {
    if (Object.keys(data).length > 0) {
      try {
        const response = await fetch("http://localhost:5000/books", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (!response.ok) {
          throw new Error('Failed to add book');
        }

        await response.json();
        fetchBooks();
      } catch (error) {
        console.error("Error adding book:", error);
      }
    }
  };
//posts books within the MyBooks section
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

      await fetch(`http://localhost:5000/MyShelf`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData),
      });

      await fetch(`http://localhost:5000/books/${bookId}`, {
        method: 'DELETE',
      });

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
