<template>
    <NavBar />
    <div>
        <el-row>
            <el-col>
                <el-table :data="sensorData">
                    <el-table-column prop="name" label="传感器" />
                    <el-table-column prop="status" label="状态" />
                    <el-table-column prop="latitute" label="纬度" />
                    <el-table-column prop="longitute" label="经度" />
                </el-table>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>
const sensorData = ref([
    {
        name: '传感器1',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器2',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器3',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器4',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器5',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器6',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器7',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器8',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    },
    {
        name: '传感器9',
        status: '正常',
        latitute: '30.123',
        longitute: '120.123'
    }
])
</script>