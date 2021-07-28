# Project brief - SDV602
## Describe the data and the sorts of analysis you will undertake.

### The Data
Firstly the data i will be exploring is individual stock or crypto market data, which will allow anyone to view the stock data in an organised way in the form of charts/graphs so that the user may obtain a broader view of what is data is saying.

The data source i have in this directory, has a few headers that are used to obtain the data:

| Header | Description of data |
| ------ | ------------------- |
| Date | The date for current data instance |
| Open | The price of the stock at market open |
| High | Current high of the day or all time high |
| Low | Current low of the day or all time |
| Close | The price of the stock at last market close | 
| Adj Close | The adjusted value after the close ?|
| Volume | Current volume of shares being traded | 

I will use the date to compare each instance, and then i could use any of the opther headers as the x axis and i will be able to view a timeline of values according to the header name, excluding adj close and volume as i may use them for other things.

| Graph | Description | 
| ----- | ----------- |
|Bar | Will use this chart to map the open, high, low and close values, either all in one with different colors according to header names. |
| Line | Possibly be used to map the same above as well as looking at volume trajectories |


## Calculations 

I will need to calculate the highest of the open, high, low, close, adj close and volume, because there was alot of data but for testing sake i put a limit on the data to 15 by using the `[start:end]` i am able to split according to a start and end index position, append the above to the end of the variable name you would like to work with, so add a function that gets the highest within current range.

Volume: To find out how many people have traded this stock look at the volume and divide by 2 because theres a seller and a buyer per transaction. high volume means high liquidity, meaning you can quickly sell your stock because there are alot of people currently trading, whereas low volume there are less buyers and sellers in the market for this stock.

 	
