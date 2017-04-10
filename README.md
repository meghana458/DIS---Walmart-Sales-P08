# DIS Walmart Weekly Sales - P08

### Team Members 

  - Harika Malempati
  - Meghana Thakkellapati

### Project Summary

  - We will be using Walmart Store transactions as our data set
  - We are working on total weekly sales for a Store, based on whether it is working day or holiday

#### Describe your data source
Our data source is train.txt, which is structured data. It contains 5 fields named Store, Dept, Date, Weekly_Sales and IsHoliday. It is of size 12.2MB.

##### Link to your original data source: 
  https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data

#### What makes it a big data problem? (Use the Vs of Big Data)
Volume:  Volume of the data set is 12.2 MB. There are 4,21,570 records.
Variety:  It is a structured data. Data is stored in text file
Velocity:  This is historical training data that covers to 2010-02-05 to 2012-11-01
Veracity:  Data is formatted/cleaned and it is trustworthy
Value:  The weekly sales for holidays week is much higher than non-holidays week

#### Map Reduce problems in the format "for each _(key)_ , we will find the _(value)__".
```sh
$ For each store, calculate the total weekly sales for a store, during Non-holiday week
$ For each store, calculate the total weekly sales for a store, during holiday week
```

#### Mapper input:  show one line of data that your mapper will read.
```sh
 45  98  9/7/2012  352.44  TRUE 
```

#### Mapper output / Reducer input:

| Store | Sales | Holidays |
| ------ | ------ | ------ |
| 45 | 874.64 | FALSE |
| 45 | 713.5 | FALSE | 
| 45 | 856.35 | FALSE |
| 45 | 622.62 | FALSE |
| 45 | 690.52 | FALSE | 
| 45 | 659.65 | FALSE | 
| 45 | 695.21 | FALSE | 
| 45 | 845.3 | FALSE | 
| 45 | 657.63|  FALSE | 
| 45 | 516.46 | FALSE | 
| 45 | 727.49 | FALSE | 
| 45 | 500.16| FALSE | 
| 45 | 415.4 | FALSE | 
| 45 | 346.04 | FALSE | 
| 45 | 352.44 | TRUE | 
| 45 | 605.96 | FALSE | 
| 45 | 467.3 | FALSE | 
| 45 | 508.37 | FALSE | 
| 45 | 628.1 | FALSE | 
| 45 | 1061.02 | FALSE | 
| 45 | 760.01 | FALSE | 
| 45 | 1076.8 | FALSE | 

#### Reducer output:
| Store | salesTotal |
| ------ | ------ |
| 1 |       204698042.21 |
| 10 |       250480154.4 | 
| 11 |      179425100.56 | 
| 12  |     132903627.48 | 
| 	13    |   265315234.99 | 
| 14  |     267760953.96 | 
| 15  |     82066133.08 | 
|  16 |      68577726.41 | 
| 17  |     117983559.02 | 
| 18 |      143417157.55 | 
| 19  |     190861645.46 | 
| 2  |      254573651.79 | 
| 	20  |     278898551.11 | 
|	21 |      99851249.85 | 
| 22  |     136214253.96 | 
| 23  |     184094132.34 | 
|  24 |      179253679.01 | 
| 25  |     93664410.75 | 
| 	26   |    132668891.18 | 
| 	27  |     234924536.03 | 
| 	28    |   174481234.53 | 
| 	29  |     71070240.61 | 
| 3   |     53204556.95 | 

#### Language:
We used Python for Map Reduce coding

##### Process:  Will your processing be numeric, or will you need text processing and/or cleaning?
Our Processing is numeric. We will be calculating the total sales for a store during holidays and Non-holidays. We don’t need any data cleaning.
