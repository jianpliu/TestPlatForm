<template>
  <div class="login">
  
    <h2>登陆</h2>
   <v-text-field
      v-model="message4"
      label="账号"
      outlined
      clearable
    ></v-text-field>
    <!-- type是html的input属性，可以设置为password -->
    <v-text-field
      v-model="message4"
      label="密码"
      outlined

      type="password"
      clearable
    ></v-text-field>
    
    
    <v-btn  color='primary'  depressed @click="login()">登陆</v-btn>
    <!-- @是vue的语法，将click事件绑定到函数 -->
    <v-btn depressed @click=goSignUp>注册</v-btn>
  </div>
</template>

<script>
export default {
  //methods代表声明一个函数
  methods:{
    login(){
      // let代表定义变量
      let loginData={username:this.username,password:this.password}
      // 使用Vue实例中注册的api变量
      // .then是axios的回调方法=>获取返回结果
      //=>函数：se6函数，定义一个匿名函数，使用当前环境
      this.$api.user.login(loginData).then(responce=>{
        console.log(responce);

      });
    },




    goSignUp(){
      //this.$router.push:是把一个路由推入栈
      this.$router.push({name:"SignUp"})
    }
  }
}
</script>

<style scoped>
/* .代表class */
.login{
   width: 600px;
   /*将整个标签居中 */
   margin: 0 auto;
   /*将文本和按钮居中*/
   text-align: center;
}
   

</style>