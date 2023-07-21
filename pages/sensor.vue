<template>
    <NavBar />
    <h1>
        这一部分还需要从华为云拉取数据，目前是一秒刷新一次的随机数据
    </h1>
    <h2>
        表格行的颜色似乎有点问题，需要调整一下
    </h2>
    <div>
        <el-row>
            <el-col>
                <ClientOnly>
                    <el-table :data="sensorData" :row-class-name="tableRowClassName" style="width: 100%">
                        <el-table-column prop="name" label="传感器" />
                        <el-table-column prop="status" label="状态" />
                        <el-table-column prop="latitute" label="纬度" />
                        <el-table-column prop="longitute" label="经度" />
                    </el-table>
                </ClientOnly>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>
// 写一个函数随机生成一组数据
const randomData = () => {
    const data = []
    for (let i = 0; i < 10; i++) {
        data.push({
            name: '传感器' + i,
            status: Math.random() > 0.5 ? '正常' : '异常',
            latitute: Math.random() * 100,
            longitute: Math.random() * 100
        })
    }
    return data
}

// 生成一组随机数据
const sensorData = ref(randomData())

// 每隔一段时间更新一次数据
setInterval(() => {
    sensorData.value = randomData()
}, 1000)

// 表格行的样式
const tableRowClassName = ({ row , rowIndex }) => {
    if (row.status === '异常') {
        return 'warning-row'
    } else {
        return 'success-row'
    }
}
</script>

<style scoped>
.el-table .warning-row {
    background: rgb(255, 0, 0);
}

.el-table .success-row {
    background: #dfd;
}
</style>