---
weight: 327
meta_title: "API Reference - Create a Santander Betaal per Maand order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
{
  "type":"direct",
  "order_id":"my-order-id-1",
  "gateway":"SANTANDER",
  "currency":"EUR",
  "amount":50000,
  "description":"Test order description",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":""
  },
  "customer":{
    "locale":"nl_NL",
    "ip_address":"31.148.195.10",
    "forwarded_ip":"",
    "first_name":"Testperson-nl",
    "last_name":"Approved",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "email":"test@example.com",
    "referrer":"http://example.com",
    "user_agent":"Mozilla//5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  },
  "gateway_info":{
    "birthday":"1970-07-10",
    "gender":"male",
    "phone":"0612345678",
    "email":"youremail@email.com"
  }
}
```
> JSON response

```shell
{
  "success":true,
  "data":{
    "transaction_id":2333720,
    "order_id":"my-order-id-1",
    "created":"2017-08-07T10:07:07",
    "currency":"EUR",
    "amount":100000,
    "description":"product description",
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
    "modified":"2017-08-07T10:07:07",
    "customer":{
      "locale":"nl_NL",
      "..."
    },
    "payment_details":{
      "recurring_id":null,
      "type":"SANTANDER",
      "account_id":null,
      "account_holder_name":null,
      "external_transaction_id":null
    },
    "costs":[
      {
        "transaction_id":406933,
        "amount":0.49,
        "description":"Cost description",
        "type":"SYSTEM"
      }
    ],
    "payment_url":"https://retailersowtest.santander.nl/EDurables/Home.aspx?guid=XXXXX"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Santander Betaal per Maand

- See also Payment methods – [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand).  
- Direct only.

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`. 

----------------
`order_id` | string | required

Your unique identifier for the order.    
Format: Maximum 50 characters.

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `SANTANDER`.

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

`birthday` | object | required

The customer's date of birth.  
In the Netherlands and Belgium, this is required for credit checks.  
Format: yyyy-mm-dd. 

`gender` | string | required

The customer's personal title.  
Options: `mr`, `mrs`, `miss`. 

`phone` | string | required

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

`email` | string | required

The email address for sending payment instructions to the customer.

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

The capture reason for the order.

----------------
`fastcheckout` | string 

Whether this is a [FastCheckout](/payments/methods/fastcheckout/) transaction.  
Options: `YES`, `NO`.

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object/).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------


{{< /description >}}
