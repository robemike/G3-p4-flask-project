import React from "react";
import {Link} from "react-router-dom"

function Navbar(){
    return(
  <div className='bar bg'>
     <Link className="p-3" to="/"><b>HaRRison's Book Club</b></Link>

     <nav className='bar-link'>
        <Link className="nav-link" to="/">◇ Home </Link>
        <Link className="nav-link" to="/form">◇ Add Book</Link>
        <Link className="nav-link" to="/MyShelves">◇ My Books</Link>
        <Link className="nav-link" to="/Events">◇ Events</Link>
     </nav>
  </div>
);
}
export default Navbar;    