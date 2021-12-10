---
weight: 323
meta_title: "API reference - Create an iDEAL QR order - MultiSafepay Docs"

---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "gateway":"iDEALQR",
  "currency":"EUR",
  "amount":1000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "gateway_info":{
    "qr_size":250,
    "allow_multiple":false,
    "allow_change_amount":true,
    "max_amount":2000,
    "min_amount":500
  },
  "customer":{
    "locale":"nl_NL"
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://testpayv2.multisafepay.com/connect/896rZ0IGzhJoP2XQdqzMtHYnIG32W68yAGX/?lang=nl_NL",
    "qr_url":"https://qrcode.ideal.nl/qrcode/15b6021c-0102-4ed2-84b3-4a99272179f7.png"
  }
}
```
{{< /code-block >}}

{{< description >}}
### iDEAL QR

- See also Payment methods – [iDEAL QR](/payments/methods/banks/idealqr).  
- Redirect only.

**Note:** The test environment is not available for iDEAL QR. You can only test transactions in the live environment. 

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway identifier for the payment method.  
Value: `iDEALQR`.

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

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

`qr_size` | integer

Sets the size of the QR image in pixels. Sizes are between 100 and 2000 pixels. If the value does not meet this rule, default is used.  
Default: 250.  

`allow_multiple` | boolean  

True: The QR code can be used more than once.  
False: The QR code can only be used once.

`allow_change_amount` | boolean

True: The customer can change the amount to pay.  
False: The customer cannot change the amount the pay.    
Required parameters: `max_amount`, or `min_amount`, or both.  

`min_amount` | string | required if `allow_change_amount` is set to `true`

Sets a minimum amount that the customer can pay.     

- The `min_amount` must be lower than the `amount`.  
- If `min_amount` is not set, but `max_amount` is set, then the `amount` value is used as the `min_amount`. 
    
`max_amount` | string | required if `allow_change_amount` is set to `true`

Sets a maximum amount that the customer can pay.    

- The `max_amount` must be higher than the `amount`.  
- If `max_amount` is not set, but `min_amount` is set, then the `amount` value is used as the `max_amount`.  

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`qr_url` | string 

The URL of the QR code.

---------------- 


{{< /description >}}
