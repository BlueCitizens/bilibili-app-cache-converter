<template>
    <div class="mdui-theme-dark">
        <mdui-text-field readonly v-model="this.form.path" variant="outlined" label="缓存文件路径">
            <mdui-button-icon slot="end-icon" @click="triggerPath">
                <mdui-icon-attach-file></mdui-icon-attach-file>
            </mdui-button-icon>
        </mdui-text-field>
        <!-- <label for="choosepath">666</label> -->
        <input id="choosepath" type='file' style="display: none;" v-on:change="triggerPath" webkitdirectory directory />
        <mdui-button v-on:click="requestConvert">转换</mdui-button>
        <!-- <button v-on:click="triggerPath" type="button" id="btn">Open a File</button>
        File path: <strong id="filePath"></strong> -->
    </div>

    <div class="actions">
        <div class="action">
            <a href="https://electron-vite.org/" target="_blank" rel="noreferrer">Documentation</a>
        </div>
        <div class="action">
            <a target="_blank" rel="noreferrer" @click="ipcHandle">Send IPC</a>
        </div>
    </div>
    <Versions />
</template>
<script>
import Versions from './Versions.vue'
import 'mdui/mdui.css';
import 'mdui/components/text-field.js';
import 'mdui/components/button.js';
import 'mdui/components/icon.js';
import 'mdui/components/button-icon.js';
import '@mdui/icons/attach-file.js';
import { snackbar } from 'mdui/functions/snackbar.js';
import { alert } from 'mdui/functions/alert.js';
import { hello, convert } from '@renderer/api';



export default {
    name: 'index',
    data() {
        return {
            form: {
                path: ''
            }
        }
    },
    methods: {
        openChoose() {
            choosepath.click()
        },
        // 触发主进程 打开文件选择
        async triggerPath() {
            const filePath = await window.electronAPI.openFile()
            this.form.path = filePath
        },
        requestConvert() {
            let form = JSON.parse(JSON.stringify(this.form));
            convert({ form }).then((response) => {

                console.log(response.data)
                if (response.code === 200) {
                }
                this.info(response.data)
            }).catch((error) => {
                console.log(error);
            });
        },
        info(message) {
            snackbar({
                message: message,
                action: "Undo",
                onActionClick: () => console.log("click action button")
            });
        },
        warn() {
            alert({
                headline: "Alert Title",
                description: "Alert description",
                confirmText: "OK",
                onConfirm: () => console.log("confirmed"),
            });
        },
        ipcHandle() {
            window.electron.ipcRenderer.send('ping')
        },
    },
    mounted() {
        /*         const btn = document.getElementById('btn')
                const filePathElement = document.getElementById('filePath')
        
                btn.addEventListener('click', async () => {
                    const filePath = await window.electronAPI.openFile()
                    filePathElement.innerText = filePath
                }) */
    }
}

</script>