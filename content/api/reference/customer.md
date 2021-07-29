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

**Parameters**

__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.   Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).   
Default: `en_US`. 

__ip_address__ | string

The IP address of the customer. Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.       

__forwarded_ip__ | string

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. [More info](/developer/api/validating-customer-ip-address)                                 

__first_name__ | string

The customer’s first name.

__last_name__ | string

The customer’s last name.   

__gender__ | string

The customer's gender.   

__birthday__ | string

The customer’s birthday.

__address1__ | string

The first line of the customer's address. 

__address2__ | string

Second line of customer’s provided address. 

__house_number__ | string

Customer's provided house number.   

__zip_code__ | string

The customer's ZIP/ postal code.                                                 

__city__ | string

The customer's city of residence.                                           

__country__ | string

The customer’s country of residence.   
Format: [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html).

__phone__ | string

The customer's phone number. 

__email__ | string

The customer’s email address.   
Used to send Second Chance emails and to conduct fraud checks.

__user_agent__ | string

A characteristic string that identifies a browser.

__referrer__ | string

Identification of where the user/browser is originating from.

{{% /description %}}
