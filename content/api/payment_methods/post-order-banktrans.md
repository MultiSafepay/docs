---
weight: 307
meta_title: "API reference - Create Bank transfer order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "gateway":"BANKTRANS",
  "description":"Test order description",
  "payment_options":{
    "notification_url":" http://www.example.com/client/notification?type=notification",
    "redirect_url":" http://www.example.com/client/notification?type=redirect ",
    "cancel_url":" http://www.example.com/client/notification?type=cancel ",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "country":"NL",
    "ip_address":"123.123.123.123",
    "email":"simonsmit@example.com"
  }
}
```

> JSON response 

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/13UeQHxVIs83238WIJdlSYsB4owgNSqZudS/?lang=nl_NL"
  }
}
```

> POST - /orders

```json 
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "gateway":"BANKTRANS",
  "description":"Test order description",
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
    "locale":"nl_NL",
    "country":"NL",
    "ip_address":"123.123.123.123",
    "disable_send_email":false
  }
}

```
> JSON response 

```json
{
  "success":true,
  "data":{
    "transaction_id":123456789,
    "order_id":"my-order-id-1",
    "created":"2019-03-01T16:12:47",
    "currency":"EUR",
    "amount":1000,
    "description":"Test order description",
    "var1":null,
    "var2":null,
    "var3":null,
    "items":null,
    "amount_refunded":0,
    "status":"initialized",
    "financial_status":"initialized",
    "reason":"",
    "reason_code":"",
    "fastcheckout":"NO",
    "modified":"2020-01-06T10:47:18",
    "customer":{
      "address1":"Kraanspoor",
      "address2":"",
      "city":"Amsterdam",
      "country":"NL",
      "country_name":"The Netherlands",
      "email":"simonsmit@example.com",
      "first_name":"Simon",
      "house_number":"39C",
      "last_name":"Smit",
      "locale":"nl_NL",
      "phone1":"0208500500",
      "phone2":"00310000001",
      "state":"NH",
      "zip_code":"1033SC"
    },
    "payment_details":{
      "type":"BANKTRANS",
      "account_holder_name":"",
      "account_id":null,
      "external_transaction_id":"9201727123406700",
      "issuer_id":"vib",
      "recurring_id":null,
      "recurring_model":null
    },
    "costs":[
      {
        "transaction_id":123456789,
        "amount":0,
        "description":"",
        "type":"SYSTEM"
      }
    ],
    "payment_methods":{
      "account_holder_name":" ",
      "amount":1000,
      "currency":"EUR",
      "description":"Test order description",
      "external_transaction_id":"234374824",
      "payment_description":"Bank transfer",
      "status":"initialized",
      "type":"BANKTRANS"
    },
    "gateway_info":{
      "NL07DEUT7351106754":"NL07DEUT7351106754",
      "reference":"234374824",
      "issuer_name":"DB",
      "destination_holder_name":"MultiSafepay",
      "destination_holder_city":"Amsterdam",
      "destination_holder_country":"NL",
      "destination_holder_iban":"NL07DEUT7351106754",
      "destination_holder_swift":"DEUTNL2NXXX",
      "account_holder_country":"NL"
    },
    "payment_url":"https://www.example.com/client/notification?type=redirect&transactionid=apitool_13890779",
    "cancel_url":"https://www.example.com/client/notification?type=cancel&transactionid=apitool_13890779"
  }
}
```

{{< /code-block >}}

{{< description >}}
## Bank Transfer
See also Payment methods – [Bank transfer](/payments/methods/banks/bank-transfer).

### Bank Transfer - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `redirect`.

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Value: `BANKTRANS`.

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

- If the `email` parameter is not provided, MultiSafepay cannot send the payment details to the customer.
- The `country` parameter provides the customer a local bank account to pay to, where available.  

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

---------------- 

### Bank Transfer - direct  

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Value: `direct`.

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`currency` | string | required

The currency you want the customer to pay in.    
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`amount` | integer | required

The amount (in cents) the customer needs to pay.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Value: `BANKTRANS`.

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

- If the `email` parameter is not provided, MultiSafepay cannot send the payment details to the customer.
- The `country` parameter provides the customer a local bank account to pay to, where available. 

Contains:  
`disable_send_email`	| boolean | optional

If emailing payment instructions to the customer yourself, set to `true`.  
For MultiSafepay to email payment instructions, set to `false`.  
Options: `true`, `false`.  
Default: `false`.

**Note:** In the JSON response, it is important to send payment instructions to the customer yourself. Note that all parameters can be different for every single transaction. Do not store this information except for a specific transaction.

**Response** 

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.

----------------
`items` | object 

See [items (object)](/api/#items-object).

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/).

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`reason` | string 


----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:  

`reference` | string | required

A unique number the customer must provide in the bank transfer for MultiSafepay to recognize the payment.

`issuer_name` | string | required

The name of MultiSafepay's bank to send the funds to.    

`destination_holder_name` | string | required

The account holder name for MultiSafepay's bank account.

`destination_holder_city` | string | required

The city where the MultiSafepay bank account is registered.  

`destination_holder_country` | string | required

The country where the MultiSafepay bank account is registered.

`destination_holder_iban` | string | required

The international bank account number (IBAN) to send the funds to.

`destination_holder_swift` | string | required

The bank identification code (BIC) to send the funds to. 

`account_holder_name` | string | required

The name of the account holder to be charged for the transaction. 

`account_holder_city` | string | required

The customer's city, if provided in the transaction request.  

`account_holder_country` | string | required

The customer's country, if provided in the transaction request.  

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{% /description %}}
