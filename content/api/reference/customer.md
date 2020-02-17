---
weight: 601
meta_title: "API - customer object - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
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

{{< /code-block >}}

{{< description >}}
## customer, object
### locale
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| locale                             | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 

### ip_address
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| ip_address                         | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                            |

### forwarded_ip
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| forwarded_ip                       | string   | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                            |

### first_name
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| first_name                         | string   | The customer’s first name.                                                            |
|

### last_name
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| last_name                          | string   | The customer’s last name.                                                             |
|                                    |          |                                                                                      | 

### address1
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| address1                           | string   | First line of customer’s provided address.                                            |
|                                    |          |                                                                                      | 

### address2
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| address2                           | string   | Second line of customer’s provided address.                                           |
|                                    |          |                                                                                      | 

### house_number
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| house_number                       | string   | Customer's provided house number.                                                     |
|                                    |          |                                                                                      | 

### zip_code
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| zip_code                           | string   | Customer’s provided zip / postal code.                                                |
|                                    |          |                                                                                      | 

### city
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| city                               | string   | Customer’s provided city.                                                             |
|                                    |          |                                                                                      | 

### country
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| country                            | string   | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)                                                                                                           |

### phone
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| phone                              | string   | Customer’s provided phone number.                                                     |
|                                    |          |                                                                                      | 

### email
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| email                              | string   | Customer’s provided email address. Used to send Second Chance emails and in fraud checks.                                                                                                                                 |

{{% /description %}}
