<template>
    <div>
        <!-- flv拉流测试 -->
        <video id="video" controls autoplay></video>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const { $mpegts } = useNuxtApp()

const video = ref(null)

let flvPlayer = ref(null)

onMounted(() => {
    if ($mpegts.getFeatureList().mseLivePlayback) {
        var videoElement = document.getElementById('video')
        flvPlayer = $mpegts.createPlayer({
            type: 'flv',
            isLive: false,
            url: 'https://vps-cn-south-1-cloud.hwcloudvis.com/work025/live?app=vis&stream=channel_10628627091320000001&project_id=3f70f7e3046f40af84ed44b81d049ab4&key=edf4045fcbe8f9cbb5d94cfb5035ef8f&t=1690121006'
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