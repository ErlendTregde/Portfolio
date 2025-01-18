
# Portfolio Project

Click the link below to see my portfolio:

[https://erlendtregde.github.io/PortfolioGithubPages/](https://erlendtregde.github.io/PortfolioGithubPages/)

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

## Additional Notes
- The portfolio is built with Vue.js and deployed using GitHub Pages.
- Make sure the `vite.config.js` file has the correct `base` path set for GitHub Pages:
   ```javascript
   export default {
     base: '/PortfolioGithubPages/',
   };

Enjoy exploring the portfolio! 🎉
```

---

### Key Fixes:
1. Removed references to a backend since it wasn't included in your original setup.
2. Focused on Vue.js and GitHub Pages setup.
3. Simplified project structure to reflect the actual folders used.
4. Updated deployment instructions for GitHub Pages to avoid confusion.

Let me know if you need further refinements! 😊
