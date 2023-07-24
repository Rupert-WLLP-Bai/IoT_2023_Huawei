<!-- pages/index.vue -->
<template>
  <el-container style="margin: 0 auto">

    <el-header>
      <h1 class="animate__animated animate__fadeIn">石油电缆防偷盗系统</h1>
    </el-header>

    <el-main>

      <el-row :gutter="20">

        <el-col :span="12">

          <el-card class="box animate__animated animate__fadeInUp">
            <div class="card-header">
              <h2>系统介绍</h2>
            </div>

            <div class="card-body">
              <p>本系统是一个石油电缆防偷盗检测系统。通过加速度传感器和视频监测进行防盗检测,使用华为云IoT平台进行数据传输和设备管理。</p>
            </div>

          </el-card>

          <el-card class="box animate__animated animate__fadeInUp">
            <div class="card-header">
              <h2>实时地图显示</h2>
            </div>
            <div class="card-body">
              <p>使用百度地图API,实时显示电缆位置。(每20秒更新一次)</p>
            </div>
          </el-card>

        </el-col>

        <el-col :span="12">

          <el-card class="box animate__animated animate__fadeInUp">
            <div class="card-header">
              <h3>关键技术</h3>
            </div>

            <div class="card-body d-flex align-items-center">

              <div>
                <p>前端:Nuxt3、Element Plus</p>
                <p>视频处理: mpegts.js</p>
              </div>

              <div>
                <p>后端: Python Flask</p>
                <p>第三方API: 百度地图API</p>
              </div>

              <div>
                <p>开发板: BearPi Nano</p>
                <p>云服务: 华为云IoTDA</p>
              </div>

            </div>

          </el-card>

        </el-col>

      </el-row>

      <el-row :gutter="20" class="services">

        <el-col :span="6">
          <el-card class="card animate__animated animate__zoomIn">
            <div class="card-header">
              <h3>加速度检测/红外检测</h3>
            </div>

            <div class="card-body">
              <p>采集电缆加速度数据和红外检测数据，判断是否发生异常。</p>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="card animate__animated animate__zoomIn">
            <div class="card-header">
              <h3>视频监测</h3>
            </div>

            <div class="card-body">
              <p>发生疑似偷盗行为时，通过摄像头进行实时监测。</p>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="card animate__animated animate__zoomIn">
            <div class="card-header">
              <h3>云平台传输</h3>
            </div>

            <div class="card-body">
              <p>通过华为云IoT平台可视化监测数据和设备状态。</p>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="card animate__animated animate__zoomIn">
            <div class="card-header">
              <h3>邮件提醒</h3>
            </div>

            <div class="card-body">
              <p>通过邮件提醒用户电缆状态。</p>
            </div>
          </el-card>
        </el-col>

      </el-row>

    </el-main>

  </el-container>
</template>

<style>
.el-header {
  background: linear-gradient(#E9F5FE, #D9ECFF);
}

.box {
  background: linear-gradient(#E9F5FE, #D9ECFF);
}

.card {
  background: linear-gradient(#D9ECFF, #C6E2FF);
}

.el-main {
  background: linear-gradient(#F2F8FC, #E9F5FE);
}

.box {
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.12);
}

.card-header {
  padding: 10px 16px;
  font-weight: bold;
}
</style>