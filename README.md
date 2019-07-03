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

When command input window appearrs, please input the following values as real numbers only without any symbols:

1. Price Per Share in USD
2. Shares Outstanding in Millions
3. The Risk Free Rate as a decimal
4. The Beta
5. Current Equity Risk Premium as a decimal. Note this can be obtained at: http://pages.stern.nyu.edu/~adamodar/
6. Initial Free Cash Flow to Equity in Millions
7. 5 Year Growth Rate as a decimal. Note that this can be estimated from the CAGR of the previous five years or as a projection from own fundamental analysis
8. Terminal Growth Rate as a decimal. Note that either a weighted average GDP long term growth rate can be used or if highly U.S. based, the long term U.S. GDP growth rate of 2.0-2.5%.

To exit the program, please click on "Close Window". 

Click on "Confirm Inputs" 
To confirm that inputs were correctly registered by the program, the shares outstanding and risk free rate values should be displayed under the "Confirmation Inputs:" column. 

A New window should open with the valuations. The Valuation window should contain the Cost of Equity as a percentage and the various calcualted values. The most important output is the Premium/Discount. The calculation is simply:

```py
Value per Share / Price per Share
```
therefore,

a value > 1.0 indicates overvaluation
a value < 1.0 indicated undervaluation

Once the outputs are noted, click "Quit" to close all windows. 

If any mistakes were made or any assumptions were changed, the new values may be input into the first window. When "Confirm Inputs" is clicked, a new window with the new calculated values will be opened. There is no need to re-execute the program from the command prompt. 

## Recommendation
If the stock is overvalued, the "premium/discount" will be over 1.0; otherwise, will be less than 1.0

## [License](/LICENSE.md)
