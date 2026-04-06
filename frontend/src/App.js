import React, { useState } from 'react';
import './App.css';
import PredictionForm from './components/PredictionForm';
import ResultCard from './components/ResultCard';
import Header from './components/Header';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePrediction = async (formData) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Prediction failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || 'An error occurred');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <Header />
      <div className="container">
        <div className="content">
          <PredictionForm onSubmit={handlePrediction} loading={loading} />
          {error && <div className="error-message">{error}</div>}
          {result && <ResultCard result={result} />}
        </div>
      </div>
    </div>
  );
}

export default App;
