# Olympics Data Analysis For SportsStats
### (A Coursera Capstone Project)

This project focuses on analyzing the Olympics dataset spanning across 120years for SportsStats. 

SportsStats is a sports analytics firm partnering with local news and elite personal trainers to provide interesting insights, patterns, and trends by highlighting groups/events/countries and helping their partners develop a news story or helping discover key health insights. 

Furthermore, this analysis is meant to help SportsStats service her clientele.
Please find the link to the dataset given below:
[SportsStats](https://www.dropbox.com/sh/0wqw8fmiwrzr8ef/AABQijjQM522INXX1FCdamzma?dl=0)

### Approach
 ```python programming``` ```pandas```  was used to load the csv dataset locally using ```pd.read_csv()```
 while ```SQL```  is used to query and filter the loaded csv file. 
 The ```ggplot2```library in ```r programming``` was used in visualizing the data.

### Entity Relationship Diagram (ERD)
The diagram below is the Entity relationship diagram showing the relationship between tables.
![Entity Relationship Diagram](https://github.com/Eddiddi/Learn-Sql-Basics-for-Data-Science-Capstone-Project/blob/master/src/img/ERD.jpg "Entity Relationship Diagram")

This analysis covers descriptive statistics, questions of interest and hypothesis.

### Questions
Q1: Are they athletes who featured in two or more year seasons?

Q2: To investigate Gender-based athlete engagement distribution across different years and Seasons.

Q3: Cummulative Sport engagement based on athlete engagement.

Q4: Gender-based Performance of athlete in sporting events

Q5: Gender with the most medals.


### Hypothesis 
Did athletes who featured in different seasons win more medals than other athletes?

### Data Visualization
Figure 1: Shows the distribution of athlete category (Male & Female) across various years. 

![Gender-based athlete engagement distribution](https://github.com/Eddiddi/Learn-Sql-Basics-for-Data-Science-Capstone-Project/blob/master/src/img/gb_plot.png "Gender-based athlete engagement distribution")

Figure 2: Shows sporting categories with highest to lowest athletes participation. 

![Cummulative Sport engagement](https://github.com/Eddiddi/Learn-Sql-Basics-for-Data-Science-Capstone-Project/blob/master/src/img/sae_plot.png "Cummulative Sport engagement based on athlete engagement")

Figure 3: Shows a pyramid describing the participation of Male athletes and Femala athletes. 

![Gender-based in sporting events](https://github.com/Eddiddi/Learn-Sql-Basics-for-Data-Science-Capstone-Project/blob/master/src/img/sae_1_plot.jpg "Gender-based in sporting events")

Figure 4: Shows a bar plot of medals won by the Male & Female athletes respectively.

![Gender with the most medals](https://github.com/Eddiddi/Learn-Sql-Basics-for-Data-Science-Capstone-Project/blob/master/src/img/gwmm_plot.jpg "Gender with the most medals")

### Limitations
The following limitations serve as the challenges encountered in the cause of this analysis.

1. No access to a database  to directly apply SQL queries
2. ```pandasql``` for SQL doesn't support code formatting for better code presentations

### Recommendations
The analysis carried out shows 
1. Low female athletes participation across various sport and seasons like their male counterparts, and as such countries are advised to develop women's teams so as to have better female representation.

2. Investments in sport with low athlete engagement is advised as observed in sporting events such as Aeronautics, Basque Pelota, Roque, Jeu De Paume, Racquets etc.	



