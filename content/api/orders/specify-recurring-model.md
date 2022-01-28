---
weight: 227
meta_title: "API reference - Specify recurring model - MultiSafepay Docs"

---

{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "gateway":"CREDITCARD",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "recurring_model":"unscheduled",
  "amount":10000,
  "description":"Tokenization - ALL - Original unscheduled",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "forwarded_ip":"",
    "first_name":"Simon",
    "last_name":"Smit",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "birthday":"1970-07-10",
    "gender":"mr",
    "phone":"0208500500",
    "email":"simonsmit@example.com",
    "referrer":"https://example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "reference":"AutoQAReference"
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
  }
}
```

{{< /code-block >}}


{{< description >}}

### Specify recurring model

Create an initial [recurring payment](/features/recurring-payments) order using a specific recurring model:

- **Card on file (COF)**: The cardholder has authorized you to store their card details.
- **Subscription**: Agreement or services that are billed at the end of your billing cycle.
- **Unscheduled**: Event triggered for application, e.g. a mobile top-up when no credit is left on the phone.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`.     

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.    

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`recurring_model` | string | required

The [recurring model](/features/recurring-payments/#recurring-models).  
Options: `unscheduled`, `subscription`, `cardonfile`.  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10     

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).  
Format: Maximum 200 characters.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/glossaries/multisafepay-glossary/#issuer), or the payment method.

----------------


{{< /description >}}
