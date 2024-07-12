// BookInfo.js
import React, { useEffect, useState } from 'react'
import './BookInfo.css';
import { Link, useNavigate, useParams } from 'react-router-dom';


function BookInfo({getBooks,handleBuyNow}) {
    const [book, setBook] = useState([]);
    const {id} = useParams()
    const navigate = useNavigate()

    const getBookById = async () => {
        try {
          const response = await fetch(`https://project2-db.onrender.com/books/${id}`);
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          const data = await response.json();
          setBook(data);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      };
    
      useEffect(() => {
        getBookById();
      }, []);


    const handleDelete = async(id) => {
        try {
            const deleteResponse = await fetch(`https://project2-db.onrender.com/books/${id}`, {
              method: 'DELETE',
            });
            if (!deleteResponse.ok) {
              throw new Error("Failed to delete book from backend");
            }
      
           alert("Book Deleted successfully!");
             navigate("/")
             getBooks()
          } catch (error) {
            console.error('Error discharging book:', error);
          }
    };
    

    const buyNow = async (id) => {
      try {
          await handleBuyNow(id,book);
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
                    <img src={book.picture} />
                    </div>
                    <div className="book-details">
                        <h2>{book.title}</h2>
                        <p>
                          <span style={{fontWeight: 'bold'}}>Category:</span>{" "}
                          <span style={{fontWeight: 'lighter'}}>{book.category}</span>
                        </p>
                        <p className="description">
                          <span style={{fontWeight: 'bold' , textWrap: 'nowrap'}}>Description:</span>{" "}
                          <span style={{fontWeight: 'lighter'}}>{book.description}</span>
                        </p>
                        <p>
                          <span style={{fontWeight: 'bold'}}>Price:</span>{" "}
                          <span style={{fontWeight: 'lighter'}} >Ksh {book.price}</span>
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

