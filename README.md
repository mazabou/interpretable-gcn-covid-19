Interpretable Spatio-Temporal GCN for COVID-19
==============================

By modeling COVID-19 spread at the county level, we aim to disentangle the influence of factors such as the presence/absence of shelter-in-place orders, socioeconomic status, and mobility patterns.

We will be implementing the Spatio-temporal graph network from [[1]](#1), using the [Pytorch Geometric](https://github.com/rusty1s/pytorch_geometric) framework.

For GNNExplainer, we use the implementation that can be found [here](https://pytorch-geometric.readthedocs.io/en/latest/modules/nn.html?highlight=gnnexplainer#torch_geometric.nn.models.GNNExplainer)

The `src/data` directory contains scripts that can be used to clean and pull the data given the necessary files that are described in our final project report. At the top of each file are variables that you can modify corresponding to the paths to the input and output files. They just depend on common pip/Anaconda packages and the C3ai COVID-19 Data Lake API code that can be downloaded from C3ai's website, which is linked in our final report.

#### Datasets
- Google's Mobility dataset: [Link](https://www.google.com/covid19/mobility/)
- UMD COVID-19 dataset: [Dashboard](https://data.covid.umd.edu)
- JHU dataset: [Dataset](https://github.com/CSSEGISandData/COVID-19)
- C3AI: [API Quickstart](https://c3.ai/covid-19-api-documentation/#section/Quickstart-Guide/Python-Quickstart)
- Delphi Covidcast API: [API documentation](https://cmu-delphi.github.io/delphi-epidata/api/covidcast.html)

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
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts and notebooks to train models and then use trained models to make
    │   │                     predictions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │
    └── README.md          <- The top-level README for developers using this project.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
