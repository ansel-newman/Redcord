// Component 3: Search
// import React from 'react'
import ReactDOM from 'react-dom/client'
import React, { useState } from 'react';
import axios from 'axios';
import './App.css'

const Search = () => {
    const [words, setWords] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.post('http://localhost:5000/search', {
                words: words.split(' ')
            });
            setResults(response.data);
        } catch (error) {
            console.error("There was an error!", error);
        }
    };

    return (
        <div>
            <input id="input" 
                type="text" 
                value={words}
                onChange={(e) => setWords(e.target.value)} 
                placeholder="Enter words separated by whitespace"
            />

            <button id="button" onClick={()=>handleSearch()}>Submit</button>
            <div>
                {results.map((result, index) => (
                    <div class="container">
                        <h4 key={index}>{result.title}</h4>
                        <p key={index}>{result.content}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Search;
