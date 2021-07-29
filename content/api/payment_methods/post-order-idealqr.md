---
weight: 315
meta_title: "API Reference - Create an iDEAL QR order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "iDEALQR",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "gateway_info": {
        "qr_size": 250,
        "allow_multiple": false,
        "allow_change_amount": true,
        "max_amount": 2000
        "min_amount": 500
    },
    "customer": {
        "locale": "nl_NL"
    }
}
```
> JSON Response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://testpayv2.multisafepay.com/connect/896rZ0IGzhJoP2XQdqzMtHYnIG32W68yAGX/?lang=nl_NL",
        "qr_url": "https://qrcode.ideal.nl/qrcode/15b6021c-0102-4ed2-84b3-4a99272179f7.png"
    }
}
```
{{< /code-block >}}

{{< description >}}
## iDEAL QR

Creates a iDEAL QR [redirect](/developer/api/difference-between-direct-and-redirect) order.

_Please note: If you would like to test iDEAL QR, please note that this will only work in a Live environment. The Testing environment is not available._

{{< alert-notice >}} Please keep in mind that in case min_amount is not set, the value of amount will be used as the min_amount and vice versa.
If max_amount is not set, the value of amount will be used as the max_amount for this transaction. In case both min_amount and max_amount are used, the value of amount will be disregarded. {{< /alert-notice >}}

- All fields must be completed correctly.

- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`, `direct`.  

----------------
__gateway__ | string

The unique gateway identifier to direct the customer straight to the payment method. To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: iDEALQR.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__gateway_info__ | object

----------------
__qr_size__ | integer

QR image size in pixels, default: 250 - Sizes are between 100 and 2000, if the value does not meet this rule, default is applied. 

----------------
__allow_multiple__ | boolean

With the allow multiple parameter you can specify if a single QR code should be able to be used more than just once.

----------------

__allow_change_amount__ | boolean

With the allow_change_amount_parameter you can specify if a customer should be able to change the amount to pay. Requires parameter max_amount or min_amount or both. Often used for donations.

----------------    
__min_amount__ | string

 With the min_amount you can specify what the minimum amount can be in case the allow_change_amount option is activated. The min_amount should not be bigger than the 'amount'. If only min_amount is used, the 'amount' should be more than the min_amount, therefore the 'amount' = max_amount. 

----------------    
__max_amount__ | string

 With the max_amount you can specify what the maximum amount can be in case the allow_change_amount option is activated. If only max_amount is used, the 'amount' should be less than the max_amount.

---------------- 

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

See also [iDEAL QR](/payments/methods/banks/idealqr).

{{< /description >}}
