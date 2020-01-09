---
weight: 601
meta_title: "API - customer object - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}
```shell 

"locale": "nl_NL",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| locale                             | string   | Displays the correct language and payment methods on the payment page. It also has an influence on sending the set email templates. Use the format ab_CD with [ISO 639](https://www.iso.org/iso-639-language-codes.html) language codes and [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes. Default: en_US. | 



```shell

 "ip_address": "31.148.195.10",
 ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| ip_address                         | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                            |

```shell 

 "forwarded_ip": "",
 ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| forwarded_ip                       | string   | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                            |

```shell
 
 "first_name": "customer's first name",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| first_name                         | string   | The customer’s first name.                                                            |
|



```shell

"last_name": "customer's last name",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| last_name                          | string   | The customer’s last name.                                                             |
|                                    |          |                                                                                      | 

```shell 

 "address1": "Kraanspoor",
 ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| address1                           | string   | First line of customer’s provided address.                                            |
|                                    |          |                                                                                      | 

```shell 

"address2": "customer's address",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| address2                           | string   | Second line of customer’s provided address.                                           |
|                                    |          |                                                                                      | 

```shell 

  "house_number": "39",
  ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| house_number                       | string   | Customer's provided house number.                                                     |
|                                    |          |                                                                                      | 

```shell 

  "zip_code": "1033SC",
  ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| zip_code                           | string   | Customer’s provided zip / postal code.                                                |
|                                    |          |                                                                                      | 


```shell 

"city": "Amsterdam",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| city                               | string   | Customer’s provided city.                                                             |
|                                    |          |                                                                                      | 


```shell 

"country": "Netherlands",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| country                            | string   | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)                                                                                                           |


```shell 

 "phone": "0208500500",
 ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| phone                              | string   | Customer’s provided phone number.                                                     |
|                                    |          |                                                                                      | 


```shell 

"email": "integration@multisafepay.com",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| email                              | string   | Customer’s provided email address. Used to send Second Chance emails and in fraud checks.                                                                                                                                 |


{{% /code %}}

{{% description %}}
## customer, object
{{% /description %}}
