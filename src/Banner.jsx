// Component 1: Banner 
import React from 'react'
import ReactDOM from 'react-dom/client'
import './App.css'
import './index.css'

function Banner() {
    return(
        <div id="header-container">
            <img id="banner" src="./src/assets/head.jpeg"/>
            <h1 id="siteName">Redcord</h1>
        </div>
    );
}
export default Banner;

