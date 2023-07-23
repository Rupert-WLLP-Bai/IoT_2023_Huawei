<template>
    <div>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1"> <nuxt-link to="/">首页</nuxt-link></el-menu-item>
            <el-menu-item index="3"> <nuxt-link to="/sensor">传感器数据</nuxt-link></el-menu-item>
            <el-menu-item index="4"> <nuxt-link to="/about">关于</nuxt-link></el-menu-item>
            <el-menu-item index="5"> <nuxt-link to="/flv">实时监控视频</nuxt-link></el-menu-item>
            <el-menu-item index="2" :disabled="true"> <nuxt-link to="/camera">摄像头测试(已弃用)</nuxt-link></el-menu-item>
        </el-menu>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const activeIndex = ref('1')

const handleSelect = (index) => {
    activeIndex.value = index
    switch (index) {
        case '1':
            router.push({ path: '/' })
            activeIndex.value = '1'
            break
        case '2':
            router.push({ path: '/camera' })
            activeIndex.value = '2'
            break
        case '3':
            router.push({ path: '/sensor' })
            activeIndex.value = '3'
            break
        case '4':
            router.push({ path: '/about' })
            activeIndex.value = '4'
            break
        case '5':
            router.push({ path: '/flv' })
            activeIndex.value = '5'
            break
    }
}
</script>