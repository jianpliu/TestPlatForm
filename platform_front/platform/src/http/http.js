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

  //导出实例：js的特点 不导出其他的类和方法用不了
  export default instance;