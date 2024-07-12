import React from "react";
import "./Form.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function FormData({ handlePost }) {
    const navigate=useNavigate()
    const [formData, setFormData] = useState({
        picture: "",
        title: "",
        category: "",
        description: "",
        price: ""
    });

const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prevFormData) => ({
        ...prevFormData,
        [id]: value
    }));
};

const handleSubmit = (e) => {
    e.preventDefault();
    console.log("submitted", formData);
    handlePost(formData);
    // Clear the form after submission if needed
    setFormData({
        picture: "",
        title: "",
        category: "",
        description: "",
        price: ""
    });
    alert("Book successfully added:");
    navigate("/")
};

return (
  <div className='form-container' id="form">
    <div className='div-container'>
        <form onSubmit={handleSubmit}>
            <h3>Book Details</h3>

            <div className='div-input'>
                <label>Picture:</label>
                <input type="text" placeholder="Add Image Url" id="picture" value={formData.picture} onChange={handleChange}
                    accept="image/*" /> 
            </div>

            <div className='div-input'>
                <label>Title:</label>
                <input type="text" placeholder="Title" id="title" value={formData.title} onChange={handleChange} />{" "}
            </div>

            <div className='div-input'>
                <label>Category:</label>
                <input type="text" placeholder="Category" id="category" value={formData.category} onChange={handleChange} />{" "}
            </div>

            <div className='div-input'>
                <label>Description:</label>
                <input type="text" placeholder="Description" id="description" value={formData.description} onChange={handleChange} />{" "}
                
            </div>

            <div className='div-input'>
                <label>Price:</label>
                <input type="text" placeholder="Price" id="price" value={formData.price} onChange={handleChange} />{" "}
                
            </div>

            <div className='div-input'>
            <button id="btn" type="submit"> Add a book </button> {" "}
            </div>
        </form>
        <footer id="footerform">Get to add a book of your choice</footer>
    </div>
   </div>
);
}

export default FormData; 