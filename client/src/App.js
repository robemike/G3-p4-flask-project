import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import HomePage from './Pages/HomePage';
import BookShelves from './Pages/BookShelves';
import Navbar from './Components/Navbar';
import Footer from './Components/Footer';
import FormData from './Pages/Form';
import BookInfo from './Pages/BookInfo';
import Login from './Components/Login';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const loggedIn = localStorage.getItem('isLoggedIn') === 'true';
    setIsLoggedIn(loggedIn);
  }, []);

  const PrivateRoute = ({ element: Component, ...rest }) => {
    return isLoggedIn ? <Component {...rest} /> : <Navigate to="/login" />;
  };

  // Adds a book
  const [books, setBooks] = useState([]);

  const handlePost = async (data) => {
    if (Object.keys(data).length > 0) {
      fetch("https://project2-db.onrender.com/books", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
        .then((res) => {
          if (!res.ok) {
            throw new Error('Failed to add book');
          }
          return res.json();
        })
        .then((data) => {
          getBooks();
        })
        .catch((error) => {
          console.error("Error adding book:", error);
        });
    }
  };

  const getBooks = async () => {
    try {
      const response = await fetch("https://project2-db.onrender.com/books");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setBooks(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    getBooks();
  }, []);

  const handleBuy = async (bookId, bookDetails) => {
    console.log();
    try {
      const bookData = {
        id: bookDetails.id,
        title: bookDetails.title,
        category: bookDetails.category,
        picture: bookDetails.picture,
        description: bookDetails.description,
        price: bookDetails.price
      };

      await fetch(`https://project2-db.onrender.com/MyShelf`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData),
      });

      await fetch(`https://project2-db.onrender.com/books/${bookId}`, { method: 'DELETE' });

      alert('You have Added The Book To Your Shelf');
      getBooks();
    } catch (error) {
      console.error('Error buying book:', error);
    }
  };

  return (
    <div>
      <BrowserRouter>
        {isLoggedIn && <Navbar />}
        <Routes>
          <Route path="/login" element={<Login setIsLoggedIn={setIsLoggedIn} />} />
          <Route path="/" element={<PrivateRoute element={() => <HomePage books={books} handleBuy={handleBuy} />} />} />
          <Route path="/form" element={<PrivateRoute element={() => <FormData handlePost={handlePost} />} />} />
          <Route path="/MyShelves" element={<PrivateRoute element={BookShelves} />} />
          <Route path="/bookinfo/:id" element={<PrivateRoute element={(props) => <BookInfo handleBuyNow={handleBuy} getBooks={getBooks} {...props} />} />} />
        </Routes>
        {isLoggedIn && <Footer />}
      </BrowserRouter>
    </div>
  );
}

export default App;
