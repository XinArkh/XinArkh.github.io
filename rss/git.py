<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess
from news_me_tzgg import me_tzgg

#查看工作区状态
def status():
    archiveCmd = 'git status'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("查看工作区状态错误")
    else:
        add()

    return True

#添加工作区
def add():
    archiveCmd = 'git add .'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("添加到缓存区错误")
    else:
        commit()

#提交本地版本库
def commit():
    # inputNote = raw_input("请输入提交内容:").decode('utf-8')
    inputNote = 'automatic upload by Wu Hsin\'s bot' 
    archiveCmd = "git commit -m ' " + inputNote + "'"
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("提交失败")
    else:
        print("提交成功",inputNote)
        pull()

#拉取
def pull():
    archiveCmd = 'git pull'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("拉取远程代码失败")
    else:
        push()

#推送
def push():
    archiveCmd = 'git push -u origin master'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("上传远程git服务器失败")
    else:
        print("上传成功")

#执行
def main():
    add()
    commit()
    push()

if __name__ == '__main__':
    me_tzgg()
    main()


=======
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

#查看工作区状态
def status():
    archiveCmd = 'git status'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print "查看工作区状态错误"
    else:
        add()

    return True

#添加工作区
def add():
    archiveCmd = 'git add .'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print "添加到缓存区错误"
    else:
        commit()

#提交本地版本库
def commit():
    # inputNote = raw_input("请输入提交内容:").decode('utf-8')
    inputNote = 'automatic upload by Wu Hsin\'s bot' 
    archiveCmd = "git commit -m ' " + inputNote + "'"
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print "提交失败"
    else:
        print "提交成功",inputNote
        pull()

#拉取
def pull():
    archiveCmd = 'git pull'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print "拉取远程代码失败"
    else:
        push()

#推送
def push():
    archiveCmd = 'git push -u origin master'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print "上传远程git服务器失败"
    else:
        print "上传成功"

#执行
def main():
    add()
    commit()
    push()

if __name__ == '__main__':
    main()


>>>>>>> e47ab9f349159e154197d8ad19d5f53b6f6c0648
