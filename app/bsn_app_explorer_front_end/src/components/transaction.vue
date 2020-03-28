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
                                <a href="#">Transactions</a>
                            </li>
                            <li>
                                <a href="#">Data On Chain</a>
                            </li>
                            <li>
                                <a href="#"></a>
                            </li>
                            
                        </ul>
                        <!-- <form class="navbar-form navbar-left" role="search">
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="请输入您的BaseKey以查询"/>
                            </div> <button type="submit" class="btn btn-default">搜索</button>
                        </form> -->
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
            
            <!--Node statistics-->
                <div class="home-center">
                    
                        <div>
                            <p style="color: white;text-align: center">Transaction</p>
                            
                            <table class="table">
                                
                                <tbody>
                                    <tr v-for="item in Transactions" :key='item.content'>
                                        <td style="color:white;text-align: center;">
                                            {{item.content}}
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
  name: 'transactions',
  data () {
    return {
      
      node_msg: '',
      Transactions: [
          {
              content: '1222222222222222222',
              
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
        height: 600px;
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
        
    }

</style>
