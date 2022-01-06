---
weight: 208
meta_title: "API reference - Adjust payment link lifetime - MultiSafepay Docs"
aliases: 
    - /faq/api/lifetime-of-a-payment-link
    - /faq/api/adjusting-payment-link-lifetimes
    - /developer/api/adjusting-payment-link-lifetimes/
---
{{< code-block >}}
> POST - /orders

```json 

{
  "type":"redirect",
  "order_id":"test-123",
  "gateway":"",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "days_active":14,
  "second_chance":{
    "send_email":true
  },
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"en_US"
  }
  }
```
{{< /code-block >}}

{{< description >}}
### Adjust session lifetimes

The lifetime of a [payment link](/payments/checkout/payment-link/) to a [MultiSafepay payment page](/payment-pages/) is how long the customer can use the link to access the payment page and complete payment. 

The lifetime begins when the payment link is generated. A `session_id` is returned in the payment page URL. The default lifetime is 30 days, after which the link expires.

This applies to [redirect](/developer/api/difference-between-direct-and-redirect/) orders only.  

To cancel a payment link, see [Cancel an order](/api/#cancel-an-order).

{{< alert-notice >}} If you have [Second Chance](/features/second-chance/) enabled, we recommend a minimum lifetime of **48&nbsp;hours**.   
&nbsp;  
Second Chance emails the customer two payment reminders: 1 hour and 24 hours after the payment link was generated. If the payment link lifetime is less than 24 hours, the link in the second email is no longer active. {{< /alert-notice >}}

**Note:** Payment link lifetimes are different to [transaction expiration times per payment method](/developer/transaction-expiration/). 

**Parameters**

Include in the main body of your `POST /orders` request:

----------------

`days_active` | string | optional

Sets the number of days the payment link is active for.  
If not set, or if `seconds_active` is also set, `seconds_active` is used.  
If neither `days_active` nor `seconds_active` is set, the default is used.  

----------------
`seconds_active` | string | optional

Sets the number of seconds the payment link is active for.  
Example: 86,400 `seconds_active` = 1 `days_active`.  
If set and larger than 0, `seconds_active` overrides `days_active`.  
If neither `days_active` nor `seconds_active` is set, the default is used.  

----------------
`description` | string | optional

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

{{< /description >}}
