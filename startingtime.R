MyTable<-read.table("startingtime.txt", header = FALSE, sep = " ", dec = ".")

#MyTable <- data.frame(TimeLogs=Sys.time()+round(rnorm(1000,5000,2500)))

firstday<-MyTable[MyTable[,1]=='2015-04-01',]
seconday<-MyTable[MyTable[,1]=='2015-04-02',]
thirday<-MyTable[MyTable[,1]=='2015-04-03',]
forthday<-MyTable[MyTable[,1]=='2015-04-04',]
lastday<-MyTable[MyTable[,1]=='2015-04-05',]
par(mfrow=c(2,3))
plot(firstday$V2,ylim=c(0,40), xlab='Trajectory Starting Time on Wednesday', ylab='Frequency')
plot(seconday$V2,ylim=c(0,40),xlab='Trajectory Starting Time on Thursday', ylab='Frequency')
plot(thirday$V2,ylim=c(0,40),xlab='Trajectory Starting Time on Friday', ylab='Frequency')
plot(forthday$V2,ylim=c(0,40), xlab='Trajectory Starting Time on Saturday', ylab='Frequency')
plot(lastday$V2,ylim=c(0,40), xlab='Trajectory Starting Time on Sunday', ylab='Frequency')

plot(MyTable$V1)
