---
weight: 301
meta_title: "API - Create AfterPay order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders

```shell

{
    "type": "direct",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
    "description": "Test Order Description",
    "manual": "false",
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "mr",
        "phone": "0612345678",
        "email": "rejection@afterpay.nl"
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
                "unit_price": "90",
                "quantity": "2",
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": "12"
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
                            "rate": "0.00"
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
    "amount": 26000,
    "amount_refunded": 0,
    "checkout_options": {
      "alternate": [
        {
          "name": "none",
          "rules": [
            {
              "country": "",
              "rate": "0.00"
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
> POST - /orders

```shell

{
    "type": "redirect",
    "gateway": "AFTERPAY",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "26000",
    "description": "Test Order Description",
    "items": "",
    "manual": "false"
    ...
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
            "alternate": [
                {
                    "name": "none",
                    "rules": [
                        {
                            "rate": "0.00"
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

__unit_price__ | decimal

The unit price (in decimals) of the specific product. A maximum of 10 decimal places is accepted.   

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object

Contains the issuer_id.

----------------
__birthday__ | object

The birth date of the customer in the format yyyy-mm-dd. This is required for credit checks. Required in countries: NL, BE

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

Read more about [AfterPay](/payment-methods/billing-suite/afterpay) on our documentation page.

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

__unit_price__ | decimal

The unit price (in decimals) of the specific product. A maximum of 10 decimal places is accepted.   

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

Read more about [AfterPay](/payment-methods/billing-suite/afterpay) on our documentation page.
{{< /description >}}

