---
weight: 301
meta_title: "API - Create AfterPay order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}


> POST - /orders

```shell

{
    "type": "direct",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "37380",
    "description": "Test Order Description",
    "var1": "",
    "var2": "",
    "var3": "",
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
        "address1": "Neherkade",
        "address2": "",
        "house_number": "1/XI",
        "zip_code": "2521VA",
        "city": "Gravenhage",
        "state": "",
        "country": "NL",
        "email": "rejection@afterpay.nl",
        "referrer": "http://multisafepay-demo.com/plugingroup/dev/magento/1901/checkout/cart/",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Neherkade",
        "address2": "",
        "house_number": "1/XI",
        "zip_code": "2521VA",
        "city": "Gravenhage",
        "state": "",
        "country": "NL",
        "phone": "0612345678",
        "email": "rejection@afterpay.nl"
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
                    "standalone": true,
                    "rules": [
                        {
                            "rate": "0.21"
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": "0.06"
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": "0"
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": "0"
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "none",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": "0.00"
                        }
                    ]
                },
                {
                    "name": "2",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": "0.0825",
                            "country": "US"
                        },
                        {
                            "rate": "0.08375",
                            "country": "US"
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
        "var1": null,
        "var2": null,
        "var3": null,
        "items": "",
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
            "address1": "Neherkade",
            "address2": null,
            "house_number": "39c",
            "zip_code": "1033SC",
            "city": "Gravenhage",
            "state": null,
            "country": "NL",
            "country_name": null,
            "phone1": "0612345678",
            "phone2": "",
            "email": "test@example.com"
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
                    "standalone": true,
                    "name": "BTW21",
                    "rules": [
                        {
                            "rate": 0.21,
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": true,
                    "name": "BTW6",
                    "rules": [
                        {
                            "rate": 0.06,
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": true,
                    "name": "BTW0",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": "",
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": "",
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": "",
                    "name": "FEE",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": "",
                    "name": "none",
                    "rules": [
                        {
                            "rate": "0.00",
                            "country": ""
                        }
                    ]
                },
                {
                    "standalone": true,
                    "name": 2,
                    "rules": [
                        {
                            "rate": 0.0825,
                            "country": "US"
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
{{% /code %}}

{{% description %}}
## AfterPay

Creates an AfterPay order to be paid after delivery.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| type                               | string | Specifies the payment flow for the checkout process. Options: direct, redirect.       |
| gateway                            | string | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: AFTERPAY. |
| order_id                           | string | The unique identifier from your system for the order. |
| currency                           | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                             | integer | The amount (in cents) that the customer needs to pay. |
| description                        | string | A free text description which will be shown with the order in MultiSafepay Control. If the customers bank supports it this description will also be shown on the customers bank statement. Max 200 characters. HTML is no longer supported. Use the required 'shopping-cart' object for this. |
| payment_options                    | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/) |                                                                                     
| customer                           | object | Contains the personal information of the customer. <i>Values for first_name and last_name require minimum two characters.</i> |                                                                                   
| delivery                           | object | Contains the delivery information for the shipment. <i>Values for first_name and last_name require minimum two characters.</i> | |                                                                                    
| shopping_cart                      | object | Contains all purchased items including tax class.                                   |
| checkout_options                   | object | Contains the definitions for the VAT class. |
| gateway_info                       | object | Contains the issuer_id. |                                                                                    |
| birthday                           | string | The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. Required in countries: DE, NL, DK, BE, AT Optional in countries: CH, NO, FI, SE. |
| phone                              | string | The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. |
| email                              | string | The email address where the system can send payment instructions to the customer. |
| gender                             | string | The gender salutation of the customer. Options: mr, mrs, miss. |
| personal_number  -                 | string | The personal ID of the customer. Required in countries: FI, SE, NO Optional in countries: DE, AT, CH, BE, NL, DK. |
| ip_address                         | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                            |
| forwarded_ip                       | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                          |
Please note that <i>first_name</i> and <i>last_name</i> in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Make sure you check out our dedicated documentation for [AfterPay](/payment-methods/afterpay/).

{{% /description %}}