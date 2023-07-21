<template>
    <NavBar />
    <div>
        <!-- 从摄像头获取视频-->
        <h1>摄像头</h1>
        <div>
            <video id="video" width="640" height="480" autoplay></video>
        </div>
        <!-- 加入一个录制计时器-->
        <div>
            <h1>录制计时器</h1>
            <p>录制时间：{{ time }}秒</p>
            <el-button @click="startRecord">开始录制</el-button>
            <el-button @click="stopRecord">停止录制</el-button>
            <el-button @click="playRecord">播放录制</el-button>
            <el-button @click="clearRecord">清除录制</el-button>
            <el-button @click="downloadRecord">下载录制</el-button>
        </div>

        <!-- 视频播放器-->
        <div>
            <h1>播放器</h1>
            <video id="player" width="640" height="480" controls></video>
        </div>
    </div>
</template>

<script setup>
// 计时器变量
let interval = null

// mounted的时候获取视频
onMounted(() => {
    const video = document.getElementById('video')
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                video.srcObject = stream
            })
            .catch((err0r) => {
                console.log('Something went wrong!', err0r)
            })
    }
})

// 录制视频
const time = ref(0) // 录制时间
const recorder = ref(null) // 录制器
const chunks = ref([]) // 录制的视频块

// 开始录制并且开始计时
const startRecord = () => {
    const video = document.getElementById('video')
    recorder.value = new MediaRecorder(video.srcObject)
    recorder.value.start()
    recorder.value.ondataavailable = (e) => {
        chunks.value.push(e.data)
    }
    time.value = 0
    // 每隔1毫秒计时器加0.001
    interval = setInterval(() => {
        time.value += 0.001
    }, 1)
}

// 停止录制并且停止计时
const stopRecord = () => {
    recorder.value.stop()
    recorder.value.onstop = (e) => {
        const blob = new Blob(chunks.value, { type: 'video/mp4' })
        chunks.value = []
        const videoURL = window.URL.createObjectURL(blob)
        const player = document.getElementById('player')
        player.src = videoURL
    }
    clearInterval(interval)
}

// 播放录制的视频
const playRecord = () => {
    const player = document.getElementById('player')
    player.play()
}

// 下载录制的视频
const downloadRecord = () => {
    const blob = new Blob(chunks.value, { type: 'video/mp4' })
    chunks.value = []
    const videoURL = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = videoURL
    a.download = 'video.mp4'
    a.click()
}

// 清除录制的视频
const clearRecord = () => {
    const player = document.getElementById('player')
    player.src = ''
}

</script>