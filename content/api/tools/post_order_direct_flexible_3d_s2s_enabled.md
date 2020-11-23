---
weight: 1330
---
{{< code-block >}}

> POST - /orders 

```shell 

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 10,
    "gateway": "CREDITCARD",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "89.20.162.110",
        "forwarded_ip": "",
        "first_name": "Testperson-nl",
        "last_name": "Approved",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "example@multisafepay.com",
        "referrer": "http://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "gateway_info": {
        "flexible_3d": true,
        "card_number": "",
        "card_holder_name": "",
        "card_expiry_date": "",
        "card_cvc": ""
    }
}
```


> JSON Response


```shell
{
  "success": true,
  "data": {
    "amount": 10,
    "amount_refunded": 0,
    "costs": [],
    "created": "2020-02-24T15:11:23",
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
      "country_name": Netherlands,
      "email": "example@multisafepay.com",
      "first_name": "Testperson-nl",
      "house_number": "39C",
      "last_name": "Approved",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "zip_code": "1033 SC"
    },
    "description": "Test Product Description",
    "fastcheckout": "NO",
    "financial_status": "initialized",
    "items": null,
    "modified": "2020-02-24T15:11:23",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_holder_name": "",
      "account_id": null,
      "card_expiry_date": ,
      "external_transaction_id": null,
      "last4": ,
      "recurring_id": null,
      "recurring_model": null,
      "type": "MASTERCARD"
    },
    "payment_methods": [
      {
        "account_holder_name": "",
        "amount": 10,
        "card_expiry_date": ,
        "currency": "EUR",
        "description": "Test Product Description",
        "payment_description": "MasterCard",
        "status": "initialized",
        "type": "MASTERCARD"
      }
    ],
    "reason": "3DS Enrolled",
    "reason_code": "",
    "related_transactions": null,
    "status": "initialized",
    "transaction_id": 335244060,
    "var1": null,
    "var2": null,
    "var3": null,
    "customer_verification": {
      "html": "<html>\n <head>\n <title>PaReq Form Submission</title>\n <script type=\"text/javascript\">\n function onLoadHandler(){ document.getElementById('PaReqForm').submit(); }\n </script>\n </head>\n <body onLoad=\"onLoadHandler();\">\n <form id=\"PaReqForm\" action=\"https://www.securesuite.co.uk/ing_retail/tdsecure/opt_in_dispatcher.jsp?VAA=B\" method=\"post\">\n <noscript>\n <center><br/>\n <h1>Processing your Transaction</h1>\n <h2>JavaScript is currently disabled or not supported by your browser.</h2><br/>\n <h3>Please click Proceed to continue the processing of your transaction.</h3>\n <input type=\"submit\" value=\"Proceed\"/>\n </center>\n </noscript>\n <input type=\"hidden\" name=\"PaReq\" value=\"eJxVkslu2zAQhl/FyL3iKss0JgTSOkhzUBEkvrg3mhrbCqwlFNXaefoOvdQtIAjzDZf5/xnCchcQ\r\nF2/ox4AWShwGt8VJXd3feZ1XxUZzqaZGy02+LtTaOOlm1bQQSvE7Cy8Pr/hh4ReGoe5aKzKeSWBX\r\npNuC37k2WnD+4+vzDyunRmracUFoMDwvrOA8fcDOCK1r0C4f35aT9AN2YvDd2MZwtLmcAbsCjGFv\r\ndzH2c8aacR/rwW2wd8cvFTZd5ruG9ftxW7fb0I09izhEillDFtvYMZEVZ8XpFmA3uS9jigaqeqgr\r\nu3r3n6v3/a5sHvXPxUqVy/KzfMrF+un3PbC0AyoX0UouOZdST4SeCzGXCtgpD65JcsknOT+H0KcK\r\nD7f8vww0i4CtP1pTJK9XAjz0XUvKLUn+G0OFg7d96KrRx0mCUPeR+k/V0wqwm5tv39MofKQua14I\r\nYZSQxmjNc5OGclpIVWpqrVSckhcAlo6yy7ypU6dnQtF/z+cPnVPCWQ==\"/>\n <input type=\"hidden\" name=\"TermUrl\" value=\"https://pay.multisafepay.com/direct/complete/?mspid=335263060\"/>\n <input type=\"hidden\" name=\"MD\" value=\"b73b9a2a8d671330null,c45d7f40236942f5b73b9a2a8d671330\"/>\n </form>\n </body>\n</html>\n",
      "type": "form"
    },
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL",
    "cancel_url": "http://www.example.com/client/notification?type=cancel&transactionid=apitool_"
  }
}
```
{{< /code-block >}}

{{< description >}}

### Direct Server to Server, Flexible 3D set on _true_

Flexible 3D is a feature that allows you to enable/disable 3D secure at API level. The Flexible 3D mandates whether or not a transaction should be completed with the 3D secure verification or not.

Credit card transactions which are processed with the 3D Secure protocol require a form of authentication of the customer during the payment process. Setting Flexible 3D to _false_ will disable the verfication process, while activating Flexible 3D secure will override the rules of the Dynamic 3D settings, meaning that payments will not be enrolled with a 3D authentication.

**__Please note__: Starting January 1st 2021, we no longer support [Flexible 3D](https://docs.multisafepay.com/tools/flexible_3d/) with merchants based in Europe due to PSD2 regulations.**

**Parameters**

----------------
__type__ | string

Specifies the payment flow for the checkout process. Options: direct.

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: CREDITCARD.

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

Contains personal information about the customer.

----------------
__gateway_info__ | object

Defines certain customer data (payment details).

----------------
__flexible_3d__ | boolean

True, enable the 3D secure authentication. False, disable the 3D secure authentication.

----------------

{{< /description >}}