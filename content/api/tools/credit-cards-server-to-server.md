---
weight: 1310
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

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
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "simonsmit@example.com",
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

```json
{
  "success": true,
  "data": {
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": ,
        "description": "",
        "transaction_id": 123456789
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
      "country_name": "The Netherlands",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033SC"
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
    "transaction_id": 123456789
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

__Please note: Server to Server must first be enabled by our Risk department. See also [activation](https://docs.multisafepay.com/tools/server2server/activate-server-to-server).__ 

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  Options: `direct`.  

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Option: VISA, MASTERCARD, AMERICAN EXPRESS, MAESTRO and CREDITCARD.

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
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

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
__customer__ | object | required

See [customer (object)](/api/#customer-object).

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

__close_window__ | bool | optional


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

See also [Server to Server](/payments/features/server-to-server).
{{% /description %}}