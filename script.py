#Please install the following python packages where needed.
#link to the dataset:

# https://www.dropbox.com/sh/0wqw8fmiwrzr8ef/AABQijjQM522INXX1FCdamzma?dl=0

#python Packages

import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
##R packages

%load_ext rpy2.ipython
library(ggplot2)
library(dplyr)
library(scales)

#import file using pandas
athletes_events = pd.read_csv("athlete_events.csv")
athletes_events

#Q1: If  there exist athletes who featured in two or more year seasons?
#python code:

m2= pysqldf("SELECT Name, Sport, COUNT(Name) AS `Number of Appearances` FROM athletes_events GROUP BY Name, Sport ORDER BY `Number of Appearances` DESC ")
m2
#ANS: YES

#Q2: To investigate Gender-based athlete engagement distribution across different years and Seasons.
#python code:

gb_dist_plot_data=pysqldf("SELECT Year, COUNT(Gender) AS Total, Gender FROM (SELECT Year,Name, Season,Sex, CASE WHEN Sex = 'M' OR 'Male' THEN 'Male' WHEN Sex = 'F' OR 'Female' THEN 'Female' ELSE NULL END AS Gender FROM athletes_events)GROUP BY Year, Gender ORDER BY Year ASC")
gb_dist_plot_data

# From the dataset and data visualization above, year 1896 has no female athletic participation. 
# And up from the preceeding year(1900)down to 2016 there has been a significant increase in female athletic 
# participation in the Olympics. Similarly, the Men's athletic engagements right from inception has been overwhelming,
# though not steady, the numbers still outrun that of the women throughout the 120years Olympic games coverage

#R code:
%%R -i gb_dist_plot_data -w 950 -h 450
gb_plot<-ggplot(gb_dist_plot_data, aes(Year,Total)) +geom_smooth(aes(colour = Gender))
gb_plot<- gb_plot + geom_point(size = 4, aes(colour = Gender))
gb_plot<- gb_plot + ggtitle("Gender-Based Sports Engagement Distribution")
gb_plot<- gb_plot + theme(plot.title = element_text(face = "bold", size = 20, hjust = 0.5), legend.position = c(0.9, 0.9))
gb_plot<- gb_plot + labs(x= "Year", y = "Total") + theme(axis.title = element_text(face = "bold", size = 15))
gb_plot<- gb_plot + theme(axis.text.x = element_text(size = 12, face = "bold"))
gb_plot<- gb_plot + theme(axis.text.y = element_text(size = 12, face = "bold"))
gb_plot<- gb_plot + theme(legend.title = element_text(size = 13, face = "bold"))
gb_plot<- gb_plot + theme(legend.text = element_text(size = 9, face = "italic"))
gb_plot<- gb_plot + theme(panel.background = element_rect(fill = 'transparent'))
gb_plot

#Q3: Cummulative Sports and Athlete Engagement.
#python & SQL code:

sae = pysqldf("SELECT Sport, COUNT(Name) AS `Total Athletes`  FROM athletes_events GROUP BY Sport ORDER BY `Total Athletes` ASC")
sae

#R code:
%%R -i sae -w 950 -h 600
sae_plot<- ggplot(sae,aes( y= reorder(Sport, `Total Athletes`), x = `Total Athletes`)) + geom_col(aes(colour = Sport, fill = "white"), alpha = 0.3, width = 1)
sae_plot<- sae_plot + ggtitle("Cummulative Sports And Athletes Engagement") 
sae_plot<- sae_plot + theme(panel.background = element_rect(fill = 'transparent'),legend.position = "none")
sae_plot<- sae_plot + theme(plot.title = element_text(face = "bold", size = 20, hjust = 0.5),axis.text.x = element_text(size = 12, face = "bold"))
sae_plot<- sae_plot + theme(axis.text.y = element_text(size = 10, face = "bold"))
sae_plot<- sae_plot + labs(x= "Total Number of Athletes", y = "Sport") + theme(axis.title = element_text(face = "bold", size = 15))
sae_plot

#The figure above shows the cummulative of athletes who participated in the various games in a 120year period 
# with some sporting categories having less number of athletes than in other sport categories.


##Q4: Gender-based Performance Pyramid in sporting events.
#python & SQL code:

sae_1 = pysqldf("SELECT Year, Sport, COUNT(Gender) AS Total, Gender FROM (SELECT Year,Name,Sport, Season,Sex, CASE WHEN Sex = 'M' OR 'Male' THEN 'Male' WHEN Sex = 'F' OR 'Female' THEN 'Female' ELSE NULL END AS Gender FROM athletes_events)GROUP BY Year, Sport, Gender ORDER BY Year ASC")
sae_1

#R code:
# %%R -i sae_1 -w 950 -h 600
sae_1_filtered<- sae_1 %>% mutate(value = ifelse (Gender == "Female", -Total, Total))
sae_1_plot<-ggplot(sae_1_filtered, aes(x = value, y = reorder(Sport,Total), fill = Gender)) + geom_col() + theme_minimal()
sae_1_plot<-sae_1_plot+ ggtitle("Gender-Based Performance Pyramid") + theme(plot.title = element_text(face ="bold",size = 20, hjust = 0.5))
sae_1_plot<-sae_1_plot+ theme(axis.text.x = element_text(size = 12, face = "bold"))
sae_1_plot<-sae_1_plot+ theme(axis.text.y = element_text(size = 10, face = "bold")) +  theme(legend.text = element_text(size = 9, face = "italic"))
sae_1_plot<-sae_1_plot+ labs(x= "Total Number of Athletes", y = "Sport") + theme(axis.title = element_text(face = "bold", size = 15)) 
sae_1_plot<-sae_1_plot+ scale_x_continuous(labels = abs,limits = 4000 * c(-1,1))
sae_1_plot

#Q5: Gender with more medals
#python & SQL code:
gwmm = pysqldf(" SELECT Sex, COUNT(Medal) AS `Medal count` FROM athletes_events WHERE Medal IS NOT NULL GROUP BY Sex")
gwmm

#R code:
%%R -i cwmm
gwmm_plot<- ggplot(cwmm, aes(x =Sex, y = `Medal count`, fill = Sex)) + geom_col() + theme_minimal()
gwmm_plot<- gwmm_plot + ggtitle("Gender-based Medal Ranking")+ theme(plot.title = element_text(face ="bold",size = 20, hjust = 0.5))
gwmm_plot<- gwmm_plot + theme(axis.text.x = element_text(size = 12, face = "bold"))
gwmm_plot<- gwmm_plot + theme(axis.text.y = element_text(size = 10, face = "bold")) + theme(legend.text = element_text(size = 9, face = "italic"))
gwmm_plot<- gwmm_plot + theme(axis.title = element_text(face = "bold", size = 15))
gwmm_plot




# Hypothesis 

# Did athletes who featured in different seasons win more medals than other athletes?
#python & SQL code:

more_than_2x = pysqldf("SELECT binary_medal, COUNT(CASE WHEN binary_medal = 1 AND Medal IS NOT NULL THEN 1 END)AS Treatment, COUNT(CASE WHEN binary_medal = 0 AND Medal IS NOT NULL THEN 0 END) AS Control, COUNT(CASE WHEN binary_medal = 0 THEN 0 ELSE NULL END) AS `Control Total`, COUNT(CASE WHEN binary_medal= 1 THEN 1 ELSE NULL END) AS `Treatment Total` FROM (SELECT Name, COUNT(Name), Medal, CASE WHEN COUNT(Name) = 1  THEN 1 WHEN COUNT(Name) >= 2 THEN 0 END AS binary_medal FROM athletes_events GROUP BY Name) WHERE binary_medal IS NOT NULL GROUP BY binary_medal")
more_than_2x

#findings:

#The binary values of 0 and 1 which serves as the control and treatment respectively of the hypothesis for athletes 
# with more than one appearance throughout the 120 years Olympics competition winning more Medals than athletes with 
# just an appearance throughout the 120years Olympics competition. The resulting values are tested using
# ABBA A/B testing statistics
# (https://thumbtack.github.io/abba/demo/abba.html#Baseline=11492%2C77009&Variation+1=7543%2C57723&abba%3AintervalConfidenceLevel=0.95&abba%3AuseMultipleTestCorrection=true)
# to verify this hypothesis.Results at 0.95 Confidence Interval show that there is a significant relationship 
# between control and treatment as p-value is less than alpha = 0.05, success rate is 15% and 
# an improvement rate of 14%. Therefore, we reject the null hypothesis and conclude that athelete who featured more 
# than once didnt win more medals. 
