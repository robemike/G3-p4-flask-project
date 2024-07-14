import React, { useState ,useEffect} from 'react';
import Header from '../components/Header';
import Filter from '../components/Filter';
import BookList from '../components/BookList';

function HomePage({ books, handleBuy }) {
  const [filteredBooks, setFilteredBooks] = useState([]);

  const sortBooksByCategory = (category) => {
    if (category === 'All') {
      setFilteredBooks(books);
    } else {
      const filtered = books.filter(book => book.category === category);
      setFilteredBooks(filtered);
    }
  };

  useEffect(() => {
    setFilteredBooks(books); // Initialize with all books
  }, [books]);

  return (
    <div>
      <Header />
      <Filter sortBooksByCategory={sortBooksByCategory} />
      <div className="homepage-container">
        <h2>Unlimited Books</h2>
        <div className="column-grid">
          {/* {filteredBooks.map((book) => (
            <BookList key={book.id} book={book} handleBuy={(bookId, bookDetails) => handleBuy(bookId, bookDetails)} />
          ))} */}
          <BookList />
        </div>
      </div>
    </div>
  );
}

export default HomePage
