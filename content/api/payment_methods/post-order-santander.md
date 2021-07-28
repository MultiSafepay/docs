---
weight: 324
meta_title: "API Reference - Create a Santander Betaal per Maand order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "SANTANDER",
    "currency": "EUR",
    "amount": 50000,
    "description": "Test Order Description",
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
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "email": "test@example.com",
        "referrer": "http://example.com",
        "user_agent": "Mozilla//5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "gateway_info": {
        "birthday": "1970-07-10",
        "gender": "male",
        "phone": "0612345678",
        "email": "youremail@email.com"
    }
}
```
> JSON Response

```shell
{
    "success": true,
    "data": {
        "transaction_id": 2333720,
        "order_id": "my-order-id-1",
        "created": "2017-08-07T10:07:07",
        "currency": "EUR",
        "amount": 100000,
        "description": "product description",
        "var1": null,
        "var2": null,
        "var3": null,
        "items": null,
        "amount_refunded": 0,
        "status": "initialized",
        "financial_status": "initialized",
        "reason": "",
        "reason_code": "",
        "fastcheckout": "NO",
        "modified": "2017-08-07T10:07:07",
        "customer": {
            "locale": "nl_NL",
        ...
        },
        "payment_details": {
            "recurring_id": null,
            "type": "SANTANDER",
            "account_id": null,
            "account_holder_name": null,
            "external_transaction_id": null
        },
        "costs": [
            {
                "transaction_id": 406933,
                "description": "Cost Description",
                "type": "SYSTEM",
                "amount": 0.49
            }
        ],
        "payment_url": "https://retailersowtest.santander.nl/EDurables/Home.aspx?guid=XXXXX"
    }
}
```
{{< /code-block >}}

{{< description >}}
## Santander Betaal per Maand
Creates a Santander Betaal per Maand [Direct](/developer/api/difference-between-direct-and-redirect) order.

* Direct transaction requires all fields completed properly

* All of the following parameters are required fields.

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect, paymentlink. |

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways). Options: SANTANDER.

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
__custom_info__ | object

custom_info is a 'placeholder' where the merchant can input specific data related to the transaction.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.     

----------------
__gateway_info__ | object                                                              

Contains the information of the customer needed for the credit check.                     

----------------
__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/developer/api/validating-customer-ip-address)      

----------------
__forwarded_ip__ | string

 The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. For more information, see [`ip_address`](/developer/api/validating-customer-ip-address).

----------------  

__close_window__ | bool (optional)


To display the MultiSafepay payment page in a new window that automatically closes after the payment is completed, set to `True`.   
Options: `True`, `False`. 

----------------

__Note: The ip_address parameter is not required, although its use is recommended to help detect fraudulent payments.__

Please note that _first_name_ and _last_name_ in the _customer_ object requires minimum two characters per entry. Failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).

Read more about [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand) on our documentation page.
{{< /description >}}
