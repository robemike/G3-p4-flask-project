import React, { useState } from 'react';
import './EventsList.css';

const EventsList = ({ src, title }) => {
    const [isActive, setIsActive] = useState(false);

    const handleCardClick = () => {
        setIsActive(!isActive);
    };

    return (
        <div className={`card ${isActive ? 'active' : ''}`} onClick={handleCardClick}>
            <img className="background" src={src} alt="" />

            <div className="card-content">
                <div className="profile-image">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                        <path fill="none" d="M0 0h24v24H0z" />
                        <path d="M19 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zm-7 6H7v10h5V9zm4-2H7V5h9v2z" />
                    </svg>
                </div>
                <h3 className="title">{title}</h3>
            </div>

            <div className="backdrop"></div>
        </div>
    );
};

export default EventsList