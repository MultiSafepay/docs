---
weight: 1370
---
{{< code-block >}}
> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "",
    "currency": "EUR",
    "amount": 0,
    "description": "Zero Authorization Test",
    "manual": false,
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "state": "NH",
        "country": "NL",
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0208500500",
        "email": "simonsmit@example.com",
        "referrer": "https://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```
> JSON Response


```json
{
  "success": true,
  "data": {
    "order_id": "My-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```
{{< /code-block >}}
{{< description >}}
## Zero Authorization

For a number of scenarios, it can be useful for our merchants to verify an account with Zero Authorization. An amount of zero will be reserved to check the authenticity of the card as well as establish an authorization to collect future payments. 

The _amount_ parameter should be set to 0.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.    
Options: `redirect`, `direct`, `checkout`, `paymentlink`.

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string. Required. (max. 50 chars).

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.    
Options: `True`, `False`. 

Read more about [Zero Authorization](/payments/features/zero-authorization) on our documentation page.
{{% /description %}}
