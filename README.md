
```markdown
# Portfolio Project

The portfolio is hosted on GitHub Pages and can be accessed here: [View Portfolio](https://erlendtregde.github.io/PortfolioGithubPages/)

## Overview
A simple portfolio project with:
- **Frontend**: Vue.js
- **Backend**: Flask (serves the Vue build as static files)

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
│       ├── dist/       # Build output
│       ├── package.json # Frontend dependencies
```

---

## Setup Instructions

### Backend Setup
1. Navigate to the backend:
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
4. Start the Flask app:
   ```bash
   python app.py
   ```
5. Access the app at:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### Frontend Setup
1. Navigate to the frontend:
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
4. Build the frontend for production:
   ```bash
   npm run build
   ```
5. Copy the `dist` folder to the backend:
   ```bash
   cp -r dist ../../backend/
   ```
6. Access the app via Flask at:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```

This version is concise but still includes all necessary details for setting up and running your project.
