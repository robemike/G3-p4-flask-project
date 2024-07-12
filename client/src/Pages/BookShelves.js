import React, { useEffect, useState } from 'react';
import axios from 'axios';

function BookShelves() {
  const [shelves, setShelves] = useState([]);

  const fetchShelves = async () => {
    try {
      const response = await axios.get("https://project2-db.onrender.com/MyShelf");
      setShelves(response.data);
    } catch (error) {
      console.error("Error fetching shelves:", error);
    }
  };

  useEffect(() => {
    fetchShelves();
  }, []);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`https://project2-db.onrender.com/MyShelf/${id}`);
      alert("Book deleted successfully!");
      fetchShelves();
    } catch (error) {
      console.error('Error deleting book:', error);
    }
  };

  return (
    <div className='homepage-container'>
      <h2>Personal Books</h2>
      <div className="column-grid">
        {shelves.map((shelf) => (
          <div className="book-div" key={shelf.id}>
            <div className="image-container">
              <img className='image' alt="" src={shelf.picture} />
            </div>
            <div className="item-container">
              <p>{shelf.title}</p>
              <p>Ksh {shelf.price}</p>
              <div className='div-button'>
                <button className="delete-button" onClick={() => handleDelete(shelf.id)}>Delete</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default BookShelves;
