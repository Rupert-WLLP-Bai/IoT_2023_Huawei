// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@element-plus/nuxt',
    'nuxt-icon',
  ],
  css: [
    '@/assets/css/main.css',
  ],
  app:{
    head:{
      title: '石油电缆防偷盗监测系统',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width,initial-scale=1' },
      ],
    },
  }
})
