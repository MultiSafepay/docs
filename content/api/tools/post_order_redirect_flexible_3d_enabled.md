---
weight: 1350
---
{{< code-block >}}
> POST - /orders 

```json


{
   "type": "redirect",
   "gateway": "MASTERCARD",
   "order_id": "my-order-id-01",
  "currency": "EUR",
   "amount": 100,
   "description": "test product description",
   "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
   }, 
   "customer": {
       "locale": "nl_NL",
       "ip_address": "123.123.123.123",
       "first_name": "Simon",
       "last_name": "Smit",
       "address1": "Kraanspoor",
       "house_number": "39C",
       "zip_code": "1033SC",
       "city": "Amsterdam",
       "country": "NL",
       "email": "simonsmit@example.com",
       "referrer": "http://example.com",
       "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
   "gateway_info": {
       "flexible_3d": true,
       "term_url": "http://example.com/?type=term&api_key=<api_key>"
        
   }
}
```

> JSON Response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-01",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
{{< /code-block >}}

{{< description >}}
### Redirect, Flexible 3D set on _true_ 

It is mandatory to enable Flexible [3D Secure(/faq/general/glossary/#3d-secure) processing in this call, even when Dynamic 3D rules could set the settings to disable it.

Flexible 3D is a feature that allows you to enable/disable 3D Secure at API level. The Flexible 3D mandates whether or not a transaction should be completed with the 3D Secure verification or not.

When Flexible 3D is set on _true_, the authentication verification is mandatory to finalize and release a successful payment. Credit card transactions which are processed without the 3D Secure protocol, are now required to complete the 3D Secure verification. Activating Flexible 3D Secure will override the rules of the Dynamic 3D settings, meaning that the payment will be enrolled with a 3D Secure authentication. 

**__Please note__: MultiSafepay no longer supports [Flexible 3D](https://docs.multisafepay.com/tools/flexible_3d) with merchants based in Europe due to PSD2 regulations.**

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`.

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Option: VISA and MASTERCARD. 

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
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`. 

----------------
__ip_address__ | string

The customer's IP address.   
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------
__first_name__ | string

The customer’s first name. 

----------------
__last_name__ | string

The customer’s last name.

----------------
__address1__ | string

The first line of the customer's address.

----------------
__house_number__ | string

First line of The customer's house number.

----------------
__zip_code__ | string

First line of customer’s provided zip_code / postal code.

----------------
__city__ | string

The customer's city of residence. 

----------------
__country__ | string

The customer’s country of residence.   
Format: [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html). 

----------------
__phone__ | string

The customer's phone number. 

----------------
__email__ | string

The customer’s email address.   
Used to send Second Chance emails and to conduct fraud checks.  

----------------
__gateway_info__ | object

----------------
__flexible_3d__ | boolean

True, enable the 3D Secure authentication. False, disable the 3D Secure authentication.

----------------
__term_url__ | string

URL that is used to instruct the card issuer where to redirect the authorisation query. 

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.    
Options: `True`, `False`. 

----------------

{{% /description %}}
