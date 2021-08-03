---
weight: 308
meta_title: "API Reference - Create Belfius order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders
```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "BELFIUS",
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
        "locale": "be_BE"
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
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BELFIUS",
    "description": "Test order description",
    "custom_info": {},
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
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
        "created": "2019-03-07T13:41:15",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test order description",
        "items": null,
        "amount_refunded":"0",
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2020-01-07T13:41:15",
        "customer": {
            "locale": "be_BE",
            "first_name": "Simon",
            "address1": "Kraanspoor",
            "house_number": "39C",
            "zip_code": "1033SC",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": "The Netherlands",
            "phone1": "0208500500",
            "email": "simonsmit@example.com",
        },
        "payment_details": {
            "recurring_id": null,
            "type": "BELFIUS",
            "account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
            "account_holder_name": null,
            "external_transaction_id": "279354751",
        },
        "costs": [
        {
            "transaction_id": 123456789
            "description": "Test order description",
            "type": "BELFIUS",
            "amount": 1000,
            }
        ],
        "payment_methods": [
            {
                "account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
                "currency": "EUR",
                "external_transaction_id": "279354751",
                "payment_description": "",
                "status": "initialized"
            }
        ],
        "payment_url": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723"
    }
}
```
{{< /code-block >}}

{{< description >}}
## Belfius
See also Payment methods – [Belfius](/payments/methods/banks/belfius).

### Redirect 

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `BELFIUS`.

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

### Direct

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `BELFIUS`.

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

{{< /description >}}