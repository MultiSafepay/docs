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

Specifies the payment flow for the checkout process. Options: direct.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: VISA, MASTERCARD, AMERICAN EXPRESS, MAESTRO and CREDITCARD. 

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

----------------
__locale__ | string

Displays the correct language and payment methods on the Payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US.

----------------
__ip_address__ | string

The IP address of the customer. “Required” with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field.  [More info](/faq/api/ip_address)

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


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

Read more about [Server to Server](/tools/server2server) on our documentation page.
{{% /description %}}