
# Portfolio Project

Click the link below to see my portfolio:

[My portfolio](http://erlendtregde.me./)

## Overview
A simple portfolio project with:
- **Frontend**: Vue.js
- **Deployment**: GitHub Pages

---

## Project Structure
```plaintext
Portfolio/
├── frontend/
│   └── PortfolioFrontend/
│       ├── src/        # Vue source files
│       ├── dist/       # Built production files
│       ├── package.json # Frontend dependencies
```

---

## Setup Instructions



### Frontend Setup
1. Navigate to the frontend:
bash
   cd frontend/PortfolioFrontend
   
2. Install dependencies:
bash
   npm install
   
3. Start the development server:
bash
   npm run dev
   
4. Build the frontend for production:
bash
   npm run build
   
5. Copy the `dist` folder to the backend:
bash
   cp -r dist ../../backend/
   
6. Access the app via Flask at:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


This version is concise but still includes all necessary details for setting up and running your project.
"

### Frontend Setup
1. Navigate to the frontend directory:
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
   - The app will be available locally at: [http://127.0.0.1:5173/](http://127.0.0.1:5173/)

4. Build the frontend for production:
   ```bash
   npm run build
   ```
   - This generates the `dist` folder with production-ready files.

---

### Deployment Instructions
1. Copy the contents of the `dist` folder to your GitHub Pages repository:
   ```bash
   cp -r dist ../PortfolioGithubPages
   ```

2. Commit and push the changes to the repository:
   ```bash
   git add -A
   git commit -m "Deploy portfolio to GitHub Pages"
   git push origin main
   ```

3. Access the portfolio at:
   [https://erlendtregde.github.io/PortfolioGithubPages/](https://erlendtregde.github.io/PortfolioGithubPages/)

---


Enjoy exploring the portfolio! 🎉

