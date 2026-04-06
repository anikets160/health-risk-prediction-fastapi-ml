import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <h1>
          <i className="fas fa-heartbeat"></i> Health Risk Prediction
        </h1>
        <p>Diabetes Risk Assessment Using Machine Learning</p>
      </div>
    </header>
  );
}

export default Header;
