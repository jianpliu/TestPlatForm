// 创建axios实例

import axios from 'axios'
const instance = axios.create({
    // 基础url地址
    baseURL: 'http://localhost:5000/',
    // 超时时间
    timeout: 1000,
    // 头信息
    headers: { 'content-type': 'application/json' }
  });

// axios的HOOK函数，在发送请求前会主动调用此函数
instance.interceptors.request.use(function(config){
  // 如果token存在并且发送的不是登陆接口的话，就把token加入到认证中
  if (localStorage.getItem("token") && config.url !="/login"){
    config.auth={username:localStorage.getItem("token"),password:""
    }
  
  }
  return config;
});





  //导出实例：js的特点 不导出其他的类和方法用不了
export default instance;