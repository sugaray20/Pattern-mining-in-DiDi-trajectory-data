library(lattice)
library(Hmisc)

MyTable<-read.table("beijingRoadNew2.txt", header = FALSE, sep = "\t")

plot(MyTable$V3)
hist(MyTable$V3, main = "Histogram of Road Length", xlab = "Road Length", ylab = "Density",xlim=c(0,1000),breaks=500)
bwplot(MyTable$V3)

hist(MyTable$V7, main= 'Road Neighbor frequency', xlab='Road Neighbor', ylab='Frequency')


bwplot(MyTable$V7,main= 'Road Neighbor frequency', xlab='Road Neighbor')
