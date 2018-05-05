axis(1,at=1:5,lab=c("월","화","수","목","금"))
axis(2,ylim=c(0,200))
title(main="APPLE", col.main="red", font.main=4)
title(xlab="요일", col.lab="black")
title(ylab="가격", col.lab="black")


par(mfrow=c(1,3))
apple<-c(10,20,25,15,20)
plot(apple,type="o")
plot(apple,type="s")
plot(apple,type="l")




par(mfrow=c(1,1))
mssql<-c(0.0336,0.0418,0.0572,0.0466,0.077)
mysql<-c(0.0274,0.0344,0.042,0.052,0.3116)
mariadb<-c(0.0294,0.0332,0.0388,0.0454,0.1636)

plot(mssql,type="o", col="red",lty=1,ylim=c(0,1),axes=FALSE,ann=FALSE)
lines(mysql, type="o", col="green",lty=2,ylim=c(0,1))
lines(mariadb, type="o", col="blue",lty=3,ylim=c(0,1))

axis(1,at=1:5,lab=c("200","1000","5000","1만","10만"))
title(main="join15%/DoubleIndex", col.main="red", font.main=4)
title(xlab="카디널리티 수", col.lab="black")
title(ylab="DB 종류", col.lab="black")


--------------------------------------------------

library(ggplot2)
setwd("d:\\r_temp")

data<-read.csv("조인50(양쪽,없음).csv",header=T)
data

ggplot(data,aes(x=카디널리티수,y=시간,color=디비이름,group=디비이름,fill=디비이름))+geom_smooth()+geom_point(size=2,shape=22)
savePlot("g11.png", type="png")
----
ggplot(data,aes(x=NumberOfTuples,y=sec.,color=database,group=database,fill=database))+geom_line()+geom_point(size=2,shape=22)
savePlot("g11.png", type="png")
---
ggplot(data,aes(x=NumberOfTuples_Scale100,y=sec.,color=database,group=database,fill=database))+geom_line()+geom_point(size=2,shape=22)
savePlot("g11.png", type="png")


----
ggplot(data,aes(x=NumberOfTuples,y=sec.,color=database,group=database,fill=database))+geom_line(aes(linetype = database))+geom_point(size=2,shape=22)
savePlot("g11.png", type="png")
----
ggplot(data,aes(x=NumberOfTuples_Scale100,y=sec.,color=database,group=database,fill=database))+geom_line(aes(linetype = database))+geom_point(size=2,shape=22)
savePlot("g11.png", type="png")

----
ggplot(data,aes(x=NumberOfTuples,y=sec.,color=database,group=database,fill=database))+geom_line(aes(linetype = database))+geom_text(aes(label=data$database),vjust=0)+geom_point(size=1,shape=22)
savePlot("g11.png", type="png")

No-Of-Tuples
Seconds

+geom_text(aes(label=data$database,x=NumberOfTuples, y=sec.),hjust=0, vjust=0)
