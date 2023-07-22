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
                        <el-table-column prop="Temperature" label="温度" />
                        <el-table-column prop="Humidity" label="湿度" />
                        <el-table-column prop="Luminance" label="光照" />
                        <el-table-column prop="LightStatus" label="灯光状态" />
                        <el-table-column prop="MotorStatus" label="电机状态" />
                    </el-table>
                </ClientOnly>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>
let sensorData = ref([])

// TODO: 从华为云获取数据

// 获取随机数据
const getRandomSensorData = async () => {
    // 先用随机数据
    const data = [
        {
            name: '传感器1',
            Temperature: Math.random() * 100,
            Humidity: Math.random() * 100,
            Luminance: Math.random() * 100,
            LightStatus: Math.random() > 0.5 ? '开' : '关',
            MotorStatus: Math.random() > 0.5 ? '开' : '关',
            status: Math.random() > 0.5 ? '正常' : '异常'
        },
        {
            name: '传感器2',
            Temperature: Math.random() * 100,
            Humidity: Math.random() * 100,
            Luminance: Math.random() * 100,
            LightStatus: Math.random() > 0.5 ? '开' : '关',
            MotorStatus: Math.random() > 0.5 ? '开' : '关',
            status: Math.random() > 0.5 ? '正常' : '异常'
        },
        {
            name: '传感器3',
            Temperature: Math.random() * 100,
            Humidity: Math.random() * 100,
            Luminance: Math.random() * 100,
            LightStatus: Math.random() > 0.5 ? '开' : '关',
            MotorStatus: Math.random() > 0.5 ? '开' : '关',
            status: Math.random() > 0.5 ? '正常' : '异常'
        },
        {
            name: '传感器4',
            Temperature: Math.random() * 100,
            Humidity: Math.random() * 100,
            Luminance: Math.random() * 100,
            LightStatus: Math.random() > 0.5 ? '开' : '关',
            MotorStatus: Math.random() > 0.5 ? '开' : '关',
            status: Math.random() > 0.5 ? '正常' : '异常'
        },
        {
            name: '传感器5',
            Temperature: Math.random() * 100,
            Humidity: Math.random() * 100,
            Luminance: Math.random() * 100,
            LightStatus: Math.random() > 0.5 ? '开' : '关',
            MotorStatus: Math.random
                () > 0.5 ? '开' : '关',
            status: Math.random() > 0.5 ? '正常' : '异常'
        },
    ]
    sensorData.value = data
}

// 每秒刷新一次数据
setInterval(() => {
    getSensorData()
}, 1000)

// 表格行的样式
const tableRowClassName = ({ row, rowIndex }) => {
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