# coding=utf-8


# 数据库配置


db_config = {
    'host':'localhost',
    'user':'root',
    'passwd':"123456",
    'db':'cmdb'
}


page_config = {
    "brand_name":'lovechunqiu\'s blog',
    'title':'blog',
    "favicon":'http://pan.baidu.com/res/static/images/favicon.ico',
    "menu":[
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'user',
            "title": '用户管理',
            "data": [{
                "name": 'username',
                "title": '用户名'
            },{
                "name":'password',
                "title":'密码'
            }]
        },
        {
          "name":"cabinet",
          "title":"机柜",
          "data":[{
              "name":"name",
              "title":"机柜名",
          }]
        },
        {
            "name":"host",
            "title":"服务器",
            "data":[{
                "name":"cabinet",
                "title":"机柜",
                "type":"select",
                "select_type":"cabinet",
            },{
                "name":"hostname",
                "title":"主机名",
            },{
                "name":"asset_no",
                "title":"资产号",
            },{
                "name":"end_time",
                "title":"过期日期",
                "type":"date"
            },{
                "name":"ups",
                "title":"是否开启",
                "type":"select",
                "value":{0:'开启',1:'关闭'}
            }]
        }
    ]
}

