<template>
    <NavBar />
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
            url: 'https://vps-cn-east-3-iec-yz.hwcloudvis.com/work021/live?app=vis&stream=channel_10739276331320000002&project_id=4bf99293674b486d8938f9a890eb84e7&key=41c5fb35ba576ea408d7aa8668b95451&t=1690035531'
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