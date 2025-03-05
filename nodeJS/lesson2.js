const http = require('http')
const path = require('path')
const fs = require('fs')

const port = 4000

let server = http.createServer((req, res) => {
	if (req.method == "GET") {
		res.writeHead(200, {
			"Content-Type" : "text/html"
		})

		console.log(`visited ${req.url} url`)

		if (req.url == "/") {
			fs.readFile(path.join(__dirname, 'index.html'), 'utf-8', (error, html) => {
				if (error) {
					throw error
				} else {
					res.end(html)
				}
			})
		} else if (req.url == "/form") { 
			fs.readFile(path.join(__dirname, 'form.html'), 'utf-8',(err, html) => {
				if (err) {
					throw err
				} else {
					res.end(html)
				}
			})
		}
	}
})

server.listen(port, () => {
	console.log(`server running on ${port} port`)
})