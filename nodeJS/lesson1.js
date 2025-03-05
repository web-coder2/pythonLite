const http = require("http")


const port = 4000

const server = http.createServer((req, res) => {
	if (req.method == "GET") {
		res.writeHead(200, {
			"Content-Type" : "text/html"
		})
		res.end(`
			<h2 style='color: green; font-family: monospace;'>we1c0me to w3b-c0d3r</h2>
			<form method='post' action='/'>
				<input name='message' type='text'>
				<button type='submit'>s3nd m3ss4ges</button>
			</form>
		`)
	} else if (req.method == "POST") {
		let messages = []
		req.on("data", data => {
			messages.push(Buffer.from(data))
		})
		req.on("end", () => {
			console.log(messages.toString())
			let comment = messages.toString().split("=")[1]
			
			res.writeHead(200, {
				'Content-Type' : "text/html"
			})

			res.end(`
				<h2 style="color: blue;">youre message >>> ${comment}</h2>
			`)
		})
	}
})

server.listen(port, () => {
	console.log(`server running on ${port} port`)
})