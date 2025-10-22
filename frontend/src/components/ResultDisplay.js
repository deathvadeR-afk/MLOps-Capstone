import React from 'react';

const ResultDisplay = ({ result }) => {
  const isPositive = result.sentiment === 'positive';

  return (
    <div className={`result ${isPositive ? 'positive' : 'negative'}`}>
      <div className="sentiment-icon">
        {isPositive ? '😊' : '😞'}
      </div>
      <div className="sentiment-text">
        {isPositive ? 'Positive Sentiment' : 'Negative Sentiment'}
      </div>
    </div>
  );
};

export default ResultDisplay;