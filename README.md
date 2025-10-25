# CI/CD Demo Project (Flask -> Tests -> Static Build -> GitHub Pages Deployment)

This project is designed for beginners who want to connect Python development with a complete CI/CD workflow. It demonstrates:
- Writing modular Python code (importing a class from a module)
- Displaying output using Flask
- Unit testing with pytest
- Generating static HTML content for deployment
- Automatic deployment to GitHub Pages using GitHub Actions

You only need to modify the class in `utils/greeting.py` to trigger the full pipeline and see the update deployed to GitHub Pages.

---

## Project Structure
```
flask-CICD-sample/
├─ app.py # Flask app
├─ generate_static.py # Converts Flask output to static HTML
├─ requirements.txt # Dependencies
├─ utils/
│ └─ greeting.py # Class file (edit this file to trigger changes)
├─ tests/
│ ├─ test_greeting.py # Tests for the greeting class
│ └─ test_route.py # Tests for Flask response
└─ .github/workflows/
└─ deploy.yml # CI/CD configuration
```

---

## Running Locally

### 1. Create and activate a virtual environment (recommended)

```bash
conda activate env_name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```
Open your browser and visit: http://127.0.0.1:5000

## Building Static Output (simulate the CI/CD build)
```bash
python generate_static.py
```
This creates the following files under the docs/ directory:
```
docs/index.html
docs/404.html
```

You can open `docs/index.html` directly in your browser to preview the deployed result.

## CI/CD Pipeline (GitHub Actions -> GitHub Pages)

When you push changes to the main branch, the workflow performs:

1. Install dependencies
2. Generate static HTML using Flask
3. Upload docs/ as the Pages artifact
4. Deploy to GitHub Pages
5. Print the deployment URL in the workflow summary
6. The GitHub Pages deployment URL typically follows: https://<your-username>.github.io/<repository-name>/

If your repository belongs to an organization, replace <your-username> with the organization name.