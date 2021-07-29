---
weight: 313
meta_title: "API Reference - Create E-invoicing order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json

{
    "type": "direct",
    "gateway": "EINVOICE",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test Order Description", 
    "items": "",
    "manual": false,
    "gateway_info": {
        "birthday": "1980-01-30",
        "bankaccount": "0417164300",
        "phone": "0208500500",
        "email": "example@multisafepay.com"
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    ...
    "shopping_cart": {
        "items": [
            {
                "name": "Item demo 1",
                "description": "",
                "unit_price": 90,
                "quantity": 2,
                "merchant_item_id": "666666",
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
        "transaction_id": 2340676,
        "order_id": "my-order-id-1",
        "created": "2017-09-29T16:13:10",
        "currency": "EUR",
        "amount": 26000,
        "description": "Test Order Description",
        "items": "",
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2017-09-29T16:13:10",
        "customer": {
        ...
        "payment_details": {
            "recurring_id": null,
            "type": "",
            "account_id": 10071970,
            "account_holder_name": null,
            "external_transaction_id": 2379429850
        },
        "shopping_cart": {
            "items": [
                {
                    "name": "Item demo 1",
                    "description": "",
                    "unit_price": "90.00",
                    "currency": "EUR",
                    "quantity": 2,
                    "merchant_item_id": 666666,
                    "tax_table_selector": "none",
                    "cashback": "",
                    "image": "",
                    "product_url": "",
                    "weight": {
                        "unit": "KG",
                        "value": 12
                    },
                    "options": []
                },
                {
                    "name": "Item shipping - Flat Rate - Fixed",
                    "description": "Shipping",
                    "unit_price": "10.00",
                    "currency": "EUR",
                    "quantity": 1,
                    "merchant_item_id": "msp-shipping",
                    "tax_table_selector": "none",
                    "cashback": "",
                    "image": "",
                    "product_url": "",
                    "weight": {
                        "unit": "KG",
                        "value": 0
                    },
                    "options": []
                }
            ]
        },
        "checkout_options": {
            "default": {
            },
            "alternate": [
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0.00,
                            "country": ""
                        }
                    ]
                }
            ]
        },
        "order_adjustment": {
            "total_adjustment": "0.00",
            "total_tax": "0.00"
        },
        "order_total": 260.00,
        "costs": [],
        "payment_url": "http://www.example.com/client/?action=notification&type=redirect&transactionid=2340676",
        "cancel_url": "http://www.example.com/client/?action=notification&type=cancel&transactionid=2340676"
    }
}
```

> POST -/orders
```json
{
    "type": "redirect",
    "gateway": "EINVOICE",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
    "description": "Test Order Description",
    "manual": false,
    "gateway_info": {
        "email": "example@multisafepay.com"
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    ...
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 90,
                "quantity": 2,
                "merchant_item_id": "11111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
            {
                "name": "Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": 10,
                "quantity": 1,
                "merchant_item_id": "123456",
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
> JSON response

```json
{
    "success": true,
    "data": {
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/82v6HsoQhaR823uIZ7hexDMwQyielzLrdox/?lang=nl_NL"
    }
}
```

{{< /code-block >}}

{{< description >}}
## E-Invoicing
See also Payment methods – [E-Invoicing](/payments/methods/billing-suite/e-invoicing).
### Direct

- Creates a [direct](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `direct`, `redirect`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `EINVOICE`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

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
__birthday__ | string

The customer's date of birth.  
Format: yyyy-mm-dd.                             

----------------
__bank_account__ | string

The customer's (formatted) international bank account number (IBAN).  
This is required for credit checks. 

----------------
__phone__ | string

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address for sending payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer.  
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.      

----------------
__forwarded_ip__ | string

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy.  
For more information, see [Validating customer IP addresses](/developer/api/validating-customer-ip-address).

----------------
__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 


### Redirect

- Creates a [redirect](/developer/api/difference-between-direct-and-redirect) order.
- All fields must be completed correctly.
- All of the following parameters are required fields, except `ip_address`.

**Parameters**

----------------
__type__ | string

The payment flow for the checkout process.  
Options: `direct`, `redirect`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).  
Options: `EINVOICE`.

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

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
__email__ | string

The email address for sending payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer.  
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.      

----------------
__forwarded_ip__ | string

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [Validating customer IP addresses](/developer/api/validating-customer-ip-address).

{{< /description >}}
