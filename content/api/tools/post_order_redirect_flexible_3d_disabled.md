---
weight: 1340
---
{{< code-block >}}
> POST - /orders

```shell

{
   "type": "redirect",
   "gateway": "VISA",
   "order_id": "my-order-id-1",
   "currency": "EUR",
   "amount": 100,
   "description": "test product description",
   "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
   }, 
   "customer": {
       "locale": "nl_NL",
       "ip_address": "10.1.5.1",
       "first_name": "Testperson-nl",
       "last_name": "Approved",
       "address1": "Kraanspoor",
       "house_number": "39",
       "zip_code": "1033SC",
       "city": "Amsterdam",
       "country": "NL",
       "email": "test@example.com",
       "referrer": "http://example.com",
       "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
   },
   "gateway_info": {
       "flexible_3d": false,
       "term_url": "http://example.com/?type=term&api_key=<api_key>"
   }
}
```

> JSON Response


```shell 
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
### Redirect, Flexible 3D set on _false_

Flexible 3D is a feature that allows you to enable/disable 3D secure at API level. The Flexible 3D mandates whether or not a transaction should be completed with the 3D secure verification or not.

Credit card transactions which are processed with the 3D Secure protocol require a form of authentication of the customer during the payment process. Setting Flexible 3D to _false_ will disable the verfication process. 

**Activating Flexible 3D secure will override the rules of the Dynamic 3D settings, meaning that payments will not be enrolled with a 3D authentication.**



| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type                           | string    | Specifies the payment flow for the checkout process. Options: redirect.       |
| gateway                        | string    | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: VISA and MASTERCARD. |
| order_id                       | integer / string    | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                  |
| currency                       | string    | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                         | integer   | The amount (in cents) that the customer needs to pay.        |
| description                    | string    | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                | object    | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/)         |
| customer                       | object    |  |
| locale                         | string    | Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 
| ip_address                     | string    | The IP address of the customer. “Required” with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field.  [More info](/faq/api/ip_address/) | 
| first_name                     | string    | The customer’s first name.                   |
| last_name                      | string    | The customer’s last name.                    |
| address1                       | string    | First line of customer’s provided address.   |
| house_number                   | string    | Customer’s provided house number.            |
| zip_code                       | string    | Customer’s provided zip / postal code.       |
| city                           | string    | Customer’s provided city.                    |
| country                        | string    | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) |
| phone                          | string    | Customer’s provided phone number.            |
| email                          | string    | Customer’s provided email address. Used to send Second Chance emails and in fraud checks.   |
| gateway_info                   | object    |  |
| flexible_3d                    | boolean   | True, enable the 3D secure authentication. False, disable the 3D secure authentication.  |
| term_url                       | string    | URL that is used to instruct the card issuer where to redirect the authorisation query. |

{{% /description %}}