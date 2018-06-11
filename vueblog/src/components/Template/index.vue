<template lang='pug'>
div
    Menu(mode="horizontal",active-name="1",@on-select='goturouter')
        MenuItem(name="1")  内容管理
        MenuItem(name="2")  用户管理
        Submenu(name="3")  
            template(slot="title") 小工具
            MenuGroup(title="工作相关")
                MenuItem(name="workingHours") 工时统计
        MenuItem(name="4")  系统管理
    router-view
</template>
<script>
export default {
  data() {
    return {};
  },
  methods:{
      goturouter(e){
          this.$router.push({
              path:e
          })
      }
  }
};
</script>
<style lang="stylus" scoped>
.Cancellation {
    float: right;
}
</style>
