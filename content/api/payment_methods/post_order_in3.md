---
weight: 301
meta_title: "API - Create an in3 order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "direct",
    "gateway": "IN3",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 37485,
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    },
    "customer": {
        "ip_address": "89.45.467.110",
        "locale": "nl_NL",
        "first_name": "Testperson-nl",
        "last_name": "",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "example@multisafepay.com"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "example@multisafepay.com"
    },
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0612345678"
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
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.21
                        }
                    ]
                },
                {
                    "name": "BTW9",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.09
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.06
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "none",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "standalone": false,
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
    "amount": 37485,
    "amount_refunded": 0,
    "checkout_options": {
      "alternate": [
        {
          "name": "BTW21",
          "rules": [
            {
              "country": "",
              "rate": "0.21"
            }
          ],
          "standalone": true
        },
        {
          "name": "BTW9",
          "rules": [
            {
              "country": "",
              "rate": "0.09"
            }
          ],
          "standalone": true
        },
        {
          "name": "BTW6",
          "rules": [
            {
              "country": "",
              "rate": "0.06"
            }
          ],
          "standalone": true
        },
        {
          "name": "BTW0",
          "rules": [
            {
              "country": "",
              "rate": "0.00"
            }
          ],
          "standalone": true
        },
        {
          "name": "none",
          "rules": [
            {
              "country": "",
              "rate": "0.00"
            }
          ],
          "standalone": ""
        },
        {
          "name": "FEE",
          "rules": [
            {
              "country": "",
              "rate": "0.00"
            }
          ],
          "standalone": ""
        }
      ],
      "default": {
        "rate": 0.21,
        "shipping_taxed": true
      }
    },
    "costs": [],
    "created": "2020-08-19T14:55:46",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "city": "Amsterdam",
      "country": "NL",
      "country_name": null,
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": 39C,
      "last_name": "",
      "locale": "nl_NL",
      "phone1": "0612345678",
      "zip_code": "1039 SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": "<table border=\"0\" cellpadding=\"5\" width=\"100%\">\n<tr>\n<th width=\"10%\"><font size=\"2\" face=\"Verdana\">Aantal </font></th>\n<th align=\"left\"></th>\n<th align=\"left\"><font size=\"2\" face=\"Verdana\">Details </font></th>\n<th width=\"19%\" align=\"right\"><font size=\"2\" face=\"Verdana\">Prijs </font></th>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">3</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Geometric Candle Holders</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">90.00</font>\n</td>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">1</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Nice apple</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">35.00</font>\n</td>\n</tr>\n<tr>\n<td align=\"center\"><font size=\"2\" face=\"Verdana\">1</font></td>\n<td width=\"6%\"></td>\n<td width=\"65%\"><font size=\"2\" face=\"Verdana\">Flat Rate - Fixed</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">10.00</font>\n</td>\n</tr>\n<tr bgcolor=\"#E9F1F7\">\n<td colspan=\"3\" align=\"right\"><font size=\"2\" face=\"Verdana\">BTW:</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">59.85</font>\n</td>\n</tr>\n<tr bgcolor=\"#E9F1F7\">\n<td colspan=\"3\" align=\"right\"><font size=\"2\" face=\"Verdana\">Totaal:</font></td>\n<td align=\"right\">&euro;<font size=\"2\" face=\"Verdana\">374.85</font>\n</td>\n</tr>\n</table>",
    "modified": "2020-08-19T14:55:46",
    "order_adjustment": {
      "total_adjustment": 59.85,
      "total_tax": 59.85
    },
    "order_id": "my-order-id-1",
    "order_total": 374.85,
    "payment_details": {
      "account_holder_name": null,
      "account_id": "1970-07-10",
      "external_transaction_id": "34bfc991bef24558a5b4f9c168753da1",
      "recurring_id": null,
      "recurring_model": null,
      "type": "IN3"
    },
    "payment_methods": [
      {
        "account_id": "1970-07-10",
        "amount": 37485,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "34bfc928374rhjnf9368753da1",
        "payment_description": "in3",
        "status": "initialized",
        "type": "IN3"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "shopping_cart": {
      "items": [
        {
          "cashback": "",
          "currency": "EUR",
          "description": "",
          "image": "",
          "merchant_item_id": 1111,
          "name": "Geometric Candle Holders",
          "options": [],
          "product_url": "",
          "quantity": 3,
          "tax_table_selector": "BTW21",
          "unit_price": "90.00",
          "weight": {
            "unit": "KG",
            "value": 12
          }
        },
        {
          "cashback": "",
          "currency": "EUR",
          "description": "",
          "image": "",
          "merchant_item_id": 666666,
          "name": "Nice apple",
          "options": [],
          "product_url": "",
          "quantity": 1,
          "tax_table_selector": "BTW9",
          "unit_price": "35.00",
          "weight": {
            "unit": "KG",
            "value": 20
          }
        },
        {
          "cashback": "",
          "currency": "EUR",
          "description": "Shipping",
          "image": "",
          "merchant_item_id": "msp-shipping",
          "name": "Flat Rate - Fixed",
          "options": [],
          "product_url": "",
          "quantity": 1,
          "tax_table_selector": "none",
          "unit_price": "10.00",
          "weight": {
            "unit": "KG",
            "value": 0
          }
        }
      ]
    },
    "status": "initialized",
    "transaction_id": 4273483,
    "payment_url": "https://capayable-payment-test.tritac.com/aanbetaling/34bfc991bef24558a5b4f9c168753da1?returnUrl=https%3A%24545F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D4273483&shopOrderExchangeUrl=https%3A%2F%2Ftestpay.multisafepay.com%2Fdirect%2Fcomplete%2F%3Fmspid%3D4273483"
  }
}
```
> POST - /orders

```shell

{
    "type": "redirect",
    "gateway": "IN3",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 37485,
    "description": "Test Order Description",
    "manual": "false",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel"
    },
    "customer": {
        "ip_address": "45.46.216.114",
        "locale": "nl_NL",
        "first_name": "Testperson-nl",
        "last_name": "",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1039 SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "example@multisafepay.com"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1039 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0612345678",
        "email": "example@multisafepay.com"
    },
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0612345678"
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
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.21
                        }
                    ]
                },
                {
                    "name": "BTW9",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.09
                        }
                    ]
                },
                {
                    "name": "BTW6",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0.06
                        }
                    ]
                },
                {
                    "name": "BTW0",
                    "standalone": true,
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "none",
                    "standalone": false,
                    "rules": [
                        {
                            "rate": 0
                        }
                    ]
                },
                {
                    "name": "FEE",
                    "standalone": false,
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
    "order_id": "apitool_10088776",
    "payment_url": "https://testpayv2.multisafepay.com/connect/82byiUAWKjrn4350x4fhNCzueapaDGvj8cs/?lang=nl_NL"
  }
}
```
{{< /code-block >}}
{{< description >}}

## in3
### Direct - in3

Creates an in3 [Direct](/faq/api/difference-between-direct-and-redirect/) order to be paid in installments.

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: IN3. 

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

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters_.

----------------
__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page.

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

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)

----------------
Please note that _first_name<_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [in3](/payment-methods/billing-suite/in3/) on our documentation page.

----------------

### Redirect - in3

Creates an in3 [Redirect](/faq/api/difference-between-direct-and-redirect/) order to be paid in installments.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: redirect, direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a [gateway request](#retrieve-all-gateways) Options: IN3. 

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

Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/) 

----------------
__customer__ | object

Contains the personal information of the customer. _Values for first_name and last_name require minimum two characters_.

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters_.

----------------
__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page.

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__ip_address__ | string

 The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)

----------------
__forwarded_ip__ | string

 The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)

----------------

Read more about [in3](/payment-methods/billing-suite/in3/) on our documentation page.
{{< /description >}}

