# Health Risk Prediction - React Frontend

A modern, responsive React UI for the Health Risk Prediction FastAPI ML application. Users can input patient health metrics and receive diabetes risk predictions with interactive visualizations.

## Features

- ✅ **Beautiful, Modern UI** - Responsive design with gradient theme
- ✅ **Form Validation** - Validates all required health metrics
- ✅ **Real-time Predictions** - Instant results from FastAPI backend
- ✅ **Risk Visualization** - Color-coded probability bars and risk badges
- ✅ **Responsive Design** - Mobile, tablet, and desktop support
- ✅ **Accessibility** - Icon-based field identification, clear instructions
- ✅ **Medical Recommendations** - Tailored advice based on prediction result
- ✅ **Professional Styling** - Smooth animations and transitions

## Tech Stack

- **Framework:** React 18
- **HTTP Client:** Axios
- **CSS:** CSS3 with animations and gradients
- **Icons:** Font Awesome 6
- **Styling Approach:** Component-scoped CSS

## Project Structure

```
frontend/
├── public/
│   └── index.html                 # Root HTML file
├── src/
│   ├── components/
│   │   ├── Header.js              # Application header
│   │   ├── Header.css
│   │   ├── PredictionForm.js       # Form for data input
│   │   ├── PredictionForm.css
│   │   ├── ResultCard.js           # Results display component
│   │   └── ResultCard.css
│   ├── App.js                      # Main application component
│   ├── App.css
│   ├── index.js                    # React DOM render
│   └── index.css                   # Global styles
├── package.json                   # Dependencies and scripts
└── README.md                       # This file
```

## Prerequisites

- **Node.js 14+** (Download from https://nodejs.org/)
- **npm** (comes with Node.js)
- **FastAPI Backend running** on http://127.0.0.1:8000

## Installation

### 1. Navigate to Frontend Directory

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

This installs:
- `react@18.2.0` - UI library
- `react-dom@18.2.0` - React rendering
- `axios@1.6.0` - HTTP client
- `react-scripts@5.0.1` - Build tools

### 3. Start Development Server

```bash
npm start
```

The application will open at `http://localhost:3000`

## How to Use

### Step 1: Fill Patient Data
- Enter all 8 health metrics in the form:
  - **Pregnancies** - Number of pregnancies
  - **Plasma Glucose** - Measured value in mg/dL
  - **Blood Pressure** - Diastolic pressure in mmHg
  - **Skin Thickness** - Triceps skinfold in mm
  - **Serum Insulin** - 2-hour reading in mu U/ml
  - **BMI** - Body Mass Index in kg/m²
  - **Diabetes Pedigree Function** - Genetic risk factor (0-1)
  - **Age** - Patient age in years

### Step 2: Click "Get Prediction"
- Form validation ensures all fields are filled
- Loading indicator appears while predicting
- API call sent to `/api/predict` endpoint

### Step 3: View Results
- **Prediction** - Binary classification (Low Risk / High Risk)
- **Probability** - Percentage likelihood (0-100%)
- **Visual Indicator** - Color-coded progress bar
- **Recommendations** - Tailored medical advice based on result
- **Disclaimer** - Important medical disclaimer

## API Integration

The frontend communicates with the FastAPI backend:

**Endpoint:** `POST /api/predict`

**Request Format:**
```json
{
  "pregnancies": 2,
  "glucose": 120.0,
  "blood_pressure": 70.0,
  "skin_thickness": 30.0,
  "insulin": 88.0,
  "bmi": 28.5,
  "diabetes_pedigree_function": 0.5,
  "age": 33
}
```

**Response Format:**
```json
{
  "prediction": 0,
  "probability": 0.0493
}
```

## CORS Configuration

The frontend connects to the backend through the `proxy` setting in `package.json`:

```json
"proxy": "http://127.0.0.1:8000"
```

This allows development without CORS issues. For production, configure CORS in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Available Scripts

### `npm start`
Runs the app in development mode with hot reload.

### `npm build`
Builds the app for production to the `build` folder.

### `npm test`
Launches the test runner (if tests are added).

## Styling

### Global Theme
- **Primary Gradient:** `#667eea` to `#764ba2`
- **Success Color:** `#28a745` (Low Risk)
- **Danger Color:** `#dc3545` (High Risk)
- **Font:** Segoe UI, Tahoma, Geneva, Verdana, sans-serif

### Responsive Breakpoints
- **Desktop:** Full grid layout (form + results side-by-side)
- **Tablet/Mobile:** Stacked layout (form above results)

## Customization

### Modify Form Fields
Edit `frontend/src/components/PredictionForm.js`:

```javascript
const fields = [
  { key: 'pregnancies', label: 'Custom Label', icon: 'fa-icon-name' },
  // Add more fields
];
```

### Change Colors
Edit theme colors in component CSS files:

```css
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Add New Components
Create new files in `frontend/src/components/` following the existing pattern.

## Deployment

### Build for Production
```bash
npm run build
```

This creates an optimized `build/` folder.

### Deploy to GitHub Pages
1. Install `gh-pages`:
   ```bash
   npm install --save-dev gh-pages
   ```

2. Add to `package.json`:
   ```json
   "homepage": "https://anikets160.github.io/health-risk-prediction-fastapi-ml",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```

3. Deploy:
   ```bash
   npm run deploy
   ```

### Deploy to Vercel
1. Connect GitHub repo to Vercel
2. Set build command: `npm run build`
3. Set output directory: `build`

## Troubleshooting

### Issue: "Cannot reach backend"
**Solution:** Ensure FastAPI server is running on `http://127.0.0.1:8000`
```bash
uvicorn app.main:app --reload
```

### Issue: Port 3000 already in use
**Solution:** Use a different port
```bash
PORT=3001 npm start
```

### Issue: CORS errors
**Solution:** Ensure `proxy` is set in `package.json` and backend FastAPI is running

### Issue: Module not found errors
**Solution:** Reinstall dependencies
```bash
rm -rf node_modules package-lock.json
npm install
```

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Optimized component rendering
- CSS animations use GPU acceleration
- Async API calls prevent UI blocking
- Lazy loading ready for future enhancements

## Future Enhancements

- [ ] Add historical prediction tracking
- [ ] Export results as PDF
- [ ] User authentication
- [ ] Multiple patient profiles
- [ ] Data visualization charts
- [ ] Dark mode theme
- [ ] Multi-language support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make changes and test
4. Commit (`git commit -am 'Add feature'`)
5. Push (`git push origin feature/improvement`)
6. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues or questions, contact the development team or open an issue on GitHub.

---

**Happy Predicting!** 🎉
