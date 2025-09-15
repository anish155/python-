from flask import Flask, request, jsonify

app = Flask(__name__)

# simple in-memory storage
stored_names = []

@app.route("/store", methods=["POST"])
def store_name():
    data = request.get_json()
    name = data.get("name", "").strip()

    if name == "":
        return jsonify({"status": "error", "message": "No input given!"}), 400
    
    stored_names.append(name)
    return jsonify({"status": "success", "message": "Name stored successfully!", "names": stored_names})

if __name__ == "__main__":
    app.run(debug=True)


