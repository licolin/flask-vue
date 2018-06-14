import Vue from "vue";
import shop from "../../api/login";
var state = {
  formItem: {
    date: "",
    Startdate: "",
    enddate: "",
    select: "",
    workingHours: 0,
    state:'Resolved, +Closed',
  }
};

var actions = {
  workingday({
    commit
  }) {
    return shop.workingday(name, {
      state
    }).then(res => {
      commit('getdata', res.data.issues)
    })
  }
}
const mutations = {
  postdata(state) {
    state.formItem.workingHours = 0
  },
  getdata(state, value) {
    value.forEach(element => {
      state.formItem.workingHours += element.fields.customfield_10101

    });
  },
  workingday(state, value) {
    state.formItem.Startdate = value[0];
    state.formItem.enddate = value[1];
  }

};
export default {
  state,
  mutations,
  actions
};
