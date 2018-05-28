/*
 * @Author: 孙福聪 
 * @Date: 2018-05-28 13:56:59 
 * @Last Modified by: 孙福聪
 * @Last Modified time: 2018-05-28 15:10:45
 */

import axios from "axios";
let baseURL = "";
process.env.NODE_ENV == "development"
  ? (baseURL = "http://localhost:5000/api")
  : (baseURL = "");
let http = axios.create({
  baseURL
});
export default {
  login(cb, pr,) {
    return http.post("./login", {
      username: pr.state.username,
      password: pr.state.password
    })
  }
};
