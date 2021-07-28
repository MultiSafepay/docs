---
weight: 1350
---

{{< code-block >}}
> POST - /orders 

```json
{
    "type": "redirect",
    "order_id": "order_id_0000001",
    "gateway": "",
    "currency": "EUR",
    "amount": 10000,
    "description": "Manual Capture Test",
    "capture": "manual",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
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
        "order_id": "order_id_0000001",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
{{< /code-block >}}
{{< description >}}
## Manual Capture Authorization

Manual Capture is a feature that allows payments to be captured once an order has been shipped or received. The API calls mandate whether a transaction should be captured partially or fully, as well as the authorization and cancellation of the transaction.

The feature can only be used with specific credit card payment methods including MasterCard, VISA and Maestro.

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

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string. Required. Max 50 char.

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
__capture__ | string

A manual capture has been generated. 

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

The customer's IP address.   
**Required** for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods because MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address).

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

Read more about [Manual Capture](/payments/features/manual-capture) on our documentation page.
{{% /description %}}