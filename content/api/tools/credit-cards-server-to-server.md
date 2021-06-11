---
weight: 1310
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```shell

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "CREDITCARD",
    "description": "product description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "example@multisafepay.com",
        "referrer": "http://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "gateway_info": {
        "card_number": "5555555555554444",
        "card_holder_name": "MasterCard-Test-Order",
        "card_expiry_date": "2512",
        "card_cvc": "123"
    }
}
```

> JSON Response

```shell
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": ,
        "description": "",
        "transaction_id": 2056142,
        "type": "SYSTEM"
      }
    ],
    "created": "2020-01-28T09:01:07",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": Netherlands,
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": "39C",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033 SC"
    },
    "description": "product description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-28T09:01:07",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": "MasterCard-Test-Order",
      "account_id": null,
      "card_expiry_date": 2512,
      "external_transaction_id": "6652390295520298",
      "last4": 4444,
      "recurring_id": null,
      "recurring_model": null,
      "type": "MASTERCARD"
    },
    "payment_methods": [
      {
        "account_holder_name": "Testperson-nl",
        "amount": 1000,
        "card_expiry_date": 2512,
        "currency": "EUR",
        "description": "Product Description",
        "external_transaction_id": "6652390295520298",
        "last4": 4444,
        "payment_description": "MasterCard",
        "status": "initialized",
        "type": "MASTERCARD"
      }
    ],
    "reason": "3D Secure Authorization",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 4034377,
    "customer_verification": {
      "type": "form",
      "html": "",
    },
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL",
    "cancel_url": "http://www.example.com/client/notification?type=cancel"
  }
}
```

{{< /code-block >}}

{{< description >}}

### Credit Cards Server to Server

This is a standard credit card API [direct order request](https://docs.multisafepay.com/api/#creates-a-direct-order) The gateway has been set to __CREDITCARD__. In this case, the type of credit card will be detected based on the first four digits.

__Please note: Server to Server must first be enabled by our Risk department. Read more about [activation](https://docs.multisafepay.com/tools/server2server/activate-server-to-server) on our documentation page.__ 

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