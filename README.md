Small Gateway
=============


#### Capture
```shell
curl -X POST \
http://localhost:5000/api/v1/capture/ \
-H 'content-type: application/json' \
-H 'X-CLIENT: 1' \
-d '{
        "amount": 50.00,
        "buyer": {
            "name": "Will Smith",
            "email": "will.smith@example.com",
            "cpf": "93621378448"
        },
        "creditcard": {
            "holder_name": "Will Ferrell",
            "number": "4485114090992814",
            "expiration_date": "02/2050",
            "cvv": "850"
        }
    }'
```
