class Project:
    # def __init__(self,stars,owners_projectname,commits,watch,language,followers,
    #              license,author,date,contributors,description,fork,issues_open,issues_closed):
    def __init__(self,stars,fork,commits,watch,contributors,issues_open,issues_closed,
                 followers,owners_projectname,author,language,license,date,description):
        self.stars=stars #star
        self.fork=fork #fork
        self.watch = watch  # watch
        self.contributors = contributors  # contributors
        self.commits=commits #commits
        self.license = license  # 协议
        self.language = language  # 项目语言
        self.description = description  # 项目对应描述
        self.owners_projectname = owners_projectname  # 作者项目名 链接
        self.date = date  # 最后更新时间
        self.issues_open=issues_open #issues
        self.issues_closed=issues_closed
        self.followers=followers#作者关注数
        self.author=author #author

    def __repr__(self):
        print(self.stars,self.fork,self.commits,self.watch,self.author,
              self.contributors,self.issues_open,
              self.issues_closed,self.followers,self.owners_projectname,
              self.language,self.license,self.date,self.description)
    def out(self):
        return ' stars:' + self.stars + '\n fork:' + self.fork + '\n watch:' + self.watch + '\n contributors:' + self.contributors +'\n commits:' + self.commits + '\n license:' + self.license + '\n language:' + self.language + '\n description:' + self.description + '\n date:' + self.date + '\n issues_open:' + self.issues_open + ' issues_closed:' + self.issues_closed + '\n author:' +self.author+'\n followers:'+self.followers