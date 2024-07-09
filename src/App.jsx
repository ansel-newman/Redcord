import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import About from './About.jsx';
import Banner from './Banner.jsx';
import Search from './Search.jsx';
import axios from 'axios';

function App() {
  return (
    <>
      <Banner />
      <div className="site-content">
        <About />
        <Search />
      </div>
    </>
  );
}

export default App;
