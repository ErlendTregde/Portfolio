from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder="dist")

# Serve the Vue frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    if path != "" and not path.startswith("api") and not path.endswith((".js", ".css", ".html", ".ico", ".png", ".jpg")):
        path = "index.html"
    try:
        return send_from_directory(app.static_folder, path)
    except FileNotFoundError:
        return "File Not Found", 404

# Example API endpoint
@app.route("/api/projects")
def get_projects():
    return jsonify([
        {"id": 1, "name": "Project 1", "description": "Description of project 1"},
        {"id": 2, "name": "Project 2", "description": "Description of project 2"},
    ])

if __name__ == "__main__":
    app.run(debug=True)
