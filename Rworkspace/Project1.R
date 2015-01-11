library(DMwR)
library(rpart)
library(rpart.plot)

##read data from file
adult <- read.csv("~/Programming/Rworkspace/adult.data", header=FALSE, col.names = c("Age", "Workclass", "Fnlwgt", "Education", "Education-num", "Marital", "Occupation","Properties", "Relationship", "Sex", "Capital-gain", "Capital-loss", "Hours-per-week", "Native-country", "Result"),stringsAsFactors=T,strip.white = T)
adult.test <- read.csv("~/Programming/Rworkspace/adult.test", header=FALSE, col.names = c("Age", "Workclass", "Fnlwgt", "Education", "Education-num", "Marital", "Occupation","Properties", "Relationship", "Sex", "Capital-gain", "Capital-loss", "Hours-per-week", "Native-country", "Result"),stringsAsFactors=T,strip.white = T)

##data clean 
##all col.name need this step
adult$Workclass = sub("\\?", NA, adult$Workclass)
adult$Workclass = as.factor(adult$Workclass)

adult$Occupation = sub("\\?", NA, adult$Occupation)
adult$Occupation = as.factor(adult$Occupation)

adult$Native.country = sub("\\?", NA, adult$Native.country)
adult$Native.country = as.factor(adult$Native.country)

##test data clean
test <- adult.test
test$Workclass = sub("\\?", NA, test$Workclass)
test$Workclass = as.factor(test$Workclass)

test$Occupation = sub("\\?", NA, test$Occupation)
test$Occupation = as.factor(test$Occupation)

test$Native.country = sub("\\?", NA, test$Native.country)
test$Native.country = as.factor(test$Native.country)

##count how many rows are NA
nrow(adult[!complete.cases(adult),])

##right data
adult.right <- adult[complete.cases(adult),]
test<- test[complete.cases(test)]
#adult.train = adult.right[c(1-1000)]
##err data
#adult.err <- adult[!complete.cases(adult),]
#save(adult.err,"~/Programming/Rworkspace/test")
##remove all row contain NA
#adult <- na.omit(adult)
#adult <- adult[-manyNAs(adult), ]


#tree <- rpartXse(Result ~ . ,data = adult.train, cp = 0.015, minsplit = 1)
#tree
#prettyTree(tree)

##這是第二種tree
#fit <- rpart(Result ~ ., data=adult.right, method="class",control=ct,parms = list(prior = c(0.65,0.35), split = "information"));
ct <- rpart.control(xval=10, minsplit=20, cp=0.011)
fit <- rpart(Result ~., data = adult.right, control = ct)
fit
rpart.plot(fit)
#rpart.plot(fit, branch=1, type=2, extra=102,shadow.col="gray", box.col="green", border.col="blue", split.col="red", split.cex=1.2, main="收入决策树");


##predict
old <- test$Result
pre <- predict(fit, test, type = "class")
t <- table(pre, old)
print(t)
print((t[1,1] + t[2,2])*100/sum(t))
