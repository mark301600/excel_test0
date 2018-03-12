# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:46:30 2018
企业发放的奖金根据利润提成。利润
(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润
I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。
@author: Administrator
"""
#单次提成
def simple_income(income):
    n=0
    #10万以内提成计算
    if income<=100000:
        n=(income*10)/100
    #10万到20万利润计算
    if income>10 and income<=20:
        n=(income-10)*7.5/100+10000
    #20万到40万利润计算
    if income>20 and income<=40:
        n=(income-20)*5/100+10000+7500
    #40万到60万利润计算
    if income>40 and income<=60:
        n=(income-40)*3/100+10000+7500+10000
    #60万到100万利润计算
    if income>60 and income<=100:
        n=(income-60)*1.5/100+10000+7500+10000+6000
    #100万以上利润计算
    if income>100:
        n=(income-100)*1/100+10000+7500+10000+6000+6000
    return n

#组提成
def group_income():
    l=[]
    a=imput('姓名：')
    l.append(a)
    while True:
        i=imput('输入净利润：')
        if i='next'
            break:
        l.append(i)

            



 
    group=[]
    for i in simple_income(x)
    
def main():
    l1=[]
    l2=[]
    while True:
        n=input("净利润输入：")
        if n == "q":
            j=0
            for i in l2:
                print(i)
                j=j+i
            print("利润总计：",j)
            l2.clear()
            print('good bye~~')
            return
        if n=='next':
            j=0
            for i in l1:
                print(i)
                j=j+i
            print("利润总计：",j)
            l2.append(l1)
            l1.clear()            
 #       if n== 0:
 #           break
        if n n=float(n)
        l1.append(n)
        print("利润",n)
    
        if n<=10:
#    print("利润",n)
            print("提成 "+"%.4f"%(n*0.1))
        if n>10 and n<=20:
#    print("利润",n)
            print("提成 "+"%.4f"%((n-10)*0.075+1))
        if n>20 and n<=40:
            print("提成 "+"%.4f"%((n-20)*0.05+1+0.75))
        if n>40 and n<=60:  
            print("提成 "+"%.4f"%((n-40)*0.03+1+0.75+1))
        if n>60 and n<=100:  
            print("提成 "+"%.4f"%((n-60)*0.015+1+0.75+1+0.6))
        if n>100:  
            print("提成 "+"%.4f"%((n-100)*0.015+1+0.75+1+0.6+0.6))
    
if __name__ == '__main__':

    #设置一个主函数，用来运行窗口，便于若其他地方下需要调用串口是可以直接调用main函数
    main()