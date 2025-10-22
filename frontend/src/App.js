import React from 'react';
import SentimentAnalyzer from './components/SentimentAnalyzer';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sentiment Analysis</h1>
      </header>
      <main>
        <SentimentAnalyzer />
      </main>
    </div>
  );
}

export default App;