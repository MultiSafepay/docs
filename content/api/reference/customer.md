---
weight: 601
meta_title: "API Reference - customer object - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```json 
{
"customer": {
	"locale": "nl_NL",
	"ip_address": "123.123.123.123",
	"forwarded_ip": "",
	"first_name": "Simon",
	"last_name": "Smit",
	"gender": "mr",
	"birthday": "1970-07-10",
	"address1": "Kraanspoor",
	"address2": "",
	"house_number": "39C",
	"zip_code": "1033SC",
	"city": "Amsterdam",
	"country": "NL", 
	"phone": "0208500500",
	"email": "simonsmit@example.com",
	"user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
	"referrer": "http://example.com"
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

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`. 

----------------
`ip_address` | string | optional but recommended

The IP address of the customer.  
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods.  
MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.       

----------------
`forwarded_ip` | string | required

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy.  
For more information, see [Validating customer IP addresses](/developer/api/validating-customer-ip-address).                         

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
Used to send [Second Chance](/payments/boost/second-chance/) emails and to conduct fraud checks.

----------------
`user_agent` | string | required

A characteristic string that identifies a browser.

----------------
`referrer` | string | required

The unique identifier of where the user/browser originates from.

----------------
`reference` | string | For tokenization transactions: required

See [Create token transaction](/api/#create-token-transaction).

----------------

{{% /description %}}
