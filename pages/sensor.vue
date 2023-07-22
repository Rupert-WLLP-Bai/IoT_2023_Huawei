<template>
    <NavBar />
    <!-- 居中显示大标题 -->
    <div style="text-align: center;">
        <h1>传感器数据</h1>
    </div>
    <!-- 显示数据的最后更新时间 -->
    <div style="text-align: center;">
        <h3>最后更新时间: {{ lastUpdateTime }}</h3>
    </div>
    <!-- 表格 -->
    <div>
        <el-row>
            <el-col>
                <el-table :data="sensorData" :row-class-name="tableRowClassName" style="width: 100%">
                    <el-table-column prop="device_id" label="设备ID"></el-table-column>
                    <el-table-column prop="Accel_x" label="加速度X"></el-table-column>
                    <el-table-column prop="Accel_y" label="加速度Y"></el-table-column>
                    <el-table-column prop="Accel_z" label="加速度Z"></el-table-column>
                    <el-table-column prop="Cable_Status" label="电缆状态"></el-table-column>
                    <el-table-column prop="Latitude" label="纬度"></el-table-column>
                    <el-table-column prop="Longitude" label="经度"></el-table-column>
                    <el-table-column prop="Temperature" label="温度"></el-table-column>
                </el-table>
            </el-col>
        </el-row>
    </div>

    <div class="instruction_div">
        <el-button type="primary" @click="sendInstruction()">发送指令</el-button>
    </div>

    <!-- 当前页面请求的最后更新时间 -->
    <div style="text-align: center;">
        <h3>当前页面请求的最后更新时间: {{ new Date() }}</h3>
    </div>

    <div hidden>
        <h1>测试数据格式如下:</h1>
        {{ shadowData }}
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import NavBar from '@/components/NavBar.vue'
let sensorData = ref([])
let lastUpdateTime = ref(null)
let shadowData = ref([])
// TODO: 从华为云获取数据
// 暂时的解决 方案是 访问Flask后端获取Shadow数据
const getShadowData = async () => {
    // 注意这个是跨域请求
    const res = await useFetch(() => 'http://127.0.0.1:5000/getShadow')
    shadowData.value = res.data.value;

    const device_id = shadowData.value['device_id']
    const shadow = shadowData.value['shadow'][0]

    const reported = shadow['reported']
    
    const event_time = reported['event_time']   // 最后更新时间
    // 20230721T153956Z 转化为 2023-07-21 15:39:56
    lastUpdateTime.value = event_time.slice(0, 4) + '-' + event_time.slice(4, 6) + '-' + event_time.slice(6, 8) + ' ' + event_time.slice(9, 11) + ':' + event_time.slice(11, 13) + ':' + event_time.slice(13, 15)

    const properties = reported['properties']
    const Accel_x = properties['Accel_x']
    const Accel_y = properties['Accel_y']
    const Accel_z = properties['Accel_z']
    const Cable_Status = properties['Cable_Status']
    const Latitude = properties['Latitude']
    const Longitude = properties['Longitude']
    const Temperature = properties['Temperature']

    // 将数据添加到表格中，不使用push，因为push会导致表格中的数据重复
    sensorData.value = [
        {
            device_id: device_id,
            Accel_x: Accel_x,
            Accel_y: Accel_y,
            Accel_z: Accel_z,
            Cable_Status: Cable_Status,
            Latitude: Latitude,
            Longitude: Longitude,
            Temperature: Temperature,
            event_time: event_time,
            status: '正常'
        }
    ]
}
// 每1秒刷新一次Shadow数据
setInterval(() => {
    getShadowData()
}, 1000)


// 按下之后发送指令, 并且将按钮的样式变为红色
const sendInstruction = () => {
    // TODO: 发送指令
    
    // 按钮变为红色
    document.getElementsByClassName('el-button')[0].style.backgroundColor = 'red'
    
    // 将文字显示为正在发送指令...
    document.getElementsByClassName('el-button')[0].innerText = '正在发送指令...'

    // 显示倒计时
    let count = 5

    // 每1秒减少1
    let timer = setInterval(() => {
        count--
        document.getElementsByClassName('el-button')[0].innerText = '正在发送指令... ' + count + 's'
        if (count == 0) {
            clearInterval(timer)
            document.getElementsByClassName('el-button')[0].innerText = '发送指令'
            document.getElementsByClassName('el-button')[0].style.backgroundColor = '#409EFF'
        }
    }, 1000)

}

</script>