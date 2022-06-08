<template>
  <div class="login">
  
   <h2>登陆</h2>
    <!--v-model双向绑定，把输入框内的东西放入username中-->
   <v-text-field
      v-model="username"
      label="账号"
      outlined
      clearable
    ></v-text-field>
    <!-- type是html的input属性，可以设置为password -->
    <v-text-field
      v-model="password"
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
//data在vue中代表定义数据
//data是函数，因为Vue中代表实例变量（也可以写成字典形式，字典形式的就是类变量，全局可用（一个vue中定义了别的vue中也可以用））
  data(){
    return {username:"",password:""}
  },



  //methods代表声明一个函数
  methods:{
    login(){
      // let代表定义变量
      let loginData={username:this.username,password:this.password};
      // 使用Vue实例中注册的api变量
      // .then是axios的回调方法=>获取返回结果
      //=>函数：se6函数，定义一个匿名函数，使用当前环境
      this.$api.user.login(loginData).then((response)=>{
        // console.log(response);
        // localStorage是存储到浏览器中的一个数据，全局可用
        localStorage.setItem("token",response.data.access_token);

      });

      this.$api.testcase.getTestcase().then(response=>{
        console.log(response);
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