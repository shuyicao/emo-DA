library('pcalg')

#read data
dd <- read.csv("C:/Users/shuyi/Desktop/New folder1/New folder/pred.csv")
an <- read.csv("C:/Users/shuyi/Desktop/New folder1/New folder/annotated.csv")

#select features to be fed into algorithms
dd <- subset(dd, select = c('session_id','speaker_id','emo_indx','swda_indx','prev_swda_indx',
                            'next_swda_indx','prev_emo_indx','next_emo_indx'))
#cast speaker_id to numerical 
#data$speaker_id <- as.numeric(data$speaker_id)

an <- subset(an, select = c('session_id','speaker_id','emo_indx','swda_indx','prev_swda_indx',
                            'next_swda_indx','prev_emo_indx','next_emo_indx'))


#combine two dataframes
new <- rbind(an, dd)
#cast speaker_id to numerical 
new$speaker_id <- as.numeric(new$speaker_id)

#FCI 
V1 <- colnames(new)
suffStat1 <- list(dm = as.matrix(new), adaptDF=FALSE)
fci.new <- fci(
  suffStat1,
  ## independence test: G^2 statistic
  indepTest = disCItest, alpha = 0.01, labels = V1, verbose = FALSE
)

summary(fci.new)