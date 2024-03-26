<template>
    <div class="mdui-theme-auto">
        <mdui-layout>
            <mdui-layout-item placement="left" class="index-layout-left">
                <mdui-navigation-rail class="navi" value="android">
                    <mdui-navigation-rail-item @click="gotoPostDetail('/index/android')" value="android">
                        <mdui-icon-phone-android--outlined slot="icon"></mdui-icon-phone-android--outlined>
                        Android</mdui-navigation-rail-item>
                    <mdui-navigation-rail-item @click="gotoPostDetail('/index/windows')" value="windows">
                        <mdui-icon-desktop-windows--outlined slot="icon"></mdui-icon-desktop-windows--outlined>
                        Windows</mdui-navigation-rail-item>
                    <mdui-navigation-rail-item @click="gotoPostDetail('/index/settings')" value="settings">
                        <mdui-icon-settings--outlined slot="icon"></mdui-icon-settings--outlined>
                        Settings</mdui-navigation-rail-item>
                </mdui-navigation-rail>
            </mdui-layout-item>

            <mdui-layout-main class="index-layout-main">
                <router-view></router-view>
            </mdui-layout-main>
        </mdui-layout>
    </div>

    <Versions />
</template>
<script>
import Versions from '@renderer/components/Versions.vue';
import 'mdui/mdui.css';
import 'mdui/components/layout.js';
import 'mdui/components/layout-item.js';
import 'mdui/components/layout-main.js';
import 'mdui/components/navigation-rail.js';
import 'mdui/components/navigation-rail-item.js';
import 'mdui/components/text-field.js';
import 'mdui/components/button.js';
import 'mdui/components/fab.js';
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
import 'mdui/components/icon.js';
import '@mdui/icons/phone-android--outlined.js';
import '@mdui/icons/desktop-windows--outlined.js';
import '@mdui/icons/settings--outlined.js';
import '@mdui/icons/attach-file.js';
import '@mdui/icons/autorenew.js';
import '@mdui/icons/close.js';


export default {

    name: 'index',
    components: { Versions },
    methods: {
        gotoPostDetail(post) {
            console.log(post)
            this.$router.push(post);
        },
    }
}

</script>