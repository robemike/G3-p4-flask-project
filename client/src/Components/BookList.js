import React from 'react';
import { Link } from 'react-router-dom';

const BookList = ({ book, handleBuy }) => {
  const handleBuyClick = () => {
    handleBuy(book.id, book);
  };

  return (
    <div className="book-div">
      <div className="image-container">
        <img className="image" alt={book.title} src={book.picture} />
      </div>
      <div className="item-container">
        <Link to={`bookinfo/${book.id}`}>
          <p className='title'>{book.title}</p>
        </Link>
        <p>Ksh {book.price}</p>
        <div className="div-button">
          <button className="buy-button" onClick={handleBuyClick}>Buy Now</button>
        </div>
      </div>
    </div>
  );
};

export default BookList;
