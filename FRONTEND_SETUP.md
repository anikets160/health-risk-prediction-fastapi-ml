# Frontend Setup Guide

## Quick Start (5 minutes)

### Prerequisites
- Node.js 14+ installed: https://nodejs.org/
- FastAPI backend running on `http://127.0.0.1:8000`

### Installation & Running

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The UI opens automatically at `http://localhost:3000`

## Architecture

```
App (Main component - manages state and API calls)
├── Header (Title and description)
├── PredictionForm (Input form for 8 health metrics)
└── ResultCard (Results display with visualization)
```

## API Communication Flow

```
User enters data → Form validation → 
POST /api/predict → FastAPI processes → 
Returns {prediction, probability} → 
ResultCard displays results
```

## Features

✅ 8-field input form with validation  
✅ Real-time API integration  
✅ Color-coded risk visualization  
✅ Medical recommendations  
✅ Fully responsive design  
✅ Loading states and error handling  
✅ Beautiful animations  

## Deployment

### Production Build
```bash
npm run build
```
Creates optimized `build/` folder ready for deployment.

### Deploy to Vercel (Recommended)
1. Push code to GitHub
2. Connect repo to Vercel
3. Set build command: `npm run build`
4. Set output: `build`
5. Deploy!

## Troubleshooting

**Port 3000 in use?**
```bash
PORT=3001 npm start
```

**Backend connection error?**
Ensure FastAPI is running:
```bash
uvicorn app.main:app --reload
```

**Missing modules?**
```bash
npm install
```

See `frontend/README.md` for complete documentation.
