Interpretable Spatio-Temporal GCN for COVID-19
==============================

By modeling COVID-19 spread at the county level, we aim to disentangle the influence of factors such as the presence/absence of shelter-in-place orders, socioeconomic status, and mobility patterns.

We will be implementing the Spatio-temporal graph network from [[1]](#1), using the [Pytorch Geometric](https://github.com/rusty1s/pytorch_geometric) framework.

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
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   └── processed      <- The final, canonical data sets for modeling.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── README.md          <- The top-level README for developers using this project.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
