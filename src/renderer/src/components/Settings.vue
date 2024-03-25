<template>
    <div class="text">
        <mdui-card class="main-card">
            <mdui-tabs placement="top" value="tab-1">
                <mdui-tab value="tab-1">安卓版设置</mdui-tab>
                <mdui-tab value="tab-2">WIN版设置</mdui-tab>
                <mdui-tab value="tab-3">About</mdui-tab>

                <mdui-tab-panel slot="panel" value="tab-1">Panel 1</mdui-tab-panel>
                <mdui-tab-panel slot="panel" value="tab-2">Panel 2</mdui-tab-panel>
                <mdui-tab-panel slot="panel" value="tab-3">
                    <div class="action">
                        <mdui-chip href="https://github.com/BlueCitizens/bilibili-app-cache-converter" target="_blank">
                            GitHub<img src="../assets/link.svg"
                                style="height: 16px;padding-left: 8px;padding-top: 3px;" />
                        </mdui-chip>
                    </div>
                </mdui-tab-panel>
            </mdui-tabs>
        </mdui-card>
    </div>
</template>

<script>
import 'mdui/components/tabs.js';
import 'mdui/components/tab.js';
import 'mdui/components/tab-panel.js';
</script>