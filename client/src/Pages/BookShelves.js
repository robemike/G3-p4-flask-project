import React, { useEffect, useState } from 'react';

function BookShelves() {
  const [shelfs, setShelf] = useState([]);

  const getShelf = async () => {
    try {
      const response = await fetch("https://project2-db.onrender.com/MyShelf");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setShelf(data);
      console.log(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    getShelf();
  }, []);

  const handleDelete = async(id) => {
    try {
      const deleteResponse = await fetch(`https://project2-db.onrender.com/MyShelf/${id}`, {
          method: 'DELETE',
        });
        if (!deleteResponse.ok) {
          throw new Error("Failed to delete book from backend");
        }

       alert("Book Deleted successfully!");
         getShelf()
      } catch (error) {
        console.error('Error discharging book:', error);
      }
};

  return (
    <div className='homepage-container'>
    <h2>Personal Books</h2>

  <div className="column-grid">
    {shelfs.map((shelf) => (
    <div className="book-div">
            <div className="image-container">
                <img className='image' alt="" src={shelf.picture} />
            </div>
            <div className="item-container">
                <p>{shelf.title}</p>
                <p>Ksh {shelf.price}</p>
                <div className='div-button'>
                  <button class="delete-button" onClick={() => handleDelete(shelf.id)}>Delete</button>
                </div>
            </div>
    </div>
    ))}
  </div>
</div>
  )
}

export default BookShelves