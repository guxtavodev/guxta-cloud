
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
app = Flask(__name__, template_folder="pages")

DIRETORIO = "C:\\Users\\larisa\\Documents\\Programação\\Guxta Cloud\\files"

CORS(app)

@app.route("/api/status")
def status():
	return jsonify({
		"message": "API ONLINE"
		})

@app.route("/api/arquivos", methods=["GET"])
def getArquivos():
	arquivos = []
	for nomeDoArquivo in os.listdir(DIRETORIO):
		endereco = os.path.join(DIRETORIO, nomeDoArquivo)
		if os.path.isfile(endereco):
			arquivos.append(nomeDoArquivo)

	return jsonify({
		"files": arquivos
		})

@app.route("/api/arquivo/<name>", methods=["GET"])
def send_file(name):
	name = name.replace("%7B%7B", "").replace("%7D%7D", "")
	return send_from_directory(DIRETORIO, name, as_attachment=True)

@app.route("/api/arquivo/save", methods=["POST"])
def postFile():
	file = request.files.get('meuArquivo')
	print(file)
	nomeDoArquivo = file.filename
	file.save(os.path.join(DIRETORIO, nomeDoArquivo))

	return jsonify({
		"message": "OK"
		})

@app.route("/api/arquivo/delete", methods=["POST"])


@app.route("/")
def homepage():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(port=8080, host="0.0.0.0")