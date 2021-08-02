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
__type__ | string | required

The payment flow for the checkout process.    
Options: `redirect`, `direct`, `checkout`, `paymentlink`.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

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
__capture__ | string

A manual capture has been generated. 

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

The customer's IP address.   
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------

__close_window__ | bool | optional


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

See also [Manual Capture](/payments/features/manual-capture).
{{% /description %}}