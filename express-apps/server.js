const express = require('express')
const path = require('path')

const app = express()
const port = 3000
const static = path.join(__dirname, "../nodeJS")

app.get("/", (req, res) => {
    res.status(200)
    res.sendFile(path.join(static, "index.html"))
})

app.get("/form", (req, res) => {
    res.status(200)
    res.sendFile(path.join(static, "form.html"))
})

app.listen(port, () => {
    console.log(`server runnning on ${port} port >>>`)
})