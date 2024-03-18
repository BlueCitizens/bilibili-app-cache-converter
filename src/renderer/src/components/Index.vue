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
import useClipboard from "vue-clipboard3";
import 'mdui/mdui.css';
import 'mdui/components/text-field.js';
import 'mdui/components/button.js';
import 'mdui/components/fab.js';
import 'mdui/components/icon.js';
import 'mdui/components/button-icon.js';
import 'mdui/components/card.js';
import 'mdui/components/chip.js';
import 'mdui/components/checkbox.js';
import 'mdui/components/dialog.js';
import 'mdui/components/top-app-bar.js';
import 'mdui/components/top-app-bar-title.js';
import 'mdui/components/linear-progress.js';
import 'mdui/components/list.js';
import 'mdui/components/list-item.js';
import 'mdui/components/list-subheader.js';
import '@mdui/icons/attach-file.js';
import '@mdui/icons/autorenew.js';
import '@mdui/icons/close.js';
import { snackbar } from 'mdui/functions/snackbar.js';
import { getTheme } from 'mdui/functions/getTheme.js';
import { dialog } from 'mdui/functions/dialog.js';
import { setColorScheme } from 'mdui/functions/setColorScheme.js';
import { hello, convert } from '@renderer/api';



export default {
    name: 'index',
    components: { Versions },
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
        const checkdel = ref(null)

        onMounted(() => {
        })
        return {
            checkup: checkup,
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