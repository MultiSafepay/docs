---
weight: 224
meta_title: "API reference - Payment Component orders - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
>  POST - /orders

```json
{
  "order_id": 1018051,
  "type": "direct",
  "currency": "EUR",
  "amount": "100",
  "description": "Test order description",
  "customer": {
    "locale": "en_US",
    "reference": "Your customer reference"
  },
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel"
  },
  "payment_data": {
    "payload": "eyJnYXRld2F5IjoiSURFQUwiLCJjdXN0b21lciI6eyJicm93c2VyIjp7ImphdmFfZW5hYmxlZCI6MCwiamF2YXNjcmlwdF9lbmFibGVkIjoxLCJsYW5ndWFnZSI6ImVuLUdCIiwic2NyZWVuX2NvbG9yX2RlcHRoIjoyNCwic2NyZWVuX2hlaWdodCI6MTQ0MCwic2NyZWVuX3dpZHRoIjozNDQwLCJ0aW1lX3pvbmUiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV83KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTMuMC40NTc3LjYzIFNhZmFyaS81MzcuMzYiLCJjb29raWVzX2VuYWJsZWQiOjEsInBsYXRmb3JtIjoiTWFjSW50ZWwifSwibG9jYWxlIjoiZW5fVVMifSwiZmllbGRzIjp7ImV4dHZhcjgiOiIwMDMxIn0sImVuY3J5cHRlZCI6ZmFsc2UsImFwcGxpY2F0aW9uIjoiQVBJQ09OTkNPTVA6VjEifQ=="
  }
}
```

> JSON response

```json
{
  "success": true,
  "data": {
    "amount": 100,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": 0.44,
        "description": "0.44 For iDEAL Transactions",
        "transaction_id": 2856265,
        "type": "SYSTEM"
      }
    ],
    "created": "2021-09-24T12:09:28",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": null,
      "address2": null,
      "city": null,
      "country": null,
      "country_name": null,
      "email": "",
      "first_name": null,
      "house_number": null,
      "last_name": null,
      "locale": "en_US",
      "phone1": null,
      "phone2": "",
      "state": null,
      "zip_code": null
    },
    "description": "product description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2021-09-24T12:09:28",
    "order_id": "connect-comp614da3d8a00e8",
    "payment_details": {
      "account_holder_name": null,
      "account_iban": "https://testpayv2.multisafepay.com/simulator/ideal?trxid=2826044090080124&ideal=prob&issuerid=0031&merchantReturnURL=https%3A%2F%2Ftestpay%2Emultisafepay%2Ecom%2Fdirect%2Fcomplete%2F%3Fmspid%3D4990929",
      "account_id": null,
      "external_transaction_id": 2826044090080124,
      "issuer_id": "0031",
      "recurring_flow": null,
      "recurring_id": null,
      "recurring_model": null,
      "type": "IDEAL"
    },
    "payment_methods": [
      {
        "amount": 100,
        "currency": "EUR",
        "description": "product description",
        "external_transaction_id": 2826044090080124,
        "payment_description": "iDEAL",
        "status": "initialized",
        "type": "IDEAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 4990929,
    "var1": null,
    "var2": null,
    "var3": null,
    "payment_url": "https://testpayv2.multisafepay.com/simulator/ideal?trxid=2826044090080124&ideal=prob&issuerid=0031&merchantReturnURL=https%3A%2F%2Ftestpay%2Emultisafepay%2Ecom%2Fdirect%2Fcomplete%2F%3Fmspid%3D4990929"
  }
}
```

{{< /code-block >}}

{{< description >}}
## Payment Component orders

Create a [Payment Component](/payment-components/) order.

**Parameters**

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`

----------------
`currency` | string | required

The currency you want the customer to pay in.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | optional

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

`customer` | object | optional

See [customer (object)](/api/#customer-object).

----------------

`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`payment_data.payload` | string | required

The response to the `getPaymentData()` Payment Component method.

See Payment Component integration manual – Step 3: Create an order:

- [Single payment method](/payment-components/single/step-3/)
- [Multiple payment methods](/payment-components/multiple/step-3/)

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`fastcheckout` | string 

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`items` | object 

See [items (object)](/api/#items-object).

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`reason` | string

----------------
`related_transactions` | object

Information about linked transactions.

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data. 

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
