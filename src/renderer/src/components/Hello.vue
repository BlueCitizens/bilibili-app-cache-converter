<template>
    <img alt="logo" class="logo" src="@renderer/assets/electron.svg" />
    <div class="creator">Powered by electron-vite</div>
    <div class="text">
        Build an Electron app with
        <span class="vue">Vue</span>
    </div>
    <p class="tip">Please try pressing <code>F12</code> to open the devTool</p>
    <mdui-button>Button</mdui-button>
    <div class="actions">
        <div class="action">
            <a href="https://electron-vite.org/" target="_blank" rel="noreferrer">Documentation</a>
        </div>
        <div class="action">
            <a target="_blank" rel="noreferrer" @click="ipcHandle">Send IPC</a>
        </div>
        <div class="action">
            <a target="_blank" href="http://0.0.0.0:5001/hello">Send flask</a>
        </div>
    </div>
    <Versions />
</template>
<script setup>
import Versions from './Versions.vue'
import 'mdui/mdui.css';
import 'mdui';

const ipcHandle = () => window.electron.ipcRenderer.send('ping')
</script>