---
weight: 328
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
    "gateway": "DIRDEB",
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
> JSON response

```json
{
  "success": true,
  "data": {
    "transaction_id": 123456789,
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
        "transaction_id": 123456789,
        "amount": 0.0,
        "description": "0.0 For SEPA Direct Debit Transactions",
        "type": "SYSTEM"        
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
See also Payment methods – [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit).

### SEPA Direct Debit - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.   
Options: `direct`, `redirect`, `checkout`, `paymentlink`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `IDEAL`. 

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

`account_id` | string

The international bank account number (IBAN) to be charged for the transaction.

`account_holder_name` | string

The name of the account holder to be charged for the transaction. 

`account_holder_iban` | string

The international bank account number (IBAN) to be charged for the transaction.

`emandate` | string

The e-mandate (for your own adminstration).

`recurring_id` | string

The unique identifier for the recurring payment. 

----------------

### SEPA Direct Debit - direct 

**Parameters**

`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `checkout`, `paymentlink`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `DIRDEB`.

----------------
`order_id` | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object). 

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

`account_id` | string

The international bank account number (IBAN) to be charged for the transaction.

`account_holder_name` | string

The name of the account holder to be charged for the transaction. 

`account_holder_iban` | string

The international bank account number (IBAN) to be charged for the transaction.

`emandate` | string

The e-mandate (for your own adminstration).

`recurring_id` | string

The unique identifier for the recurring payment. 

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------

{{< /description >}}
