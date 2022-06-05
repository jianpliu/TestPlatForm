import axios from "./http";
// const代表定义一个常量
const user={
    login(loginData){
        // 使用axios的get方法发送get请求，其中auth代表校验，和Requests的auth参数相同
        return axios.get("/login",{auth:loginData})
    },

};

export default user;