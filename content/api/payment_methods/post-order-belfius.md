---
weight: 308
meta_title: "API Reference - Create Belfius order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```json

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "BELFIUS",
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
        "locale": "be_BE"
    }
}
```

> JSON Response 

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
    "description": "Test Order Description",
    "custom_info": {},
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    }
}
```

> JSON Response
```json
{
    "success": true,
    "data": {
        "transaction_id": 123456789
        "order_id": "my-order-id-1",
        "created": "2019-03-07T13:41:15",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test Order Description",
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
            "description": "Test Order Description",
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

- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__gateway__ | string

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `BELFIUS`.

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
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

---------------- 

### Direct

- Creates a [direct](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__gateway__ | string

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `BELFIUS`.

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

{{< /description >}}