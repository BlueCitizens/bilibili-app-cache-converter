<template>
    <div class="text mdui-theme-auto">
        <div class="">
            <mdui-card style="width: 400px;padding: 20px 20px 20px 20px;background-color: hsla(0, 0%, 100%, 0.95);">
                <mdui-linear-progress :style="this.progress.visible"></mdui-linear-progress>
                <mdui-text-field style="margin-bottom: 20px;" v-model="this.form.path" variant="outlined"
                    label="Cache Directory">
                    <mdui-button-icon slot="end-icon" @click="triggerPath('path')">
                        <mdui-icon-attach-file></mdui-icon-attach-file>
                    </mdui-button-icon>
                </mdui-text-field>
                <mdui-text-field style="margin-bottom: 20px;" v-model="this.form.output" variant="outlined"
                    label="Output Directory">
                    <mdui-button-icon slot="end-icon" @click="triggerPath('output')">
                        <mdui-icon-attach-file></mdui-icon-attach-file>
                    </mdui-button-icon>
                </mdui-text-field>
                <mdui-checkbox ref="checkup" checked>UP主Folder</mdui-checkbox>
                <mdui-checkbox ref="checkdel">删除源</mdui-checkbox>
                <mdui-button full-width variant="tonal" :disabled="this.btn" v-on:click="requestConvert">
                    <mdui-icon-autorenew></mdui-icon-autorenew>
                </mdui-button>
            </mdui-card>
        </div>
    </div>


    <div class="actions mdui-theme-auto">
        <div class="action">
            <mdui-chip href="https://github.com/BlueCitizens/bilibili-app-cache-converter" target="_blank">
                GitHub<img src="../assets/link.svg" style="height: 16px;padding-left: 8px;padding-top: 3px;" />
            </mdui-chip>
        </div>
    </div>
    <Versions />
</template>
<script>
import { onMounted, ref } from 'vue';
import Versions from '@renderer/components/Versions.vue';
import 'mdui/mdui.css';
import 'mdui/components/text-field.js';
import 'mdui/components/button.js';
import 'mdui/components/fab.js';
import 'mdui/components/icon.js';
import 'mdui/components/button-icon.js';
import 'mdui/components/card.js';
import 'mdui/components/chip.js';
import 'mdui/components/checkbox.js';
import '@mdui/icons/attach-file.js';
import '@mdui/icons/autorenew.js';
import 'mdui/components/linear-progress.js';
import { snackbar } from 'mdui/functions/snackbar.js';
import { getTheme } from 'mdui/functions/getTheme.js';
import { alert } from 'mdui/functions/alert.js';
import { setColorScheme } from 'mdui/functions/setColorScheme.js';
import { hello, convert } from '@renderer/api';



export default {
    name: 'index',
    components: { Versions },
    setup() {
        const checkup = ref(null);
        const checkdel = ref(null);

        onMounted(() => {
        });
        return {
            checkup: checkup,
            checkdel: checkdel
        };
    },
    data() {
        return {
            form: {
                path: '',
                output: '',
                isUp: false,
                isDel: false
            },

            checked: false,
            btn: false,
            progress: {
                visible: 'visibility: hidden',
                value: '0'
            },
            websocket: null, // WebSocket对象
        }
    },
    methods: {
        setupWebSocket() {
            this.websocket = new WebSocket("ws链接"); // 创建WebSocket连接
            this.websocket.onopen = this.onWebSocketOpen; // WebSocket连接打开时的处理函数
            this.websocket.onmessage = this.onWebSocketMessage; // 收到WebSocket消息时的处理函数
            this.websocket.onclose = this.onWebSocketClose; // WebSocket连接关闭时的处理函数
        },
        onWebSocketOpen() {
            console.log("链接成功");
            const initMessage = {
                type: 'sub',
                topic: '/aa/bb/cc/d',
                parameter: {},
                id: 'bb',
            };
            this.sendMessage(JSON.stringify(initMessage));
        },
        closeWebSocket() {
            if (this.websocket) {
                this.websocket.close(); // 关闭WebSocket连接
            }
        },
        check() {
            if (this.checked === false) {
                this.checked = true
            }
            console.log(this.checked)
        },
        // 触发主进程 打开文件选择
        async triggerPath(val) {
            const filePath = await window.electronAPI.openFile()
            if (val === 'path') {
                this.form.path = filePath
            } else if (val === 'output') {
                this.form.output = filePath
            }
        },
        requestConvert() {

            this.form.isUp = this.checkup.checked
            this.form.isDel = this.checkdel.checked
            console.log(this.form)
            this.btn = true
            this.progress.visible = ''
            let form = JSON.parse(JSON.stringify(this.form));
            convert({ form }).then((response) => {
                console.log(response.data)
                if (response.code === 200) {
                }
                console.log(this.form.isUp)
                let res = response.data
                if (res === true) {
                    this.info('转换成功 :)')
                } else {
                    this.info('转换失败 请检查日志')
                }
                this.btn = false
                this.progress.visible = 'visibility: hidden'
            }).catch((error) => {
                console.log(error);
            });
        },
        info(message) {
            snackbar({
                message: message
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