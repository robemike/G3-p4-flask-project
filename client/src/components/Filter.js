function Filter({sortBooksByCategory}) {


  return (
    
      <div className="container">
        <p>Filter Books By Category</p>
        <div className='button-container'>
          <button onClick={() => sortBooksByCategory('All')}>All</button>
          <button onClick={() => sortBooksByCategory('Action')}>Action</button>
          <button onClick={() => sortBooksByCategory('Fantasy')}>Fantasy</button>
          <button onClick={() => sortBooksByCategory('Drama')}>Drama</button>
          <button onClick={() => sortBooksByCategory('Finance')}>Finance</button>
          <button onClick={() => sortBooksByCategory('Horror')}>Horror</button>
          <button onClick={() => sortBooksByCategory('Thriller')}>Thriller</button>
          <button onClick={() => sortBooksByCategory('Theological')}>Theological</button>
        </div>
        </div>)
    
     
     

}

export default Filter;