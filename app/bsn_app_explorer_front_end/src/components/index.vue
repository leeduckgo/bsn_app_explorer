<template>
    <div style="background-color: #2a2c3b;">
        <div class="row clearfix" >
            <div class="col-md-12 column">
                <nav class="navbar navbar-default  navbar-inverse" role="navigation" id="header">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button> <a class="navbar-brand" href="#" style="color:white">Home</a>
                    </div>
                    
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                        <ul class="nav navbar-nav">
                            <li>
                                <a href="#"></a>
                            </li>
                            <li>
                                <a href="#"></a>
                            </li>
                            <li>
                                <a href="#"></a>
                            </li>
                            
                        </ul>
                        <form class="navbar-form navbar-left" role="search">
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="请输入您的BaseKey以查询"/>
                            </div> <button type="submit" class="btn btn-default">搜索</button>
                        </form>
                        <ul class="nav navbar-nav navbar-right">
                            <li>
                                <a href="#" style="font-size: 14px; color:white" >MainNet TestNet</a>
                            </li>
                            
                            
                        </ul>
                    </div>
                    
                </nav>
            </div>
        </div>
        <!-- node message -->
        <div class="home">
            <div class="home-head">
                <div >
                    <!--blockChain Statistics-->
                    <div class="home-head-data"
                        v-loading="loading1" element-loading-text="数据加载中..."  element-loading-background="rgba(0, 0, 0, 0.8)">
                        <p class='text'>节点信息：{{ node_msg }}</p>

                    </div>
                
                    <!--Chart statistics-->
                    
                </div>
            </div>
            <!--Node statistics-->
                <div class="home-center">
                    
                        <div>
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th style="color:white;text-align: center;">
                                            键
                                        </th>
                                        <th style="color:white;text-align: center;">
                                            值
                                        </th>
                                        <th style="color:white;text-align: center;">
                                            最近更新日期
                                        </th>
                                        
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="item in DataOnChain" :key='item.key'>
                                        <td style="color:white;text-align: center;">
                                            {{item.key}}
                                        </td>
                                        <td style="color:white;text-align: center;">
                                            {{item.value}}
                                        </td>
                                        <td style="color:white;text-align: center;">
                                            {{item.latest}}
                                        </td>
                                        
                                    </tr>
                                    
                                </tbody>
                            </table>
                        </div>
                    
                    <!-- <el-table :data="DataOnChain"  :header-cell-style="bgTable" :row-class-name="tableRowClassName" :cell-style="tableCellStyle"
                          v-loading="loading3" element-loading-text="数据加载中..."  element-loading-background="rgba(0, 0, 0, 0.8)">
                    <el-table-column  label="键"  :show-overflow-tooltip="true" prop="key" align="center">
                        
                    </el-table-column>
                    <el-table-column  label="值"  :show-overflow-tooltip="true" prop="value" align="center"></el-table-column>
                    <el-table-column  label="最近更新日期"  :show-overflow-tooltip="true" prop="latest" align="center"></el-table-column>
                    
                    </el-table> -->
                </div>
                <div class="home-foot">
                    <!--Block list-->
                    <div class="home-foot-box margin-right-10">
                        <div class="home-foot-box-nav">
                            <div class="left">
                                <span class="line"></span>
                                <span class="text">Transaction</span>
                            </div>
                            <div class="right">
                                <span @click="linkPage('block')" class="table-link" style="padding-right: 30px; color: white"> 更多 ></span>
                            </div>
                        </div>
                        <div class="home-foot-box-content" v-loading="loading4" element-loading-text="数据加载中..." element-loading-background="rgba(0, 0, 0, 0.8)">
                            <ul>
                                <li class="item" v-for="item in TransactionList" :key='item.hash'>
                                    <div class="left">
                                        <div @click="linkPage('blockDetail','blockHash',item.blockHash)" class="table-link">交易key: &nbsp;{{item.key}}</div>
                                        <div>hash值：{{item.hash}}</div>
                                    </div>
                                    <div class="right">
                                        <div>
                                            <span class="block-number" :title="item.sealer">操作：{{item.op}}</span>
                                        </div>
                                        <div>时间戳：{{item.timestamp}}</div>
                                        
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!--transaction list-->
                    
                </div>
                <hr />
                <div style="text-align: center;color: white;margin-top: 20px;">
                    上海对外经贸大学·区块链技术与应用研究中心 © 2019 all right reserved
                    <div style="float:right;width:10%">
                        <a href="https://github.com/leeduckgo/bsn_app_explorer" target="_blank">Source Code </a>
                        <br>
                        <a href="https://github.com/leeduckgo/bsn_app_explorer/issues" target="_blank">Submit Issues </a>
                        <br>
                        <a href="http://www.suibe.edu.cn/ai/2020/0112/c7666a96188/page.htm" target="_blank">研究中心主页 </a>
                    </div>
                </div>
            </div>
        </div>
    
     
</template>

<script>

export default {
  name: 'index',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      info: 'info',
      node_msg: '',
      DataOnChain: [
          {
              key: 'key1',
              value: 'value1',
              latest: 'latest1'
          },
        //   {
        //       key: 'key2',
        //       value: 'value2',
        //       latest: 'latest2'
        //   },
        //   {
        //       key: 'key3',
        //       value: 'value3',
        //       latest: 'latest3'
        //   }
      ],
      TransactionList: [
          {
              hash: '1222222222222222222',
              key: 'key1',
              op: 'add',
              timestamp: '201901222233'
          }
      ]
    
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#header {
    background-image: url("../assets/images/header-ng.png");
    font-size: 14px;
    height:50px;
}
.text{
    color: white;
    font-size: 14px;
}
.home{
        width: 100%;
        background-color: #2a2c3b;
        padding: 20px;
        height: 800px;
    }
        
    
    .home-head-data{
        display: inline-block;
        width: 100%;
        box-sizing: border-box;
        padding: 30px;
        background-color: #3b3e54;
        vertical-align: middle;
        height: 100px;
    }
    .home-center{
        width: 100%;
        margin-top: 20px;
        height: 300px;
        background-color: #3b3e54;
    }
    .home-center-table{
        background-color: #3b3e54;
    }
    .home-center .el-table .table-style{
        background-color: #3b3e54;
        color: #fff;
        text-align: center;
        overflow: hidden;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        -webkit-text-overflow: ellipsis;
        -moz-text-overflow: ellipsis;
        white-space: nowrap; 
        border-color: #666
    }
    .home-center .el-table .table-style:hover{
        color: #333;
    }
    .el-table{
        border-color: #666 !important;
    }
    .el-table__body-wrapper{
        border-color: #666 !important;
    }
    .el-table table{
        border-color: #666 !important;
    }
    .el-table tbody{
        border-color: #666 !important;
    }
    .el-table tr{
        border-color: #666 !important;
    }
    .el-table th{
        border-color: #666 !important;
    }
    .el-table td{
        border-color: #666 !important;
    }
    .el-table--border:after, .el-table--group:after, .el-table:before{
        background-color: #666 !important;
    }
    
    .home-center .el-table .name-wrapper{
        width: 100%;
        height: 100%;
        display: inline-block;
        /*width: 450px;*/
        overflow: hidden;
        text-overflow: ellipsis !important;
        white-space: nowrap !important; 
    }
    .home-center .el-table .el-table__empty-block{
        background-color: #3b3e54;
    }
    .home-foot{
        margin-top: 20px;
        font-size: 0;
        height: 200px;
    }
    .home-foot-box{
        display: inline-block;
        width: 100%;
        padding-bottom: 20px;
        background-color: #3b3e54;
        font-size: 14px;
        color: #fff;
        vertical-align: top;
        box-sizing: border-box;
    }
    .home-foot-box-nav{
        width: 100%;
        height: 50px;
        line-height: 50px;
        margin-left: 15px;
        padding-right: 15px;
        overflow: hidden;
        box-sizing: border-box;
    }
    .home-foot-box-nav .left{
        float: left;
        width: 50%;
    }
    .home-foot-box-nav .left .line{
        display: inline-block;
        width: 3px;
        height: 14px;
        margin-right: 12px;
        background-color: #2196f3;
        vertical-align: middle;
    }
    .home-foot-box-nav .right{
        float: right;
        width: 50%;
        text-align: right;
        cursor: pointer;
    }
    .home-foot-box-content ul{
        padding: 0;
        margin: 0;
        list-style: none;
    }
    .home-foot-box-content .item{
        border-bottom: 1px solid #999;
        overflow: hidden;
        line-height: 28px;
        padding: 12px 30px;
    }
    .home-foot-box-content .item .left{
       float: left;
    }
    .home-foot-box-content .item .right{
        float: right;
        text-align: right;
        overflow: hidden;
    }
    .home-foot-box-content .item .block-number{
        display: inline-block;
        width: 116px;
        overflow: hidden;
        text-overflow: ellipsis !important;
        white-space: nowrap !important;  
        vertical-align: middle;
    }
    .home-foot-box-content .item .txn {
        float: right;
        width: 70px;
        height: 28px;
        line-height: 28px;
        background-color: #2196f3;
        color: #fff;
        text-align: center;
        cursor: pointer;
    }
    .home-foot-box-content .item .transaction{
        width: 320px;
        overflow: hidden;
        text-overflow: ellipsis !important;
        white-space: nowrap !important;  
        vertical-align: middle;
    }
    .home-foot-box-content .number{
        display: inline-block;
        width: 148px;
        overflow: hidden;
        text-overflow: ellipsis !important;
        white-space: nowrap !important;  
        vertical-align: middle;
    }
    .home-foot-box-content .image{
        vertical-align: middle;
    }

    table{
        border-color: #999!important;
    }
    .node-false{
        color: #f00 !important;
    }
    @media screen and (max-width: 1200px){
        .home-head-data{
            display: inline-block;
            width: calc(41% - 10px);
            box-sizing: border-box;
            padding: 20px 20px;
            background-color: #3b3e54;
            vertical-align: middle;
        }
        .home-head-data-content{
            display: block;
            color: white;
            padding-top: 10px;
            font-size: 28px;
            text-align: right;
        }
        .home-head-chart{
            width: calc(59% - 10px) !important;
            height: 290px;
            vertical-align: middle;
        }
        .home-foot-box-content .item{
            border-bottom: 1px solid #999;
            overflow: hidden;
            line-height: 28px;
            padding: 12px 20px;
        }
        .home-foot-box-content .item .transaction{
            width: 280px;
            overflow: hidden;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;  
            vertical-align: middle;
        }
        .home-foot-box-content .number{
            display: inline-block;
            width: 130px;
            overflow: hidden;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;  
            vertical-align: middle;
        }
    }
    @media screen and (max-width: 1000px){
        .home-head-data{
            display: inline-block;
            width: calc(41% - 10px);
            box-sizing: border-box;
            padding: 10px 10px;
            background-color: #3b3e54;
            vertical-align: middle;
        }
        .home-head-chart{
            width: calc(59% - 10px) !important;
            height: 270px;
            vertical-align: middle;
        }
        .home-head-data-content{
            display: block;
            color: white;
            padding-top: 10px;
            font-size: 24px;
            text-align: right;
        }
        .home-head-data ul li{
            display: inline-block;
            height: 110px;
            padding: 25px 10px;
            font-size: 14px;
            cursor: pointer;
            color: #fff;
            box-sizing: border-box;
        }
        .home-foot-box-content .item{
            border-bottom: 1px solid #999;
            overflow: hidden;
            line-height: 28px;
            padding: 12px 20px;
        }
        .home-foot-box-content .item .transaction{
            width: 200px;
            overflow: hidden;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;  
            vertical-align: middle;
        }
        .home-foot-box-content .number{
            display: inline-block;
            width: 85px;
            overflow: hidden;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;  
            vertical-align: middle;
        }
        .home-foot-box-content .item .txn {
            float: right;
            width: 70px;
            height: 28px;
            line-height: 28px;
            background-color: #2196f3;
            color: #fff;
            text-align: center;
            cursor: pointer;
        }
    }

</style>
