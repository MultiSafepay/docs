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
See also Payment methods – [iDEAL QR](/payments/methods/banks/idealqr).

- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Note:** The test environment is not available for iDEAL QR. You can only test transactions in the live environment. 

- If the `min_amount` parameter is not set, the `amount` value is used as the `min_amount` and vice versa.  
- If the `max_amount` parameter is not set, the `amount` is used as the `max_amount`.  
- If you set both `min_amount` and `max_amount` parameters, the `amount` value is ignored.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `redirect`, `direct`.  

----------------
__gateway__ | string

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `iDEALQR`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

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

The size of the QR image in pixels. Sizes are between 100 and 2000 pixels. If the value does not meet this rule, default is used.  
Default: 250.  

----------------
__allow_multiple__ | boolean

Set if a specific QR code can be used more than once.

----------------

__allow_change_amount__ | boolean

Set if customers can change the amount to pay. Often used for donations.  
Required parameters: `max_amount`, or `min_amount`, or both. 

----------------    
__min_amount__ | string

Set the minimum amount if `allow_change_amount` is set to `true`.  
The `min_amount` must not be more than the `amount`.  
If you only use `min_amount`, the `amount` must be more than the `min_amount`. That is, the `amount` = `max_amount`. 

----------------    
__max_amount__ | string

Set the maximum amount if `allow_change_amount option` is set to `true`.  
If you only use `max_amount`, the `amount` must be less than the `max_amount`.

---------------- 
__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

{{< /description >}}
