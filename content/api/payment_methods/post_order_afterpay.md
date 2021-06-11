---
weight: 301
meta_title: "API - Create AfterPay order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "direct",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
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
                "unit_price": "90",
                "quantity": "2",
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "12"
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
                            "rate": "0.00"
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
              "rate": "0.00"
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

```shell

{
    "type": "redirect",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
    "description": "Test Order Description",
    "items": "",
    "manual": "false"
    ...
    "shopping_cart": {
        "items": [
            {
                "name": "Item demo 1",
                "description": "",
                "unit_price": "90",
                "quantity": "2",
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "12"
                }
            },
            {
                "name": "Item shipping - Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": "10",
                "quantity": "1",
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "0"
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
                            "rate": "0.00"
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
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13sEMtA491h823BLOx5Upa9H9XGEpYeUEg9/?lang=en_US"
  }
}
```
{{< /code-block >}}
{{< description >}}

## AfterPay
### Direct - AfterPay

Creates an AfterPay [Direct](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery.

* For direct transactions, all fields must be completed properly.

* All the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway ID that immediately directs the customer to the payment method. Retrieve gateway IDs using a [gateway request](#retrieve-all-gateways). Options: AFTERPAY. 

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are numbers only, the type is integer, otherwise it is string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text displayed with the order in your MultiSafepay Control, and on the customer's bank statement (if supported by the bank). Max. 200 characters. HTML formatting is not supported. To add descriptions in HTML format, use the `items` or `shopping_cart` objects instead.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/faq/api/how-does-the-notification-url-work). 

----------------
__customer__ | object

Contains the customer's personal information. The values for `first_name` and `last_name` require at least 2 characters.

----------------
__delivery__ | object

Contains the delivery information for the shipment. The values for `first_name` and `last_name` require at least 2 characters.

----------------
__shopping_cart__ | object

Contains all purchased items, including the tax class. If you have a custom integration, include a complete specification of the `shopping_cart` when sending the transaction.

 **Note:** For the `shopping_cart` to function correctly, the shipment item requires a `merchant_item_id` parameter with the value `msp-shipping`.

----------------

__items__ | object

Specification of products (items) you want to display on the checkout page. For descriptions of these parameters, see API Reference - [shopping_cart.items](/api/#shopping-cart-items).

----------------

__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object

Contains the `issuer_id`.

----------------
__birthday__ | object

The customer's date of birth. Format: yyyy-mm-dd. This is required for credit checks in NL and BE.

----------------
__phone__ | string

The customer's phone number. This is required for credit checks and to contact the customer in case of non-payment.

----------------
__email__ | string

The email address where the system can send payment instructions to the customer.

----------------
__gender__ | string

The customer's personal title. Options: `mr`, `mrs`, `miss`. 

----------------
__ip_address__ | string

 The customer's IP address. This is required for post-payment methods and credit cards. To validate the customer's IP address, we need to receive the actual IP address of the end user in the [`ip_address`](/faq/api/ip_address) field.

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. For more information, see [`ip_address`](/faq/api/ip_address).

----------------

__close_window__ | bool (optional)

Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.  

----------------

**Note:** The `first_name` and `last_name` fields in both the `customer` and `delivery` objects require at least 2 characters. For Afterpay, we recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

For more information, see [AfterPay](/payment-methods/billing-suite/afterpay).

----------------

### Redirect - AfterPay

Creates an AfterPay [Redirect](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery.

- For redirect transactions, all fields must be completed properly.

- All the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway ID that immediately directs the customer to the payment method. Retrieve gateway IDs using a [gateway request](#retrieve-all-gateways). Options: AFTERPAY. 

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are numbers only, the type is integer, otherwise it is string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text displayed with the order in your MultiSafepay Control, and on the customer's bank statement (if supported by the bank). Max. 200 characters. HTML formatting is not supported. To add descriptions in HTML format, use the `items` or `shopping_cart` objects instead.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/faq/api/how-does-the-notification-url-work). 

----------------
__customer__ | object

Contains the customer's personal information. The values for `first_name` and `last_name` require at least 2 characters.

----------------
__delivery__ | object

Contains the delivery information for the shipment. The values for `first_name` and `last_name` require at least 2 characters.

----------------

__shopping_cart__ | object

Contains all purchased items, including the tax class. If you have a custom integration, include a complete specification of the `shopping_cart` when sending the transaction.

 **Note:** For the `shopping_cart` to function correctly, the shipment item requires a `merchant_item_id` parameter with the value `msp-shipping`.

----------------

__items__ | object

Specification of products (items) you want to display on the checkout page. For descriptions of these parameters, see API Reference - [shopping_cart.items](/api/#shopping-cart-items).

----------------

__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__ip_address__ | string

 The customer's IP address. This is required for post-payment methods and credit cards. To validate the customer's IP address, we need to receive the actual IP address of the end user in the [`ip_address`](/faq/api/ip_address) field.

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------

**Note:** The `first_name` and `last_name` fields in both the `customer` and `delivery` objects require at least 2 characters. For Afterpay, we recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

For more information, see [AfterPay](/payment-methods/billing-suite/afterpay).
{{< /description >}}
