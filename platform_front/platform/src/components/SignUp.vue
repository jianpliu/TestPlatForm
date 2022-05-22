<template>
  <div class="sign-up">
  
    <h2>注册</h2>
   <v-text-field
      v-model="message4"
      label="账号"
      outlined
      clearable
    ></v-text-field>
    <v-text-field
      v-model="message4"
      label="密码"
      outlined

      type="password"
      clearable
    ></v-text-field>
    <!-- type是html的input属性，可以设置为password -->
    <v-text-field
      v-model="message4"
      label="邮箱"
      outlined
    
      type="password"
      clearable
    ></v-text-field>
    <v-btn  color='primary'  depressed @click="goLogin()">登陆</v-btn>
    
    <v-btn depressed >注册</v-btn>
  </div>
</template>

<script>
export default {
  methods:{
    goLogin(){
      this.$router.push({name:"Login"})
    }
  }
}
</script>

<style scoped>
/* .代表class */
.sign-up{
   width: 600px;
   /*将整个标签居中 */
   margin: 0 auto;
   /*将文本和按钮居中*/
   text-align: center;
}
   

</style>