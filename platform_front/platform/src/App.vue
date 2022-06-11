<template>
  <v-app>
    <div id="app" >
    <v-app-bar  height="70" color=primary dark app  clipped-left >
      
      <!-- <h1>欢迎来到测试平台</h1> -->
      <v-img alt="Vue logo" src="./assets/logo.png"
      
      contain
      height="70"
      width="40"

    
      ></v-img>
      <v-spacer></v-spacer>
     
    </v-app-bar>
    </div>
   
    <router-view/>
  
    
    

  </v-app>
</template>

// <style lang="scss">
// #app {
//   font-family: Avenir, Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
//   width:100%;
// }


// </style>
