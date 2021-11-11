---
weight: 334
meta_title: "API reference - Create a Trustly order - MultiSafepay Docs"

---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"redirect",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":1000,
  "gateway":"TRUSTLY",
  "description":"Test order description",
  "custom_info":{
    
  },
  "payment_options":{
    "notification_url":"https://www.example.com/client/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  "customer":{
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
    "payment_url":"https://payv2.multisafepay.com/connect/13oElUaESR7YS2b4gUJV9oI4tUXeb1mj1D8/?lang=nl_NL"
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
  "gateway":"TRUSTLY",
  "description":"product description",
  "custom_info":{
    
  },
  "payment_options":{
    "notification_url":"http://10.1.10.111/testtool/client/json-test/notification?type=notification",
    "redirect_url":"https://www.example.com/client/notification?type=redirect",
    "cancel_url":"https://www.example.com/client/notification?type=cancel"
  },
  "customer":{
    "first_name":"Testperson-nl",
    "last_name":"Approved",
    "country":"NL",
    "email":"example@multisafepay.com"
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "amount":1000,
    "amount_refunded":0,
    "costs":[
      
    ],
    "created":"2021-11-08T13:14:05",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":null,
      "address2":null,
      "city":null,
      "country":"NL",
      "country_name":null,
      "email":"example@multisafepay.com",
      "first_name":"Testperson-nl",
      "house_number":null,
      "last_name":"Approved",
      "locale":"en_US",
      "phone1":null,
      "phone2":"",
      "state":null,
      "zip_code":null
    },
    "description":"product description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":null,
    "modified":"2021-11-08T13:14:05",
    "order_id":"my-order-id-1",
    "payment_details":{
      "account_holder_name":null,
      "account_id":null,
      "external_transaction_id":1234567,
      "recurring_flow":null,
      "recurring_id":null,
      "recurring_model":null,
      "type":"TRUSTLY"
    },
    "payment_methods":[
      {
        "amount":1000,
        "currency":"EUR",
        "description":"product description",
        "external_transaction_id":1234567,
        "payment_description":"Trustly",
        "status":"initialized",
        "type":"TRUSTLY"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "status":"initialized",
    "transaction_id":1234567,
    "var1":null,
    "var2":null,
    "var3":null,
    "payment_url":"https://testpayv2.multisafepay.com/simulator/trustly?transactionid=5095261&return_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&cancel_url=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F&mspid=5095261"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Trustly

See also Payment methods – [Trustly](/payment-methods/trustly).  

### Trustly - redirect

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

The unique gateway identifier for the payment method.  
Value: `TRUSTLY`. 

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).                                

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

### Trustly - direct

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

The unique gateway identifier for the payment method.  
Value: `TRUSTLY`. 

----------------
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by their bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).                                

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom-info-object).

----------------
`customer` | object 

See [customer (object)](/api/#customer-object). 

----------------
`fastcheckout` | string 

Value: `NO`.

----------------
`financial_status` | string

The [transaction status](/payments/multisafepay-statuses/) of the order.

----------------
`items` | object 

See [items (object)](/api/#items-object).

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment-methods-object).

----------------
`reason` | string

----------------
`related_transactions` | object

Information about linked transactions.

----------------
`status` | string

The [order status](/payments/multisafepay-statuses/).

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`var1` / `var2` / `var3` | string 

Variables for storing additional data.

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
