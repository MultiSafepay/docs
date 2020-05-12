---
weight: 52
meta_title: "API - Discount added as unit price - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< description >}}
## Discount added as unit price 
A discount added as seperate discount rule may conflict in refunding with postpaid payment methods. Therefore, it is advised to add the discount as unit price. As a result, no negative order rule is created, which means that refunding from a postpaid payment method will not cause a conflict.
{{% /description %}}

{{< code-block >}}
> Example with 20% discount calculated in all unit prices:

```shell 
{
    "type": "redirect",
    "gateway": "PAYAFTER",
    "order_id": "apitool_5313092",
    "currency": "EUR",
    "amount": 20800,
    "description": "Test Order Description",
    "var1": "",
    "var2": "",
    "var3": "",
    "items": "",
    "manual": false,
    "gateway_info": {
        "birthday": "1980-01-30",
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
    "plugin": {
        "shop": "ApiTestTool",
        "plugin_version": "1.0.0",
        "shop_version": "1",
        "partner": "partner",
        "shop_root_url": "https://multisafepay.com"
    },
    "customer": {
        "locale": "us",
        "ip_address": "80.123.456.789",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39c",
        "zip_code": "1033 SC",
        "city": "AMSTERDAM",
        "state": "",
        "country": "NL",
        "email": "example@multisafepay.com"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39c",
        "zip_code": "1033 SC",
        "city": "AMSTERDAM",
        "state": "",
        "country": "NL",
        "phone": "",
        "email": ""
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 72,
                "quantity": 2,
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
            {
                "name": "Nice apple",
                "description": "",
                "unit_price": 28,
                "quantity": 2,
                "merchant_item_id": "333333",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 20
                }
            },
            {
                "name": "Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": 8,
                "quantity": 1,
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 0
                }
            },
            {
                "name": "20% discount on all items",
                "description": "Discount",
                "unit_price": 0,
                "quantity": 1,
                "merchant_item_id": "discount",
                "tax_table_selector": "none"
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
                            "rate": 0.00
                        }
                    ]
                },
                {
                    "name": "0.0000",
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "0.0000",
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
                            "rate": 0.00
                        }
                    ]
                },
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": 0.00
                        }
                    ]
                },
                {
                    "name": "2",
                    "rules": [
                        {
                            "rate": 0.0825,
                            "country": "US"
                        },
                        {
                            "rate": 0.08375,
                            "country": "US"
                        }
                    ]
                }
            ]
        }
    }
}
```
{{< /code-block >}}