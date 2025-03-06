const express = require('express')

const app = express()
const port = 4000 

app.set("view engine", "hbs") // второй параметр это какое расширение нужно использовать файлам для рендера
app.set("views", __dirname)

app.get("/", (req, res) => {
	res.render("index.hbs", {
		user : "web-coder",
		role : "coder",
		lps : ["javascript" , "python"] 
	})
})


app.listen(port, () => {
	console.log(`app running on port ${port}`)
})