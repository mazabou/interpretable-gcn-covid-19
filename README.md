Interpretable Spatio-Temporal GCN for COVID-19
==============================

By modeling COVID-19 spread at the county level, we aim to disentangle the influence of factors such as the presence/absence of shelter-in-place orders, socioeconomic status, and mobility patterns.

We will be implementing the Spatio-temporal graph network from [[1]](#1), using the [Pytorch Geometric](https://github.com/rusty1s/pytorch_geometric) framework.

For GNNExplainer, we use the implementation that can be found [here](https://pytorch-geometric.readthedocs.io/en/latest/modules/nn.html?highlight=gnnexplainer#torch_geometric.nn.models.GNNExplainer)

The `src/data` directory contains scripts that can be used to clean and pull the data given the necessary files that are described in our final project report. At the top of each file are variables that you can modify corresponding to the paths to the input and output files. They just depend on common pip/Anaconda packages and the C3ai COVID-19 Data Lake API code that can be downloaded from C3ai's website, which is linked in our final report. Due to time constraints, we were not able to streamline the data aggregation and processing. You can find and download processed data for training and evaluation [here](https://www.dropbox.com/sh/7vjsbmry3q2g5sq/AADowcjsc8EhWZM-2efWCFdwa?dl=0).

#### Datasets
- Google's Mobility dataset: [Link](https://www.google.com/covid19/mobility/)
- UMD COVID-19 dataset: [Dashboard](https://data.covid.umd.edu)
- JHU dataset: [Dataset](https://github.com/CSSEGISandData/COVID-19)
- C3AI: [API Quickstart](https://c3.ai/covid-19-api-documentation/#section/Quickstart-Guide/Python-Quickstart)
- Delphi Covidcast API: [API documentation](https://cmu-delphi.github.io/delphi-epidata/api/covidcast.html)


### How to run Experiments
First experiment is training the network to predict new case counts: For training the network, refer to `src/models/train.ipynb`. We instantiate the dataset to load data and build graphs in `src/models/dataset.py` and define all the building blocks for the network in `src/models/st_gnn.py`. A trained model can be found in `models`.

Second experiment is for explaining the network's prediction, please refer to `src/models/gcn_explanation.ipynb`

#### References:
<a id="1">[1]</a> 
Kapoor, A., Ben, X., Liu, L., Perozzi, B., Barnes, M., Blais, M. and O'Banion, S., 2020. Examining covid-19 forecasting using spatio-temporal graph neural networks. arXiv preprint arXiv:2007.03113.
Vancouver

Project Organization
------------

    ├── data
    │   ├── train.npy       <- Train data
    │   ├── test.npy        <- Test data
    │   └── scripts      <- scripts to download and process data
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── docs            <- Report and presentation.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts and notebooks to train models and then use trained models to make
    │                         predictions
    │   
    │
    └── README.md          <- The top-level README for developers using this project.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
