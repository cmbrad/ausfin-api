# Australian Personal Finance API

This repository is intended to expose a HTTP API for retrieving balance data over time, scraped from financial accounts.
This data is intended to be consumed by charting libraries.

```json
{
    "id": 1,
    "created_at": 123213213313,
    "events": [
        {
            "source": {
                "name": "btcmarkets",
                "tags": ["investment", "cryptocurrency"]
            },
            "balance": 9999.99
        },
        {
            "source": {
                "name": "commbank",
                "tags": ["investment", "shares"]
            },
            "balance": 9999.99
        },
        {
            "source": {
                "name": "ubank",
                "tags": ["bank", "cash"]
            },
            "balance": 9999.99
        }
    ]
}
```
