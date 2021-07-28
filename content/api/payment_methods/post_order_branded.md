---
weight: 309
meta_title: "API Reference - Create a Co-branded Credit Card order - MultiSafepay Docs"
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
    "description": "Test Order Description",
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
> JSON Response

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
## Co-branded credit card 

Creates a Co-branded credit card [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct , redirect , paymentlink.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: CREDITCARD, VISA and MASTERCARD.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

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
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

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

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

 The desired logo of a Co-branded credit card will only be shown if the locale is correctly supplied in a transaction request. 

Please make sure to read more about [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires), [Dankort](/payments/methods/credit-and-debit-cards/dankort) and [Postepay](/payments/methods/credit-and-debit-cards/postepay) on our documentation page.
{{< /description >}}
