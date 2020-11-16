# Group Members



Mehdi Azabou         |  Tanya Churaman | Kipp Morris
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://drive.google.com/uc?export=view&id=1q9gtLcnP81Lxkf1nyHM2ygtYpChmGVU5" height="250" width="250" style="border-radius:100%">|<img src="https://drive.google.com/uc?export=view&id=1FOfCCVC0A9bwYVDHKnVr5QndiebH69ov" height="250" width="250" style="border-radius:100%">|<img src="https://drive.google.com/uc?export=view&id=1dKFfOWe4ZPOAA9E0sqG1KVuXBiwsSnb0" height="250" width="250" style="border-radius:100%">


<br>
# Note
Please open this website in Google Chrome or Firefox. Safari does not like the PDF embedding.

# Abstract

Accurately and quickly predicting case counts for any epidemic disease is a difficult problem with a wide variety of approaches, and having accurate counts would be extremely helpful in planning epidemic responses for a wide variety of stakeholders (public health officials, etc.). We decided to tackle COVID-19 case count prediction by improving on the performance of a spatio-temporal graph neural network model proposed by Kapoor et al., adding additional data features to the model to improve the performance, including more detailed data on mobility flow between counties, county-level population data, and county-level unemployment data. We were able to reduce the test RMSLE on the top 20 most populous counties from 0.0109 to 0.0080, and through a few ablation studies that we performed with the goal of finding out which features contribute most to the spread of COVID-19, we found that the mobility flow data is particularly significant to the predictions.



# Summary of the Project

The goal of this project was to determine the extent to which factors such as the presence/absence of shelter-in-place orders, socioeconomic status, and mobility patterns influence the spread of COVID-19 at the county level. We achieved this goal by: 
1. Predicting case counts using a graph neural network model that takes into account the aforementioned factors 
2. Explaining the network's predictions by looking at neuron activations and identifying salient features causing COVID-19 spread

The primary result we aimed for was a graph neural network that forecasts case counts, where the neural network’s input is a graph with a node for each county that contains data about case counts and all or some of the factors mentioned in the previous paragraph. If possible, we wanted to determine which individual factors are most significant while also finding the model that makes the best predictions.

This project should be of significant interest to health professionals and public health officials. By understanding the factors that affect the transmission of COVID-19 within and between counties, better mitigation strategies can be put into place. A one-size-fits-all approach might not be the best course of action for certain areas. Awareness of the different factors that affect the infection rate at can help officials understand the efficacy of mobility restrictions and how to implement strategies that are best for both the citizens and the economy, helping save lives.

# Results

## Baselines

RMSLE      |  RMSLE (top 20)
:-------------------------:|:-------------------------:
ARIMA      | 0.0144
LSTM      |  0.0121
Kapoor et al.      |  0.0109
Our Method |  0.0080

We find that our extension outperforms the baselines as well as the network from Kapoor et al. We find that the RMSLE over all counties is higher, which is to be expected. However, examine the predicted new case counts for Fulton county for example, which can be seen in the figure below. While the prediction isn't fully accurate, we find that the network mostly overestimates the number of new cases.

<img src="https://drive.google.com/uc?export=view&id=1nG3W63fMmOwErLE4_-OhetogeT3iRIgv" height="500" width="500">




<img src="https://drive.google.com/uc?export=view&id=1D78PTD228DiMz5RBLnVZUpFNqBRlU5jQ" height="500" width="500">



<img src="https://drive.google.com/uc?export=view&id=1nG3W63fMmOwErLE4_-OhetogeT3iRIgv" height="500" width="500">
<img src="https://drive.google.com/uc?export=view&id=17dGdf5pWeH00x16guj5CF06vgNGc7i8l" height="500" width="500">

<img src="https://drive.google.com/uc?export=view&id=1OVgWCgTiDedlSDNeZ5slHIhEwqSnVUqO" height="500" width="500">
<img src="https://drive.google.com/uc?export=view&id=1hET_XHg0Q8q1NxsPu6bAt_-yTFFooF9j" height="500" width="500">


  . |  RMSLE (top 20) | RMSLE
:-------------------------:|:-------------------------:|:-------------------------:
Baseline      | 8.0e-3 | 0.013
No Edge Weights (Mobility Flow)      |  9.6e-3| 0.030
No Population Features      | 7.7e-3| 0.028
No unemployment features|  8.8e-3| 0.022



# Write Up

THIS IS OUR MIDTERM REPORT AND SERVES AS A PLACEHOLDER

Below is a pdf of project. This write up contains these files in this listed order: Final Report, Milestone Report, Proposal. To download to your machine, please click on the folder with a down arrow (Firebox) or the down arrow (Chrome) in the grey ribbon on the top of PDF window.

<embed src="https://drive.google.com/uc?export=view&id=14WHRuNXix59hUl6IjyApXOXoBZPknGo7" width="830" height="1000" type="application/pdf" />

# Presentation Slides
RN THIS IS AN EXAMPLE

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<!-- this is the embed code provided by Google -->
  <iframe src="https://docs.google.com/presentation/d/1F0DQTNPg3YG_By6LMGcgwT3icJ3eMhCiupAZm76CIfE/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
<!-- Google embed ends -->
</div>

# Software Tar-Ball Files

Please click [here][1] to access the software tar-ball file!

[1]: Temp
