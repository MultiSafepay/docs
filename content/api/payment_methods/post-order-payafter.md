---
weight: 318
meta_title: "API - Create Pay After Delivery order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
> POST - /orders 

```shell

{
    "type": "redirect",
    "gateway": "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
    "description": "Test Order Description",
    "var1": "",
    "var2": "",
    "var3": "",
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
    "customer": {
        "locale": "us",
        "ip_address": "31.148.195.10",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "state": "",
        "country": "NL",
        "email": "test@example.com",
        "referrer": "http://www.example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "address2": "",
        "house_number": "39",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "state": "",
        "country": "NL",
        "phone": "020 8500 500",
        "email": ""
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
                            "country": "US"
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
    "order_id": "apitool_2710316",
    "payment_url": "https://payv2.multisafepay.com/connect/820UDg9zumqA13QovrRq1YVgpdTVxAlpJAP/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Pay After Delivery
 Creates a Pay After Delivery order.

* All parameters shown are required field(s)

| Parameter                        | Type     | Description                                                                            |
|----------------------------------|----------|----------------------------------------------------------------------------------------|
| type                             | string | Specifies the payment flow for the checkout process. Options: direct, redirect.        |
| gateway                          | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: PAYAFTER. |
| order_id                         | integer / string | The unique identifier from your system for the order. If the values are only numbers the type will be integer otherwise it will be string.                                  |
| currency                         | string | The currency ([ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)) you want the customer to pay with. |
| amount                           | integer | The amount (in cents) that the customer needs to pay.                                  |
| description                      | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max 200 characters. HTML is no longer supported. Use the required 'shopping-cart' object for this. |
| payment_options                  | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/) |
| custom_info                      | object | custom_info is a 'placeholder' where the merchant can input specific data related to the transaction |
| customer                         | object | Contains the personal information of the customer. <i>Values for first_name and last_name require minimum two characters.</i> |  
| delivery                         | object | Contains the delivery information for the shipment. <i>Values for first_name and last_name require minimum two characters.</i> |
| shopping_cart                    | object | Contains all purchased items including tax class.                                      |
| checkout_options                 | object | Defines all tax classes to be used for the shopping cart items.                        |
| gateway_info                     | object | Defines certain customer data (issuer_id) needed for the credit check.                             |
| birthday                         | string | The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. (Required for Klarna & Pay After Delivery, optional for E-Invoicing on request). |
| bank_account                     | string | The formatted IBAN for the customer. This is required for credit checks. (Required for Pay After Delivery). |
| phone                            | string | The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. |
| email                            | string | The email address where the system can send payment instructions to the customer.      |
| ip_address                       | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                              |
| forwarded_ip                     | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                                                                           |

Please note that <i>first_name</i> and <i>last_name</i> in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Make sure you check out our dedicated documentation for [Pay After Delivery](/payment-methods/pay-after-delivery/).
{{% /description %}}