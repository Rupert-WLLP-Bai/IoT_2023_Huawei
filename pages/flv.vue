<!-- pages/flv.vue -->
<template>
    <div>
        <!-- flv拉流测试 -->
        <video id="video" controls autoplay width="80%" height="80%"></video>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const { $mpegts } = useNuxtApp()

const video = ref(null)

let flvPlayer = ref(null)

onMounted(() => {
    // 1690208522
    // 获取当前时间戳
    if ($mpegts.getFeatureList().mseLivePlayback) {
        var videoElement = document.getElementById('video')
        flvPlayer = $mpegts.createPlayer({
            type: 'flv',
            isLive: false,
            url: 'https://vps-cn-east-3-iec-yz.hwcloudvis.com/work029/live?app=vis&stream=channel_10739276331320000003&project_id=4bf99293674b486d8938f9a890eb84e7&key=2198f56b9771a928495eb57d33749e0b&t=1690289115'
        })
        flvPlayer.attachMediaElement(videoElement)
        flvPlayer.load()
        flvPlayer.play()
    }
})

onUnmounted(() => {
    if (flvPlayer) {
        flvPlayer.unload()
        flvPlayer.detachMediaElement()
        flvPlayer.destroy()
    }
})

</script>