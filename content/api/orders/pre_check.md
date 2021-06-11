---
weight: 220
meta_title: "API - Order pre-check - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
> POST - /json/padprechecks

```shell
{
    "type": "checkout",
    "gateway" : "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "9000",
    "description": "Order description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "184.43.169.4",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "test@multisafepay.com",
        "referrer": "http://multisafepay-demo.com/plugingroup/testtool/client/json-test",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0612345678",
        "email": "test@multisafepay.com"
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": "90",
                "quantity": "1",
                "merchant_item_id": "hdd006",
                "tax_table_selector": "BTW0",
                "weight": {
                    "unit": "KG",
                    "value": "1"
                }
            }
        ]
    },
    "checkout_options": {
        "rounding_policy": {
            "mode": "UP",
            "rule": "PER_ITEM"
        },
        "shipping_methods": {
            "flat_rate_shipping": [
                {
                    "name": "TNT - verzending NL",
                    "price": "7",
                    "allowed_areas": [
                        "NL",
                        "ES"
                    ]
                },
                {
                    "name": "Seur - Spain",
                    "price": "7",
                    "allowed_areas": [
                        "NL",
                        "ES"
                    ]
                },
                {
                    "name": "TNT - verzending BE en FR",
                    "price": "12",
                    "excluded_areas": [
                        "NL",
                        "FR",
                        "ES"
                    ]
                }
            ]
        },
        "tax_tables": {
            "alternate": [
                {
                    "name": "BTW0",
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
                            "rate": "0.09",
                            "country": "US"
                        }
                    ]
                }
            ]
        }
    },
    "custom_fields": [
        {
            "name": "acceptagreements",
            "type": "checkbox",
            "label": "This label",
            "description_right": {
                "value": [
                    {
                        "nl": "Ik ga akkoord met de <a href='http://test.nl' target='_blank'>algemene voorwaarden</a>"
                    },
                    {
                        "en": "I accept the <a href='http://test.nl' target='_blank'>terms and conditions</a>"
                    }
                ]
            },
            "validation": {
                "type": "regex",
                "data": "^[1]$",
                "error": [
                    {
                        "nl": "U dient akkoord te gaan met de algemene voorwaarden"
                    },
                    {
                        "en": "Please accept the terms and conditions"
                    }
                ]
            }
        },
        {
            "standard_type": "companyname"
        }
    ]
}
```


> JSON Response


```shell
{
  "success": true,
  "data": {
    "result": false | true
  }
}

```
{{< /code-block >}}

{{< description >}}

## Pay After Delivery Pre-check

A Pay After Delivery order can have a pre-check carried out. This type of request contains all data related to the order and customer. 

The pre-check decides if MultiSafepay accepts the order or whether the customer is required to selected a different payment methods to complete the transaction.


**Parameters**

----------------

__type__ | string

Specifies the payment flow for the checkout process. Options: direct.

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
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__gateway_info__ | object

----------------
__issuer_id__ | string

Contains the [issuer_id](/api/#gateway-issuers)  

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__customer__ | object

Contains the personal information of the customer. Values for first_name and last_name require minimum two characters.

----------------
__delivery__ | object

Contains the delivery information for the shipment. Values for first_name and last_name require minimum two characters.

----------------

__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart.

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page. The descriptions of these parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.




{{< /description >}}