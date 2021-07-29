---
weight: 1310
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
  "type": "direct",
  "gateway": "CREDITCARD",
  "order_id": "order-1",
  "currency": "EUR",
  "amount": 1000,
  "description": "product description",
  "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123"
  },
  "gateway_info": {
    "card_number": "4111111111111111",
    "card_holder_name": "Holder Name",
    "card_expiry_date": "1612",
    "card_cvc": "123"
  }
}
```

> JSON Response     
> When [3D Secure](/faq/general/multisafepay-glossary/#3d-secure) verification is required, the HTML form will be returned and should be rendered.

```json
"customer_verification": {
     "html": "<html>\n<head>\n<title>3D Html form</title>....",
     "type": "form" 
}
```
{{< /code-block >}}

{{< description >}}
## Server to Server API Calls
### 3D Enabled Request

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  Options: `direct`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Option: VISA, MASTERCARD, AMERICAN EXPRESS, MAESTRO and CREDITCARD. 

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
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------
__ip_address__ | string

The customer's IP address.   
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------
__gateway_info__ | object

----------------
__card_number__ | string

Full credit card number.

----------------
__card_holder_name__ | string

Name on the credit card.

----------------
__card_expiry_date__ | string

Card expiry date.

----------------
__card_cvc__ | string

Card CVC (Card Verification Code) number is a 3 or 4 digit code used as an additional security feature for card not present transactions. For some cards like MAESTRO, this may not be required. CVC is also not required for recurring transactions.

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

See also [Server to Server](/payments/features/server-to-server).
{{% /description %}}

