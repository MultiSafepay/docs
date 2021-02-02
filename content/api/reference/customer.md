---
weight: 601
meta_title: "API - customer object - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
```shell 
"locale": "nl_NL",
```

```shell
"ip_address": "31.148.195.10",
```

```shell 
"forwarded_ip": "",
```

```shell
"first_name": "customer's first name",
```

```shell
"last_name": "customer's last name",
```

```shell
"gender": "",
```

```shell
"birthday": "",
```

```shell 
"address1": "Kraanspoor",
```

```shell 
"address2": "customer's address",
```

```shell 
"house_number": "39",
```

```shell 
"zip_code": "1033SC",
```

```shell 
"city": "Amsterdam",
```

```shell 
"country": "Netherlands",
```

```shell 
"phone": "0208500500",
```

```shell 
"email": "integration@multisafepay.com",
```

```shell 
"user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
```

```shell 
"referrer": "http://example.com"
```

{{< /code-block >}}

{{< description >}}
## customer, object
### locale 


**Parameter**

__locale__ | string

Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. 

----------------


### ip_address

**Parameter**

__ip_address__ | string

The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address)       

----------------

### forwarded_ip

**Parameter**

__forwarded_ip__ | string

The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address)                                 

----------------

### first_name

**Parameter**

__first_name__ | string

The customer’s first name.

----------------

### last_name

**Parameter**

__last_name__ | string

The customer’s last name.   

----------------

### gender

**Parameter**

__gender__ | string

The customer's gender.   

----------------

### birthday

**Parameter**

__birthday__ | string

The customer’s birthday.

----------------

### address1

**Parameter**

__address1__ | string

First line of customer’s provided address. 

----------------

### address2

**Parameter**

__address2__ | string

Second line of customer’s provided address. 

----------------

### house_number

**Parameter**

__house_number__ | string

Customer's provided house number.   

----------------

### zip_code

**Parameter**

__zip_code__ | string

Customer’s provided zip / postal code.                                                 

----------------

### city

**Parameter**

__city__ | string

Customer’s provided city.                                           

----------------

### country

**Parameter**

__country__ | string

Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)

----------------

### phone

**Parameter**

__phone__ | string

Customer’s provided phone number. 

----------------

### email

**Parameter**

__email__ | string

Customer’s provided email address. Used to send Second Chance emails and in fraud checks.

----------------

### user_agent

**Parameter**

__user_agent__ | string

A characteristic string that identifies a browser.

----------------

### referrer

**Parameter**

__referrer__ | string

Identification of where the user/browser is originating from.

----------------

{{% /description %}}
