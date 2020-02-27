---
weight: 260
meta_title: "API - Retrieve an order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> GET - /orders/{order_id}


> JSON Response

```shell
{
  "success": true,
  "data": {
    "transaction_id": 258655825,
    "order_id": "{order_id}",
    "created": "2019-03-01T16:12:47",
    "currency": "EUR",
    "amount": 200,
    "description": "Test Order Description",
    "var1": null,
    "var2": null,
    "var3": null,
    "items": null,
    "amount_refunded": 200,
    "status": "refunded",
    "financial_status": "completed",
    "reason": "Successful approval/completion",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-01T16:13:14",
    "customer": {
      "locale": "nl_NL",
      "first_name": "Testperson-nl",
      "last_name": "Approved",
      "address1": "Kraanspoor",
      "address2": null,
      "house_number": "39",
      "zip_code": "1033 SC",
      "city": "Amsterdam",
      "state": null,
      "country": "NL",
      "country_name": null,
      "phone1": "020 8500 500",
      "phone2": "",
      "email": "test@example.com"
    },
    "payment_details": {
      "recurring_id": "{Recurring_id}",
      "type": "VISA",
      "account_id": null,
      "account_holder_name": "Testperson-nl Approved",
      "external_transaction_id": 906015000050,
      "last4": "1234",
      "card_expiry_date": 1904
    },
    "costs": [
      {
        "transaction_id": 258656087,
        "description": "Refund order 258655825 for TEST TEST",
        "type": "internal",
        "status": "completed",
        "created": "2019-03-01T16:14:02",
        "amount": 0.19
      }
    ],
    "related_transactions": [
      {
        "amount": 200,
        "costs": [
          {
            "amount": 19,
            "currency": "EUR",
            "description": "EURO 0.19 per refund",
            "status": "reserved",
            "type": "SYSTEM"
          }
        ],
        "created": "2019-03-01T16:14:02",
        "currency": "EUR",
        "description": "Refund order 258655825 for TEST TEST",
        "modified": "2019-03-01T16:14:02",
        "status": "completed",
        "transaction_id": 258656087
      }
    ],
    "payment_methods": [
      {
        "account_holder_name": "Testperson-nl Approved",
        "amount": 200,
        "card_expiry_date": 1904,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": 906015000050,
        "last4": 1234,
        "payment_description": "Visa",
        "status": "completed",
        "type": "VISA"
      }
    ]
  }
}
```
{{< /code-block >}}

{{< description >}}
## Retrieve an order

Get order status & information. Depending on the order type or method, the structure may be different.

| Parameter          | Type      | Description                                                                                         |
|--------------------|-----------|-----------------------------------------------------------------------------------------------------|
| order_id           | integer / string    | The unique identifier of the order to be returned. If the values are only numbers the type will be integer, otherwise it will be string.                                                  |

{{% /description %}}
