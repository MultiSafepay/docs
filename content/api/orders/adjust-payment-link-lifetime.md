---
weight: 208
meta_title: "API reference - Adjust payment link lifetime - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
aliases: 
    - /faq/api/lifetime-of-a-payment-link
    - /faq/api/adjusting-payment-link-lifetimes
    - /developer/api/adjusting-payment-link-lifetimes/
---
{{< code-block >}}
> POST - /orders

```json 

{
  "type":"paymentlink",
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
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"en_US"
  }
  }
```
{{< /code-block >}}

{{< description >}}
### Adjust payment link lifetimes

The lifetime of [payment links](/payments/checkout/payment-link/) for MultiSafepay payment pages is how long the link remains valid for the customer to complete payment. This applies to [redirect](/developer/api/difference-between-direct-and-redirect/) orders only. The default is 30 days, after which the link expires. Except for:  

- [Bank Transfer](/payments/methods/banks/bank-transfer/): 60 days
- [PayPal](/payments/methods/wallet/paypal/): 14 days
- [Post-payment methods](/payments/methods/billing-suite/): You cannot adjust payment link lifetimes.

To cancel a payment link, see [Cancel an order](/api/#cancel-an-order).

**Second Chance**  
You cannot edit payment links in [Second Chance](/payments/boost/second-chance/) emails, because the `session_id` of the initial transaction has already been used. You can only edit the link in the initial `POST /orders` request. 

If set for under 24 hours:  

- `days_active`: The payment link displays an error message when opened.
- `seconds_active`: The second email is still sent, even though the payment link it contains is no longer valid. This can't be changed.  

**Parameters**

Include in the main body of your `POST /orders` request:

----------------

`days_active` | string | optional

The number of days the payment link is valid for.  
If not set, or if `seconds_active` is also set, `seconds_active` is used.  
If neither `days_active` nor `seconds_active` is set, the default is used.  
Default: 30 days.

----------------
`seconds_active` | string | optional

The number of seconds the payment link is valid for.  
Example: 86.400 `seconds_active` = 1 `days_active`.  
If set and larger than 0, `seconds_active` overrides `days_active`.  
If neither `days_active` nor `seconds_active` is set, the default is used.  
Default: 30 days. 

----------------
`description` | string | optional

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).  
Format: Maximum 200 characters.  
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

{{< /description >}}
