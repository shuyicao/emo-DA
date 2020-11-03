library(dplyr)
#read the data
annotated <- read.csv("annotated.csv")


#get a table with only emotion and SWDA
emo_da <- subset(annotated, select=c('emo', 'swda'))
dim(emo_da)
#get the contingency table
cont <- table(emo_da)

fisher.test(cont, simulate.p.value=TRUE) 


#get number of happiness utterances
nrow(emo_da[emo_da$emo=='happiness',])#394

#get happiness and thanking
happiness_ft <- as.table(rbind(c(20, 7), c(364, 833)))
dimnames(happiness_ft) <- list(group = c('thanking', 'non-thanking'), happiness = c('yes', 'no'))
happiness_ft
fisher.test(happiness_ft) 


#get happiness and appreciation
happiness_ba <- as.table(rbind(c(63, 23), c(331, 787)))
dimnames(happiness_ba) <- list(group = c('ba', 'non-ba'), happiness = c('yes', 'no'))
happiness_ba
fisher.test(happiness_ba) 

#get happiness and statement-opinion
happiness_sv <- as.table(rbind(c(27, 48), c(367, 762)))
dimnames(happiness_sv) <- list(group = c('sv', 'non-sv'), happiness = c('yes', 'no'))
happiness_sv
fisher.test(happiness_sv) 


#get number of sadness utterances
nrow(emo_da[emo_da$emo=='sadness',]) 

#get sadness and apology
sadness_fa <- as.table(rbind(c(3, 3), c(33, 1165)))
dimnames(sadness_fa) <- list(group = c('apology', 'non-apology'), sadness = c('yes', 'no'))
sadness_fa
fisher.test(sadness_fa) 

#get sadness and statement-opinion
sadness_sv <- as.table(rbind(c(4, 71), c(32, 1097)))
dimnames(sadness_sv) <- list(group = c('sv', 'non-sv'), sadness = c('yes', 'no'))
sadness_sv
fisher.test(sadness_sv) 


#get number of anger utterances
nrow(emo_da[emo_da$emo=='anger',]) 

#get anger and active-directive
anger_ad <- as.table(rbind(c(7, 30), c(65, 1102)))
dimnames(anger_ad) <- list(group = c('Adirective', 'non-Adirective'), anger = c('yes', 'no'))
anger_ad
fisher.test(anger_ad) 

#get anger and statement-opinion 
anger_sv <- as.table(rbind(c(6, 69), c(66, 1063)))
dimnames(anger_sv) <- list(group = c('sv', 'non-sv'), anger = c('yes', 'no'))
anger_sv
fisher.test(anger_sv) 

#get anger and appreciation
anger_ba <- as.table(rbind(c(5, 81), c(67, 1051)))
dimnames(anger_ba) <- list(group = c('ba', 'non-ba'), anger = c('yes', 'no'))
anger_ba
fisher.test(happiness_ba) 


#get number of disgust utterances
nrow(emo_da[emo_da$emo=='disgust',])

#get disgust and statement-opinion
disgust_sv <- as.table(rbind(c(2, 73), c(1, 1128)))
dimnames(disgust_sv) <- list(group = c('sv', 'non-sv'), disgust = c('yes', 'no'))
disgust_sv
fisher.test(disgust_sv) 

#get disgust and wh-question
disgust_qw <- as.table(rbind(c(1, 68), c(2, 1133)))
dimnames(disgust_qw) <- list(group = c('wh-question', 'non-wh-question'), disgust = c('yes', 'no'))
disgust_qw
fisher.test(disgust_qw) 


#get number of surprise utterances
nrow(emo_da[emo_da$emo=='surprise',]) 

#get surprise and wh-question
surprise_bh <- as.table(rbind(c(8, 5), c(41, 1150)))
dimnames(surprise_bh) <- list(group = c('wh-question', 'non-wh-question'), surprise = c('yes', 'no'))
surprise_bh
fisher.test(surprise_bh)

#get surprise and appreciation
surprise_ba <- as.table(rbind(c(7, 79), c(42, 1076)))
dimnames(surprise_ba) <- list(group = c('appreciation', 'non-appreciation'), surprise = c('yes', 'no'))
surprise_ba
fisher.test(surprise_ba) 

#get surprise and yes-no-question
surprise_qy <- as.table(rbind(c(5, 78), c(44, 1077)))
dimnames(surprise_qy) <- list(group = c('yes-no-question', 'non-yes-no-question'), surprise = c('yes', 'no'))
surprise_qy
fisher.test(surprise_qy) 


