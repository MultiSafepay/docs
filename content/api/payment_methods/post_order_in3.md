---
weight: 318
meta_title: "API Reference - Create an in3 order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json
{
  "type":"direct",
  "gateway":"IN3",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":37485,
  "description":"Test order description",
  "manual":"false",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel"
  },
  "customer":{
    "ip_address":"89.45.467.110",
    "locale":"nl_NL",
    "first_name":"Testperson-nl",
    "last_name":"",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "country":"NL",
    "email":"example@multisafepay.com"
  },
  "delivery":{
    "first_name":"Testperson-nl",
    "last_name":"",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1033 SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0208500500",
    "email":"example@multisafepay.com"
  },
  "gateway_info":{
    "birthday":"1970-07-10",
    "gender":"mr",
    "phone":"0612345678"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":90,
        "quantity":3,
        "merchant_item_id":"1111",
        "tax_table_selector":"BTW21",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"Nice apple",
        "description":"",
        "unit_price":35,
        "quantity":1,
        "merchant_item_id":"666666",
        "tax_table_selector":"BTW9",
        "weight":{
          "unit":"KG",
          "value":20
        }
      },
      {
        "name":"Flat Rate - Fixed",
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
      "default":{
        "shipping_taxed":"true",
        "rate":0.21
      },
      "alternate":[
        {
          "name":"BTW21",
          "standalone":true,
          "rules":[
            {
              "rate":0.21
            }
          ]
        },
        {
          "name":"BTW9",
          "standalone":true,
          "rules":[
            {
              "rate":0.09
            }
          ]
        },
        {
          "name":"BTW6",
          "standalone":true,
          "rules":[
            {
              "rate":0.06
            }
          ]
        },
        {
          "name":"BTW0",
          "standalone":true,
          "rules":[
            {
              "rate":0
            }
          ]
        },
        {
          "name":"none",
          "standalone":false,
          "rules":[
            {
              "rate":0
            }
          ]
        },
        {
          "name":"FEE",
          "standalone":false,
          "rules":[
            {
              "rate":0
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
    "amount":37485,
    "amount_refunded":0,
    "checkout_options":{
      "alternate":[
        {
          "name":"BTW21",
          "rules":[
            {
              "country":"",
              "rate":0.21
            }
          ],
          "standalone":true
        },
        {
          "name":"BTW9",
          "rules":[
            {
              "country":"",
              "rate":0.09
            }
          ],
          "standalone":true
        },
        {
          "name":"BTW6",
          "rules":[
            {
              "country":"",
              "rate":0.06
            }
          ],
          "standalone":true
        },
        {
          "name":"BTW0",
          "rules":[
            {
              "country":"",
              "rate":0.00
            }
          ],
          "standalone":true
        },
        {
          "name":"none",
          "rules":[
            {
              "country":"",
              "rate":0.00
            }
          ],
          "standalone":""
        },
        {
          "name":"FEE",
          "rules":[
            {
              "country":"",
              "rate":0.00
            }
          ],
          "standalone":""
        }
      ],
      "default":{
        "rate":0.21,
        "shipping_taxed":true
      }
    },
    "costs":[
      
    ],
    "created":"2020-08-19T14:55:46",
    "currency":"EUR",
    "custom_info":{
      "custom_1":null,
      "custom_2":null,
      "custom_3":null
    },
    "customer":{
      "address1":"Kraanspoor",
      "city":"Amsterdam",
      "country":"NL",
      "country_name":null,
      "email":"example@multisafepay.com",
      "first_name":"Testperson-nl",
      "house_number":"39C",
      "last_name":"",
      "locale":"nl_NL",
      "phone1":"0612345678",
      "zip_code":"1039 SC"
    },
    "description":"Test order description",
    "fastcheckout":"NO",
    "financial_status":"initialized",
    "items":"<table border=\"0\" cellpadding=\"5\" width=\"100%\">\n<tr>\n<th width=\"10%\"><font size=\"2\" face=\"Verdana\">Aantal </font></th>\n<th align=\"left\"></th>\n<th align=\"left\"><font size=\"2\" face=\"Verdana\">Details </font></th>\n<th width=\"19%\" align=\"right\"><font size=\"2\" face=\"Verdana\">Prijs </font></th>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">3</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Geometric Candle Holders</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">90.00</font>\n</td>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">1</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Nice apple</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">35.00</font>\n</td>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">1</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Flat Rate - Fixed</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">10.00</font>\n</td>\n</tr>\n<tr bgcolor=\"#E9F1F7\">\n<td colspan=\"3\" align=\"right\"><font size=\"2\" face=\"Verdana\">BTW:</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">59.85</font>\n</td>\n</tr>\n<tr bgcolor=\"#E9F1F7\">\n<td colspan=\"3\" align=\"right\"><font size=\"2\" face=\"Verdana\">Totaal:</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">374.85</font>\n</td>\n</tr>\n</table>",
    "modified":"2020-08-19T14:55:46",
    "order_adjustment":{
      "total_adjustment":59.85,
      "total_tax":59.85
    },
    "order_id":"my-order-id-1",
    "order_total":374.85,
    "payment_details":{
      "account_holder_name":null,
      "account_id":"1970-07-10",
      "external_transaction_id":"34bfc991bef24558a5b4f9c168753da1",
      "recurring_id":null,
      "recurring_model":null,
      "type":"IN3"
    },
    "payment_methods":[
      {
        "account_id":"1970-07-10",
        "amount":37485,
        "currency":"EUR",
        "description":"Test order description",
        "external_transaction_id":"34bfc928374rhjnf9368753da1",
        "payment_description":"in3",
        "status":"initialized",
        "type":"IN3"
      }
    ],
    "reason":"",
    "reason_code":"",
    "related_transactions":null,
    "shopping_cart":{
      "items":[
        {
          "cashback":"",
          "currency":"EUR",
          "description":"",
          "image":"",
          "merchant_item_id":1111,
          "name":"Geometric Candle Holders",
          "options":[
            
          ],
          "product_url":"",
          "quantity":3,
          "tax_table_selector":"BTW21",
          "unit_price":"90.00",
          "weight":{
            "unit":"KG",
            "value":12
          }
        },
        {
          "cashback":"",
          "currency":"EUR",
          "description":"",
          "image":"",
          "merchant_item_id":666666,
          "name":"Nice apple",
          "options":[
            
          ],
          "product_url":"",
          "quantity":1,
          "tax_table_selector":"BTW9",
          "unit_price":"35.00",
          "weight":{
            "unit":"KG",
            "value":20
          }
        },
        {
          "cashback":"",
          "currency":"EUR",
          "description":"Shipping",
          "image":"",
          "merchant_item_id":"msp-shipping",
          "name":"Flat Rate - Fixed",
          "options":[
            
          ],
          "product_url":"",
          "quantity":1,
          "tax_table_selector":"none",
          "unit_price":"10.00",
          "weight":{
            "unit":"KG",
            "value":0
          }
        }
      ]
    },
    "status":"initialized",
    "transaction_id":4273483,
    "payment_url":"https://capayable-payment-test.tritac.com/aanbetaling/34bfc991bef24558a5b4f9c168753da1?returnUrl=https%3A%24545F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D4273483&shopOrderExchangeUrl=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D4273483"
  }
}
```
> POST - /orders

```json
{
  "type":"redirect",
  "gateway":"IN3",
  "order_id":"my-order-id-1",
  "currency":"EUR",
  "amount":37485,
  "description":"Test order description",
  "manual":"false",
  "payment_options":{
    "notification_url":"http://www.example.com/client/notification?type=notification",
    "redirect_url":"http://www.example.com/client/notification?type=redirect",
    "cancel_url":"http://www.example.com/client/notification?type=cancel"
  },
  "customer":{
    "ip_address":"45.46.216.114",
    "locale":"nl_NL",
    "first_name":"Testperson-nl",
    "last_name":"",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1039 SC",
    "city":"Amsterdam",
    "country":"NL",
    "email":"example@multisafepay.com"
  },
  "delivery":{
    "first_name":"Testperson-nl",
    "last_name":"",
    "address1":"Kraanspoor",
    "house_number":"39C",
    "zip_code":"1039 SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0612345678",
    "email":"example@multisafepay.com"
  },
  "gateway_info":{
    "birthday":"1970-07-10",
    "gender":"mr",
    "phone":"0612345678"
  },
  "shopping_cart":{
    "items":[
      {
        "name":"Geometric Candle Holders",
        "description":"",
        "unit_price":90,
        "quantity":3,
        "merchant_item_id":"1111",
        "tax_table_selector":"BTW21",
        "weight":{
          "unit":"KG",
          "value":12
        }
      },
      {
        "name":"Nice apple",
        "description":"",
        "unit_price":35,
        "quantity":1,
        "merchant_item_id":"666666",
        "tax_table_selector":"BTW9",
        "weight":{
          "unit":"KG",
          "value":20
        }
      },
      {
        "name":"Flat Rate - Fixed",
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
      "default":{
        "shipping_taxed":"true",
        "rate":0.21
      },
      "alternate":[
        {
          "name":"BTW21",
          "standalone":true,
          "rules":[
            {
              "rate":0.21
            }
          ]
        },
        {
          "name":"BTW9",
          "standalone":true,
          "rules":[
            {
              "rate":0.09
            }
          ]
        },
        {
          "name":"BTW6",
          "standalone":true,
          "rules":[
            {
              "rate":0.06
            }
          ]
        },
        {
          "name":"BTW0",
          "standalone":true,
          "rules":[
            {
              "rate":0
            }
          ]
        },
        {
          "name":"none",
          "standalone":false,
          "rules":[
            {
              "rate":0
            }
          ]
        },
        {
          "name":"FEE",
          "standalone":false,
          "rules":[
            {
              "rate":0
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
    "order_id":"apitool_10088776",
    "payment_url":"https://testpayv2.multisafepay.com/connect/82byiUAWKjrn4350x4fhNCzueapaDGvj8cs/?lang=nl_NL"
  }
}
```
{{< /code-block >}}
{{< description >}}

## in3
See also Payment methods – [in3](/payments/methods/billing-suite/in3).

### in3 - direct

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `IN3`. 

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
`manual` | string | required

Fixed value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object). 

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object

See [delivery (object)](/api/#delivery-object).

----------------
`gateway_info` | object

The customer data (`issuer_id`) required for conducting credit checks.

Contains:  

`birthday` | object

The customer's date of birth.  
Required for credit checks in: DE, NL, DK, BE, AT. 
Optional: CH, NO, FI, SE.
Format: yyyy-mm-dd.

`gender` | string

The customer's personal title.  
Options: `mr`, `mrs`, `miss`. 

`phone` | string

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping_cartitems). 

----------------
`items` | object

See [items (object)](/api/#items-object/).

----------------
`checkout_options` | object

The definitions for the VAT class.

**Response**

----------------
`amount_refunded` | integer

The amount refunded to the customer.

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------
`created` | string

The timestamp for when the order was created.

----------------
`custom_info` | object

See [custom_info (object)](/api/#custom_info).

----------------
`fastcheckout` | string 

Whether this is a [FastCheckout](/payments/methods/fastcheckout/) transaction.  
Options: `YES`, `NO`.

----------------
`modified` | string

The timestamp when the order was last modified.

----------------
`payment_details` | object

See [payment_details (object)](/api/#payment_details-object).

----------------
`payment_methods` | object

See [payment_methods (object)](/api/#payment_methods-object).

----------------
`reason` | string

The capture reason for the order.

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
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

### in3 - redirect

**Parameters**

----------------
`type` | string | required

The payment flow for the checkout process.  
Options: `redirect`, `direct`.

----------------
`gateway` | string | required

The unique gateway identifier to direct the customer straight to the payment method.  
Fixed value: `IN3`. 

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
`manual` | string | required

Fixed value: `false`.

----------------
`payment_options` | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
`customer` | object | required

See [customer (object)](/api/#customer-object).

----------------
`delivery` | object

See [delivery (object)](/api/#delivery-object).

----------------
`gateway_info` | object

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

----------------
`shopping_cart` | object

See [shopping_cart.items (object)](/api/#shopping_cartitems). 

----------------
`checkout_options` | object

The definitions for the VAT class.

**Response**

----------------
`payment_url` | string 

The URL of the page where the customer is redirected from your checkout to complete payment, which may be hosted by [MultiSafepay](/payments/checkout/payment-pages/), the [issuer](/getting-started/glossary/#issuer), or the payment method.

----------------

{{< /description >}}
