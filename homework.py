import tkinter as T
from tkinter import simpledialog
from tkinter import messagebox
import matplotlib.pyplot as pt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

wen=open(r"C:\Users\lenovo\Desktop\单词文章.txt",'r')
st = wen.read()
wen.close()
l1=list(st.split())
win=T.Tk()
win.title("文本编译器")
win.geometry('900x700')
ll=open(r"C:\Users\lenovo\Desktop\单词文章.txt",'r')
lll=l1[:]
llll=""
f1=open(r"C:\Users\lenovo\Desktop\停用词表.txt",'r')
l2=f1.read()
l22=list(l2.split())
for j in l22:
    if j=="1":
        l22.remove(j)
l222=""
for i in l22:
    l222+=i.lower()+" "
l3= list(l222.split())
f3=open(r"C:\Users\lenovo\Desktop\单词文章.txt",'r')
l4=list(llll.split())
for i in l4[:]:
    if i in l3:
        l4.remove(i)
l5=" ".join(l4)
for i in lll:
    llll+=i.lower()+" "
llll=llll.replace(" ",',') 
llll=llll.replace(",,",',')
l=llll.split("\n")


def zhuanhua():
    global l1,st
    x=""
    for i in l1:
       x+=i.lower()+" "
    return x

t=T.Text(win,width=100,height=32)
t.insert('end',zhuanhua())
t.pack()

var=T.StringVar()
dancishu=len(l1)
def cishu():
    global dancishu
    var.set(str(dancishu))
    T.messagebox.showinfo(title='总词数', message=dancishu)
b=T.Button(win,text='查看单词总数',width=20,height=1,command=cishu)
b.pack()
var1=T.StringVar()

def cipin():
    global l
    rows=[]
    dic={}
    for i in l:
        row=i.split(",")
        rows.append(row)
        for ii in rows:
            for each in ii:
                if each in dic:
                    dic[each]=dic[each]+1
                else:
                    dic[each]=1
    ci=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    var1.set(str(cishu))
    T.messagebox.showinfo(title='词频', message=ci) 
b2=T.Button(win,text='查看词频',width=20,height=1,command=cipin)
b2.pack()

def chaci():
    b3=T.simpledialog.askstring(u'提示',u'请输入想查询的单词')
    c=zhuanhua().count(str(b3))
    T.messagebox.showinfo(u'查询结果',u'查询单词出现次数为：'+str(c))
b4=T.Button(win,text=u'查询某个单词出现次数',command=chaci,width=20,height=1).pack()

def tihuan():
     b31=T.simpledialog.askstring(u'提示',u'请输入用于替换的单词')
     b32= b3=T.simpledialog.askstring(u'提示',u'请输入被替换的单词')
     weizhi=l1.index(str(b32))
     l1[weizhi]=str(b31)
     T.messagebox.showinfo(u'提示',u'替换成功')
b6=T.Button(win,text=u'单词替换',command=tihuan,width=20,height=1).pack()

def shanchu():
    b33=T.simpledialog.askstring(u'提示',u'请输入需要删除的单词')
    l1.remove(str(b33))
    T.messagebox.showinfo(u'提示',u'删除成功')
b7=T.Button(win,text=u'删除单词',command=shanchu,width=20,height=1).pack()

def keyw():
    f1=open(r"C:\Users\lenovo\Desktop\停用词表.txt",'r')
    l2=f1.read()
    l22=list(l2.split())
    for j in l22:
        if j=="1":
            l22.remove(j)
    l222=""
    for i in l22:
        l222+=i.lower()+" "
    l3= list(l222.split())
    f3=open(r"C:\Users\lenovo\Desktop\单词文章.txt",'r')
    ll=f3.read()
    lll=list(ll.split())
    llll=""
    for i in lll:
        llll+=i.lower()+" "
    l4=list(llll.split())
    for i in l4[:]:
        if i in l3:
            l4.remove(i)
    llll=" ".join(l4)
    llll=llll.replace(" ",',') 
    llll=llll.replace(",,",',')
    l=llll.split("\n")
    rows=[]
    dic={}
    for i in l:
        row=i.split(",")
        rows.append(row)
        for ii in rows:
                for each in ii:
                    if each in dic:
                        dic[each]=dic[each]+1
                    else:
                        dic[each]=1
    keyword=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    ci1=[]
    shu1=[]
    zongbiao=[]
    for i in range (6): 
        word,count=keyword[i]
        ci1.append(word)
        shu1.append(count)
    zongbiao.append(ci1)
    zongbiao.append(shu1)
    return zongbiao
zong=keyw()
ci2,shu2=zong[0],zong[1]
ci3=",".join(ci2)
L1 = T.Label(win, text="关键词:"+ci3, bg='white', font=('Arial', 12), width=60, height=2)
L1.pack()