<template>
    <div class="text mdui-theme-auto">
        <div class="">
            <mdui-card style="width: 400px;padding: 20px 20px 20px 20px;">
                <mdui-linear-progress :style="this.progress.visible"></mdui-linear-progress>
                <mdui-text-field style="margin-bottom: 20px;" v-model="this.form.path" variant="outlined"
                    label="Cache Directory">
                    <mdui-button-icon slot="end-icon" @click="triggerPath">
                        <mdui-icon-attach-file></mdui-icon-attach-file>
                    </mdui-button-icon>
                </mdui-text-field>
                <mdui-text-field style="margin-bottom: 20px;" v-model="this.form.output" variant="outlined"
                    label="Output Directory">
                    <mdui-button-icon slot="end-icon" @click="triggerPath">
                        <mdui-icon-attach-file></mdui-icon-attach-file>
                    </mdui-button-icon>
                </mdui-text-field>
                <mdui-button full-width variant="tonal" :disabled="this.btn" v-on:click="requestConvert">
                    <mdui-icon-autorenew></mdui-icon-autorenew>
                </mdui-button>
            </mdui-card>
        </div>
    </div>


    <div class="actions mdui-theme-auto">
        <div class="action">
            <mdui-chip elevated href="https://www.mdui.org" target="_blank">
                GitHub
            </mdui-chip>
            <mdui-chip elevated href="https://www.mdui.org" target="_blank">
                GitHub
            </mdui-chip>
        </div>
    </div>
    <Versions />
</template>
<script>
import Versions from './Versions.vue'
import 'mdui/mdui.css';
import 'mdui/components/text-field.js';
import 'mdui/components/button.js';
import 'mdui/components/fab.js';
import 'mdui/components/icon.js';
import 'mdui/components/button-icon.js';
import 'mdui/components/card.js';
import 'mdui/components/chip.js';
import '@mdui/icons/attach-file.js';
import '@mdui/icons/autorenew.js';
import 'mdui/components/layout.js';
import 'mdui/components/layout-item.js';
import 'mdui/components/layout-main.js';
import 'mdui/components/linear-progress.js';
import { snackbar } from 'mdui/functions/snackbar.js';
import { getTheme } from 'mdui/functions/getTheme.js';
import { alert } from 'mdui/functions/alert.js';
import { setColorScheme } from 'mdui/functions/setColorScheme.js';
import { hello, convert } from '@renderer/api';



export default {
    name: 'index',
    data() {
        return {
            form: {
                path: '',
                output: ''
            },
            btn: false,
            progress: {
                visible: 'visibility: hidden',
                value: '0'
            }
        }
    },
    methods: {
        // 触发主进程 打开文件选择
        async triggerPath() {
            const filePath = await window.electronAPI.openFile()
            this.form.path = filePath
        },
        requestConvert() {
            this.btn = true
            this.progress.visible = ''
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
                onActionClick: () => {
                    this.btn = false
                    this.progress.visible = 'visibility: hidden'
                }
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
    },
    created() {

        setColorScheme('#80DAF6');
    },
    mounted() {
        console.log(getTheme())
    }
}

</script>