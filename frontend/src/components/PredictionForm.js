import React, { useState } from 'react';
import './PredictionForm.css';

function PredictionForm({ onSubmit, loading }) {
  const [data, setData] = useState({
    pregnancies: '',
    glucose: '',
    blood_pressure: '',
    skin_thickness: '',
    insulin: '',
    bmi: '',
    diabetes_pedigree_function: '',
    age: '',
  });

  const fields = [
    {
      key: 'pregnancies',
      label: 'Number of Pregnancies',
      icon: 'fa-baby',
      min: 0,
      reference: 'Reference: 0–2 pregnancies. Higher counts are associated with increased risk.',
    },
    {
      key: 'glucose',
      label: 'Plasma Glucose (mg/dL)',
      icon: 'fa-droplet',
      min: 0,
      step: 0.1,
      reference: 'Reference: < 100 mg/dL fasting for lower risk.',
    },
    {
      key: 'blood_pressure',
      label: 'Blood Pressure (mmHg)',
      icon: 'fa-heart',
      min: 0,
      step: 0.1,
      reference: 'Reference: < 120 mmHg is generally considered healthy.',
    },
    {
      key: 'skin_thickness',
      label: 'Skin Thickness (mm)',
      icon: 'fa-ruler',
      min: 0,
      step: 0.1,
      reference: 'Reference: 10–30 mm is a typical healthy range in the dataset.',
    },
    {
      key: 'insulin',
      label: 'Serum Insulin (mu U/ml)',
      icon: 'fa-syringe',
      min: 0,
      step: 0.1,
      reference: 'Reference: 5–20 μU/mL fasting insulin is typical for lower risk.',
    },
    {
      key: 'bmi',
      label: 'BMI (kg/m²)',
      icon: 'fa-weight',
      min: 0,
      step: 0.1,
      reference: 'Reference: 18.5–24.9 is considered normal healthy BMI.',
    },
    {
      key: 'diabetes_pedigree_function',
      label: 'Diabetes Pedigree Function',
      icon: 'fa-dna',
      min: 0,
      step: 0.001,
      reference: 'Reference: lower values indicate lower inherited risk.',
    },
    {
      key: 'age',
      label: 'Age (years)',
      icon: 'fa-calendar',
      min: 0,
      reference: 'Reference: age is a risk factor; enter current age in years.',
    },
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setData((prev) => ({
      ...prev,
      [name]: value === '' ? '' : parseFloat(value),
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Validate all fields are filled
    if (Object.values(data).some((v) => v === '')) {
      alert('Please fill all fields');
      return;
    }

    onSubmit(data);
  };

  return (
    <div className="form-container">
      <h2>Enter Patient Data</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          {fields.map((field) => (
            <div key={field.key} className="form-group">
              <label htmlFor={field.key}>
                <i className={`fas ${field.icon}`}></i> {field.label}
              </label>
              <input
                type="number"
                id={field.key}
                name={field.key}
                value={data[field.key]}
                onChange={handleChange}
                min={field.min || 0}
                step={field.step || 1}
                placeholder="Enter value"
                disabled={loading}
                required
              />
              {field.reference && (
                <p className="field-reference">{field.reference}</p>
              )}
            </div>
          ))}
        </div>
        <button type="submit" disabled={loading} className="submit-btn">
          {loading ? (
            <>
              <i className="fas fa-spinner fa-spin"></i> Predicting...
            </>
          ) : (
            <>
              <i className="fas fa-wand-magic-sparkles"></i> Get Prediction
            </>
          )}
        </button>
      </form>
    </div>
  );
}

export default PredictionForm;
