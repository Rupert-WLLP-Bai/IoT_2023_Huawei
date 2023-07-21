# IoT_2023_Huawei

2023 物联网大赛 华为 - 石油电缆防偷盗 - 前端

## 运行

```bash
npm install
npm run serve
```

## 问题记录

### 1. 在Nuxt3中使用mpegts.js

1, 安装依赖

```bash
npm install --save mpegts.js
```

2, 在`plugins`目录下创建`mpegts.client.ts`文件

```typescript
//mpegts.client.ts
import Mpegts from 'mpegts.js';

export default defineNuxtPlugin(nuxtApp => {
    nuxtApp.provide('mpegts', Mpegts)
})
```

3. 在`xxx.vue`中使用

```typescript
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
```

