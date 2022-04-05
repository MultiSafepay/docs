---
weight: 601
meta_title: "API reference - customer object - MultiSafepay Docs"

aliases:
    - /faq/api/ip_address
    - /faq/api/validating-customer-ip-address
    - /developer/api/validating-customer-ip-address/
---
{{< code-block >}}
```json 
{
  "customer":{
    "locale":"nl_NL",
    "ip_address":"123.123.123.123",
    "forwarded_ip":"",
    "first_name":"Simon",
    "last_name":"Smit",
    "gender":"mr",
    "birthday":"1970-07-10",
    "address1":"Kraanspoor",
    "address2":"",
    "house_number":"39C",
    "zip_code":"1033SC",
    "city":"Amsterdam",
    "country":"NL",
    "phone":"0208500500",
    "email":"simonsmit@example.com",
    "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "referrer":"https://example.com",
    "reference": "customer-00001"
  }
}
```

{{< /code-block >}}

{{< description >}}
## customer (object)

The customer's personal information.   

Contains:  

**Parameters**

----------------
`locale` | string | required

Localizes the [payment page](/payment-pages/) with the customer's language, region, and available payment methods.   
For more information, see [Locale parameter](/developer/locale/).  
Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US` (American English). 

----------------
`ip_address` | string | required / recommended 

The customer's IP address.  
Required for [pay later methods](/payment-methods/pay-later/) and [credit cards](/payment-methods/credit-debit-cards/) as part of our [fraud check](/glossaries/credit-cards/#uncleared-transactions), optional but recommended for other payment methods.  
If empty or incorrect (e.g. your IP address instead of the customer's) when required, the transaction status may be **Uncleared**, or even **Declined**.       

----------------
`forwarded_ip` | string | required

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer object when using a proxy.  
To retrieve the customer's IP address:

- If there is a proxy, use `forwarded_ip`.
- Otherwise, use `ip_address`.                        

----------------
`first_name` | string | required

The customer’s first name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations. 

----------------
`last_name` | string | required

The customer’s last name.  
Format: Minimum two characters.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
`gender` | string | required

The customer's gender.   

----------------
`birthday` | string | required

The customer’s birthday.

----------------
`address1` | string | required

The first line of the customer's address. 

----------------
`address2` | string | required

The second line of the customer’s address. 

----------------
`house_number` | string | required

The customer's house number.   

----------------
`zip_code` | string | required

The customer's ZIP/postal code.                                                 

----------------
`city` | string | required

The customer's city of residence.                                           

----------------
`country` | string | required

The customer’s country of residence.   
Format: [ISO 3166-1 country code](https://www.iso.org/iso-3166-country-codes.html).

----------------
`phone` | string | required

The customer's phone number. 

----------------
`email` | string | required

The customer’s email address.   
Used to send [Second Chance](/features/second-chance/) emails and to conduct fraud checks.

----------------
`user_agent` | string | required

A characteristic string that identifies a browser.

----------------
`referrer` | string | required

The unique identifier of where the user/browser originates from.

----------------
`reference` | string | For [recurring payments](/features/recurring-payments/) transactions: required

A unique client-defined identifier for your customer.

See [Recurring Payments orders](/api/#recurring-payments-orders).

----------------

{{% /description %}}
