---
weight: 323
meta_title: "API Reference - Create a PayPal order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "PAYPAL",
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
        "locale": "nl_NL"
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
    "gateway": "PAYPAL",
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
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "state": "NH",
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
    "amount": 1000,
    "amount_refunded": 0,
    "costs": [],
    "created": "2020-01-30T11:16:11",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "state": "NH",
      "country": "NL",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033SC"
    },
    "description": "Test order description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-30T11:16:11",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": "Test-person-nl",
      "account_id": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
      "external_transaction_id": "8K013819T00365502LLL",
      "paypal_eligibility": "",
      "recurring_id": null,
      "recurring_model": null,
      "type": "PAYPAL"
    },
    "payment_methods": [
      {
        "account_holder_name": "Test-person-nl",
        "account_id": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp",
        "amount": 1000,
        "currency": "EUR",
        "description": "Test order description",
        "external_transaction_id": "EC-8K013819T00365502L",
        "payment_description": "PayPal",
        "status": "initialized",
        "type": "PAYPAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789
    "payment_url": "https://www.paypal.com/cgi-bin/webscr?cmdmsp=_express-checkout&token=EC-8K013819T00365502LLL-msp"
  }
}
```

{{< /code-block >}}

{{< description >}}
## PayPal
See also Payment methods – [PayPal](/payments/methods/wallet/paypal).

### Redirect

Once the customer has completed payment, the `status` changes to **Completed**. The `financial_status` remains **Initialized**, and during this status you cannot ship the order. You must first set the order to **Completed** for both the `status` and `financial_status` and then ship the order.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `checkout`, `paymentlink`. 

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `PAYPAL`.

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

**Note:** To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes) the transaction request must include the __state__ parameter in the customer's address. 

----------------

### Direct 

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `checkout`, `paymentlink`. 

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.   
Fixed value: `PAYPAL`.

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

**Note:** To be eligible for [PayPal Seller Protection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156), for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes) the transaction request must include the __state__ parameter in the customer's address.

----------------

{{< /description >}}
