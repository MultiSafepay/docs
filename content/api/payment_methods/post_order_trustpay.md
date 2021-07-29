---
weight: 327
meta_title: "API Reference - Create a TrustPay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "CZK",
    "amount": 1000,
    "gateway": "TRUSTPAY",
    "description": "Test Order Description",
    "custom_info": {},
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "email": "simonsmit@example.com"
        "locale": "cs_CZ"
    }
}
```

> JSON Response


```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=en_CZ"
  }
}
```
{{< /code-block >}}

{{< description >}}
## TrustPay
See also [TrustPay](/payments/methods/banks/trustpay).

- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `redirect`.  

----------------
__gateway__ | string

The unique gateway identifier.  
Options: `TRUSTPAY`.

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
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
See also [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object 

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__email__ | string   

The customer’s email address.  
Used for sending Second Chance and bank transfer emails, and for conducting fraud checks.                              

----------------
__locale__ | string   

Displays the correct language and payment methods on the payment page, and influences sending email templates.  Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).                         

----------------

__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`.

{{< /description >}}
