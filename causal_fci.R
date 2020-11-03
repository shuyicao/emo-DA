library('pcalg')

#read data
dd <- read.csv("pred.csv")
an <- read.csv("annotated.csv")

#select features to be fed into algorithms
dd <- subset(dd, select = c('emo_indx','swda_indx','prev_swda_indx',
                            'next_swda_indx','prev_emo_indx','next_emo_indx'))


an <- subset(an, select = c('emo_indx','swda_indx','prev_swda_indx',
                            'next_swda_indx','prev_emo_indx','next_emo_indx'))


#combine two dataframes
new <- rbind(an, dd)


#FCI 
V1 <- colnames(new)
suffStat1 <- list(dm = as.matrix(new), adaptDF=FALSE)
fci.new <- fci(
  suffStat1,
  ## independence test: G^2 statistic
  indepTest = disCItest, alpha = 0.01, labels = V1, verbose = FALSE
)

summary(fci.new)
