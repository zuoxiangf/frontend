<template>
<el-dialog :visible.sync="dialogVisible" title="编辑" v-model="dialogVisible" width="30%" :before-close="handleClose">
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="姓氏">
      <el-input v-model="form.familyName"></el-input>
    </el-form-item>
    <el-form-item label="名字">
      <el-input v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="手机号">
      <el-input v-model="form.mobile"></el-input>
    </el-form-item>
    <el-form-item label="员工类型">
      <el-select v-model="form.staffType" placeholder="请选择员工类型" style="width: 100%">
        <el-option label="正式" value="1"/>
        <el-option label="临时" value="0"/>
      </el-select>
    </el-form-item>
    <el-form-item label="身份证号">
      <el-input v-model="form.userCardno"></el-input>
    </el-form-item>
    <el-form-item label="注册时间">
      <el-date-picker
          v-model="form.registerTime"
          type="datetime"
          placeholder="选择日期时间"
          value-format="yyyy-MM-dd HH:mm:ss"
          format="yyyy-MM-dd HH:mm:ss"
          style="width: 100%">
      </el-date-picker>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="onUpdated">确 定</el-button>
  </div>
</el-dialog>
</template>


<script>
import {defineComponent, onUpdated} from 'vue'
import axios from "axios";

export default defineComponent({
  name: "Edit",
  data() {
    return {
      dialogVisible: false,
      form: {
        familyName: '',
        name: '',
        mobile: '',
        staffType: '',
        userCardno: '',
        registerTime: ''
      }
    }
  },
  methods: {
    async onUpdated() {
      await axios.put('/api/user/updateDetail', this.form)
      this.dialogVisible = false
      this.$emit('refresh')
    },
    open(row) {
      this.dialogVisible = true;
      Object.assign(this.form, row);
    },
    handleClose() {
      this.dialogVisible = false;
    }

  }
})
</script>



<style scoped>

</style>