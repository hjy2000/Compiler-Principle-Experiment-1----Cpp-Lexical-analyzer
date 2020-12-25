# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:44:31 2020
编译原理C++词法分析器 20182131055 侯佳耀
@author: ASUS
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename

def read():
    filename = askopenfilename(initialdir = 'd:/ASUS')
    f = open(filename,encoding='utf-8')
    a=f.read()
    
    print(a)
    return a
    f.close()
    
def main(a):
    DIC1=['asm','else','new','this','auto','enum','operator',
          'throw','bool','explicit','private','true','break','exprot','protected','try'
          ,'case','extern','public','typedef','catch','false','register','typeid',
          'char','float','int','reinterpret_cast','typename',
          'class','for','return','union','const','friend',
          'short','unsigned','const_cast','goto','signed','using',
          'continue','if','sizeof','virtual','default','inline','static','void',
          'delete','static_cast','volatile','do','long','struct','wchar_t','double',
          'mutable','switch','while','dynamic_cast','namespace','template']#关键字
    
    DIC3=['+','-','*','/','%','++','--','==','!=','>','<','>=','<=','&&','||','!','&',
          '|','^','~','<<','>>','=','+=','-=','*=','/=','%=','<<=','>>=','&=','^=','|=']
    #运算符
    DIC4=['\\','#',',','(',')','{','}',';','::']#特殊符号
    L=[]
    #global s
    s=[]
    
    
    print("下面是词法分析的结果：")
    for i in range(len(a)):
        L.append(a[i])
   
    
    i=0
    
    while(i<len(a)):
        
        if a[i]=='/':
            string1='/'
            if a[i+1]=='/':
                
                
                k=i
                while(True):
                    if a[k+1]!='\n' and a[k+1]!='\r':
                        string1=string1+a[k+1]
                        k=k+1
                    else:
                        break
                str1=string1+' 注释'
                s.append(str1)
                print(str1)
                i=i+len(string1)
                
            elif a[i+1]=='*':
                 k=i
                 string1=string1+'*'
                 while(True):
                    if a[k+2]!='*' and a[k+3]!='/':
                        string1=string1+a[k+2]
                        k=k+1
                    else:
                        break
                 str1=string1+'*/'+' 注释'
                 s.append(str1)
                 print(str1)
                 i=i+len(string1)+2
                
                
        elif a[i]=='“':
            
            str0='“'
            j=i
            while(True):
                
                if a[j+1]!='”':
                    
                    str0=str0+a[j+1]
                    j=j+1
                    
                    
                else:
                    
                    
                    break
                
            str0=str0+'”'
            
            str1=str0+'字符串'
            s.append(str1)
            print(str1)
            i=i+len(str0)
        elif a[i] in DIC3:
            
            if a[i+1] in['+','-','=','&','|','>','<']:
                if a[i+2]=='=':
                    str1=a[i]+a[i+1]+a[i+2]+'运算符'
                    i=i+2
                else:
                    str1=a[i]+a[i+1]+'运算符'
                    i=i+1
            else:
                str1=a[i]+'运算符'
            
            s.append(str1)
            print(str1)
            i=i+1
        elif a[i] in DIC4:
            if a[i]=='}':
                str1=a[i]+'特殊符号'
            else:
                if a[i+1]==':':
                    str1=':: 特殊符号'
                    i=i+1
                else:
                    str1=a[i]+'特殊符号'
            
            s.append(str1)
            print(str1)
            i=i+1
            
        elif a[i].isalpha()==True or a[i]=='_':
            ss=''
            k=i
            
            while(True):
                
                
                if a[k]=='_' or a[k].isalpha()==True or a[k].isdigit()==True or a[k]=='.':
                    ss=ss+a[k]
                    k=k+1
                else:
                    
                    break
            
            if ss in DIC1:
                str1=ss+'关键字'
            else:
                str1=ss+'标识符'
            
            s.append(str1)
            print(str1)
            i=i+len(ss)
            
        elif a[i].isdigit()==True:
            sss=''
            k=i
            while(True):
                
                
                if a[k].isdigit()==True or a[k]=='.' or a[k]=='e' or a[k]=='E':
                    sss=sss+a[k]
                    k=k+1
                else:
                    
                    break
            str1=sss+'数'
            s.append(str1)
            print(str1)
            i=i+len(sss)
        else:
            i=i+1
    
    return s
    
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('C++词法分析器')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('640x480')  # 这里的乘是小x
l = tk.Label(window, text='欢迎使用C++词法分析器', bg='blue', font=('Arial', 12), width=30, height=2)
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

def show():
    c=read()
    t = tk.Text(window)
    t.pack()
    for i in main(c):
        t.insert(tk.INSERT,i)
        t.insert(tk.INSERT,'\n')
print()
b = tk.Button(window, text="analyze", command=show)
b.pack()


window.mainloop()