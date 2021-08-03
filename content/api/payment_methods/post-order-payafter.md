---
weight: 323
meta_title: "API Reference - Create a Pay After Delivery order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders 

```json

{
    "type": "redirect",
    "gateway": "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test order description",
    "items": "",
    "manual": "false",
    "gateway_info": {
        "birthday": "1980-01-30",
        "bankaccount": "0417164300",
        "phone": "0208500500",
        "email": "example@example.com"
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
...
    "shopping_cart": {
        "items": [
            {
                "name": "Item demo 1",
                "description": "",
                "unit_price": 90,
                "quantity": 2,
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
              }
            }
            {
                "name": "Item shipping - Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": 10,
                "quantity": 1,
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 0
                }
            }
        ]
    },
    "checkout_options": {
        "tax_tables": {
            "default": {
            },
            "alternate": [
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0.00
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
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/820UDg9zumqA13QovrRq1YVgpdTVxAlpJAP/?lang=nl_NL"
  }
}
```
> POST - /orders

```json

{
    "type": "direct",
    "gateway": "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test order description",
    "manual": "false",
    "gateway_info": {
        "birthday": "1979-02-22",
        "bank_account": "0417164300",
        "phone": "0208500500",
        "email": "example@multisafepay.com"
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    ...
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 90,
                "quantity": 2,
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
        ]
    },
    "checkout_options": {
        "tax_tables": {
            "alternate": [
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0.00
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
  "success": true,
  "data": {
    "amount": 26000,
    "amount_refunded": 0,
    "checkout_options": {
      "alternate": [
        {
          "name": "none",
          "rules": [
            {
              "country": "",
              "rate": 0.00
            }
          ]
        }
      ],
      "default": {
        "rate": 0.21,
        "shipping_taxed": true
      }
    },
    "costs": [
      {
        "amount":,
        "description": "",
        "transaction_id": 2045938,
        "type": "SYSTEM"
      },
      {
        "amount":,
        "description": "",
        "transaction_id": 2045939,
        "type": "SYSTEM"
      }
    ],
    "created": "2019-01-12T13:55:38",
    "currency": "EUR",
    "custom_info": {
    },
    ...
    
    "status": "uncleared",
    "transaction_id": 4022655,
    "payment_url": " https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US",
    "cancel_url": " http://www.example.com/client/notification?type=cancel&transactionid=apitool"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Pay After Delivery

See also Payment methods – [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery).

### Pay After Delivery - redirect

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Fixed value: `redirect`.  

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `PAYAFTER`.

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
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__items__ | object
  
See [items (object)](/api/#items-object/).

----------------
__manual__ | string | required

Fixed value: `false`.

----------------
__gateway_info__ | object  | required

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

__birthday__ | object | required

The customer's date of birth.  
In the Netherlands and Belgium, this is required for credit checks.  
Format: yyyy-mm-dd. 

__bankaccount__ | string | required

The customer's formatted international bank account number (IBAN).  
This is required for credit checks.   

__phone__ | string | required

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

__email__ | string | required

The email address for sending payment instructions to the customer.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object). 

----------------
__delivery__ | object

See [delivery (object)](/api/#delivery-object).

----------------
__shopping_cart__ | object

See [shopping_cart.items (object)](/api/#shopping_cartitems).

----------------
__checkout_options__ | object

The definitions for the VAT class.

----------------
__custom_info__ | object

See [custom_info (object)](/api/#custom_info).

----------------


### Pay After Delivery - direct

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Fixed value: `direct`.  

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `PAYAFTER`.

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
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__manual__ | string | required

Fixed value: `false`.

----------------
__gateway_info__ | object  | required

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

__birthday__ | object | required

The customer's date of birth.  
In the Netherlands and Belgium, this is required for credit checks.  
Format: yyyy-mm-dd. 

__bankaccount__ | string | required

The customer's formatted international bank account number (IBAN).  
This is required for credit checks.   

__phone__ | string | required

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

__email__ | string | required

The email address for sending payment instructions to the customer.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------
__delivery__ | object

See [delivery (object)](/api/#delivery-object).

----------------
__shopping_cart__ | object

See [shopping_cart.items (object)](/api/#shopping_cartitems).

----------------
__items__ | object
  
See [items (object)](/api/#items-object/).

----------------
__checkout_options__ | object

The definitions for the VAT class. 

----------------
__custom_info__ | object

See [custom_info (object)](/api/#custom_info).

----------------

{{< /description >}}
