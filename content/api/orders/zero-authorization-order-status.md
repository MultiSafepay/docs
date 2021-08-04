---
weight: 239
meta_title: "API Reference - Get zero authorization order details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#order-status
---
{{< code-block >}}
> GET - /orders/<order_id>

> JSON response


```json
{
  "success": true,
  "data": {
    "amount": 0,
    "amount_refunded": 0,
    "costs": [],
    "created": "2019-10-17T10:44:59",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "address2": "",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": "The Netherlands",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "state": "NH",
      "zip_code": "1033SC"
    },
    "description": "MultiSafepay Test",
    "fastcheckout": "NO",
    "financial_status": "completed",
    "items": null,
    "modified": "2019-09-17T10:44:59",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": "MultiSafepay",
      "account_id": null,
      "card_expiry_date": 4412,
      "external_transaction_id": 234374824,
      "last4": 1111,
      "recurring_id": "57876598769",
      "recurring_model": null,
      "type": "VISA"
    },
    "payment_methods": [
      {
        "account_holder_name": "MultiSafepay",
        "amount": 9743,
        "card_expiry_date": 2203,
        "currency": "EUR",
        "description": "MultiSafepay Test",
        "external_transaction_id": 234374824,
        "last4": 0,
        "payment_description": "Visa CreditCards",
        "status": "completed",
        "type": "VISA"
      }
    ],
    "reason": "Successful approval/completion",
    "reason_code": "",
    "related_transactions": null,
    "status": "completed",
    "transaction_id": 123456789
    "var1": null,
    "var2": null,
    "var3": null
  }
}
```
{{< /code-block >}}
{{< description >}}
### Get zero authorization order details

**Parameter**

----------------
`order_id` | string / integer

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment_methods-object).

----------------

{{% /description %}}