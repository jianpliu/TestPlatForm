import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import api from './http/api'

// 取消初运行的提示
Vue.config.productionTip = false
// 将api变量注册到Vue的变量池中，其他使用Vue实例的组件就可以拿到api使用
Vue.prototype.$api=api

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
