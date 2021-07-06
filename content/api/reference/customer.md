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

Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. 

__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)       

__forwarded_ip__ | string

The [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header of the customer request when using a proxy. [More info](/faq/api/ip_address)                                 

__first_name__ | string

The customer’s first name.

__last_name__ | string

The customer’s last name.   

__gender__ | string

The customer's gender.   

__birthday__ | string

The customer’s birthday.

__address1__ | string

First line of customer’s provided address. 

__address2__ | string

Second line of customer’s provided address. 

__house_number__ | string

Customer's provided house number.   

__zip_code__ | string

Customer’s provided zip / postal code.                                                 

__city__ | string

Customer’s provided city.                                           

__country__ | string

Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)

__phone__ | string

Customer’s provided phone number. 

__email__ | string

Customer’s provided email address. Used to send Second Chance emails and in fraud checks.

__user_agent__ | string

A characteristic string that identifies a browser.

__referrer__ | string

Identification of where the user/browser is originating from.

{{% /description %}}
