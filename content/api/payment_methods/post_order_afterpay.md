---
weight: 301
meta_title: "API Reference - Create AfterPay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json

{
    "type": "direct",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test Order Description",
    "manual": "false",
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0612345678",
        "email": "rejection@afterpay.nl"
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

> JSON Response

```shell

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
> POST - /orders

```json

{
    "type": "redirect",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test Order Description",
    "items": "",
    "manual": "false"
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
            },
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
> JSON Response

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13sEMtA491h823BLOx5Upa9H9XGEpYeUEg9/?lang=en_US"
  }
}
```
{{< /code-block >}}
{{< description >}}

## AfterPay
See also [AfterPay](/payments/methods/billing-suite/afterpay/).

### Direct 

- Creates a [direct](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `redirect`, `direct`.

----------------
__gateway__ | string

The unique gateway identifier that directs the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: `AFTERPAY`. 

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`, otherwise it is `string`. Format: Maximum 35 characters.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text displayed with the order in your MultiSafepay account, and on the customer's bank statement (if supported by the bank).  
Max. 200 characters.  
HTML formatting is not supported. To add descriptions in HTML format, use the `items` or `shopping_cart` objects instead.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url). 

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__delivery__ | object

The delivery information for the shipment.  
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__shopping_cart__ | object

All items in the customer's shopping cart, including the tax class.  
If you have a custom integration, include a complete specification of the `shopping_cart` when sending the transaction.

**Note:** For the `shopping_cart` to function correctly, the shipment item requires a `merchant_item_id` parameter with the value `msp-shipping`.

----------------

__items__ | object

A specification of the order items to display on the checkout page.  
For descriptions of these parameters, see [shopping_cart.items](/api/#shopping-cart-items).

----------------

__checkout_options__ | object

The definitions for the VAT class.

----------------
__gateway_info__ | object

Contains the `issuer_id`.

----------------
__birthday__ | object

The customer's date of birth. In the Netherlands and Belgium, this is required for credit checks.
Format: yyyy-mm-dd. 

----------------
__phone__ | string

The customer's phone number. Required for credit checks and to contact the customer in case of non-payment.

----------------
__email__ | string

The email address for sending payment instructions to the customer.

----------------
__gender__ | string

The customer's personal title. Options: `mr`, `mrs`, `miss`. 

----------------
__ip_address__ | string

 The customer's IP address.  
 Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy.  
 For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------

__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`.   

----------------

### Redirect - AfterPay

Creates an AfterPay [redirect](/developer/api/difference-between-direct-and-redirect) order to be paid after delivery.

- For redirect transactions, all fields must be completed properly.

- All the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `redirect`, `direct`.

----------------
__gateway__ | string

The unique gateway ID that immediately directs the customer to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `AFTERPAY`. 

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer, otherwise it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text displayed with the order in your MultiSafepay account, and on the customer's bank statement (if supported by the bank). Max. 200 characters. HTML formatting is not supported. To add descriptions in HTML format, use the `items` or `shopping_cart` objects instead.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url). 

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__delivery__ | object

The delivery information for the shipment.  
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__shopping_cart__ | object

Contains all purchased items, including the tax class. If you have a custom integration, include a complete specification of the `shopping_cart` when sending the transaction.

 **Note:** For the `shopping_cart` to function correctly, the shipment item requires a `merchant_item_id` parameter with the value `msp-shipping`.

----------------
__items__ | object

A specification of the order items to display on the checkout page. For descriptions of these parameters, see API Reference - [shopping_cart.items](/api/#shopping-cart-items).

----------------
__checkout_options__ | object

The definitions for the VAT class.

----------------
__ip_address__ | string

 The customer's IP address.  
 Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

{{< /description >}}
