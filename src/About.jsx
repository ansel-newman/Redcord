// Component 2: About
import './App.css'
import React from 'react'
import ReactDOM from 'react-dom/client'

function About(){
    return(
        <div id="about">
            <h2>About</h2>
            <p>This site is a proof of concept project that scrapes reddit and discord to 
            find information relevant to given search query. 
            It is meant to make searching for techinical questions easier 
            for developers by navigating a wealth of forums to find the answer to a 
            question or to get recent public chatter on a topic.
            
            The currently supported list of searched forums are below (more will be added over time):
            </p>
            <ul>
                <li>Reddit/WebDev</li>
                <li>Discord/JavaScript Mastery</li>
            </ul>
        </div>
    );
}
export default About;
