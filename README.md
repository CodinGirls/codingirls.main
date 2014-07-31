# codingirls.main

the Codingirls.org main site pelican project

## Changelog

- 140730 ZQ rebuilded base MkDocs
    - because github-pages only bind one domain
    - transfer base gitcafe.com
    - publish as
        http://codingirl.us
        http://codingirls.org

- 140119 ZQ publish base Pelican
    public base codingirls.github.io

- 140107 ZQ created githuba repo.


## MkDoc

基于 [MkDoc](http://www.mkdocs.org/user-guide/writing-your-docs/) 通过
[qrsync 命令行同步工具 | 七牛云存储](http://developer.qiniu.com/docs/v6/tools/qrsync.html)免费发布;

运维流程:

- 初始化:
    - 安装 Python 2.7 以上, MkDoc, fabric, git, qrsync
    - clone https://github.com/CodinGirls/codingirls.main
    - clone https://gitcafe.com/CodinGirls/codingirls as cafe.codingirls
- 布置目录,类似:

```
/path/2/local/CodinGirls:
   .<~~ +- cafe.codingirls   用以发布网络,基于 gitcafe-pages 服务
   |        `- ...
 ln -s  
   |    +- codingirls.main
   |        +- .git
   |        +- .gitignore 配置忽略 site/
   |        +- ... 
   |        +- docs .md 文章入口 
   .~~>     `- site 静态网站编译输出

```

- 日常维护:
    - 进入 `codingirls.main`
    - 执行 `fab serve`
    - 进入 `codingirls.main/docs` 修订相关页面, 在 `localhost:8000` 观察效果
    - 满意后 先用 `git pl` 同步最新修订,并解决冲突
    - 执行 `fab pu2pages` 重新生成静态网站,并同步到 7牛空间

ps:

有关资源/资料文件的发布/管理/增补, 不建议直接通过 git 仓库,
参考: [我们是如何使用7牛云储存的 | GDG Livin ZhuHai Life;-)](http://blog.zhgdg.org/2013-08/usage7niu/)

通过各自或是相同 bucket 中不同的专用目录来完成快速发布.


### gitcafe-pages
基于 [[2012/10/31]GitCafe正式推出的Pages服务](http://blog.gitcafe.com/116.html)
发布方案,因为 gitcafe-pages 服务,支持同时绑定多个域名,
原先使用 github-pages 服务时,不仅仅要配合 `CNAME` 文件,还只能使用一个域名.
所以,回收为复本,备用.
