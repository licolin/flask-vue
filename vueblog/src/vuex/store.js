import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
import login from './login/login' //登录



export default new Vuex.Store({
    modules: {
        login
    }
});