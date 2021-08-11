---
weight: 217
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#generating-a-payment-link
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


> JSON response


```json 
{
  "success":true,
  "data":{
    "order_id":"test-123",
    "payment_url":"https://devpayv2.multisafepay.com/connect/89QENbhQYcJoP2CO0kx6pSRrw8v2JFnTynr/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Generate payment links

Generate a payment link.  Your MultiSafepay account creates a unique transaction to match to the payment.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Fixed value: `paymentlink`.  
These orders are visible in your MultiSafepay account under **Tools** > **Payment link generator**.

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters. 

----------------
`gateway` | string | optional

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

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
`second_chance` | object | optional

Sends a payment reminder to the customer in the form of an email.

**Note:** Payment links no longer [send second chance emails](/api/#send-second-chance-emails) by default. You must include the Second Chance script in the JSON request as per the example request.

Contains:  

`send_email` | boolean | optional

- `true`: Sends a Second Chance email to the customer.  
- `false` or empty: No email reminder is sent.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{% /description %}}