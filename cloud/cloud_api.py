from flask import Flask, request

app = Flask(__name__)
shelf_status_log = []

@app.route("/api/shelf", methods=["POST"])
def shelf_event():
    data = request.get_json()
    print(f"[CLOUD RECEIVED] Shelf status: {data['status']}")
    shelf_status_log.append(data["status"])
    return {"message": "Received"}, 200

if __name__ == "__main__":
    app.run(debug=True)
