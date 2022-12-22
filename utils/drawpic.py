from Model import  project
from impala.util import as_pandas
import matplotlib.pyplot as plt
import numpy as np

from Model.project import Project

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.rcParams.update({'font.size': 30})

def drawpic(pro):
    # 统计开源协议比例
    dict_license={}
    for project_now in pro:
        print(project_now.license)
        if project_now.license in dict_license:
            dict_license[project_now.license] += 1
        else:
            dict_license[project_now.license] = 1
    print(dict_license)
    license_x=dict_license.keys()
    license_y=dict_license.values()
    plt.figure(figsize=(50, 30))
    plt.bar(license_x, license_y)
    plt.title("Github热门项目协议直方图")
    plt.savefig('static\licensebar.png',stretch=100)
    plt.figure(figsize=(45, 30))
    plt.pie(license_y,
            labels=license_x,
            autopct='%.2f%%',
            )
    plt.title("Github热门项目协议饼图")  # 设置标题
    plt.savefig('static\licensepie.png', stretch=100)
    # 统计贡献者比例
    dict_contributors={'1-50':0,'51-200':0,'201-500':0,'501-2000':0,'2001-4999':0,'5000+':0}
    for project_now in pro:
        if project_now.contributors < 51:
            dict_contributors['1-50']+=1
        elif project_now.contributors < 201:
            dict_contributors['51-200'] += 1
        elif project_now.contributors < 501:
            dict_contributors['201-500'] += 1
        elif project_now.contributors < 2001:
            dict_contributors['501-2000'] += 1
        elif project_now.contributors < 5000:
            dict_contributors['2001-4999'] += 1
        else:
            dict_contributors['5000+'] += 1
    contributors_x=dict_contributors.keys()
    contributors_y=dict_contributors.values()
    plt.figure(figsize=(45, 30))
    plt.pie(contributors_y,
            labels=contributors_x,
            autopct='%.2f%%',
            )
    plt.title("Github热门项目贡献者人数饼图")  # 设置标题
    plt.savefig('static\contributorspie.png', stretch=100)
    # 分析issues完成率对star的影响
    dict_issues = {'0-30': 0, '31-100': 0, '101-200': 0, '201-500': 0, '500+': 0}
    for project_now in pro:
        print(project_now.issues_open)
        if int(project_now.issues_open) > 500:
            dict_issues['500+']+=1
        elif int(project_now.issues_open) > 200:
            dict_issues['201-500']+=1
        elif int(project_now.issues_open) > 100:
            dict_issues['101-200']+=1
        elif int(project_now.issues_open) > 30:
            dict_issues['31-100']+=1
        else:
            dict_issues['0-30'] += 1
    print(dict_issues)
    issues_x=dict_issues.keys()
    issues_y=dict_issues.values()
    plt.figure(figsize=(45, 30))
    plt.pie(issues_y,
            labels=issues_x,
            autopct='%.2f%%',
            )
    plt.title("Github热门项目Issues Open状态个数饼图")  # 设置标题
    plt.savefig('static\issuespie.png', stretch=100)
    # fork数
    dict_fork={'0-30': 0, '31-100': 0, '101-200': 0, '201-500': 0, '500+': 0}
    for project_now in pro:
        print(project_now.fork)
        if int(project_now.fork)>500:
            dict_fork['500+']+=1
        elif int(project_now.fork)>200:
            dict_fork['201-500']+=1
        elif int(project_now.fork)>100:
            dict_fork['101-200']+=1
        elif int(project_now.fork)>30:
            dict_fork['31-100']+=1
        else:
            dict_fork['0-30']+=1
    fork_x=dict_fork.keys()
    fork_y=dict_fork.values()
    plt.figure(figsize=(45, 30))
    plt.pie(fork_y,
            labels=fork_x,
            autopct='%.2f%%',
            )
    plt.title("Github热门项目Fork数饼图")  # 设置标题
    plt.savefig('static\myforkpie.png', stretch=100)
    # 粉丝数
    dict_followers= {'0-30': 0, '31-200': 0, '201-500': 0, '501-1000': 0, '1001-5000': 0,'5000+':0}
    for project_now in pro:
        print(project_now.followers)
        if int(project_now.followers)>5000:
            dict_followers['5000+']+=1
        elif int(project_now.followers)>1000:
            dict_followers['1001-5000']+=1
        elif int(project_now.followers)>500:
            dict_followers['501-1000']+=1
        elif int(project_now.followers)>200:
            dict_followers['201-500']+=1
        elif int(project_now.followers)>30:
            dict_followers['31-200']+=1
        else:
            dict_followers['0-30']+=1
    followers_x=dict_followers.keys()
    followers_y=dict_followers.values()
    plt.figure(figsize=(45, 30))
    plt.pie(followers_y,
            labels=followers_x,
            autopct='%.2f%%',
            )
    plt.title("Github热门项目Followers数饼图")  # 设置标题
    plt.savefig('static\myfollowerspie.png', stretch=100)












