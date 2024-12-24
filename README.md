```markdown
# Portfolio Project - README

## Overview
A simple portfolio project using Vue for the frontend and Flask for the backend. The backend serves the built Vue frontend as static files along with API endpoints.

---

## Project Structure
```plaintext
Portfolio/
├── backend/
│   ├── app.py          # Flask application
│   ├── dist/           # Built Vue frontend files
│   ├── venv/           # Python virtual environment
├── frontend/
│   └── PortfolioFrontend/
│       ├── src/        # Vue source files
│       ├── dist/       # Build output (copied to backend/dist)
│       ├── package.json # Frontend dependencies
```

---

## Requirements
### Backend
- Python 3.x
- Flask

### Frontend
- Node.js
- npm

---

## Getting Started

### Backend Setup
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Flask:
   ```bash
   pip install flask
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access:
   - API: [http://127.0.0.1:5000/api/projects](http://127.0.0.1:5000/api/projects)
   - Frontend: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### Frontend Setup (Development Mode)
1. Navigate to the frontend folder:
   ```bash
   cd frontend/PortfolioFrontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Access:
   - [http://localhost:5173/](http://localhost:5173/)

---

### Build the Frontend
1. Navigate to the frontend folder:
   ```bash
   cd frontend/PortfolioFrontend
   ```
2. Build the frontend:
   ```bash
   npm run build
   ```
3. Copy the `dist` folder to the backend:
   ```bash
   cp -r dist ../../backend/
   ```
4. Access the app via Flask:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
