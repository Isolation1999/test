import matplotlib.pyplot as plt
qqfilerate=[0.009058851708840005,0.13794629289832513,0.09360740683754248,0.029666743598431466,0.10520446116937374,0.09110630605856744,0.11040690356194072,0.09132673466125198,0.11182059294202891]
qqfilerate=[x*100 for x in qqfilerate]
for i in qqfilerate:
    print("%.2f"%i+"%")
def draw_number(date, rate1, rate2):
    plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号
    plt.plot(date, rate1, color = "red", label = "qqdata")
    plt.plot(date, rate2, color = "blue", label = "qqolddata")
    for a,b in  zip(date,rate1):
        plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize='10')
    plt.legend()#显示图例
    plt.xlabel("date")
    plt.ylabel("proportion")
    plt.title("qqfile/qqFileold")
    plt.show()#画图

draw_number(date=[1,2,3,4,5,6,7,8,9], rate1=qqfilerate, rate2=[0.01,0.024,0.035,0.004,0.0057,0.00322,0.0024,0.067,0.08988])