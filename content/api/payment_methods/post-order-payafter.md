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

Creates a Pay After Delivery [Redirect](/developer/api/difference-between-direct-and-redirect) order.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: PAYAFTER.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/developer/api/notification-url)

----------------
__custom_info__ | object

custom_info is a 'placeholder' where the merchant can input specific data related to the transaction.

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.     

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------

__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart.

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

Defines certain customer data (issuer_id) needed for the credit check.                      

----------------
__birthday__ | string

The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. (Required for Klarna & Pay After Delivery, optional for E-Invoicing on request). 

----------------
__bank_account__ | string

The formatted IBAN for the customer. This is required for credit checks. (Required for Pay After Delivery). 

----------------
__phone__ | string

The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------  

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------


Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery) on our documentation page.

### Direct - Pay After Delivery

Creates a Pay After Delivery [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: PAYAFTER.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in your MultiSafepay account. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/developer/api/notification-url)

----------------
__custom_info__ | object

custom_info is a 'placeholder' where the merchant can input specific data related to the transaction.

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.     

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------
__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart. 

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

Defines certain customer data (issuer_id) needed for the credit check.                      

----------------
__birthday__ | string

The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. (Required for Klarna & Pay After Delivery, optional for E-Invoicing on request). 

----------------
__bank_account__ | string

The formatted IBAN for the customer. This is required for credit checks. (Required for Pay After Delivery). 

----------------
__phone__ | string

The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------  


Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery) on our documentation page.

{{< /description >}}
