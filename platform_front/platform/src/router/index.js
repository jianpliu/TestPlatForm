import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp.vue'
import Main from '../components/Main.vue'
import TestReport from '../components/TestReport.vue'
import TestCase from '../components/TestCase.vue'
import Draft from '../components/Draft.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/draft',
    name: 'Draft',
    component: Draft
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    children:[
    {
      path:"/report",
      name:"TestReport",
      component:TestReport,

    },
    {
      path:"/testcase",
      name:"TestCase",
      component:TestCase,

    },

    ]
  },
 
  
]

const router = new VueRouter({
  routes
})

export default router
