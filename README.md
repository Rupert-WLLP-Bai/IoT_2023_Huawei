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

### 2. 获取华为云的IoTDA的数据

1. 注意使用`华为云账户`获取Token，而不是`华为账户`
2. 如果使用`华为账户`，则需要创建一个IAM用户，再调用相应的接口获取Token
3. 将`X-Subject-Token`放入`X-Auth-Token`中，即可获取数据
