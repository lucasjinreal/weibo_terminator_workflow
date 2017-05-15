# Weibo Terminator Work Flow

![PicName](http://ofwzcunzi.bkt.clouddn.com/7gOwGp5K4FPWHkHQ.png)

> 这个项目是之前项目的重启版本，之前的项目地址[这里](https://github.com/jinfagang/weibo_terminater.git)，那个项目依旧会保持更新，这是weibo terminator的工作版本，这个版本对上一个版本做了一些优化，这里的最终目标是一起爬取语料，包括情感分析、对话语料、舆论风控、大数据分析等应用。

# UPDATE 2017-5-15

经过一些小修改和几位contributor的PR，代码发生了一些小变化，基本上都是在修复bug和完善一些逻辑，修改如下：

1. 修复了保存出错的问题，这个大家在第一次push的时候clone的代码要pull一下;
2. 关于 `WeiboScraper has not attribute weibo_content`的错误，新代码已经修复;

@Fence 提交PR修改了一些内容:
1. 原先的固定30s休息换成随机时间，具体参数可自己定义
2. 增加了big_v_ids_file，记录已经保存过粉丝的明星id； 用txt格式，方便contributor手动增删
3. 两个函数的爬取页面都改成了page+1，避免断点续爬时重复爬取上次已经爬过最后一页
4. 把原先的“爬取完一个id的所有微博及其评论”改为“爬完一条微博及其所有评论就保存”
5. （Optional）把保存文件的部分单独为函数，因为分别有2个和3个地方需要保存

大家可以`git pull origin master`， 获取一下新更新的版本，同时也欢迎大家继续问我要uuid，我会定时把名单公布在`contirbutor.txt` 中，我近期在做数据merge的工作，以及数据清洗，分类等工作，merge工作完成之后会把大数据集分发给大家。

 
# Improve

对上一版本做了以下改进：

* 没有了太多的distraction，直奔主题，给定id，获取该用户的所有微博，微博数量，粉丝数，所有微博内容以及评论内容；
* 和上一版本不同的是，这一次我们的理念是把所有数据保存到三个pickle文件中，以字典的文件存储，这么做的目的是方便断点续爬；
* 同时做到了，已经爬过的id爬虫不会再次爬取，也就是说爬虫会记住爬取过的id，每个id获取完了所有内容之后会被标记为已经爬取；
* 除此之外，微博内容和微博评论被单独分开，微博内容爬取过程中出现中断，第二次不会重新爬取，会从中断的页码继续爬取；
* 更加重要的是！！！每个id爬取互不影响，你可以直接从pickle文件中调取出任何你想要的id的微博内容，可以做任何处理！！
* 除此之外之外，测试了新的反爬策略，采用的延时机制能够很好的工作，不过还无法完全做到无人控制。

**更更加重要的是！！！**，在这一版本中，爬虫的智能性得到了很大提升，爬虫会在爬取每个id的时候，**自动去获取该id的所有粉丝id！！**
相当于是，我给大家的都是种子id，种子id都是一些明星或者公司或者媒体大V的id，从这些种子id你可以获取到成千上万的其他种子id！！
假如一个明星粉丝是3.4万，第一次爬取你就可以获得3.4万个id，然后在从子代id继续爬，每个子代id有粉丝100，第二次你就可以获取到340万个id！！！足够了吗？！！！当然不够！！！

**我们这个项目永远不会停止！！！** 会一直进行下去，直到收获足够多的语料！！！

（当然实际上我们不能获得所有粉丝，不过这些也足够了。）

![PicName](http://ofwzcunzi.bkt.clouddn.com/lqcx6MLSdS8whJVt.png)

# Work Flow

这一版本的目标是针对contributor，我们的工作流程也非常简单：

1. 获取uuid，这个uuid可以调取到 distribute_ids.pkl 的2-3个id，这个是我们的种子id，当然大家也可以直接获取到所有id，但是为了防止重复工作，建议大家向我申请一个uuid，你只负责你的那个，爬完之后，把最终文件反馈给我，我整理去重之后，把最终的大语料发放给大家。
2. 运行 `python3 main.py uuid`，这里说明一下，uuid指定的id爬取完之后才会取爬fans id；
3. Done！

# Discuss

依旧贴出一下讨论群，欢迎大家添加：
```
QQ
AI智能自然语言处理: 476464663
Tensorflow智能聊天Bot: 621970965
GitHub深度学习开源交流: 263018023
```
微信可以加我好友： jintianiloveu

# Copyright

```
(c) 2017 Jin Fagang & Tianmu Inc. & weibo_terminator authors LICENSE Apache 2.0
```
