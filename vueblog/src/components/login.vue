<template lang='pug'>
div.login
  div.conter
    span.home
    ul
      li
        input(placeholder="账号",v-model='$store.state.login.username')
      li
        input(type='password',placeholder="密码",v-model='$store.state.login.password').password
      Button(type="success",long,@click='login').button 登录
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      formInline: {
        user: ""
      }
    };
  },
  methods: {
    login() {
      this.$store.dispatch("login").then(res => {
        console.log(res);
        if (res.data.success) {
          this.$Message.success("登陆成功");
          this.$router.push({
            path: "index"
          });
        } else {
          this.$Message.error(res.data.data);
        }
      });
    }
  }
};
</script>

<style scoped lang='stylus'>
.login {
  background: url('../assets/login/login.jpg') fixed;
  background-size: 100% 100%;
  height: 100%;

  .conter {
    padding: 360px;
    font-size: 22px;

    .home {
      background: url('../assets/login/home.png');
      width: 50px;
      background-size: 100% 100%;
      height: 50px;
      display: inline-block;
    }

    input {
      width: 280px;
      height: 35px;
      border: none;
      border-radius: 5px;
      font-size: 18px;
      padding-left: 10px;
    }

    .password {
      margin-top: 25px;
    }

    .button {
      width: 280px;
      margin-top: 25px;
    }
  }
}
</style>
