<template>
    <div class="text">
        <mdui-card class="main-card">
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
            <mdui-checkbox ref="checkup" checked>UP主独立文件夹</mdui-checkbox>
            <mdui-checkbox ref="checkdm" checked>同时转换弹幕</mdui-checkbox>
            <mdui-checkbox ref="checkdel" disabled>删除源</mdui-checkbox>
            <mdui-button full-width variant="tonal" :disabled="this.btn" v-on:click="requestConvert">
                <mdui-icon-autorenew></mdui-icon-autorenew>
            </mdui-button>
        </mdui-card>

        <mdui-dialog fullscreen class="example-dialog">
            <mdui-top-app-bar slot="header">
                <mdui-button-icon @click="closeDialog()">
                    <mdui-icon-close></mdui-icon-close>
                </mdui-button-icon>
                <mdui-top-app-bar-title>部分成功 以下路径出错</mdui-top-app-bar-title>
                <mdui-button variant="text" @click="copyPath(JSON.stringify(failedItems))">复制到剪贴板</mdui-button>
            </mdui-top-app-bar>
            <mdui-list>
                <mdui-list-subheader>点击项目可复制路径</mdui-list-subheader>
                <mdui-list-item v-for="item in failedItems" @click="copyPath(item.path)">
                    {{ item.path }}
                    <span slot="description">{{ item.error }}</span>
                </mdui-list-item>
            </mdui-list>

            <div class="clipboardInner" @click="copyPath" style="display: inline;"></div>
        </mdui-dialog>
        <div ref="clipboard" @click="handleCopy" style="display: inline; "></div>
    </div>
</template>
<script>

import { onMounted, ref } from 'vue';
import useClipboard from "vue-clipboard3";
import { snackbar } from 'mdui/functions/snackbar.js';
import { getTheme } from 'mdui/functions/getTheme.js';
import { setColorScheme } from 'mdui/functions/setColorScheme.js';
import { hello, convert } from '@renderer/api';
export default {
    name: 'android',
    setup() {
        const clipboard = ref(null)
        const { toClipboard } = useClipboard()
        const text = ref('')
        const handleCopy = async () => {
            try {
                console.log(text)
                await toClipboard(text.value, document.querySelector(".clipboardInner"))
                console.log('复制成功')
            } catch (e) {
                console.error(e);
                console.error('复制失败')
            }
        }
        const checkup = ref(null)
        const checkdm = ref(null)
        const checkdel = ref(null)

        onMounted(() => {
        })
        return {
            checkup: checkup,
            checkdm: checkdm,
            checkdel: checkdel,
            clipboard: clipboard,
            handleCopy,
            text
        }
    },
    data() {
        return {
            form: {
                path: '',
                output: '',
                isUp: false,
                isDm: false,
                isDel: false
            },

            checked: false,
            btn: false,
            progress: {
                visible: 'visibility: hidden',
                value: '0'
            },
            failedItems: [],
            clipboardTemp: ''
        }
    },
    methods: {
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
            this.form.isDm = this.checkdm.checked
            this.form.isDel = this.checkdel.checked
            console.log(this.form)
            this.btn = true
            this.progress.visible = ''
            let form = JSON.parse(JSON.stringify(this.form));
            convert({ form }).then((response) => {
                // console.log(response.data)
                // if (response.code === 200) {
                // }
                let res = response.data
                console.log(res[1][0])
                if (res[0] === 'true') {
                    if (res[1].length === 0) {
                        this.info('转换成功 :)')
                    } else {
                        console.log(res[1])
                        // this.warn(res[1])
                        this.failedItems = res[1]
                        const dialog = document.querySelector(".example-dialog")
                        dialog.open = true
                    }
                } else if (res[0] === 'false') {
                    this.info('致命错误 请检查日志')
                }
                this.btn = false
                this.progress.visible = 'visibility: hidden'
            }).catch((error) => {
                console.log(error);
            });
        },
        copyPath(val) {
            this.text = val
            console.log(this.clipboard)
            this.clipboard.click()
        },
        info(message) {
            snackbar({
                message: message
            });
        },
        closeDialog() {
            const dialog = document.querySelector(".example-dialog")
            dialog.open = false
            this.failedItems = []
        }
    },
    created() {
        setColorScheme('#80DAF6');
    },
    mounted() {
        console.log(getTheme())
    }
}
</script>