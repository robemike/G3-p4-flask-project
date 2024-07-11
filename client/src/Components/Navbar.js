//https://project2-db.onrender.com/books
import React from "react";
import {Link} from "react-router-dom"

function Navbar(){
    return(
  <div className='bar bg'>
     <Link className="p-2" to="/"><b>ReadFinder</b></Link>

<nav className='bar-link'>
<Link className="nav-link" to="/">Home </Link>
  <Link className="nav-link" to="/MyShelves">Shelf</Link>
  <Link className="nav-link" to="/form">Add Book</Link>
</nav>
  </div>
);
}
export default Navbar;    