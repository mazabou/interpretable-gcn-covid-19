# Group Members



Mehdi Azabou         |  Tanya Churaman | Kipp Morris
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://drive.google.com/uc?export=view&id=1q9gtLcnP81Lxkf1nyHM2ygtYpChmGVU5" height="250" width="250" style="border-radius:100%">|<img src="https://drive.google.com/uc?export=view&id=1FOfCCVC0A9bwYVDHKnVr5QndiebH69ov" height="250" width="250" style="border-radius:100%">|<img src="https://drive.google.com/uc?export=view&id=1dKFfOWe4ZPOAA9E0sqG1KVuXBiwsSnb0" height="250" width="250" style="border-radius:100%">


# Abstract

Accurately and quickly predicting case counts for any epidemic disease is a difficult problem with a wide variety of approaches. Even harder is explaining how an outbreak took place and what the driving factor was. Being able to answer these questions would be extremely helpful in planning epidemic responses for a wide variety of stakeholders (public health officials, etc.). We decided to tackle COVID-19 case count prediction by improving on the performance of a spatio-temporal graph neural network model proposed by Kapoor et al., adding additional data features to the model to improve the performance, including more detailed data on mobility flow between counties, county-level population data, and county-level unemployment data. We were able to reduce the test RMSLE on the top 20 most populous counties from 0.0109 to 0.0080, and through a few ablation studies that we performed with the goal of finding out which features contribute most to the spread of COVID-19. We finally use Ying et al. to closely study the dynamics of the spread within counties and between counties.


# Summary of the Project

The goal of this project was to have a performant and explainable network for COVID-19 case prediction. We aimed to make available to all stakeholders, a powerful tool that not only is capable of prediction but also of explaining why a breakout happened and what driving factors are behind a change in the spread dynamics. Using our proposed method for spatio-temporal graph networks, we leverage the graph structure to explicitly disentangle the within county spread and the between county spread. We also utilize a wide range of features to make our prediction.

We achieved this goal by: 
1. Aggregating and processing data from multiple sources, to build our train and test datasets.
2. Predicting case counts using a graph neural network model that takes into account the aforementioned factors 
3. Explaining the network's predictions by looking at node feature importance as well as messages passed along edges, and identifying salient features causing COVID-19 spread.

The primary result we aimed for was a graph neural network that forecasts case counts, where the neural network’s input is a graph with a node for each county that contains data about case counts and all or some of the factors mentioned in the previous paragraph. If possible, we wanted to determine which individual factors are most significant while also finding the model that makes the best predictions.

This project should be of significant interest to health professionals and public health officials. By understanding the factors that affect the transmission of COVID-19 within and between counties, better mitigation strategies can be put into place. A one-size-fits-all approach might not be the best course of action for certain areas. Awareness of the different factors that affect the infection rate at can help officials understand the efficacy of mobility restrictions and how to implement strategies that are best for both the citizens and the economy, helping save lives.

# Results


RMSLE      |  RMSLE (top 20)
:-------------------------:|:-------------------------:
ARIMA      | 0.0144
LSTM      |  0.0121
Kapoor et al.      |  0.0109
Our Method |  0.0080

We find that our extension outperforms the baselines as well as the network from Kapoor et al. We find that the RMSLE over all counties is higher.


#  Ablation studies

As one method of attempting to interpret the predictions of our model, we did a couple of ablation studies. For each ablation study, we removed a particular predictor variable or some set of predictor variables from the model, trained the network with the partial dataset, and compared the testing results to those of the network trained with all of the predictor variables, the idea being that if one of the networks from the ablation studies performs worse than the network that had access to all of the data, it indicates that the variable(s) removed during the corresponding ablation study are significant to the predictions and important for us to pay attention to in real life. We performed three ablation studies: one where we removed the mobility flow data, one where we removed the two population-related features, and one where we removed the unemployment-related features. The results are summarized in the table below, the takeaway being that all of the features we tried removing are significant to the predictions. Taking any of the features away increased the RMSLE by around 200-300\%. Specifically, we can see that at least on the top 20 most populous counties, the network performed better without the population features and that the mobility flow data looks to be particularly significant to the predictions among the features we looked at in the ablation studies.

  . |  RMSLE (top 20) | RMSLE
:-------------------------:|:-------------------------:|:-------------------------:
Baseline      | 8.0e-3 | 0.013
No Edge Weights (Mobility Flow)      |  9.6e-3| 0.030
No Population Features      | 7.7e-3| 0.028
No unemployment features|  8.8e-3| 0.022


# GNNExplainer
We use GNNExplainer to identify compact subgraph structures and node features that play a crucial role in the graph network's predictions.

We select a county and a day in which there is a spike in new cases or a change of slope in the number of total cases and try to understand what happened, or how the network was able to predict the spike.

First, we look at Crawford County, Wisconsin, on day 20 of the test set. As can be seen in the figure below, there is a spike in the next day, which is also predicted by the network. Crawford County has a small number of cases, thus, we hypothesize that the spike in cases might come from an inflow of cases from neighboring counties. 

<img src="https://drive.google.com/uc?export=view&id=1xTwUwHvVUwQ4joiqyZeoFWKXMd8axqeV">

We run the GNNExplainer and get the results in Figure 5. We find that indeed a lot of graph neighbors (2 counties in Oklahoma, 1 county in Texas) are contributing to the network's decision. This observation does not mean that the spike is specifically due to these counties. These counties might just be correlated in their dynamics as we can see in the figure above, but it does indicate where the cases might have came from. 
<img src="https://drive.google.com/uc?export=view&id=1m4pGsLAZHlCVRai6VRmPgWAz-Ihi3eKZ">

Another county that we consider, which has a higher case count than Crawford County, is Fort Bend County, Texas, which has a spike at the end of the month (Figure 4). GNNExplainer (Figure 6) finds that there is some link to Fort Bend, which again might explain where this increase in cases is coming from.

In each of these experiments, we look at both node feature importance and edge importance, and in both, we find that edges are more important, so they might be the leading factor for spread. Now we look at a more populous county: LA County. We interestingly find that edge importance is very low, while in terms of nodes, we find that both unemployment rates and previous day case count are most important, with importance scores over 0.8. The unemployment rate in LA is around 20\%, which is higher than the national average. We suspect that the unemployment rate is just correlated with the case count, but it is not clear that it is a driving factor for COVID-19 spread. Unfortunately, no further experiments were conducted to analyse this further.


# Write Up
Below is a pdf of project. This write up contains these files in this listed order: Final Report, Milestone Report, Proposal. To download to your machine, please click on the folder with a down arrow (Firebox) or the down arrow (Chrome) in the grey ribbon on the top of PDF window.

<embed src="https://drive.google.com/uc?export=view&id=12PNpOvoD4lgpLfSDILGfqDpd_pG4OYe1" width="830" height="1000" type="application/pdf" />

The report can also be found [here](https://github.com/mazabou/interpretable-gcn-covid-19/blob/main/docs/cse_8803_final_report.pdf)

# Presentation Slides

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<!-- this is the embed code provided by Google -->
 <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vStssGyxLyjnatnU2wW8r-wXMsNyTNnbNDHuNwOZ99V4WUaCBqOqTW81wgO1bm9nxUKcS5WTITCMDVz/embed?start=false&loop=true&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
<!-- Google embed ends -->
</div>


The presentation can also be found [here](https://github.com/mazabou/interpretable-gcn-covid-19/blob/main/docs/Final%20Presentation.pdf)

# Software Tar-Ball Files

Please click [here][1] to access the software tar-ball file!

[1]: Temp
