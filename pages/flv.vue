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
            url: 'https://vps-cn-south-1-cloud.hwcloudvis.com/work021/live?app=vis&stream=channel_10628627091320000001&project_id=3f70f7e3046f40af84ed44b81d049ab4&key=6d139daf405332d1d4ce0819f94a8df9&t=1690208522'
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