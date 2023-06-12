# NBA Salary Predictor
## Contents:
- [Problem Statement](#Problem-Statement)
- [Software Requirements](#Software-Requirements)
- [Notebook Descriptions](#Notebook-Descriptions)
- [Data Source](#Data-Source)
- [Data Dictionary](#Data-Dictionary)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)

## Problem Statement: 
The goal of this project is to develop a Machine Learning Regression model to predict NBA player salary. The model will be based on statistics and salary data from the website basketball-reference.com. The model can be applied to data it was not trained on, and used as an all-encompassing metric for player performance. If a player's predicted salary is much lower than their actual salary, then they did not have statistics to match their salary and vice-versa. I plan to optimize for the R squared and RMSE when developing my models. This project will be useful for NBA Staff, Agents, and as an application for fans of Basketball.

## Software Requirements
-Pandas
-Scikit-learn
-numpy
-matplotlib.pyplot
-seaborn
-requests
-bs4
-re
-warnings
-urllib

## Notebook Descriptions
|File Name|Description|
|---|---|
|1_Data_Collection.ipynb | In this notebook, I wrote several functions to acquire the data. I acquired statistical data, salary data, team salary data, draft data, and salary cap data seperately. These were scraped from the website basketballreference.com or spotrac.com. In this section, I also cleaned the data and merged it into one dataframe to prepare it for EDA.|
|2)EDA_and_Feature_Engineering.ipynb| In this notebook, I cleaned the data more to prepare it for EDA and modeling. I imputed for missing values in a fashion that I found appropriate. I created several graphs of x variables compared to the target variable, noticing that the graphs often follow a non-linear trend. In addition, I engineered several new features using my basketball knowledge to try to improve model performance.|
|3)Modeling.ipynb|In this section, I experimented with several machine learning models to try to optimize for R^2 and RMSE. The best model was a stacked model using Boosting and RandomForest regressors. The model was slightly overfit towards the lower salaries. I looked into the predictions for the 2023 dataset, to see if the predictions matched up with domain knowledge- and they did.
|streamlit.py| A streamlit app which allows a user to type in the name of a player and get their true salary, predicted salary, and the disparity between the two|

## Data Source
The data is scraped from the website basketball-reference.com. Credit to basketball-reference.com for the data! I also scraped salary cap data from Spotrac.com. Without these two websites this project would not be possible.

## Data Dictionary
Below are the features available in the `modeling_dataset`:

| Feature               | Type   | Description                                                                 |
|-----------------------|--------|-----------------------------------------------------------------------------|
| Player                | Object | The name of the player                                                      |
| Pos                   | Object | The position that the player plays                                          |
| Age                   | Int    | The age of the player                                                       |
| Tm                    | Object | Abbreviated version of the team that they play for                          |
| G                     | Int    | Number of games played that season                                          |
| GS                    | Int    | Number of games started that season                                         |
| MP                    | Float  | Minutes played per game                                                     |
| FG                    | Float  | Number of shots made per game                                               |
| FGA                   | Float  | Number of shots attempted per game                                          |
| FG%                   | Float  | Percentage of shots made per game                                           |
| 3P                    | Float  | Number of 3-point shots made per game                                       |
| 3PA                   | Float  | Number of 3-point shots attempted per game                                  |
| 3P%                   | Float  | Percentage of 3-point shots made out of those attempted per game            |
| 2P                    | Float  | Number of 2-point shots made per game                                       |
| 2PA                   | Float  | Number of 2-point shots attempted per game                                  |
| 2P%                   | Float  | Percentage of 2-point shots made out of those attempted per game            |
| FT                    | Float  | Number of free throws made per game                                         |
| FTA                   | Float  | Number of free throws attempted per game                                    |
| FT%                   | Float  | Percentage of free throws made out of those attempted per game              |
| ORB                   | Float  | Offensive rebounds per game                                                 |
| DRB                   | Float  | Defensive rebounds per game                                                 |
| TRB                   | Float  | Total rebounds per game                                                     |
| AST                   | Float  | Assists per game                                                            |
| STL                   | Float  | Steals per game                                                             |
| BLK                   | Float  | Blocks per game                                                             |
| TOV                   | Float  | Turnovers per game                                                          |
| PF                    | Float  | Personal fouls per game                                                     |
| Pts                   | Float  | Points per game                                                             |
| PER                   | Float  | A measure of per-minute production standardized so that league average is 15|
| TS%                   | Float  | A measure of shooting efficiency considering 3-point, 2-point, and free throws|
| 3PAr                  | Float  | Percentage of shots attempted from 3-point range                            |
| FTr                   | Float  | Number of free throw attempts per field goal attempt                        |
| ORB%                  | Float  | An estimate of the percentage of available offensive rebounds a player grabbed while they were on the court |
| DRB%                  | Float  | An estimate of the percentage of available defensive rebounds a player grabbed while they were on the court |
| TRB%                  | Float  | An estimate of the percentage of available rebounds a player grabbed while they were on the court |
| AST%                  | Float  | An estimate of the percentage of available assists a player made while they were on the court |
| STL%                  | Float  | An estimate of the percentage of opponent possessions that end in a steal by this player |
| BLK%                  | Float  | An estimate of the percentage of opponent possessions that end in a block by this player |
| TOV%                  | Float  | Turnovers committed per 100 plays                                           |
| USG%                  | Float  | An estimate of the number of plays used by a player while they were on the court |
| OWS                   | Float  | An estimate of the number of wins contributed by a player due to their offense |
| DWS                   | Float  | An estimate of the number of wins contributed by a player due to their defense |
| WS                    | Float  | An estimate of the total number of wins contributed by a player             |
| WS/48                 | Float  | Win Shares per 48 minutes played                                            |
| Year                  | Int    | The year the season took place (e.g., 2009-10 is referred to as 2010)       |
| Draft Position Category| Object| Which draft position category a player is in, separated by various draft rankings into groups (e.g., top 4 pick, undrafted) |
| Total Minutes         | Float  | Total minutes a player played in a season                                   |
| Salary                | Int    | The salary of a player in a given season                                    |
| Cap Maximum           | Int    | The salary cap maximum of the NBA in a given season                         |
| Years Experience      | Int    | The number of years a player has been in the NBA (1 for rookies)            |

### Conclusions and Recommendations
The stacked model can be used to evaluate player performance in a given season based on whether they underperformed or outperformed their salary. The model had an r^2 score of 77%. In addition, it can be used by general managers and player agents as a tool in negotiations. The model is biased towards overpredicting lower salaries and underpredicting higher salaries. This is either a limitation of the model, or a misuse of financial resources across the entire NBA. I will leave it up to the reader to decide which one they think it is, but it is likely a bit of both!


More stats could be added, like per 36 minutes stats.
Could cross validate salary data with another source.
Experimentation with neural networks would be beneficial for potential improved results.


