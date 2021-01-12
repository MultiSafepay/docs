---
weight: 318
meta_title: "API - Create a Klarna order - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
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
        "email": "example@multisafepay.com"
    },
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
    ...
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
        "payment_url": "https://payv2.multisafepay.com/connect/12oyNt6GDQS823vwlxIbfBe45H8HYqoQWAi/?lang=nl_NL"
    }
}
```

{{< /code-block >}}

{{< description >}}
## Klarna
### Redirect - Klarna
Creates a Klarna [Redirect](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery

Klarna is available as both a direct and redirect request. 
However, Klarna Payments (the new environment of Klarna) is only available as a redirect request. The direct request is no longer supported by Klarna Payments. 

* Direct transaction requires all fields completed properly

* All parameters shown are required field(s)

{{< alert-notice >}} __Please note__: In order for the shopping_cart to work correctly, the shipment item requires a special 'merchant_item_id'. This parameter is called 'msp-shipping' and can be seen in the JSON code. {{< /alert-notice >}}

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: KLARNA.

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

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------
__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart.

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page.

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

----------------
__phone__ | string

The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__gender__ | string

The gender of the customer. (Required for Klarna, optional for Pay After Delivery and E-Invoicing) Options: male, female.

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)      

----------------
__forwarded_ip__ | string

The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------    

Please note that _first_name_ and _last_name_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Klarna](/payment-methods/billing-suite/klarna) on our documentation page.

### Redirect - Klarna Payments
Creates a Klarna Payments [Redirect](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery

Please note this request is for Klarna Payments. This request can only be processed as a redirect request.

* Redirect transaction requires all fields completed properly

* All parameters shown are required field(s)

{{< alert-notice >}} __Please note__: In order for the shopping_cart to work correctly, the shipment item requires a special 'merchant_item_id'. This parameter is called 'msp-shipping' and can be seen in the JSON code. {{< /alert-notice >}}


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: KLARNA.

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

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------
__shopping_cart__ | object

Contains all purchased items including tax class. If you are using your own integration, the transaction should be sent including the complete specification of the shopping_cart.

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page.

----------------
__checkout_options__ | object

Contains the definitions for the VAT class.

----------------
__gateway_info__ | object                                                              

----------------
__phone__ | string

The phone number where the customer can be reached. This is required for credit checks and to contact the customer in case of non-payment. 

----------------
__email__ | string

The email address to which the system can send payment instructions to the customer.  

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)      

----------------
__forwarded_ip__ | string

The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)

----------------    

Please note that _first_name_ and _last_name<_ in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Klarna](/payment-methods/billing-suite/klarna) on our documentation page.

{{< /description >}}