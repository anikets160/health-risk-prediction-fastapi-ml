import React from 'react';
import './ResultCard.css';

function ResultCard({ result }) {
  const { prediction, probability } = result;
  
  // Determine risk level and color
  const isHighRisk = prediction === 1;
  const riskLevel = isHighRisk ? 'HIGH RISK' : 'LOW RISK';
  const riskColor = isHighRisk ? '#dc3545' : '#28a745';
  const percentageProb = Math.round(probability * 100);

  return (
    <div className={`result-container ${isHighRisk ? 'high-risk' : 'low-risk'}`}>
      <div className="result-header">
        <h2>Prediction Result</h2>
        <i className={`fas ${isHighRisk ? 'fa-exclamation-triangle' : 'fa-check-circle'}`}></i>
      </div>

      <div className="result-main">
        <div className="risk-badge">
          <span>{riskLevel}</span>
        </div>
        <p className="classification">
          {isHighRisk 
            ? 'Patient shows signs of diabetes risk' 
            : 'Patient shows minimal diabetes risk'}
        </p>
      </div>

      <div className="probability-section">
        <div className="probability-label">
          <span>Diabetes Probability</span>
          <span className="prob-value">{percentageProb}%</span>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${percentageProb}%`, backgroundColor: riskColor }}
          ></div>
        </div>
        <p className="probability-text">
          {isHighRisk 
            ? 'High likelihood of diabetes. Consult a healthcare professional.' 
            : 'Low likelihood of diabetes. Continue healthy lifestyle practices.'}
        </p>
      </div>

      <div className="recommendations">
        <h3><i className="fas fa-lightbulb"></i> Recommendations</h3>
        {isHighRisk ? (
          <ul>
            <li>Schedule an appointment with your doctor for confirmation</li>
            <li>Get a proper medical diagnosis</li>
            <li>Consider lifestyle modifications</li>
            <li>Monitor blood glucose levels regularly</li>
          </ul>
        ) : (
          <ul>
            <li>Maintain a healthy diet and exercise routine</li>
            <li>Regular health check-ups are recommended</li>
            <li>Monitor your weight and BMI</li>
            <li>Stay hydrated and manage stress</li>
          </ul>
        )}
      </div>

      <div className="disclaimer">
        <i className="fas fa-info-circle"></i>
        <p>
          <strong>Disclaimer:</strong> This prediction is based on a machine learning model 
          and should not be used as a medical diagnosis. Please consult with a healthcare 
          professional for accurate diagnosis and treatment.
        </p>
      </div>
    </div>
  );
}

export default ResultCard;
