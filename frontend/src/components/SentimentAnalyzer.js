import React, { useState } from 'react';
import ResultDisplay from './ResultDisplay';

const SentimentAnalyzer = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (data.success) {
        setResult(data);
      } else {
        setError(data.error || 'An error occurred');
      }
    } catch (err) {
      setError('Failed to connect to the server');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="sentiment-analyzer">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="text">Write text:</label>
          <textarea
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows="5"
            placeholder="Enter your text here..."
            disabled={loading}
          />
        </div>
        <button type="submit" disabled={loading || !text.trim()}>
          {loading ? 'Analyzing...' : 'Predict'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}
      {result && <ResultDisplay result={result} />}
    </div>
  );
};

export default SentimentAnalyzer;