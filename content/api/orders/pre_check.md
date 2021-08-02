---
weight: 220
meta_title: "API Reference - Pay After Delivery pre-check - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
> POST - /json/padprechecks

```json
{
    "type": "checkout",
    "gateway" : "PAYAFTER",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 9000,
    "description": "Order description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "simonsmit@example.com",
        "referrer": "http://multisafepay-demo.com/plugingroup/testtool/client/json-test",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Simon",
        "last_name": "Smit",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "simonsmit@example.com"
    },
    "shopping_cart": {
        "items": [
            {
                "name": "Geometric Candle Holders",
                "description": "",
                "unit_price": 90,
                "quantity": 1,
                "merchant_item_id": "hdd006",
                "tax_table_selector": "BTW0",
                "weight": {
                    "unit": "KG",
                    "value": 1
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
                    "price": 7,
                    "allowed_areas": [
                        "NL",
                        "ES"
                    ]
                },
                {
                    "name": "Seur - Spain",
                    "price": 7,
                    "allowed_areas": [
                        "NL",
                        "ES"
                    ]
                },
                {
                    "name": "TNT - verzending BE en FR",
                    "price": 12,
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
                            "rate": 0.00
                        }
                    ]
                },
                {
                    "name": "2",
                    "rules": [
                        {
                            "rate": 0.09,
                            "country": "NL"
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


```json
{
  "success": true,
  "data": {
    "result": false | true
  }
}

```
{{< /code-block >}}

{{< description >}}

## Pay After Delivery pre-check

Submit data related to a Pay After Delivery order and customer for MultiSafepay to conduct a pre-check to determine whether to accept the order. 

If not accepted, the customer must select another payment method to complete payment.


**Parameters**

----------------

__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`.

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__currency__ | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__gateway_info__ | object | required

Contains:  

__issuer_id__ | string | required

The unique identifier of the gateway issuer.  
See [Retrieve gateway issuers](/api/#gateway-issuers). 

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).

----------------
__delivery__ | object

See [delivery (object)](/api/#delivery-object).

----------------

__shopping_cart__ | object

See [shopping_cart.items (object)](/api/#shopping_cartitems).

----------------

__items__ | object

See [items (object)](/api/#items-object/).

{{< /description >}}