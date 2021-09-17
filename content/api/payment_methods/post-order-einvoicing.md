---
weight: 313
meta_title: "API reference - Create E-Invoicing order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST -/orders
```json
{
  "type":"redirect",
  "gateway":"EINVOICE",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":26000,
  "description":"Test order description",
  "manual":false,
  "gateway_info":{
    "email":"example@multisafepay.com"
  },
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  ...
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":90,
        "quantity":2,
        "merchant_item_id":"11111",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"Flat Rate - Fixed",
        "description":"Shipping",
        "unit_price":10,
        "quantity":1,
        "merchant_item_id":"123456",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":0
        }
      }
    ]
  },
  "checkout_options":{
    "tax_tables":{
      "alternate":[
        {
          "name":"none",
          "rules":[
            {
              "rate":0.00
            }
          ]
        }
      ]
    }
  }
}
```
> JSON response

```json
{
  "success":true,
  "data":{
    "order_id":"my-order-id-1",
    "payment_url":"https://payv2.multisafepay.com/connect/82v6HsoQhaR823uIZ7hexDMwQyielzLrdox/?lang=nl_NL"
  }
}
```
> POST - /orders

```json
{
  "type":"direct",
  "gateway":"EINVOICE",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":26000,
  "description":"Test order description",
  "items":"",
  "manual":false,
  "gateway_info":{
    "birthday":"1980-01-30",
    "bankaccount":"0417164300",
    "phone":"0208500500",
    "email":"example@multisafepay.com"
  },
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel",
    "close_window":true
  },
  ...
  "shopping_cart":{
    "items":[
      {
        "name":"Item demo 1",
        "description":"",
        "unit_price":90,
        "quantity":2,
        "merchant_item_id":"666666",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"Item shipping - Flat Rate - Fixed",
        "description":"Shipping",
        "unit_price":10,
        "quantity":1,
        "merchant_item_id":"msp-shipping",
        "tax_table_selector":"none",
        "weight":{
          "unit":"KG",
          "value":0
        }
      }
    ]
  },
  "checkout_options":{
    "tax_tables":{
      "alternate":[
        {
          "name":"none",
          "rules":[
            {
              "rate":0.00
            }
          ]
        }
      ]
    }
  }
}
```
> JSON response 

```json
{
  "success":true,
  "data":{
    "transaction_id":2340676,
    "order_id":"my-order-id-1",
    "created":"2017-09-29T16:13:10",
    "currency":"EUR",
    "amount":26000,
    "description":"Test order description",
    "items":"",
    "amount_refunded":0,
    "status":"completed",
    "financial_status":"initialized",
    "reason":"",
    "reason_code":"",
    "fastcheckout":"NO",
    "modified":"2017-09-29T16:13:10",
    "customer":{
      ...
      "payment_details":{
        "recurring_id":null,
        "type":"",
        "account_id":10071970,
        "account_holder_name":null,
        "external_transaction_id":2379429850
      },
      "shopping_cart":{
        "items":[
          {
            "name":"Item demo 1",
            "description":"",
            "unit_price":"90.00",
            "currency":"EUR",
            "quantity":2,
            "merchant_item_id":666666,
            "tax_table_selector":"none",
            "cashback":"",
            "image":"",
            "product_url":"",
            "weight":{
              "unit":"KG",
              "value":12
            },
            "options":[
              
            ]
          },
          {
            "name":"Item shipping - Flat Rate - Fixed",
            "description":"Shipping",
            "unit_price":"10.00",
            "currency":"EUR",
            "quantity":1,
            "merchant_item_id":"msp-shipping",
            "tax_table_selector":"none",
            "cashback":"",
            "image":"",
            "product_url":"",
            "weight":{
              "unit":"KG",
              "value":0
            },
            "options":[
              
            ]
          }
        ]
      },
      "checkout_options":{
        "default":{
          
        },
        "alternate":[
          {
            "name":"none",
            "rules":[
              {
                "rate":0.00,
                "country":""
              }
            ]
          }
        ]
      },
      "order_adjustment":{
        "total_adjustment":"0.00",
        "total_tax":"0.00"
      },
      "order_total":260.00,
      "costs":[
        
      ],
      "payment_url":"http://www.example.com/client/?action=notification&type=redirect&transactionid=2340676",
      "cancel_url":"http://www.example.com/client/?action=notification&type=cancel&transactionid=2340676"
    }
  }
```
{{< /code-block >}}

{{< description >}}
## E-Invoicing
See also Payment methods – [E-Invoicing](/payments/methods/billing-suite/e-invoicing).

### E-Invoicing - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `EINVOICE`.

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
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`manual` | string 

Fixed value: `false`.

----------------
`gateway_info` | object                                                              

Contains:  

`email` | string

The email address for sending payment instructions to the customer. 

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class. 

----------------

### E-Invoicing - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`.  

----------------
`gateway` | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `EINVOICE`.

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
`description` | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`items` | object
 
See [items (object)](/api/#items-object).

----------------
`manual` | string 

Fixed value: `false`.

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.                                                                

Contains:  

`birthday` | string

The customer's date of birth.  
Format: yyyy-mm-dd.                             

`bank_account` | string

The customer's (formatted) international bank account number (IBAN).  
This is required for credit checks. 

`phone` | string

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment. 

`email` | string

The email address for sending payment instructions to the customer.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping-cart-items-object).

----------------
`checkout_options` | object

The definitions for the VAT class.


**Response**

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`created` | string

The timestamp for when the order was created.

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

Whether this is a [FastCheckout](/payments/methods/fastcheckout/) transaction.  
Options: `YES`, `NO`.

----------------
`modified` | string

The timestamp of the last modification of the balance.  
Modifications include incoming payments, refunds, charges, and [payouts](/account/payouts/).  
Format: [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).

----------------
`customer` | object 

See [customer (object)](/api/#customer-object).

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment-details-object).

----------------
`shopping_cart.items` | required

See [shopping_cart.items object](/api/#shopping-cart-items-object).

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------
`cancel_url` | string 

The page the customer is redirected to if the payment fails.

----------------

{{< /description >}}
