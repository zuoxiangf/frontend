import Vue from 'vue'
import App from './App.vue'
import elementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/main.css'

Vue.use(elementUI)

new Vue({
  render: (h) => h(App)
}).$mount('#app')
