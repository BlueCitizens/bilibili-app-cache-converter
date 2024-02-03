// main.js

// Modules to control application life and create native browser window
const { app, BrowserWindow } = require('electron')
const { PythonShell } = require('python-shell')
const path = require('node:path')

const options = {
  mode: 'text',
  pythonPath: '/usr/bin/python', // Python 解释器的路径
  pythonOptions: ['-u'], // 解释器选项
  scriptPath: path.join(__dirname, ''), // Python 脚本的路径
  args: [] // 传递给 Python 脚本的参数
};

let pyshell = new PythonShell('hello.py', options);

pyshell.send('hello');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

pyshell.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
});

/* PythonShell.run(pyshell, options).then(messages => {
  // results is an array consisting of messages collected during execution
  console.log('results: %j', messages);
}); */

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.