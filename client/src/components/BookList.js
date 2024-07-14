import React, {useState, useEffect} from 'react'

const BookList = () => {
  const [books, setBooks] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/books')
    .then(response => {
      if (!response.ok){
        throw new Error('Failed to fetch the books.')
      }
      return response.json()
    })
    .then(data => setBooks(data))
    .catch(error => console.error('Error in fetching the books:', error))
  }, [])

  return (
    <div className='books_list-container'>
      {books.map(book => (
        <div className='book-card'>
          <img src={book.image}/>
          <h4>{book.title}</h4>
          <p>{book.author}</p>
          <p>{book.publication_year}</p>
        </div>
      ))}
    </div>
  )
}

export default BookList