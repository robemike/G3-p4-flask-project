import React, { useState } from 'react';

function Book({ id, title, author, publicationYear, onDelete }) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const handleDeleteClick = () => {
    onDelete(id);
  };

  return (
    <div className='book-card' onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      <h4>{title}</h4>
      <p>Author: {author}</p>
      <p>Publication Year: {publicationYear}</p>
      {isHovered && (
        <div className='delete-icon' onClick={handleDeleteClick}>
          <span role='img' aria-label='delete'>
            🗑️
          </span>
        </div>
      )}
    </div>
  );
}

export default Book;