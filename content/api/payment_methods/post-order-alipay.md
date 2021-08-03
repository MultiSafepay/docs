---
weight: 302
meta_title: "API Reference - Create an Alipay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test order description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "locale": "cn_CN"
    }
}
```

> JSON response 

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```
> POST - /orders

```json
{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "ALIPAY",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test order description",
    "manual": false,
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "cn_CN",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "simonsmit@example.com",
        "referrer": "https://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON response

```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
        "order_id": "my-order-id-1",
        "created": "2020-01-08T10:51:04",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test order description",
        "items": null,
        "amount_refunded": 0,
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2020-01-08T10:51:04",
        "customer": {
            "first_name": "Simon",
            "last_name": "Smit",
            "address1": "Kraanspoor",
            "house_number": "39C",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": "The Netherlands",
            "zip_code": "1033SC"
            "email": "simonsmit@example.com",
            "locale": "cn_CN",
            "phone1": "0208500500",
        },
        "payment_details": {
            "type": "ALIPAY"
           	 "account_holder_name": null,
            "account_id": "",
            "external_transaction_id": null,
            "recurring_id": null,
            "recurring_model": null,
        },
        "costs": [
        {
            "amount":,
            "description": "",
            "transaction_id": 123456789
            "type": "SYSTEM"
        }
        ],
            "payment_methods": [
                {
                    "account_id": "",
                    "amount": 1000,
                    "currency": "EUR",
                    "description": "Test order description",
                    "payment_description": "ALIPAY",
                    "status": "initialized",
                    "type": "ALIPAY"
                }
            ],
            "payment_url": "https://excashier.alipay.com/standard/auth.htm?auth_order_id=exc_5fc2c0045b9b455f87fedd6d7f41f021"
        }
    }
```

{{< /code-block >}}

{{< description >}}
## Alipay
See also Payment methods – [Alipay](/payments/methods/wallet/alipay).

### Alipay - redirect

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`, `paymentlink`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `ALIPAY`. 

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

### Alipay - direct

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`, `paymentlink`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `ALIPAY`. 

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
__manual__ | string | required

Fixed value: `false`.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------

{{< /description >}}
