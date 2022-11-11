# Olympics Data Analysis For SportsStats
### (A Coursera Capstone Project)

This project focuses on analyzing the Olympics dataset spanning across 120years for SportsStats. 

SportsStats is a sports analytics firm partnering with local news and elite personal trainers to provide interesting insights, patterns, and trends by highlighting groups/events/countries and helping their partners develop a news story or helping discover key health insights. 

Furthermore, this analysis is meant to help SportsStats service her clientele.
Please find the link to the dataset given below:
https://www.dropbox.com/sh/0wqw8fmiwrzr8ef/AABQijjQM522INXX1FCdamzma?dl=0

### Approach
 ```pandas```  was used to load the csv dataset locally using ```read.csv()```
 while ```SQL``` was is used to query and filter the csv file with the help of ```python programming``` and ```ggolot2``` in ```r programming``` is equally used in visualizing the data.

### Entity Relationship Diagram (ERD)
![Entity Relationship Diagram](Learn-Sql-Basics-for-Data-Science-Capstone-Project\src\img\ERD.jpg "Entity Relationship Diagram")

This analysis covers the descriptive statistics, questions of interest and hypothesis.

### Questions
Q1: If  there exist athletes who featured in two or more year seasons?

Q2: To investigate Gender-based athlete engagement distribution across different years and Seasons.
![Gender-based athlete engagement distribution](Learn-Sql-Basics-for-Data-Science-Capstone-Project\src\img\gb_plot.png "Gender-based athlete engagement distribution")

Q3: Cummulative Sport engagement based on athlete engagement.
![Cummulative Sport engagement](Learn-Sql-Basics-for-Data-Science-Capstone-Project\src\img\sae_1_plot.jpg "Cummulative Sport engagement based on athlete engagement")

Q4: Gender with the most medals.
![Gender with the most medals](Learn-Sql-Basics-for-Data-Science-Capstone-Project\src\img\gwmm_plot.jpg "Gender with the most medals")

### Hypothesis 

Did athletes who featured in different seasons win more medals than other athletes?

### Limitations 
The following limitations serve as the challenges encountered in the cause of the analysis of this capstone project.

1. No access to a database  to directly apply sql queries
2. ```pandasql``` for SQL doesn't support code formatting for better code presentations

### Recommendations
The analysis carried out shows 
1. Low female athletes participation across various sport and seasons like their male counterparts, and as such countries are advised to develop women's teams so as to have better female representation.

2. Investments in sport with low athlete engagement is advised as observed in sporting events such as Aeronautics, Basque Pelota, Roque, Jeu De Paume, Racquets etc.	



