---
weight: 312
meta_title: "API Reference - Create an Edenred order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - / order 


```json 
{
  "type":"redirect",
  "order_id":"my-order-id",
  "gateway":"EDENCO",
  "currency":"EUR",
  "amount":100,
  "description":"Test order description",
  "manual":false,
  "payment_options": {
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "settings": {
      "gateways": {
        "coupons": {
          "allow": [
            "EDENECO"
                    ],
          "disabled": false
                }
            }
        }
    },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "country":"NL",
    "email":"simonsmit@example.com"
  }
}
```

> JSON response
```json 
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```  
{{< /code-block >}}

{{< description >}}
## Edenred

- See also Payment methods – [Edenred](/payments/methods/prepaid-cards/edenred).  
- Redirect only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
`order_id` | string | required

Your unique identifier for the order.  
Format: Maximum 50 characters.

----------------
`gateway` | string | optional

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  

Options:  
`EDENCOM` = Ticket Compliments  
`EDENECO` = Ticket EcoCheque  
`EDENRES` = Ticket Restaurant  
`EDENSPORTS` = Ticket Sport & Culture  

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
`manual` | string | required

Fixed value: `false`.

----------------
`payment_options` | object | required

To manage which vouchers are offered to the customer.

For more information, see [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}