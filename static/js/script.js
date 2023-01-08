var files = {
	files: []
}

axios.get("/api/arquivos").then((res) => {
	var data = res.data
	data["files"].forEach(function(item) {
		files.files.push({
			filename: item,
			url: `/api/arquivo/${item}`
		})
	})
})

function pegarArquivo() {
	console.log("Clicado")
	console.log(this.files.files[0].url)
	window.location.href = `${this.files.files[0].url}`
}

function deletaFile() {
	console.log("Deletado")
	filename = document.querySelector('#deleteFilename').value
	
}

var listFiles = Vue.extend({
	data: function() {
		return files
	},
	template: `
		<ul>
			<li v-for="file in files">
				<button key='{{ file.filename }}'' class='btn btn-dark mb-2' onclick="pegarArquivo()">{{ file.filename }}</button>
			</li>
		</ul>
	`
})

function sendFile() {
	var data = new FormData();
	data.append('file', document.getElementById('arquivo'));

	axios.post('/api/arquivo/save', data)
}

Vue.component('list-file', listFiles)

new Vue({
	el: '#app'
})