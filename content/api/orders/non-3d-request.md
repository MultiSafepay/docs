---
weight: 227
meta_title: "API Reference - 3D disabled or non-3D requests - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#3d-disabled-or-non-3d-transaction
---
{{< code-block >}}

> POST - /orders

```json

{
  "type": "direct",
  "gateway": "CREDITCARD",
  "order_id": "order-1",
  "currency": "EUR",
  "amount": 1000,
  "description": "product description",
  "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123"
  },
  "gateway_info": {
    "card_number": "4111111111111111",
    "card_holder_name": "Holder Name",
    "card_expiry_date": "1612",
    "card_cvc": "123"
  }
}
```
> JSON response    
> When no 3D verification is required, the [transaction status](/payments/multisafepay-statuses/) response will be processed directly and no form will be sent.

```json 
{
    "success": true,
    "data": {
        ...
    }
}
```
{{< /code-block >}}

{{< description >}}
### 3D disabled or non-3D requests

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `CREDITCARD`. 

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`gateway_info` | object

Contains:  

`card_number` | string

The customer's full credit card number.

`card_holder_name` | string

The name of the cardholder on the credit card.

`card_expiry_date` | string

The expiry date on the credit card.

`card_cvc` | string

The card verification code (CVC) is a 3 or 4 digit number used as an additional security feature for card-not-present transactions.  
For some cards, like MAESTRO, this may not be required.  
CVC is also not required for recurring transactions.

----------------

{{% /description %}}