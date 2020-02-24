---
weight: 318
meta_title: "API - Create Klarna order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "redirect",
    "gateway": "KLARNA",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
    "description": "Test Order Description",
    "items": "",
    "manual": "false",
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "male",
        "phone": "0208500500",
        "email": "youremail@email.com"
    },
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
        "email": "test@example.com",
        "referrer": "http://www.example.com",
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
        "email": "example@multisafepay.com"
    },
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
                "name": "Item demo 2",
                "description": "",
                "unit_price": "35",
                "quantity": "2",
                "merchant_item_id": "666666",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "20"
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
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/13sEMtA491h823BLOx5Upa9H9XGEpYeUEg9/?lang=en_US"
  }
}
```
> POST - /orders

```shell
{
    "type": "redirect",
    "gateway": "KLARNA",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "31500",
    "description": "Test Order Description",
    "manual": "false",
    "gateway_info": {
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
        "shop_root_url": "http://multisafepay.com"
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "example@multisafepay.com",
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
        "email": "example@multisafepay.com"
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": "90",
                "quantity": "3",
                "merchant_item_id": "1111111",
                "tax_table_selector": "none",
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
                "merchant_item_id": "222222",
                "tax_table_selector": "none",
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
        "order_id": "my-order-id-1",
        "payment_url": "https://payv2.multisafepay.com/connect/12oyNt6GDQS823vwlxIbfBe45H8HYqoQWAi/?lang=nl_NL"
    }
}
```

{{< /code-block >}}

{{< description >}}
## Klarna
### Direct - Klarna
Creates a Klarna order to be paid after delivery

Klarna is available as both a direct and redirect request. 
However, Klarna Payments (the new environment of Klarna) is only available as a redirect request. The direct request is no longer supported by Klarna Payments. 

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: direct, redirect.        |
| gateway                         | string | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways). Options: KLARNA. |
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer needs to pay.                                   |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
| payment_options                 | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/). |
| customer                        | object | Contains personal information about the customer. <i>Values for first_name and last_name require minimum two characters.</i> |
| delivery                        | object | Contains the delivery information for the shipment. <i>Values for first_name and last_name require minimum two characters.</i>  |
| shopping_cart                   | object | Contains all purchased items including tax class.                                       |
| checkout_options                | object | Contains the definitions for the VAT class. |                    |
| gateway_info                    | object | |
| phone                           | string | The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. |
| email                           | string | The email address where the system can send payment instructions to the customer.       |
| gender                          | string | The gender of the customer. (Required for Klarna, optional for Pay After Delivery and E-Invoicing) Options: male, female.                                                                                                    |
| ip_address                      | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                              |
| forwarded_ip                   | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/).                                                                                                                           |    

Please note that <i>first_name</i> and <i>last_name</i> in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Make sure you check out our dedicated documentation for [Klarna](/payment-methods/klarna/).

### Redirect - Klarna (Klarna Payments)
Creates a Klarna Payments Redirect order to be paid after delivery

Please note this request is for Klarna Payments. This request can only be processed as a redirect request.

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: direct, redirect.        |
| gateway                         | string | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways). Options: KLARNA. |
| order_id                        | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer needs to pay.                                   |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer’s bank supports it this description will also be shown on the customer’s bank statement. Max. 200 characters. HTML is no longer supported. Use the ‘items’ or ‘shopping_cart’ objects for this. |
| payment_options                 | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/). |
| customer                        | object | Contains personal information about the customer. <i>Values for first_name and last_name require minimum two characters.</i> |
| delivery                        | object | Contains the delivery information for the shipment. <i>Values for first_name and last_name require minimum two characters.</i>  |
| shopping_cart                   | object | Contains all purchased items including tax class.                                       |
| checkout_options                | object | Contains the definitions for the VAT class. |                    |
| gateway_info                    | object | |
| phone                           | string | The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. |
| email                           | string | The email address where the system can send payment instructions to the customer.       |
| ip_address                      | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/).                                                                                              |
| forwarded_ip                   | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/).                                                                                                                           |    

Please note that <i>first_name</i> and <i>last_name</i> in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Make sure you check out our dedicated documentation for [Klarna](/payment-methods/klarna/).
{{< /description >}}