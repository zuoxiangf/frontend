<template>
  <div class="page-container">
    <el-card class="table-card" shadow="never">
      <div slot="header" class="card-header">
        <span class="card-title">员工列表</span>
        <el-button type="primary" size="small" icon="el-icon-refresh" @click="getList">
          刷新
        </el-button>
      </div>

      <el-table
          :data="users"
          border
          stripe
          size="medium"
          :header-cell-style="{ background: '#fafafa', color: '#909399', fontWeight: '500' }"
          style="width: 100%"
      >
        <el-table-column prop="userWorkno" label="员工工号" width="120"/>
        <el-table-column label="姓名" width="100">
          <template v-slot="scope">{{ scope.row.familyName }}{{ scope.row.name }}</template>
        </el-table-column>
        <el-table-column prop="mobile" label="电话" width="140"/>

        <el-table-column prop="staffType" label="员工类型" width="100">
          <template v-slot="scope">
            {{ String(scope.row.staffType) === '1' || scope.row.staffType === '正式' ? '正式' : '外包' }}
          </template>
        </el-table-column>

        <el-table-column prop="userCardno" label="身份证号" width="180"/>
        <el-table-column prop="registerTime" label="注册时间" width="180"/>
        <el-table-column fixed="right" label="操作" min-width="140">
          <template v-slot="scope">
            <el-button type="primary" size="small" @click="edit(scope.row)">编辑</el-button>
            <el-button type="danger" size="small" @click="handleDelete(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <Edit ref="edit" @refresh="handleRefresh"></Edit>

  </div>
</template>

<script>
import axios from "axios";
import Edit from "@/components/Edit.vue";

axios.defaults.baseURL = 'http://localhost:9001';

export default {
  name: 'App',
  components: {Edit},
  data() {
    return {
      users: [
          { userWorkno: 'A001', familyName: '张', name: '三', mobile: '13800000001', staffType: '正式', userCardno: '110101199001011234', registerTime: '2016-05-02 10:00:00' },
        { userWorkno: 'A002', familyName: '李', name: '四', mobile: '13800000002', staffType: '正式', userCardno: '110101199002022345', registerTime: '2016-05-04 09:00:00' },
        { userWorkno: 'A003', familyName: '王', name: '五', mobile: '13800000003', staffType: '外包', userCardno: '110101199003033456', registerTime: '2016-05-01 14:00:00' },
      ]
    }
  },
  methods: {
    async getList() {
      const api = await axios.get('/api/user/detail');
      this.users = api.data.data;
    },
    handleClick(row) {
      console.log(row);
    },
    async handleDelete(id) {
      try {
        await this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
          distinguishCancelAndClose: true,
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        });
      } catch (action) {
        // 用户取消或关闭弹窗，无需刷新
        this.$message({
          type: 'info',
          message: action === 'cancel' ? '已取消删除' : '已关闭删除'
        });
        return;
      }
    
      try {
        await axios.delete(`/api/user/deleteDetail/${id}`);
        this.$message({ type: 'success', message: '删除成功' });
      } catch (e) {
        this.$message({ type: 'error', message: '删除失败，请稍后重试' });
        return;
      }
    
      await this.getList();
    },
    edit(row){
      this.$refs.edit.open(row);
    },
    handleRefresh() {
      this.getList();
      this.$message({ type: 'success', message: '刷新成功' });
    }
  },
  mounted() {
    this.getList();
  }
}
</script>

<style scoped>
.page-container {
  max-width: 1400px;
  margin: 0 auto;
}

.table-card {
  border-radius: 4px;
  border: 1px solid #ebeef5;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.06);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-title {
  font-size: 16px;
  font-weight: 500;
  color: #303133;
}

/* 表格 hover / 斑马纹颜色贴合 Element 规范 */
.table-card ::v-deep .el-table__body tr:hover > td {
  background-color: #f5f7fa !important;
}

.table-card ::v-deep .el-table__row--striped td {
  background-color: #fafafa;
}

/* 固定右侧操作列补白，避免视觉断层 */
.table-card ::v-deep .el-table th.el-table__cell {
  letter-spacing: 0;
}
</style>