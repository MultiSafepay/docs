---
weight: 316
meta_title: "API Reference - Create an iDEAL order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "IDEAL",
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
    "currency": "EUR",
    "amount": 1000,
    "gateway": "iDEAL",
    "description": "Test order description",
    "custom_info": {},
    "gateway_info": {
        "issuer_id": "0031"
    },
     "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
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
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 123456789
        "type": "SYSTEM"
      }
    ],
    "created": "2020-01-14T12:08:43",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "address2": "",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": "The Netherlands",
      "email": "simonsmit@example.com",
      "first_name": "Simon",
      "house_number": "39C",
      "last_name": "Smit",
      "locale": "en_US",
      "phone1": "0208500500",
      "phone2": "00310000001",
      "state": "NH",
      "zip_code": "1033SC"
    },
    "description": "Test order description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-01-14T12:08:43",
    "order_id": "my-order-id-1",
    "payment_details": {
	  "account_bic": "string",
      "account_holder_name": null,
      "account_iban": "*** 1234",
      "account_id": null,
      "external_transaction_id": "1150001181473373",
      "issuer_id": "0031",
      "recurring_id": null,
      "recurring_model": null,
      "type": "IDEAL"
    },
    "payment_methods": [
      {
        "amount": 1000,
        "currency": "EUR",
        "description": "Test order description",
        "external_transaction_id": "1150001181473373",
        "payment_description": "iDEAL",
        "status": "initialized",
        "type": "IDEAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 123456789
    "payment_url": "https://www.abnamro.nl/en/ideal-betalen/index.html?randomizedstring=8641247395&trxid=1150001181473373"
  }
}
```
{{< /code-block >}}
{{< description >}}
## iDEAL
See also Payment methods – [iDEAL](/payments/methods/banks/ideal).

### Redirect

Customers are redirected to a MultiSafepay payment page where they can select iDEAL as a payment method.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `checkout`, `paymentlink`.  

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `IDEAL`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__currency__ | string | required

The currency for the payment.  
Fixed value: `EUR`.

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

Customers select iDEAL and the issuing bank on the checkout page, and are then directed to the **issuer's** payment page.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`.  

----------------
__gateway_info__ | object | required

Contains:  

__issuer_id__ | integer | required

The unique identifier of the [issuer](#gateway-issuers).

----------------

{{< /description >}}

