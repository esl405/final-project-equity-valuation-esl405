# final-project-equity-valuation-esl405
Final Project for ESL405

This is based on the README.md from Professor Rossetti (https://github.com/prof-rossetti/nyu-info-2335-201905/tree/master/projects/robo-advisor)

Issues requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "equity-env":

```sh
conda create -n equity-env python=3.7 # (first time only)
conda activate equity-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
or 
```sh
pip install pandas
pip install os
pip install tkinter
```
## Setup

## Usage

Run the recommendation script:

```py
python app/equity-valuation.py
```
## Recommendation
If the stock is overvalued, the "premium/discount" will be over 1.0; otherwise, will be less than 1.0

## [License](/LICENSE.md)
