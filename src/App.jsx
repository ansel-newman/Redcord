import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import About from './About.jsx';
import Banner from './Banner.jsx';
import Search from './Search.jsx';
import axios from 'axios';

function App() {
  // const load = () => {
  //   // Call your Flask backend here
  //   axios.get('http://localhost:5000/load')
  //     .then(response => {
  //       console.log("Response from load function:", response.data);
  //       // Handle the response data as needed
  //     })
  //     .catch(error => {
  //       console.error("There was an error calling the Flask function!", error);
  //     });
  // };

  // useEffect(() => {
  //   load();
  // }, []); // Empty dependency array ensures this runs only once when the component mounts

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
