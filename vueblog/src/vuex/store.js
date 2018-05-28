import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);
import login from "./modules/login"; //登录

export default new Vuex.Store({
  modules: {
    login
  }
});
