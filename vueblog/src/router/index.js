import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import index from '@/components/Template/index'
import home from '@/components/Template/home'
import workingHours from '@/components/Template/workingHours'


Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'login',
    component: login
  }, {
    path: '/index',
    name: 'index',
    component: index,
    children: [{
      path: '/index',
      name: 'home',
      component: home,
    }, {
      path: '/workingHours',
      name: 'workingHours',
      component: workingHours,
    }]
  }]
})
