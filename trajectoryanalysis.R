TrajectoryLength<-read.table("trajectorylength.txt", header = FALSE, sep = " ", dec = ".")
TravelTime<-read.table("traveltime.txt", header = FALSE, sep = " ", dec = ".")
plot(TrajectoryLength)
plot(TravelTime)

par(mfrow=c(1,1))
hist(TrajectoryLength$V1,main="Histogram of Trajectory Length",xlim=c(0,20000),breaks=750,xlab="Trajectory Length",ylab="Frequency")
bwplot(TrajectoryLength$V1,xlab="Trajectory Length")
hist(TravelTime$V1,main="Trajectory Travel Time",xlim=c(0,4000),breaks=100,xlab="Cost Time")

roadPassTime<-read.table("roadPassTime.txt", header = FALSE, sep = "\t", dec = ".")
hist(roadPassTime$V2,main="Histogram of Road Pass Time",xlim=c(0,100),breaks = 5000,xlab="Road Pass Times",ylab="Frequency")
