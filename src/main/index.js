import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import { join, dirname } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'

async function handleFileOpen() {
  const { canceled, filePaths } = await dialog.showOpenDialog({ properties: ['openDirectory'] })
  if (!canceled) {
    return filePaths[0]
  }
}

function createWindow() {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 600,
    height: 450,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'), { hash: '/' })
  }
}


var { PythonShell } = require('python-shell');
let pyshell = new PythonShell('src/flask/app.py');
let pyProc = require('child_process')
var myExec = null;
// 启动flask server，通过python-shell 调用python脚本（开发调试阶段）
function startServer() {
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
  });
}

// 启动flask server，通过子进程执行已经将python项目打包好的exe文件（打包阶段）
function startServer_EXE() {
  // 当前应用的目录
  // 由于打包前后 即开发环境和生产环境的根目录不同
  // const appPath = app.isPackaged ? dirname(app.getPath('exe')) : app.getAppPath()
  let serverpath = join(__dirname, "../../resources/app.exe").replace("app.asar", "app.asar.unpacked");
  console.log(serverpath)
  // let script = join(__dirname, 'app.exe')

  myExec = pyProc.execFile(serverpath)
  myExec.stdout.on('data', (data) => {
    console.log(`Received chunk ${data}`);
  }); 
}

function stopServer() {
  pyshell.end(function (err, code, signal) {
    if (err) throw err;
    console.log('Server shutdown code: ' + code);
    console.log('Server shutdown signal: ' + signal);
    console.log('Server shutdown normally');
  });
  pyshell.kill('SIGTERM')
}

const { execSync } = require('child_process');
const os = require('os');
const platform = os.platform();
const process = require('node:process');

const GetProcessInfo = (port) =>
  new Promise((resolve, reject) => {
    if (platform === 'win32') {
      const order = `netstat -aon | findstr ${port}`;
      try {
        const stdout = execSync(order);
        const portInfo = stdout.toString().trim().split(/\s+/);
        const pId = portInfo[portInfo.length - 1];
        const processStdout = execSync(`tasklist | findstr ${pId}`);
        const [pName] = processStdout.toString().trim().split(/\s+/);
        resolve({
          pId,
          pName,
        });
        var plist = [], idx
        for (idx = 0; idx < portInfo.length - 1;) {
          plist.push(portInfo.slice(idx, idx += 5))
        }
        plist.forEach((element) => {
          console.log('Killing process: ' + element)
          process.kill(element[element.length - 1], 'SIGTERM')
        })
        console.log('flask server shutdown success')
      } catch (error) {
        reject(error);
      }
    } else {
      const order = `lsof -i :${port}`;
      try {
        const stdout = execSync(order);
        const [pName, pId] = stdout
          .toString()
          .trim()
          .split(/\n/)[1]
          .split(/\s+/);
        resolve({
          pId,
          pName,
        });
      } catch (error) {
        reject(error);
      }
    }
  });

// 停止flask server 函数
function stopServer_EXE() {
  GetProcessInfo('5001')
  let exc = myExec.kill('SIGTERM')
  console.log(exc)
  pyProc = null
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  ipcMain.handle('dialog:openFile', handleFileOpen)
  // Set app user model id for windows
  electronApp.setAppUserModelId('com.electron')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  createWindow()

  startServer_EXE()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
  stopServer_EXE()
})

// In this file you can include the rest of your app"s specific main process
// code. You can also put them in separate files and require them here.
