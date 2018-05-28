import Vue from "vue";
import shop from "../../api/login";
var state = {
  username: "",
  password: "",
  then: ""
};

var actions = {
  login({ commit }) {
   return shop.login(name, {
      state
    })
  }
}
const mutations = {
  
};
export default {
  state,
  mutations,
  actions
};
