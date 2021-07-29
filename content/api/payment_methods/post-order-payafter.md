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
    "description": "Test Order Description",
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

> JSON Response

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
    "description": "Test Order Description",
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

> JSON Response

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
### Redirect - Pay After Delivery

Creates a Pay After Delivery [redirect](/developer/api/difference-between-direct-and-redirect) order.

- All fields must be completed correctly.

- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `direct`, `redirect`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: PAYAFTER.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__custom_info__ | object

custom_info is a 'placeholder' where the merchant can input specific data related to the transaction.

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

All items in the shopping cart, including the tax class.   
If you have a custom integration, include the complete specification of the `shopping_cart`.

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

A specification of the order items to display on the checkout page. For descriptions of these parameters, see [shopping_cart.items](/api/#shopping-cart-items).

----------------

__checkout_options__ | object

The definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

Defines certain customer data (issuer_id) needed for the credit check.                      

----------------
__birthday__ | string

The customer's date of birth.  Format: yyyy-mm-dd. This is required for credit checks. (Required for Klarna & Pay After Delivery, optional for E-Invoicing on request). 

----------------
__bank_account__ | string

The formatted IBAN for the customer. This is required for credit checks. (Required for Pay After Delivery). 

----------------
__phone__ | string

The customer's phone number. Required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer. Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------  

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------


Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

See also [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery).

### Direct - Pay After Delivery

Creates a Pay After Delivery [direct](/developer/api/difference-between-direct-and-redirect) order.

- All fields must be completed correctly.

- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process. Options: `direct`, `redirect`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: PAYAFTER.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__custom_info__ | object

custom_info is a 'placeholder' where the merchant can input specific data related to the transaction.

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

All items in the shopping cart, including the tax class.   
If you have a custom integration, include the complete specification of the `shopping_cart`. 

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

A specification of the order items to display on the checkout page. For descriptions of these parameters, see [shopping_cart.items](/api/#shopping-cart-items).

----------------

__checkout_options__ | object

The definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

Defines certain customer data (issuer_id) needed for the credit check.                      

----------------
__birthday__ | string

The customer's date of birth.  Format: yyyy-mm-dd. This is required for credit checks. (Required for Klarna & Pay After Delivery, optional for E-Invoicing on request). 

----------------
__bank_account__ | string

The formatted IBAN for the customer. This is required for credit checks. (Required for Pay After Delivery). 

----------------
__phone__ | string

The customer's phone number. Required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer. Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------  


Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

See also [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery).

{{< /description >}}
