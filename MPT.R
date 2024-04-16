library(lme4)
library(lmerTest)
library(tidyverse)
library(ggplot2)

setwd("~/Documents/nancelab/diff_viz/diff_viz/tests/testing_data/r_testing_data") ### Change this to whatever folder you save things to

##### Read in all the data and subset down to D_fit and D_eff1, then add variables for Age, Slice, and Video
##### P14
P14_s1_v1 <- read.csv("P14_s1_v1.csv")
P14_s1_v1 <- subset(P14_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s1_v1$Age <- "P14"
P14_s1_v1$Slice <- "P14 S1"
P14_s1_v1$Video <- "P14 V11"

P14_s1_v2 <- read.csv("P14_s1_v2.csv")
P14_s1_v2 <- subset(P14_s1_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s1_v2$Age <- "P14"
P14_s1_v2$Slice <- "P14 S1"
P14_s1_v2$Video <- "P14 V12"

P14_s1_v3 <- read.csv("P14_s1_v3.csv")
P14_s1_v3 <- subset(P14_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s1_v3$Age <- "P14"
P14_s1_v3$Slice <- "P14 S1"
P14_s1_v1$Video <- "P14 V13"

P14_s1_v4 <- read.csv("P14_s1_v4.csv")
P14_s1_v4 <- subset(P14_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s1_v4$Age <- "P14"
P14_s1_v4$Slice <- "P14 S1"
P14_s1_v1$Video <- "P14 V14"

P14_s1_v5 <- read.csv("P14_s1_v5.csv")
P14_s1_v5 <- subset(P14_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s1_v5$Age <- "P14"
P14_s1_v5$Slice <- "P14 S1"
P14_s1_v1$Video <- "P14 V15"


P14_s2_v1 <- read.csv("P14_s2_v1.csv")
P14_s2_v1 <- subset(P14_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s2_v1$Age <- "P14"
P14_s2_v1$Slice <- "P14 S2"
P14_s2_v1$Video <- "P14 V21"

P14_s2_v2 <- read.csv("P14_s2_v2.csv")
P14_s2_v2 <- subset(P14_s2_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s2_v2$Age <- "P14"
P14_s2_v2$Slice <- "P14 S2"
P14_s2_v2$Video <- "P14 V22"

P14_s2_v3 <- read.csv("P14_s2_v3.csv")
P14_s2_v3 <- subset(P14_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s2_v3$Age <- "P14"
P14_s2_v3$Slice <- "P14 S2"
P14_s2_v1$Video <- "P14 V23"

P14_s2_v4 <- read.csv("P14_s2_v4.csv")
P14_s2_v4 <- subset(P14_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s2_v4$Age <- "P14"
P14_s2_v4$Slice <- "P14 S2"
P14_s2_v1$Video <- "P14 V24"

P14_s2_v5 <- read.csv("P14_s2_v5.csv")
P14_s2_v5 <- subset(P14_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s2_v5$Age <- "P14"
P14_s2_v5$Slice <- "P14 S2"
P14_s2_v1$Video <- "P14 V25"


P14_s3_v1 <- read.csv("P14_s3_v1.csv")
P14_s3_v1 <- subset(P14_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s3_v1$Age <- "P14"
P14_s3_v1$Slice <- "P14 S3"
P14_s3_v1$Video <- "P14 V31"

P14_s3_v2 <- read.csv("P14_s3_v2.csv")
P14_s3_v2 <- subset(P14_s3_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s3_v2$Age <- "P14"
P14_s3_v2$Slice <- "P14 S3"
P14_s3_v2$Video <- "P14 V32"

P14_s3_v3 <- read.csv("P14_s3_v3.csv")
P14_s3_v3 <- subset(P14_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s3_v3$Age <- "P14"
P14_s3_v3$Slice <- "P14 S3"
P14_s3_v1$Video <- "P14 V33"

P14_s3_v4 <- read.csv("P14_s3_v4.csv")
P14_s3_v4 <- subset(P14_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s3_v4$Age <- "P14"
P14_s3_v4$Slice <- "P14 S3"
P14_s3_v1$Video <- "P14 V34"

P14_s3_v5 <- read.csv("P14_s3_v5.csv")
P14_s3_v5 <- subset(P14_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P14_s3_v5$Age <- "P14"
P14_s3_v5$Slice <- "P14 S3"
P14_s3_v1$Video <- "P14 V35"


##### P35
P35_s1_v1 <- read.csv("P35_s1_v1.csv")
P35_s1_v1 <- subset(P35_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s1_v1$Age <- "P35"
P35_s1_v1$Slice <- "P35 S1"
P35_s1_v1$Video <- "P35 V11"

P35_s1_v2 <- read.csv("P35_s1_v2.csv")
P35_s1_v2 <- subset(P35_s1_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s1_v2$Age <- "P35"
P35_s1_v2$Slice <- "P35 S1"
P35_s1_v2$Video <- "P35 V12"

P35_s1_v3 <- read.csv("P35_s1_v3.csv")
P35_s1_v3 <- subset(P35_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s1_v3$Age <- "P35"
P35_s1_v3$Slice <- "P35 S1"
P35_s1_v1$Video <- "P35 V13"

P35_s1_v4 <- read.csv("P35_s1_v4.csv")
P35_s1_v4 <- subset(P35_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s1_v4$Age <- "P35"
P35_s1_v4$Slice <- "P35 S1"
P35_s1_v1$Video <- "P35 V14"

P35_s1_v5 <- read.csv("P35_s1_v5.csv")
P35_s1_v5 <- subset(P35_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s1_v5$Age <- "P35"
P35_s1_v5$Slice <- "P35 S1"
P35_s1_v1$Video <- "P35 V15"


P35_s2_v1 <- read.csv("P35_s2_v1.csv")
P35_s2_v1 <- subset(P35_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s2_v1$Age <- "P35"
P35_s2_v1$Slice <- "P35 S2"
P35_s2_v1$Video <- "P35 V21"

P35_s2_v2 <- read.csv("P35_s2_v2.csv")
P35_s2_v2 <- subset(P35_s2_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s2_v2$Age <- "P35"
P35_s2_v2$Slice <- "P35 S2"
P35_s2_v2$Video <- "P35 V22"

P35_s2_v3 <- read.csv("P35_s2_v3.csv")
P35_s2_v3 <- subset(P35_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s2_v3$Age <- "P35"
P35_s2_v3$Slice <- "P35 S2"
P35_s2_v1$Video <- "P35 V23"

P35_s2_v4 <- read.csv("P35_s2_v4.csv")
P35_s2_v4 <- subset(P35_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s2_v4$Age <- "P35"
P35_s2_v4$Slice <- "P35 S2"
P35_s2_v1$Video <- "P35 V24"

P35_s2_v5 <- read.csv("P35_s2_v5.csv")
P35_s2_v5 <- subset(P35_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s2_v5$Age <- "P35"
P35_s2_v5$Slice <- "P35 S2"
P35_s2_v1$Video <- "P35 V25"


P35_s3_v1 <- read.csv("P35_s3_v1.csv")
P35_s3_v1 <- subset(P35_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s3_v1$Age <- "P35"
P35_s3_v1$Slice <- "P35 S3"
P35_s3_v1$Video <- "P35 V31"

P35_s3_v2 <- read.csv("P35_s3_v2.csv")
P35_s3_v2 <- subset(P35_s3_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s3_v2$Age <- "P35"
P35_s3_v2$Slice <- "P35 S3"
P35_s3_v2$Video <- "P35 V32"

P35_s3_v3 <- read.csv("P35_s3_v3.csv")
P35_s3_v3 <- subset(P35_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s3_v3$Age <- "P35"
P35_s3_v3$Slice <- "P35 S3"
P35_s3_v1$Video <- "P35 V33"

P35_s3_v4 <- read.csv("P35_s3_v4.csv")
P35_s3_v4 <- subset(P35_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s3_v4$Age <- "P35"
P35_s3_v4$Slice <- "P35 S3"
P35_s3_v1$Video <- "P35 V34"

P35_s3_v5 <- read.csv("P35_s3_v5.csv")
P35_s3_v5 <- subset(P35_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P35_s3_v5$Age <- "P35"
P35_s3_v5$Slice <- "P35 S3"
P35_s3_v1$Video <- "P35 V35"


##### P70
P70_s1_v1 <- read.csv("P70_s1_v1.csv")
P70_s1_v1 <- subset(P70_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s1_v1$Age <- "P70"
P70_s1_v1$Slice <- "P70 S1"
P70_s1_v1$Video <- "P70 V11"

P70_s1_v2 <- read.csv("P70_s1_v2.csv")
P70_s1_v2 <- subset(P70_s1_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s1_v2$Age <- "P70"
P70_s1_v2$Slice <- "P70 S1"
P70_s1_v2$Video <- "P70 V12"

P70_s1_v3 <- read.csv("P70_s1_v3.csv")
P70_s1_v3 <- subset(P70_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s1_v3$Age <- "P70"
P70_s1_v3$Slice <- "P70 S1"
P70_s1_v1$Video <- "P70 V13"

P70_s1_v4 <- read.csv("P70_s1_v4.csv")
P70_s1_v4 <- subset(P70_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s1_v4$Age <- "P70"
P70_s1_v4$Slice <- "P70 S1"
P70_s1_v1$Video <- "P70 V14"

P70_s1_v5 <- read.csv("P70_s1_v5.csv")
P70_s1_v5 <- subset(P70_s1_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s1_v5$Age <- "P70"
P70_s1_v5$Slice <- "P70 S1"
P70_s1_v1$Video <- "P70 V15"


P70_s2_v1 <- read.csv("P70_s2_v1.csv")
P70_s2_v1 <- subset(P70_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s2_v1$Age <- "P70"
P70_s2_v1$Slice <- "P70 S2"
P70_s2_v1$Video <- "P70 V21"

P70_s2_v2 <- read.csv("P70_s2_v2.csv")
P70_s2_v2 <- subset(P70_s2_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s2_v2$Age <- "P70"
P70_s2_v2$Slice <- "P70 S2"
P70_s2_v2$Video <- "P70 V22"

P70_s2_v3 <- read.csv("P70_s2_v3.csv")
P70_s2_v3 <- subset(P70_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s2_v3$Age <- "P70"
P70_s2_v3$Slice <- "P70 S2"
P70_s2_v1$Video <- "P70 V23"

P70_s2_v4 <- read.csv("P70_s2_v4.csv")
P70_s2_v4 <- subset(P70_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s2_v4$Age <- "P70"
P70_s2_v4$Slice <- "P70 S2"
P70_s2_v1$Video <- "P70 V24"

P70_s2_v5 <- read.csv("P70_s2_v5.csv")
P70_s2_v5 <- subset(P70_s2_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s2_v5$Age <- "P70"
P70_s2_v5$Slice <- "P70 S2"
P70_s2_v1$Video <- "P70 V25"


P70_s3_v1 <- read.csv("P70_s3_v1.csv")
P70_s3_v1 <- subset(P70_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s3_v1$Age <- "P70"
P70_s3_v1$Slice <- "P70 S3"
P70_s3_v1$Video <- "P70 V31"

P70_s3_v2 <- read.csv("P70_s3_v2.csv")
P70_s3_v2 <- subset(P70_s3_v2, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s3_v2$Age <- "P70"
P70_s3_v2$Slice <- "P70 S3"
P70_s3_v2$Video <- "P70 V32"

P70_s3_v3 <- read.csv("P70_s3_v3.csv")
P70_s3_v3 <- subset(P70_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s3_v3$Age <- "P70"
P70_s3_v3$Slice <- "P70 S3"
P70_s3_v1$Video <- "P70 V33"

P70_s3_v4 <- read.csv("P70_s3_v4.csv")
P70_s3_v4 <- subset(P70_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s3_v4$Age <- "P70"
P70_s3_v4$Slice <- "P70 S3"
P70_s3_v1$Video <- "P70 V34"

P70_s3_v5 <- read.csv("P70_s3_v5.csv")
P70_s3_v5 <- subset(P70_s3_v1, select = c(Track_ID,Mean.D_fit,Mean.Deff1))
P70_s3_v5$Age <- "P70"
P70_s3_v5$Slice <- "P70 S3"
P70_s3_v1$Video <- "P70 V35"

##### bind all the files together
mpt <- bind_rows(P14_s1_v1,P14_s1_v2,P14_s1_v3,P14_s1_v4,P14_s1_v5,
                 P14_s2_v1,P14_s2_v2,P14_s2_v3,P14_s2_v4,P14_s2_v5,
                 P14_s3_v1,P14_s3_v2,P14_s3_v3,P14_s3_v4,P14_s3_v5,
                 P35_s1_v1,P35_s1_v2,P35_s1_v3,P35_s1_v4,P35_s1_v5,
                 P35_s2_v1,P35_s2_v2,P35_s2_v3,P35_s2_v4,P35_s2_v5,
                 P35_s3_v1,P35_s3_v2,P35_s3_v3,P35_s3_v4,P35_s3_v5,
                 P70_s1_v1,P70_s1_v2,P70_s1_v3,P70_s1_v4,P70_s1_v5,
                 P70_s2_v1,P70_s2_v2,P70_s2_v3,P70_s2_v4,P70_s2_v5,
                 P70_s3_v1,P70_s3_v2,P70_s3_v3,P70_s3_v4,P70_s3_v5)

#### Model for D fit
m = lmer(Mean.D_fit ~ Age + (1 | Slice)  + (1 | Video), data = mpt)
print(m)
summary(m)
confint(m)

#### Model for Deff1
m = lmer(Mean.Deff1 ~ Age + (1 | Slice)  + (1 | Video), data = mpt)
summary(m)
confint(m)

#### ANOVA comparing main model to null model to get single p-value
m = lmer(Mean.Deff1 ~ Age + (1 | Slice)  + (1 | Video), data = mpt)
m0 = lmer(Mean.Deff1 ~ (1 | Slice) + (1 | Video), data = mpt)
anova(m,m0)

p = ggplot(data=mpt, aes(x=Age, y=Mean.D_fit)) + geom_violin(trim=FALSE)
#p + stat_summary(fun.y=median, geom="point", shape=23, size=2, color='blue')
p + geom_boxplot(width=0.1)