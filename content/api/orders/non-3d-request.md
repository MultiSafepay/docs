---
weight: 230
meta_title: "API reference - 3D disabled or non-3D requests - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"direct",
  "gateway":"CREDITCARD",
  "order_id":"order-1",
  "currency":"EUR",
  "amount":1000,
  "description":"product description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123"
  },
  "gateway_info":{
    "card_number":"4111111111111111",
    "card_holder_name":"Holder Name",
    "card_expiry_date":"1612",
    "card_cvc":"123"
  }
}
```
> JSON response    
> When no 3D verification is required, the [transaction status](/about-payments/multisafepay-statuses/) response will be processed directly and no form will be sent.

```json 
{
  "success":true,
  "data":{
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

The unique gateway identifier for the payment method.  
Value: `CREDITCARD`. 

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | required

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
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
Format: YYMM

`card_cvc` | string

The card verification code (CVC) is a 3 or 4 digit number used as an additional security feature for card-not-present transactions.  
For some cards, like MAESTRO, this may not be required.  
CVC is also not required for recurring transactions.

----------------

{{% /description %}}
