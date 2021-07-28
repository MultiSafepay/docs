---
weight: 325 
meta_title: "API Reference - Create a SEPA Direct Debit order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "DIRDEB",
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
        "locale": "nl_NL"
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
    "gateway": "DIRDEB",
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
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "forwarded_ip": ""
    },
    "gateway_info": {
        "account_id": "NL87ABNA0000000001",
        "account_holder_name": "Example",
        "account_holder_iban": "NL87ABNA0000000001",
        "emandate": "mandateID"
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
    "created": "2019-03-08T09:23:46",
    "currency": "EUR",
    "amount": 9743,
    "description": "Test order description",
    "items": "",
    "amount_refunded": 0,
    "status": "initialized",
    "financial_status": "initialized",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "NO",
    "modified": "2019-03-08T09:23:46",
    "customer": {
      "locale": "nl_NL",
 ...
    },
    "payment_details": {
      "recurring_id": "",
      "type": "DIRDEB",
      "account_id": "NL87ABNA0000000001",
      "account_holder_name": "Example",
      "external_transaction_id": "6190662598986790",
      "account_iban": "*** 1234",
    },
    "costs": [
      {
        "transaction_id": 123456789
        "description": "0.0 For SEPA Direct Debit Transactions",
        "type": "SYSTEM",
        "amount": 0.0
      }
    ],
    "payment_url": "https://www.example.com/client/notification?type=redirect&transactionid=my-order-id-1",
    "cancel_url": "https://www.example.com/client/notification?type=cancel&transactionid=my-order-id-1"
  }
}
```

{{< /code-block >}}
{{< description >}}
## SEPA Direct Debit
### Redirect - SEPA Direct Debit

Creates a SEPA Direct Debit [Redirect](/developer/api/difference-between-direct-and-redirect) order.

{{< alert-notice >}} The __recurring_id__ parameter can be used to process subsequent payments when the recurring option is enabled in your MultiSafepay account. The recurring_id must be included in the gateway info section of the request. Read more about [recurring payments](/payments/features/recurring-payments/processing-recurring-payments/) {{< /alert-notice >}}

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: IDEAL.

----------------

__recurring_id__ | string

The recurring_id is a unique id that can be used to process subsequent payments.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

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
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.

----------------
__locale__ | string

 Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`.

----------------

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

### Direct - SEPA Direct Debit

Creates a SEPA Direct Debit [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, checkout, paymentlink.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: DIRDEB.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.     

----------------
__gateway_info__ | object

----------------
__account_id__ | string

IBAN to be charged for the transaction.

----------------
__account_holder_name__ | string

Name of the owner of the bank account to be charged for the transaction. 

----------------
__account_holder_iban__ | string

IBAN to be charged for the transaction.

----------------
__emandate__ | string

For your own adminstration, put the e-mandate here.

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)

----------------
__forwarded_ip__ | string

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. [More info](/developer/api/validating-customer-ip-address)

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Read more about [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit) on our docuemntation page.

{{< /description >}}
