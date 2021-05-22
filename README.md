# 淘宝接口文档

[TOC]



## 淘宝商品名称

#### 简要描述

- 用于获取淘宝商品的名称，购买，提问数

#### 请求URL

- `http://{服务器IP}:9083/getProductName?productId=538992099820&client=dandan&ts=1616065181&sign=d3caadaf71476b6469d8bc83e11a0db7b944de81`

#### 请求方式

- GET

#### 参数

| 参数名    | 类型   | 说明                  |
| :-------- | :----- | --------------------- |
| productId | string | 单个产品id            |
| client    | string | 客户id                |
| ts        | int    | 10位数当前时间戳      |
| sign      | string | 签名,签名规则联系作者 |

#### 代码调用示例

```
curl "http://{ip服务器}:9083/getProductName?productId=623406584415&client=dandan&ts=1618798786&sign=2ed4c0382af0d6d59755043c9a20e0ad36ee55ab"
```

#### 返回示例

```json
{
    "msg":"ok",
    "code":200,
    "data":{
        "questionCount":"0",
        "itemPic":"https://gw.alicdn.com/tfscom/tuitui/i2/2816031767/O1CN01hGRb8D1OvKSgJlYVo_!!0-item_pic.jpg",
        "itemTitle":"松下净水器原装正品滤芯适用TK-AD59C\TK-AD69T专用滤芯",
        "buyerCount":"191"
    }
}
```

#### 返回参数说明

| 参数名        | 类型   | 说明         |
| :------------ | :----- | ------------ |
| questionCount | string | 提问者数     |
| itemPic       | string | 商品图片地址 |
| buyerCount    | int    | 买家数       |
| itemTitle     | string | 商品名称     |

#### 备注

- 更多返回错误代码请看首页的错误代码描述





## 淘宝商品sku

#### 简要描述

- 用于获取淘宝商品sku信息

#### 请求URL

- `http://{服务器IP}:9083/getDetail?productId=538992099820&client=dandan&ts=1616065181&sign=d3caadaf71476b6469d8bc83e11a0db7b944de81`

#### 请求方式

- GET

#### 参数

| 参数名    | 类型   | 说明                  |
| :-------- | :----- | --------------------- |
| productId | string | 单个产品id            |
| client    | string | 客户id                |
| ts        | int    | 10位数当前时间戳      |
| sign      | string | 签名,签名规则联系作者 |

#### 代码调用示例

```
curl "http://{ip服务器}:9083/getDetail?productId=623406584415&client=dandan&ts=1618798786&sign=2ed4c0382af0d6d59755043c9a20e0ad36ee55ab"
```

#### 返回示例

```json
{
  "code": 200,
  "data": {
    "item": {
      "picUrl": "//img.alicdn.com/bao/uploaded/i2/2089354788/O1CN01IMUsqQ1lEx22I7fzc_!!2-item_pic.png",
      "price": "3800",
      "stock": "61698"
    },
    "prop": {
      "颜色分类": {
        "1627207:9197791974": [
          "Redmi/红米9A 中国红【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01hErIWc1lEwyWrtE5v_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791975": [
          "Redmi/红米9A 星空黑【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01rJ2dVl1lEwyZvsZfZ_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791976": [
          "Redmi/红米9A 午夜蓝【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN018NDxUM1lEwyc2I3Ef_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791977": [
          "Redm/i红米9A 紫罗兰【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01NrB3dq1lEwyc2IWMC_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791978": [
          "Redmi/红米9A 抹茶绿【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01uF98DU1lEwyYJ9aoX_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791979": [
          "Redmi/红米9A 樱花粉【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN016BY8wb1lEwyXqyoof_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791980": [
          "Redmi/红米9A 柠檬黄【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01Yw8YF41lEwyay25um_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791981": [
          "红米9 中国红【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01awW0aO1lEwyHgTyxx_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791982": [
          "红米9 星空黑【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01PvzsIL1lEwyCQJawu_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791983": [
          "红米9 午夜蓝【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01PVRXC41lEwyG2Slk9_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791984": [
          "红米9 抹茶绿【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01ChssHO1lEwyF12VM1_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791985": [
          "红米9 紫罗兰【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01Yxm0Lc1lEwyEQq7Fo_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791986": [
          "红米9 樱花粉【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN011bbbRW1lEwyF126PX_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9197791987": [
          "红米9 柠檬黄【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01DpIDcH1lEwyGc4LzF_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9251064892": [
          "【镜头√全包】Redmi/红米9A 星空黑【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN016XQXyu1lEwyadKf1z_!!2089354788.jpg_30x30.jpg"
        ],
        "1627207:9251064893": [
          "【镜头√全包】Redmi/红米9A 午夜蓝【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01T3kbD91lEwyfNglvd_!!2089354788.png_30x30.jpg"
        ],
        "1627207:9251064894": [
          "【镜头√全包】Redmi/红米9A 中国红【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN0162KcXE1lEwyhwXs3X_!!2089354788.jpg_30x30.jpg"
        ],
        "1627207:9251064895": [
          "【镜头√全包】Redmi/红米9A 紫罗兰【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01wUw76a1lEwyd6hrN9_!!2089354788.jpg_30x30.jpg"
        ],
        "1627207:9251064896": [
          "【镜头√全包】Redmi/红米9A 抹茶绿【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01VkSmHW1lEwyeozeEu_!!2089354788.jpg_30x30.jpg"
        ],
        "1627207:9251064897": [
          "【镜头√全包】Redmi/红米9A 樱花粉【收藏宝贝/赠送钢化膜】",
          "//img.alicdn.com/bao/uploaded/O1CN01MsUYVh1lEwyb6KrTk_!!2089354788.jpg_30x30.jpg"
        ]
      }
    },
    "skuMap": {
      ";1627207:9197791974;": {
        "price": "3800",
        "skuId": "4418151881882",
        "stock": "1598"
      },
      ";1627207:9197791975;": {
        "price": "3800",
        "skuId": "4418151881883",
        "stock": "1312"
      },
      ";1627207:9197791976;": {
        "price": "3800",
        "skuId": "4418151881884",
        "stock": "3612"
      },
      ";1627207:9197791977;": {
        "price": "3800",
        "skuId": "4418151881885",
        "stock": "1805"
      },
      ";1627207:9197791978;": {
        "price": "3800",
        "skuId": "4418151881886",
        "stock": "5547"
      },
      ";1627207:9197791979;": {
        "price": "3800",
        "skuId": "4418151881887",
        "stock": "6997"
      },
      ";1627207:9197791980;": {
        "price": "3800",
        "skuId": "4418151881888",
        "stock": "8374"
      },
      ";1627207:9197791981;": {
        "price": "3800",
        "skuId": "4395026597056",
        "stock": "1654"
      },
      ";1627207:9197791982;": {
        "price": "3800",
        "skuId": "4395026597057",
        "stock": "724"
      },
      ";1627207:9197791983;": {
        "price": "3800",
        "skuId": "4395026597058",
        "stock": "1294"
      },
      ";1627207:9197791984;": {
        "price": "3800",
        "skuId": "4395026597059",
        "stock": "1769"
      },
      ";1627207:9197791985;": {
        "price": "3800",
        "skuId": "4395026597060",
        "stock": "1546"
      },
      ";1627207:9197791986;": {
        "price": "3800",
        "skuId": "4395026597061",
        "stock": "1730"
      },
      ";1627207:9197791987;": {
        "price": "3800",
        "skuId": "4395026597062",
        "stock": "1903"
      },
      ";1627207:9251064892;": {
        "price": "3800",
        "skuId": "4417133196198",
        "stock": "6038"
      },
      ";1627207:9251064893;": {
        "price": "3800",
        "skuId": "4417133196199",
        "stock": "2023"
      },
      ";1627207:9251064894;": {
        "price": "3800",
        "skuId": "4417133196200",
        "stock": "5963"
      },
      ";1627207:9251064895;": {
        "price": "3800",
        "skuId": "4417133196201",
        "stock": "6141"
      },
      ";1627207:9251064896;": {
        "price": "3800",
        "skuId": "4417133196202",
        "stock": "982"
      },
      ";1627207:9251064897;": {
        "price": "3800",
        "skuId": "4417133196203",
        "stock": "686"
      }
    },
    "success": true
  },
  "msg": "ok"
}
```

#### 返回参数说明

json数据表示



#### 备注

- 更多返回错误代码请看首页的错误代码描述



## 淘宝商品销量

#### 简要描述

- 用于获取淘宝商品销量接口

#### 请求URL

- `http://{服务器IP}:9083/sales?productId=538992099820&client=dandan&ts=1616065181&sign=d3caadaf71476b6469d8bc83e11a0db7b944de81`

#### 请求方式

- GET

#### 参数

| 参数名    | 类型   | 说明                                   |
| :-------- | :----- | -------------------------------------- |
| productId | string | 产品id，可以填多个，多个以英文逗号隔开 |
| client    | string | 客户id                                 |
| ts        | int    | 10位数当前时间戳                       |
| sign      | string | 签名,签名规则联系作者                  |

#### 代码调用示例

```
curl "http://{ip服务器}:9083/sales?productId=623406584415&client=dandan&ts=1618798786&sign=2ed4c0382af0d6d59755043c9a20e0ad36ee55ab"
```

#### 返回示例

```json
{
  "code": 200,
  "data": [
    {
      "cur_month_sale": "14790",
      "inSale": "true",
      "productId": "621507473909",
      "product_link": "https://item.taobao.com/item.htm?id=621507473909",
      "return": "0",
      "start_sale_time": "1618513592000",
      "stock": "61685",
      "total_sale": "102564"
    }
  ],
  "msg": "oks",
  "status": [
    {
      "621507473909": "200"
    }
  ]
}
```

#### 返回参数说明

| 参数名 | 类型    | 说明                               |
| :----- | :------ | ---------------------------------- |
| productId    | string  | 产品id                             |
| return     | int     | 退货数                             |
| cur_month_sale | int     | 本月销售数量                             |
| stock     | int     | 库存                               |
|product_link|String|商品链接|
| total_sale  | int     | 累计总销量                             |
| start_sale_time  | long    | 13位时间戳表示，从什么时间开始销售 |
| inSale | boolean | 当前是否正在销售                   |
| status | jsonArray | 表示商品id是否获取成功，200表示获取成功，404表示获取失败 |

#### 备注

- 更多返回错误代码请看首页的错误代码描述