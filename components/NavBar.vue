<template>
    <div>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1"> <nuxt-link to="/">首页</nuxt-link></el-menu-item>
            <el-menu-item index="2"> <nuxt-link to="/video">视频</nuxt-link></el-menu-item>
            <el-menu-item index="3"> <nuxt-link to="/home">传感器</nuxt-link></el-menu-item>
            <el-menu-item index="4"> <nuxt-link to="/about">关于</nuxt-link></el-menu-item>
            <el-menu-item index="5"> <nuxt-link to="/rtmp">rtmp测试</nuxt-link></el-menu-item>
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
            break
        case '2':
            router.push({ path: '/video' })
            break
        case '3':
            router.push({ path: '/home' })
            break
        case '4':
            router.push({ path: '/about' })
            break
    }
}
</script>