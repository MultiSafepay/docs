---
weight: 318
meta_title: "API Reference - Create a Klarna order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json

{
    "type": "redirect",
    "gateway": "KLARNA",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 26000,
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
                "unit_price": 90,
                "quantity": 2,
                "merchant_item_id": "111111",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 12
                }
            },
            {
                "name": "Item shipping - Flat Rate - Fixed",
                "description": "Shipping",
                "unit_price": 10,
                "quantity": 1,
                "merchant_item_id": "msp-shipping",
                "tax_table_selector": "none",
                "weight": {
                    "unit": "KG",
                    "value": 0
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
                            "rate": 0.00
                        }
                    ]
                }
            ]
        }
    }
}
```
> JSON Response

```json
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
Creates a Klarna [Redirect](/developer/api/difference-between-direct-and-redirect) order to be paid after delivery

Processing transactions with Klarna (the old environment) is only available as a Redirect request.

Klarna Payments (the new environment of Klarna) is available as a Redirect request, although you may use the Direct request if you have your own integration. The JSON request remains the same for both Klarna and Klarna payments.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: KLARNA.

----------------
__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.     

----------------

__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------

__shopping_cart__ | object

All items in the shopping cart, including the tax class.   
If you have a custom integration, include the complete specification of the `shopping_cart`.

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__quantity__ | integer

The quantity of a specific item in the shopping cart. Decimals are not accepted and the value should be stated as a whole number e.g. '13'

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

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------    

Please note that *first_name* and *last_name* in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Klarna](/payments/methods/billing-suite/klarna) on our documentation page.

### Redirect - Klarna Payments
Creates a Klarna Payments [Redirect](/developer/api/difference-between-direct-and-redirect) order to be paid after delivery

Please note this request is for Klarna Payments. This request can only be processed as a redirect request.

* Redirect transaction requires all fields completed properly

* All of the following parameters are required fields.


**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: KLARNA.

----------------

__order_id__ | integer / string

Your unique identifier for the order. If the values are numbers only, the type is integer. Otherwise, it is string.

----------------

__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html).  

----------------

__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------

__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------

__payment_options__ | object

Contains the `redirect_url`, `cancel_url` and [`notification_url`](/developer/api/notification-url).

----------------

__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.     

----------------
__delivery__ | object

Contains the delivery information for the shipment. _Values for first_name and last_name require minimum two characters._

----------------

__shopping_cart__ | object

All items in the shopping cart, including the tax class.   
If you have a custom integration, include the complete specification of the `shopping_cart`. 

 __Please note__: In order for the shopping_cart to function correctly, the shipment item requires a parameter ‘merchant_item_id’ with the value ‘msp-shipping'

----------------

__items__ | object

Specification of products (items) which can be set in order to be displayed on the checkout page. The descriptions of the shopping cart parameters can be viewed in the [shopping_cart.items](/api/#shopping-cart-items) API section.

----------------

__unit_price__ | float

The unit price (in decimals) of the specific product excluding VAT. A maximum of 10 decimal places is accepted. 

----------------

__quantity__ | integer

The quantity of a specific item in the shopping cart. Decimals are not accepted and the value should be stated as a whole number e.g. '13'

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

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------    

Please note that *first_name* and *last_name* in both _customer_ and _delivery_ objects require minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Klarna](/payments/methods/billing-suite/klarna) on our documentation page.

{{< /description >}}
