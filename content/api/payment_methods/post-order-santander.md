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
    "description": "Test order description",
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

- See also Payment methods – [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand).  
- Direct only.

**Parameters**

----------------
__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`. 

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__gateway__ | string | required

The unique gateway ID to direct the customer straight to the payment method.  
Fixed value: `SANTANDER`.

----------------
__currency__ | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__customer__ | object | required

See [customer (object)](/api/#customer-object).    

----------------
__gateway_info__ | object                                                              

The customer data (`issuer_id`) required for conducting credit checks.

Contains:

__birthday__ | object | required

The customer's date of birth.  
In the Netherlands and Belgium, this is required for credit checks.  
Format: yyyy-mm-dd. 

__gender__ | string | required

The customer's personal title.  
Options: `mr`, `mrs`, `miss`. 

__phone__ | string | required

The customer's phone number.  
Required for credit checks and to contact the customer in case of non-payment.

__email__ | string | required

The email address for sending payment instructions to the customer.

----------------
__custom_info__ | object

See [custom_info (object)](/api/#custom_info).

----------------


{{< /description >}}
