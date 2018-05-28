import Vue from "vue";
import axios from "axios";
var state = {

    username: '',
    password: '',
    then: ''
};
let baseURL = "";
process.env.NODE_ENV == "development" ?
    (baseURL = "http://localhost:5000/api") :
    (baseURL = "");
let http = axios.create({
    baseURL
});
var actions = {
    // 封装一个 ajax 方法
    login(login) {
        http
            .post("./login", {
                username: state.username,
                password: state.password
            })
            .then(res => {
                login.commit('login', res.data)
            })
    }
};
const mutations = {
    login(state, data) {
        state.then = data
    }
}
export default {
    state,
    mutations,
    actions
};