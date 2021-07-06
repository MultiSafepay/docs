---
weight: 260
meta_title: "API Reference - Retrieve an order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> GET - /orders/{order_id}


> JSON Response

```json
{
  "success": true,
  "data": {
    "transaction_id": 123456789
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
      "first_name": "Simon",
      "last_name": "Smit",
      "address1": "Kraanspoor",
      "address2": "",
      "house_number": "39C",
      "zip_code": "1033SC",
      "city": "Amsterdam",
      "state": "NH",
      "country": "NL",
      "country_name": "The Netherlands",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "email": "simonsmit@example.com"
    },
    "payment_details": {
      "recurring_id": 133761993_gTp2,
      "type": "VISA",
      "account_id": null,
      "account_holder_name": "Testperson-nl Approved",
      "external_transaction_id": 906015000050,
      "last4": "1234",
      "card_expiry_date": 1904
    },
    "costs": [
      {
        "transaction_id": 123456789
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
        "transaction_id": 123456789
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

**Parameters**

----------------

__order_id__ | integer / string

The unique identifier of the order to be returned. If the values are only numbers the type will be integer, otherwise it will be string.                                      


{{% /description %}}
