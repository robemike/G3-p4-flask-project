import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login'; // Import your Login component

function App() {
  return (
    <Router>
      <Routes>
        {/* Login as the initial route (empty path) */}
        <Route path="/" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
