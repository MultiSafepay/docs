---
weight: 309
meta_title: "API Reference - Create a co-branded credit card order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /order

```json 
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "VISA",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test order description",
     "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "locale": "it_IT",
         "ip_address": "123.123.123.123"
    }
}
```
> JSON response

```json 

{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=it_IT"
  }
}
```

{{< /code-block >}}

{{< description >}}
## Co-branded credit cards 

- See also Payment methods:  
  - [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires)
  - [Dankort](/payments/methods/credit-and-debit-cards/dankort) 
  - [Postepay](/payments/methods/credit-and-debit-cards/postepay)  
- Redirect only.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `CREDITCARD`, `VISA`, `MASTERCARD`.

----------------
__currency__ | string | required

The currency you want the customer to pay in.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

**Note:** The co-branded card logo only displays if the locale is correctly supplied.

---------------- 

{{< /description >}}
