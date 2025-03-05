function buildJSON() {

	args = []

	for (let idx = 2; idx < process.argv.length; idx++) {
		let param = process.argv[idx].split("=")
		args.push({
			"param" : param[0],
			"value" : param[1] ? param[1] : "N0 VALU3"
		})
	}

	console.log(args)

}

buildJSON()