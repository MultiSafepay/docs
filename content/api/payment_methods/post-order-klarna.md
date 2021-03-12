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
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": ""
    },
    "plugin": {
        "shop": "my-shop",
        "plugin_version": "1.0.0",
        "shop_version": "1",
        "partner": "partner",
        "shop_root_url": "http://multisafepay.com"
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "127.0.0.1",
        "forwarded_ip": "127.0.0.1",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": 39C,
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0612345678",
        "email": "example@multisafepay.com",
        "disable_send_email": false,
        "referrer": "http://test.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "delivery": {
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": 39C,
        "zip_code": "1033 SC",
        "city": "Amsterdam",
        "country": "NL"
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

## Klarna
### Redirect - Klarna
Creates a Klarna [Redirect](/faq/api/difference-between-direct-and-redirect) order to be paid after delivery

Processing transactions with Klarna (the old environment) is only available as a Redirect request.

Klarna Payments (the new environment of Klarna) is available as a Redirect request, although you may use the Direct request if you have your own integration. The JSON request remains the same for both Klarna and Klarna payments.

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

Contains an array of all purchased items.

__unit_price__ | float

The unit price (in decimals) of the specific product excluding VAT. A maximum of 10 decimal places is accepted. 

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

Please note that *first_name* and *last_name* in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Klarna](/payment-methods/billing-suite/klarna) on our documentation page.

{{< /description >}}