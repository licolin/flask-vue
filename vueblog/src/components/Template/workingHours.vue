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
        FormItem(label="周期小结:")
            p {{p}}
</template>
<script>
import timerelyon from "../../api/time.json";

export default {
  data() {
    return {
      loading: false,
      p: ""
    };
  },
  methods: {
    //时间转换
    formatDate1(now) {
      var now = new Date(now);
      var year = now.getFullYear(),
        month = now.getMonth() + 1,
        date = now.getDate(),
        hour = now.getHours(),
        minute = now.getMinutes(),
        second = now.getSeconds();
      return (
        year + "-" + month + "-" + date + " " + hour + ":" + minute
        //  +
        // ":" +
        // second
      );
    },
    mGetDate(year, month) {
      var d = new Date(year, month, 0);
      return d.getDate();
    },
    //时间转换
    formatDate(now) {
      var now = new Date(now);
      var year = now.getFullYear(),
        month = now.getMonth() + 1,
        date = now.getDate(),
        hour = now.getHours(),
        minute = now.getMinutes(),
        second = now.getSeconds();
      return this.mGetDate(year, month);
      // return (
      //   year + "-" + month + "-" + date + " " + hour + ":" + minute
      //   //  +
      //   // ":" +
      //   // second
      // );
    },
    chengedate(value) {
      console.log(value);
      this.$store.commit("workingday", value);
      /**
       * 字符串转时间（yyyy-MM-dd)
       * result （分钟）
       */

      var OneDate = value[0].split("-");
      var one = new Date(OneDate[0], OneDate[1] - 1, OneDate[2]).getTime();
      var TwoDate = value[1].split("-");
      var Two = new Date(TwoDate[0], TwoDate[1] - 1, TwoDate[2]).getTime();
      var timeone = this.formatDate(one);
      var timeTwo = this.formatDate(Two);
      var Numberday = 0; //天数
      var Weekend = 0; //周末数
      var Holidayandvacations = 0;
      for (let index = new Date(one).getDate(); index <= timeone; index++) {
        var week = new Date(
          new Date(OneDate[0], OneDate[1] - 1, index).getTime()
        ).getDay();
        // console.log(week);
        Numberday += 1;
        if (week === 0 || week === 6) {
          Weekend += 1;
        }
        var month =
          new Date(
            new Date(OneDate[0], OneDate[1] - 1, index).getTime()
          ).getMonth() + 1;
        if (month < 10) {
          month = "0" + month;
        }
        if (index < 10) {
          index = "0" + index;
        }
        month = "d" + month + index;
        if (timerelyon[2018][month] === 1) {
          Holidayandvacations += 1;
        }
        if (timerelyon[2018][month] === 0) {
          Weekend -= 1;
        }
      }
      for (let index = new Date(Two).getDate(); index <= timeTwo; index--) {
        var week = new Date(
          new Date(TwoDate[0], TwoDate[1] - 1, index).getTime()
        ).getDay();
        Numberday += 1;
        if (week === 0 || week === 6) {
          Weekend += 1;
        }
        if (index === 1) {
          break;
        }
      }
      var Workingday = Numberday - Weekend - Holidayandvacations;
      this.p =
        "周期内总天数=" +
        Numberday +
        ",周末数=" +
        Weekend +
        ",节假日数=" +
        Holidayandvacations +
        ",工作日天数=" +
        Workingday +
        "周期内标准工时为" +
        Workingday * 8
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
