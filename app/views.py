from app import app
from flask import jsonify,request



@app.route("/process",methods=["POST"])
def prompt():
    return jsonify({"response":"Initiated"})