---
weight: 604
meta_title: "API Reference - Tokenization - Original transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

> POST - /orders

```json
{
        "type": "redirect",
        "gateway": "CREDITCARD",
        "order_id": "my-order-id-1",
        "currency": "EUR",
        "recurring_model": "unscheduled",
        "amount": 10000,
        "description": "Tokenization - ALL - Original unscheduled",
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
                "house_number": "39C",
                "zip_code": "1033SC",
                "city": "Amsterdam",
                "country": "NL",
                "birthday": "1970-07-10",
                "gender": "mr",
                "phone": "0208500500",
                "email": "simonsmit@example.com",
                "referrer": "http://example.com",
                "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "reference": "AutoQAReference"
        }
}
```
> JSON response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```

{{< /code-block >}}


{{< description >}}

### Original Tokenization transaction

This API call allows you to create an original order using a specific recurring model.

MultiSafepay offers the following recurring models: 

1. __Card on file (COF)__: transaction where a cardholder authorized a merchant to store the cardholder's details 

2. __Subscription__: agreement or services that are billed at the end of a merchant’s billing cycle

3. __Unscheduled__: event triggered for application (for example a mobile top up when no credit is left on the phone)




- All of the following parameters are required fields.

**Parameters**

__type__ | string | required

The payment flow for the checkout process. Options: `direct`, `redirect`.     

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method. To retrieve gateway IDs, see [Gateways](/api/#gateways). E.g. CREDITCARD.

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
__recurring_model__ | string

The function of the recurring model e.g. Card on file, Subscription, Unscheduled.

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.     

----------------
__description__ | string | required

A text which will be shown with the order in your MultiSafepay account. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is **not** supported. Use the ‘items’ or ‘shopping_cart’ objects for this.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).                                

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails. 

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------
Read our decicated documentation on [Tokenization](https://docs.multisafepay.com/payments/features/tokenization)

__close_window__ | bool | optional


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

{{< /description >}}
