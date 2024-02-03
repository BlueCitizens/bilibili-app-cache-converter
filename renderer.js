const information = document.getElementById('info')
information.innerText = `本应用正在使用 Chrome (v${versions.chrome()}), Node.js (v${versions.node()}), 和 Electron (v${versions.electron()})`

function sendToPython() {

    PythonShell.run(
        "hello.py", null, function (err, results) {
            if (err) throw err
            console.log('finished')
            console.log(results)
        }
    )
}