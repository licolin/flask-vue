<template lang='pug'>
div
    //- h1 工时统计小工具
    Form(:model="$store.state.workingHours.formItem",:label-width="80").Form
        FormItem(label="计算周期")
            DatePicker(type="daterange",placeholder="选择时间",v-model="$store.state.workingHours.formItem.date",style="width: 100%",value='yyyy-MM-dd',@on-change='chengedate')
        FormItem(label="选择人员")
            Select(v-model="$store.state.workingHours.formItem.select")
                Option(value='sunfucong') 我
                Option(value='guotonghao') 小郭
        FormItem(label="任务状态")
            Select(v-model="$store.state.workingHours.formItem.state")
                Option(value='Closed') 关闭
                Option(value='Resolved') 已解决
                Option(value='Resolved, Closed') 已解决+关闭
        FormItem
            Button(type="primary",@click='query',:loading="loading") 查询
        FormItem(label="工时统计:")
            p {{$store.state.workingHours.formItem.workingHours}}
</template>
<script>
export default {
  data() {
    return {
      loading: false
    };
  },
  methods: {
    chengedate(value) {
      this.$store.commit("workingday", value);
    },
    query() {
      this.loading = true;
      this.$store.commit("postdata");
      this.$store.dispatch("workingday").then(res => {
        this.loading = false;
      });
    }
  },
  mounted() {}
};
</script>
<style lang="stylus" scoped>
.Form {
  width: 80%;
  text-align: center;
  margin: 20vh auto;
}
</style>
