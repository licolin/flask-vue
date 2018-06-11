/*
 * @Author: 孙福聪 
 * @Date: 2018-05-28 13:56:59 
 * @Last Modified by: 孙福聪
 * @Last Modified time: 2018-06-11 17:53:37
 */

import axios from "axios";
let baseURL = "";
process.env.NODE_ENV == "development" ?
  (baseURL = "http://localhost:5000/api") :
  (baseURL = "");
let http = axios.create({
  baseURL
});
export default {
  login(cb, pr, ) {
    return http.post("./api/login", {
      username: pr.state.username,
      password: pr.state.password
    })
  },
  workingday(cb, pr, ) {
    return http.post("./api/workingday", {
      Startdate: pr.state.formItem.Startdate,
      enddate: pr.state.formItem.enddate,
      code:pr.state.formItem.select
    })
  }
};
