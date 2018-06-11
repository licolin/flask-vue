import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);
import login from "./modules/login"; //登录
import workingHours from "./modules/workingHours"; //工时统计页面

export default new Vuex.Store({
  modules: {
    login,workingHours
  }
});
