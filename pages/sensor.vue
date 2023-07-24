<!-- pages/sensor.vue -->
<template>
    <!-- 居中显示大标题 -->
    <div style="text-align: center;">
        <h1>传感器数据</h1>
    </div>
    <!-- 显示数据的最后更新时间 -->
    <div style="text-align: center;">
        <h3>最后更新时间: {{ lastUpdateTime }}</h3>
    </div>
    <div style="text-align: center;">
        <h3>邮箱提醒状态: {{ mail_available }}</h3>
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
        <el-button type="primary" @click="refreshData()">刷新数据</el-button>
        <el-button type="primary" @click="resetStatus()">重置电缆状态</el-button>
        <el-button type="primary" @click="sendTestMail()">发送测试邮件</el-button>
    </div>

    <div class="instruction_div">
        <!-- 需要检查邮箱是否符合格式 -->
        <el-input placeholder="请输入邮箱地址" v-model="emailAddress" style="width: 20%;" clearable>
        </el-input>
    </div>

    <div class="instruction_div">
        <!-- 加入一个el-switch 开启的时候显示(自动布控) -->
        <el-switch v-model="value1" active-color="#13ce66" inactive-color="#ff4949" active-text="自动布控" inactive-text="默认状态"
            @change="handleSwitch">
        </el-switch>
    </div>

    <div class="instruction_div">
        <h3> 实时地图 (若未显示, 请刷新页面)</h3>
        <!-- 这部分显示一个地图，显示电缆的位置 -->
        <!-- 使用百度地图API -->
        <!-- center的参数使用获取的经纬度 -->
        <!-- 20秒轮询一次更新当前的位置 --> 
        <img :src="img_url" alt="图片加载失败" width="80%" height="80%">        
    </div>
</template>

<script setup>
let sensorData = ref([])
let lastUpdateTime = ref(null)
let shadowData = ref([])
let mail_available = ref(true)  // 是否可以进行邮件提醒
let img_url = ref(null) // 图片的url
let longitude = '0'
let latitude = '0'

let emailAddress = ref('2052526@tongji.edu.cn') // 邮箱地址

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
    // 加上8小时时差
    lastUpdateTime.value = new Date(lastUpdateTime.value).getTime() + 8 * 60 * 60 * 1000
    // 转化为 YYYY-MM-DD HH:MM:SS
    lastUpdateTime.value = new Date(lastUpdateTime.value).toLocaleString('chinese', { hour12: false })


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

    // 更新经纬度
    longitude = Longitude
    latitude = Latitude

    // 检查电缆状态， 如果为异常并且mail_available为true， 则发送邮件
    if (Cable_Status === 'Intrude' && mail_available.value === true) {
        // 发送邮件
        const subject = '电缆状态异常'
        const content = '电缆状态异常, 请及时处理, 设备ID: ' + device_id
        const res = useFetch(() => 'http://localhost:5000/sendEmail/' + emailAddress.value + '/' + subject + '/' + content)
        ElNotification({
            title: '电缆状态异常',
            message: '电缆状态异常, 请及时处理',
            type: 'error'
        })
        mail_available.value = false
    }


}
// 每5秒刷新一次Shadow数据
let interval = setInterval(() => {
    getShadowData()
}, 5000)


// 按下之后发送指令, 并且将按钮的样式变为红色
const sendInstruction = () => {
    // TODO: 发送指令
    // 按钮变为红色
    ElNotification({
        title: '这是一个测试按钮',
        message: '倒计时3秒',
        type: 'warning'
    })
    document.getElementsByClassName('el-button')[0].style.backgroundColor = 'red'

    // 将文字显示为正在发送指令...
    document.getElementsByClassName('el-button')[0].innerText = '正在发送指令...'

    // 显示倒计时
    let count = 3

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

const refreshData = () => {
    getShadowData()
    ElNotification({
        title: '刷新数据成功',
        message: '刷新数据成功',
        type: 'success'
    })
}

const handleSwitch = (value) => {
    //  value = true 时，自动布控
    if (value === true) {
        const res = useFetch(() => 'http://localhost:5000/sendMessage/ON')
        // 如果res.data中有"error_code"，则说明发送失败, 使用ELNotification提示
        if (res.data.value['error_code']) {
            // 将res.data.value Object转化为String 以便于ELNotification显示
            const str = JSON.stringify(res.data.value)
            // 显示ELNotification
            ElNotification({
                title: '开启自动布控失败',
                message: str,
                type: 'error'
            })
        } else {
            ElMessage({
                message: '已经发送指令, 开始自动布控',
                type: 'success'
            })
        }
        console.log(res.data.value)
    } else {
        const res = useFetch(() => 'http://localhost:5000/sendMessage/OFF')
        // 如果res.data中有"error_code"，则说明发送失败, 使用ELNotification提示
        if (res.data.value['error_code']) {
            // 将res.data.value Object转化为String 以便于ELNotification显示
            const str = JSON.stringify(res.data.value)
            // 显示ELMessage
            ElNotification({
                title: '关闭自动布控失败',
                message: str,
                type: 'error'
            })
        } else {
            ElMessage({
                message: '已经发送指令, 停止自动布控',
                type: 'success'
            })
        }
        console.log(res.data.value)
    }
}

// 重置电缆状态
const resetStatus = () => {
    const res = useFetch(() => 'http://localhost:5000/resetStatus/Safe')
    // 如果res.data中有"error_code"，则说明发送失败, 使用ELNotification提示
    if (!res.data.value) {
        ElNotification({
            title: '重置电缆状态失败',
            message: '重置电缆状态失败',
            type: 'error'
        })
    }
    if (res.data.value['error_code']) {
        // 将res.data.value Object转化为String 以便于ELNotification显示
        const str = JSON.stringify(res.data.value)
        // 显示ELMessage
        ElNotification({
            title: '重置电缆状态失败',
            message: str,
            type: 'error'
        })
    } else {
        ElMessage({
            message: '已经发送指令, 重置电缆状态',
            type: 'success'
        })
    }
    console.log(res.data.value)
    mail_available.value = true
}

// 发送测试邮件 
const sendTestMail = async () => {
    // @app.route('/sendEmail/<email_address>/<subject>/<content>', methods=['GET'])
    try {
        const email_address = emailAddress.value
        const subject = '测试邮件'
        const content = '这是一封测试邮件'
        const res = useFetch(() => 'http://localhost:5000/sendEmail/' + email_address + '/' + subject + '/' + content)
    }
    catch (err) {
        console.log(err)
        ElNotification({
            title: '发送测试邮件失败',
            message: err,
            type: 'error'
        })
    }
    ElNotification({
        title: '发送测试邮件',
        message: '发送测试邮件成功',
        type: 'success'
    })

}

// 每20秒刷新一次图片
const getImg = async () => {
    // 使用Latitute和Longitude获取图片
    const ak = "o3zv0zIOtX7LtGUNncjyEHoFIfQ1L48w";
    const url = "http://api.map.baidu.com/staticimage/v2?ak=" + ak + "&width=1024&height=512&center="+longitude + "," + latitude + "&zoom=18" + "&markers=" + longitude + "," + latitude;
    
    // 更新img标签的src
    img_url.value = url
    console.log(img_url.value)
}
// 每20秒刷新一次图片
let img_interval = setInterval(() => {
    getImg()
}, 20000)

onMounted(() => {
    getShadowData()
    getImg()
})

onUnmounted(() => {
    clearInterval(interval)
    clearInterval(img_interval)
})
</script>

<style>
.instruction_div {
    text-align: center;
    margin-top: 20px;
}
</style>