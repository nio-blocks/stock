Stock
=====
Returns some stock quotes, along with other information, from [Yahoo Finance](https://finance.yahoo.com/).

Properties
----------
- **include_query**: Whether to include queries in request to Yahoo Stocks.
- **polling_interval**: How often Yahoo Stocks is polled. When using more than one query. Each query will be polled at a period equal to the *polling interval* times the number of queries.
- **queries**: Queries to include on request to Yahoo Stocks.
- **retry_interval**: When a url request fails, how long to wait before attempting to try again.
- **retry_limit**: Number of times to retry on a poll.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: A list of signals, one per ticker.

Commands
--------
None

Dependencies
------------
None

Output Example
--------------
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

