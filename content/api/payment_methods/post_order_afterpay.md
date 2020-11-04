---
weight: 301
meta_title: "API - Create AfterPay order - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "direct",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "37380",
    "description": "Test Order Description",
    "items": "",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "31.148.195.10",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "approved@afterpay.nl",
        "referrer": "http://multisafepay-demo.com/plugingroup/dev/magento/1901/checkout/cart/",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "approved@afterpay.nl"
    },
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0612345678",
        "email": "rejection@afterpay.nl"
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": "90",
                "quantity": "3",
                "merchant_item_id": "1111",
                "tax_table_selector": "BTW21",
                "weight": {
                    "unit": "KG",
                    "value": "12"
                }
            },
            {
                "name": "Nice apple",
                "description": "",
                "unit_price": "35",
                "quantity": "1",
                "merchant_item_id": "666666",
                "tax_table_selector": "BTW6",
                "weight": {
                    "unit": "KG",
                    "value": "20"
                }
            },
            {
                "name": "Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": "10.0000",
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
            "default": {
                "shipping_taxed": "true",
                "rate": "0.21"
            },
            "alternate": [
                {
                    "name": "BTW21",
                    "rules": [
                        {
                            "rate": "0.21"
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "rules": [
                        {
                            "rate": "0.06"
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0"
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0"
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "2",
                    "rules": [
                        {
                            "rate": "0.0825",
                            "country": "NL"
                        },
                        {
                            "rate": "0.08375",
                            "country": "NL"
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
        "transaction_id": 2340676,
        "order_id": "my-order-id-1",
        "created": "2017-09-29T16:13:10",
        "currency": "EUR",
        "amount": 26000,
        "description": "Test Order Description",
        "amount_refunded": 0,
        "status": "completed",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2017-09-29T16:13:10",
        "customer": {
            "locale": "en_US",
            "first_name": "Testperson-nl",
            "last_name": "Approved",
            "address1": "Kraanspoor",
            "house_number": "39C",
            "zip_code": "1033 SC",
            "city": "Amsterdam",
            "country": "NL",
            "country_name": null,
            "phone1": "0208500500",
            "email": "example@multisafepay.com"
        },
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
                    "name": "Item demo 2",
                    "description": "",
                    "unit_price": "35.00",
                    "currency": "EUR",
                    "quantity": 2,
                    "merchant_item_id": 666666,
                    "tax_table_selector": "none",
                    "cashback": "",
                    "image": "",
                    "product_url": "",
                    "weight": {
                        "unit": "KG",
                        "value": 20
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
                "shipping_taxed": true,
                "rate": 0.21
            },
            "alternate": [
                {
                    "name": "BTW21",
                    "rules": [
                        {
                            "rate": 0.21,
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "rules": [
                        {
                            "rate": 0.06,
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "name": 2,
                    "rules": [
                        {
                            "rate": 0.0825,
                            "country": "NL"
                        },
                        {
                            "rate": 0.08375,
                            "country": "NL"
                        }
                    ]
                }
            ]
        },
        "order_adjustment": {
            "total_adjustment": "0.00",
            "total_tax": "0.00"
        },
        "order_total": "260.00",
        "costs": [],
        "payment_url": "http://www.example.com/client/?action=notification&type=redirect&transactionid=2340676",
        "cancel_url": "http://www.example.com/client/?action=notification&type=cancel&transactionid=2340676"
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
    "amount": 37485,
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "customer": {
        "locale": "nl_NL",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "example@multisafepay.com"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "example@multisafepay.com"
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 90,
                "quantity": 3,
                "merchant_item_id": "1111",
                "tax_table_selector": "BTW21",
                "weight": {
                    "unit": "KG",
                    "value": "12"
                }
            },
            {
                "name": "Nice apple",
                "description": "",
                "unit_price": 35,
                "quantity": 1,
                "merchant_item_id": "666666",
                "tax_table_selector": "BTW9",
                "weight": {
                    "unit": "KG",
                    "value": "20"
                }
            },
            {
                "name": "Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": 10,
                "quantity": 1,
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
            "default": {
                "shipping_taxed": "true",
                "rate": 0.21
            },
            "alternate": [
                {
                    "name": "BTW21",
                    "rules": [
                        {
                            "rate": 0.21
                        }
                    ]
                },
                {
                    "name": "BTW9",
                    "rules": [
                        {
                            "rate": 0.09
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "rules": [
                        {
                            "rate": 0.06
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "rules": [
                        {
                            "rate": 0
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
        "payment_url": "https://payv2.multisafepay.com/connect/137LMJCe0GP8238bseHBnf97COSGr7mKGku/?lang=nl_NL"
    }
}
```
{{< /code-block >}}
{{< description >}}

## AfterPay
### Direct - AfterPay

Creates an AfterPay [Direct](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

{{< alert-notice >}} __Please note__: In order for the shopping_cart to work correctly, the shipment item requires a special 'merchant_item_id'. This parameter is called 'msp-shipping' and can be seen in the JSON code. {{< /alert-notice >}}

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: AFTERPAY. 

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

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters_.

----------------
__shopping_cart__ | object

Contains all purchased items including tax class.                                   

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object

Contains the issuer_id.

----------------
__birthday__ | object

The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. Required in countries: DE, NL, DK, BE, AT Optional in countries: CH, NO, FI, SE.

----------------
__phone__ | string

The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment.

----------------
__email__ | string

The email address where the system can send payment instructions to the customer.

----------------
__gender__ | string

The gender salutation of the customer. Options: mr, mrs, miss. 

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------
Please note that _first_name<_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [AfterPay](/payment-methods/afterpay) on our documentation page.

----------------

### Redirect - AfterPay

Creates an AfterPay [Redirect](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

{{< alert-notice >}} __Please note__: In order for the shopping_cart to work correctly, the shipment item requires a special 'merchant_item_id'. This parameter is called 'msp-shipping' and can be seen in the JSON code. {{< /alert-notice >}}


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: AFTERPAY. 

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

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters_.

----------------
__shopping_cart__ | object

Contains all purchased items including tax class.                                   

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------

Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [AfterPay](/payment-methods/afterpay) on our documentation page.
{{< /description >}}

