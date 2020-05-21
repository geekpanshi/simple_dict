# simple_dict
> 一个包含 10 万单词支持中英文搜索的简单词典，可以通过连接 mysql 数据库使用，也可以本地使用。
----

### 安装和使用方法

#### 安装方法
`$ git clone https://github.com/geekpanshi/simple_dict.git simple_dict`

#### 使用方法
1. `$ python abc.py [你要搜索的词]`
2. 改别名 ：
2.1 一次性别名 `$ alias abc='python [your simple_dict path]/abc.py'` 然后用 `$ abc python`
2.2 永久性别名
```
$ echo alias abc='python [your simple_dict path]/abc.py'>>~/.bashrc
$ source ~/.bashrc
```

### 3. 使用举例
#### 3.1 没有别名的情况下使用
`$ python [your simple_dict path]/abc.py python`
`$ python [your simple_dict path]/abc.py 小偷`

#### 3.2 有别名的情况下使用
```
GeekPanshi MINGW64 /e/selfDatas/simple_dict (master)
$ abc python

        Search by Local Datas

    ALL result contain words : python

python              ,n.[动]大蟒,巨蟒
pythoness           ,n.古希腊德尔菲的太阳神殿的女祭司,女巫
pythonic            ,adj.神谕的,预言的,大蟒似的
```
```
GeekPanshi MINGW64 /e/selfDatas/simple_dict (master)
$ abc 小偷

        Search by Local Datas

    ALL result contain words : 小偷

ganov               ,n.小偷,扒手
ganef               ,n.<俚>小偷,骗子,扒手
ganof               ,n.(=ganef)小偷,扒手
lifter              ,n.举起的人,升降机,举重运动员,小偷,扒手
lurcher             ,n.小偷,奸细,间谍,杂种猎狗
pilferer            ,n.小偷
prowler             ,n.徘徊者,小偷
spivery             ,n.<英俚>不务正业专以小偷小摸(或黑市买卖)为生
swellmobsman        ,n.衣着讲究的小偷,扒手或骗子
thief               ,n.小偷,贼
thieves             ,n.pl.小偷
```

### TODO LIST：

- [x] 数据库版本的支持；
- [x] 本地脱机版本的支持；
- [x] 命令行版本的搜索支持；
- [ ] 打包成 exe 或者安装包的支持；
- [ ] 做一个本地 小程序、app 的；
- [ ] 做一个本地 小程序、app 的，使用 `vue + rust + mysql`。
