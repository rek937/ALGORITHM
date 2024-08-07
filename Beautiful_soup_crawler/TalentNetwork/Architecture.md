#### 初始化
- 第一次抓取（只抓取信息主页信息，不访问信息链接）
- 生成 **Log_init.log** 和 **getLogINFO.log** 文件
- 生成 **resource** 文件存储信息

注: Log_init.log只存储第一次抓取信息

#### 定时抓取任务
windows定时执行脚本。脚本任务是在前一次任务的基础上补充库中没有的数据，并且在初始化任务之后的所有任务都会访问信息链接，分析信息给出预警。
（数据去重，错误提示和重试）

#### 程序可视化
最近一次获取的数据展示在pyqt的窗口上，把分析出来权重较高的任务放在最前面。