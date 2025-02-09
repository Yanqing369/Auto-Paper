一个自动爬取相关领域论文，并使用ChatGPT总结论文内容的脚本  

使用原理
1.该脚本会根据connected paper生成的论文map来爬取本领域相关论文的摘要、标题和信息
2.使用chatGPT 4o-mini总结这些摘要的内容，并输出一篇摘要  


使用方法
1.找一篇本领域论文，放在connected paper网站上，生成map，复制map的url
2.将代码中的url替换为自己的url
3.将openai.base_url和openai.api_key替换为自己的api和网址。默认网址和api来源于其它开源项目，不建议直接使用
4.运行程序，程序会输出爬取的论文信息和生成的introduction
