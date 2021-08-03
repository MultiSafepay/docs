---
weight: 307
meta_title: "API Reference - Create Bank transfer order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "gateway": "BANKTRANS",
    "description": "Test order description",
    "payment_options": {
        "notification_url": " http://www.example.com/client/notification?type=notification",
        "redirect_url": " http://www.example.com/client/notification?type=redirect ",
        "cancel_url": " http://www.example.com/client/notification?type=cancel ",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "country": "NL",
        "ip_address": "123.123.123.123",
        "email": "simonsmit@example.com"
    }
}
```

> JSON response 

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/13UeQHxVIs83238WIJdlSYsB4owgNSqZudS/?lang=nl_NL"
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
    "gateway": "BANKTRANS",
    "description": "Test order description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "country": "NL",
        "ip_address": "123.123.123.123",
        "disable_send_email": false,
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
        "created": "2019-03-01T16:12:47",
        "currency": "EUR",
        "amount": 1000,
        "description": "Test order description",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2020-01-06T10:47:18",
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
            "locale": "nl_NL",
            "phone1": "0208500500",
            "phone2": "00310000001",
            "state": "NH",
            "zip_code": "1033SC"
        },
        "payment_details": {
            "type": "BANKTRANS"
            "account_holder_name": "",
            "account_id": null,
            "external_transaction_id": "9201727123406700",
            "issuer_id": "vib",
            "recurring_id": null,
            "recurring_model": null,
        },
        "costs": [
            {
                "transaction_id": 123456789
                "amount": 0,
                "description": "",
                "type": "SYSTEM"
            }
        ],
        "payment_methods": {
            "account_holder_name": " ",
            "amount": 1000,
            "currency": "EUR",
            "description": "Test order description",
            "external_transaction_id": "234374824",
            "payment_description": "Bank transfer",
            "status": "initialized",
            "type": "BANKTRANS"
        },
        "gateway_info": {
            "NL07DEUT7351106754": "NL07DEUT7351106754",
            "reference": "234374824",
            "issuer_name": "DB",
            "destination_holder_name": "MultiSafepay",
            "destination_holder_city": "Amsterdam",
            "destination_holder_country": "NL",
            "destination_holder_iban": "NL07DEUT7351106754",
            "destination_holder_swift": "DEUTNL2NXXX",
            "account_holder_country": "NL"
        },
        "payment_url": "http://www.example.com/client/notification?type=redirect&transactionid=apitool_13890779",
        "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=apitool_13890779"
    }
}
```

{{< /code-block >}}

{{< description >}}
## Bank transfer
See also Payment methods – [Bank transfer](/payments/methods/banks/bank-transfer).

### Redirect

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
__currency__ | string | required

The currency you want the customer to pay in.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `BANKTRANS`.

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

- If the __email__ parameter is not provided, MultiSafepay cannot send the payment details to the customer.
- The __country__ parameter provides the customer a local bank account to pay to, where available.  

---------------- 

### Direct  

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
__currency__ | string | required

The currency you want the customer to pay in.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__gateway__ | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `BANKTRANS`.

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

- If the __email__ parameter is not provided, MultiSafepay cannot send the payment details to the customer.
- The __country__ parameter provides the customer a local bank account to pay to, where available. 

----------------
__disable_send_email (optional)__	| boolean | required

If emailing payment instructions to the customer yourself, set to `true`.  
For MultiSafepay to email payment instructions, set to `false`.  
Options: `true`, `false`.  
Default: `false`.

**Note:** In the JSON response, it is important to send payment instructions to the customer yourself. Note that all parameters can be different for every single transaction. Do not store this information except for a specific transaction.

----------------
__gateway_info__ | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:  

__reference__ | string | required

A unique number the customer must provide in the bank transfer for MultiSafepay to recognize the payment.

__issuer_name__ | string | required

The name of MultiSafepay's bank to send the funds to.    

__destination_holder_name__ | string | required

The account holder name for MultiSafepay's bank account.

__destination_holder_city__ | string | required

The city where the MultiSafepay bank account is registered.  

__destination_holder_country__ | string | required

The country where the MultiSafepay bank account is registered.

__destination_holder_iban__ | string | required

The international bank account number (IBAN) to send the funds to.

__destination_holder_swift__ | string | required

The bank identification code (BIC) to send the funds to. 

__account_holder_name__ | string | required

The customer's name, if provided in the transaction request. 

__account_holder_city__ | string | required

The customer's city, if provided in the transaction request.  

__account_holder_country__ | string | required

The customer's country, if provided in the transaction request.  

----------------

{{% /description %}}
