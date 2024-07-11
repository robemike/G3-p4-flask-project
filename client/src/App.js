import './App.css';
import EventsList from './components/EventsList';
import Login from './components/Login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import EventsList from './components/EventsList';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Login />} />
          <Route path='/dashboard' element={<EventsList />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
