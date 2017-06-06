Stock
============

Returns some stock quotes, along with other information, from [Yahoo Finance](https://finance.yahoo.com/)

Properties
---------

-   **symbols**: List of stock tickers to get quotes for

Dependencies
------------
None

Commands
--------
None

Input
-----
None

Output
------
A list of signals, one per ticker. 

The following is an example of fields that are returned in each signal:

```
{  
  fields: {  
    change: string,
    chg_percent: double,
    day_high: double,
    day_low: double,
    issuer_name: string,
    name: string,
    price: double,
    type: string,
    utctime: datetime,
    year_high: double,
    year_low: double
  }
}
```
