import React, { useEffect, useState } from 'react';
import './BookShelves.css'; 

function BookShelves() {
  const [shelves, setShelves] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  const fetchShelves = async () => {
    try {
      const response = await fetch("http://localhost:5000/MyShelf");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setShelves(data);
    } catch (error) {
      console.error("Error fetching shelves:", error);
    }
  };

  useEffect(() => {
    fetchShelves();
  }, []);

  const handleDelete = async (id) => {
    try {
      const deleteResponse = await fetch(`http://localhost:5000/MyShelf/${id}`, {
        method: 'DELETE',
      });
      if (!deleteResponse.ok) {
        throw new Error("Failed to delete shelf item from backend");
      }

      alert("Book deleted successfully!");
      fetchShelves();
    } catch (error) {
      console.error('Error deleting book:', error);
    }
  };

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  const filteredShelves = shelves.filter(shelf => 
    shelf.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className='homepage-container'>
      <h2>Personal Books</h2>
      <input 
        type="text" 
        placeholder="Search books..." 
        value={searchQuery} 
        onChange={handleSearch} 
        className="search-bar"
      />
      <div className="column-grid">
        {filteredShelves.map((shelf) => (
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
