<template>
    <div>
        <!-- rtmp拉流测试 -->
        <video id="video" controls autoplay></video>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const { $mpegts } = useNuxtApp()

const video = ref(null)

onMounted(() => {
    if ($mpegts.getFeatureList().mseLivePlayback) {
        var videoElement = document.getElementById('video')
        var flvPlayer = $mpegts.createPlayer({
            type: 'flv',
            isLive: false,
            url: 'https://sf1-hscdn-tos.pstatp.com/obj/media-fe/xgplayer_doc_video/flv/xgplayer-demo-360p.flv'
        })
        flvPlayer.attachMediaElement(videoElement)
        flvPlayer.load()
        flvPlayer.play()
    }
})

onUnmounted(() => {
    flvPlayer.destroy()
})

</script>