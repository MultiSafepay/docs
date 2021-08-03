---
weight: 1304
meta_title: "API Reference - Direct: Flexible 3D set to false - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#direct-flexible-3d-set-on-_false_
---
{{< code-block >}}
> POST - /orders 

```json 

{
   "type": "direct",
   "gateway": "VISA",
   "order_id": "my-test-order-01",
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
       "phone": "0208500500",
       "email": "simonsmit@example.com",
       "referrer": "http://example.com",
       "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
   },
   "gateway_info": {
       "flexible_3d": false,
       "card_number": "4111111111111111",
       "card_holder_name": "MultiSafepay",
       "card_expiry_date": "2412",
      "term_url": "http://example.com/?type=term&api_key=<api_key>",
        "card_cvc": "321"
   }
}

```
> JSON response

```json 
{
    "success": true,
    "data": {
        "transaction_id": 123456789
        "order_id": "my-test-order-01",
        "created": "2019-05-16T10:51:54",
        "currency": "EUR",
        "amount": 100,
        "description": "test product description",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "completed",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2019-05-16T10:51:54",
        "customer": {
            "locale": "nl_NL",
            "first_name": "Simon",
            "last_name": "Smit",
            "address1": "Kraanspoor",
            "address2": "",
            "house_number": "39C",
            "zip_code": "1033SC",
            "city": "Amsterdam",
            "state": "NH",
            "country": "NL",
            "country_name": "The Netherlands",
            "phone1": "0208500500",
            "phone2": "00310000001",
            "email": "simonsmit@example.com"
        },
        "custom_info": {
            "custom_1": null,
            "custom_2": null,
            "custom_3": null
        },
        "payment_details": {
            "type": "VISA",
            "account_id": null,
            "account_holder_name": "MultiSafepay",
            "external_transaction_id": 0010,
            "last4": 1111,
            "card_expiry_date": 2412
        },
        "costs": [
            {
                "transaction_id": 123456789
                "description": "0.0 % For Visa CreditCards Transactions",
                "type": "SYSTEM",
                "amount": 0.0
            }
        ],
         "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-test-order-01",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-test-order-01"
    }
}
```
{{< /code-block >}}

{{< description >}}

### Direct: Flexible 3D set to false

Use [Flexible 3D](/payments/features/flexible-3ds/) to set whether or not to complete the transaction with [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/) verification.

To disable 3D Secure, in the `POST /orders` request > `gateway_info` object, set the `flexible_3d` parameter to `false`.

**Notes:**  

- Activating Flexible 3D Secure overrides Dynamic 3D settings, so that payments are not enrolled with a 3D authentication.

- We no longer support [Flexible 3D](https://docs.multisafepay.com/tools/flexible_3d) for merchants based in Europe due to PSD2 regulations.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Options: `VISA`, `MASTERCARD`.

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
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------
__gateway_info__ | object | required

Defines certain customer data (payment details).

Contains:  

__flexible_3d__ | boolean | required

True, enable the 3D Secure authentication. False, disable the 3D Secure authentication.

__term_url__ | string | required

URL that is used to instruct the card issuer where to redirect the authorisation query. 

----------------


{{< /description >}}
