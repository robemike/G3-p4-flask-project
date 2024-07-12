import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import './BookInfo.css';

function BookInfo({ getBooks, handleBuyNow }) {
  const [book, setBook] = useState({});
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBookById = async () => {
      try {
        const response = await axios.get(`https://project2-db.onrender.com/books/${id}`);
        setBook(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchBookById();
  }, [id]);

  const handleDelete = async (id) => {
    try {
      const deleteResponse = await axios.delete(`https://project2-db.onrender.com/books/${id}`);
      alert("Book deleted successfully!");
      navigate("/");
      getBooks();
    } catch (error) {
      console.error('Error deleting book:', error);
    }
  };

  const buyNow = async (id) => {
    try {
      await handleBuyNow(id, book);
      navigate('/');
      alert('You have added the book to your shelf.');
    } catch (error) {
      console.error('Error buying book:', error);
    }
  };

  return (
    <div>
      <h1 className='h1'>Book Information</h1>
      <div className="books">
        <div className='div'>
          <div className="book">
            <div className='image-div'>
              <img src={book.picture} alt={book.title} />
            </div>
            <div className="book-details">
              <h2>{book.title}</h2>
              <p>
                <span style={{ fontWeight: 'bold' }}>Category:</span>{" "}
                <span style={{ fontWeight: 'lighter' }}>{book.category}</span>
              </p>
              <p className="description">
                <span style={{ fontWeight: 'bold' }}>Description:</span>{" "}
                <span style={{ fontWeight: 'lighter' }}>{book.description}</span>
              </p>
              <p>
                <span style={{ fontWeight: 'bold' }}>Price:</span>{" "}
                <span style={{ fontWeight: 'lighter' }}>Ksh {book.price}</span>
              </p>
            </div>
            <div className='button-div'>
              <Link to='/'>
                <button className='back'>Back Home</button>
              </Link>
              <button className="buy" onClick={() => buyNow(book.id)}>Buy Now</button>
              <button className='delete' onClick={() => handleDelete(book.id)}>Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default BookInfo;
