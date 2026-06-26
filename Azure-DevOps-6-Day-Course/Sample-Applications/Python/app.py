from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    # In-memory task store (resets on restart) — fine for a demo.
    app.config["TASKS"] = [{"id": 1, "title": "Learn Azure DevOps", "done": False}]
    app.config["NEXT_ID"] = 2

    @app.get("/")
    def index():
        return jsonify(message="Welcome to the Contoso Tasks API")

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/tasks")
    def list_tasks():
        return jsonify(app.config["TASKS"])

    @app.post("/tasks")
    def add_task():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="title is required"), 400
        task = {"id": app.config["NEXT_ID"], "title": title, "done": False}
        app.config["NEXT_ID"] += 1
        app.config["TASKS"].append(task)
        return jsonify(task), 201

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
