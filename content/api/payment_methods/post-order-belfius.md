---
weight: 308
meta_title: "API - Create Belfius order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```shell

{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "BELFIUS",
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "locale": "be_BE"
    }
}
```

> JSON Response 

```shell
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
    }
}
```

> POST - /orders

```shell
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
```shell
{
    "success": true,
    "data": {
        "transaction_id": "279354751",
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
            "first_name": "Testperson-nl",
            "address1": "Kraanspoor",
            "house_number": "39C",
            "zip_code": "1033SC"
            "city": "Amsterdam",
            "country": "NL";,
            "country_name": "Netherlands",
            "phone1": "0208500500",
            "email": "example@multisafepay.com",
},
        "payment_details": {
            "recurring_id": null,
            "type": "BELFIUS"
"account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
            "account_holder_name": null,
            "external_transaction_id": "279354751",
},
        "costs": [
{
        "transaction_id": "279354751",
        "description": "Test Order Description",
        "type": "BELFIUS"
        "amount": "1000",
},
        "payment_methods": [
                "account_id": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723",
                "currency": "EUR",
                "external_transaction_id": "279354751",
                "payment_description": "",
                "status": "initialized",
}
],
  "payment_url": "https://testpayv2.multisafepay.com/simulator/belfius?transactionid=4014723&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&AMOUNT=1000&CURRRENCY=EUR&mspid=4014723"
    }
}
```
{{< /code-block >}}

{{< description >}}
## Belfius
### Redirect - Belfius 

Creates a Belfius [Redirect](/faq/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct , redirect , paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BELFIUS.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__customer__ | object

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

---------------- 

### Direct - Belfius

Creates a Belfius [Direct](/faq/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct , redirect , paymentlink.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__gateway__ | string

The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: BELFIUS.

----------------
__currency__ | string

The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with.

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

Read more about [Belfius](/payment-methods/banks/belfius) on our documentation page.

{{< /description >}}