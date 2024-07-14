import React, { useState, useEffect } from 'react';
import Header from '../Components/Header';
import Filter from '../Components/Filter';
import BookList from '../Components/BookList';

function HomePage({ books, handleBuy }) {
  const [filteredBooks, setFilteredBooks] = useState([]);

  useEffect(() => {
    setFilteredBooks(books);
  }, [books]);

  const sortBooksByCategory = (category) => {
    const filtered = category === 'All' ? books : books.filter(book => book.category === category);
    setFilteredBooks(filtered);
  };

  return (
    <div>
      <Header />
      <Filter sortBooksByCategory={sortBooksByCategory} />
      <div className="homepage-container">
        <h2>The Current Selection</h2>
        <div className="column-grid">
          {filteredBooks.map((book) => (
            <BookList key={book.id} book={book} handleBuy={handleBuy} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default HomePage;
