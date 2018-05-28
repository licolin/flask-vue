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
      this.$store.dispatch("login").then(() => {
        if (this.$store.state.login.then.success) {
          this.$Message.success(this.$store.state.login.then.data);
        } else {
          this.$Message.warning(this.$store.state.login.then.data);
          this.$store.commit('login',null)
        }
      })
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
