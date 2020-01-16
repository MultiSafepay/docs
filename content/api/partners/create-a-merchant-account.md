---
weight: 710
meta_title: "API - Create a Partner account - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{< code-block >}}

> POST - /partners

```shell 

{
    "product": "connect300",
    "company_name": "Company name Partner",
    "address1": "Kraanspoor",
    "address2": "",
    "zip_code": "1033SC",
    "city": "Amsterdam",
    "email": "",
    "country": "NL",
    "phone": "0205800500",
    "password": "test123",
    "address_apartment": "",
    "software_partner": "Anders",
    "partner": {
        "api_user": "partner-account-user-name",
        "api_pass": "partner-account-password"
    },
    "contact_details": {
        "title": "Mr",
        "name": "your name"
    },
    "bank_details": {
        "account_number": "0123456789",
        "bank_name": "Rabobank",
        "country": "NL"
    }
}
```


JSON Response 


```shell
{
    "success": true,
    "data": {
        "account_id": 11027991,
        "signup_fee": ""
    }
}
```

{{< /code-block >}}

{{< description >}}
## Create a merchant account

| Parameter                   | Type      | Description                                                                                |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------|
| product                     | string    | Select the desired MultiSafepay subscription: Connect 300, Connect 1000 or FastCheckout.    | 
| company_name                | string    | Company name of partner.                                                                    | 
| address1                    | string    | First line of customer’s provided address.                                                  | 
| address2                    | string    | Second line of customer’s provided address.                                                 | 
| zip_code                    | string    | Customer’s provided zip / postal code.                                                      | 
| city                        | string    | Customer’s provided city.                                                                   |
| email                       | string    | Customer’s provided email address. Used to send Second Chance emails and in fraud checks.   | 
| country                     | string    | Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) |     
| phone                       | string    | Customer’s provided phone number.                                                           |
| password                    | string    | Supply a password for creating credentials for partner account.                             | 
| address_apartment           | string    |                                                                                             | 
| software_partner            | string    | Put on "Anders".                                                                            |  
| partner                     | object    |                                                                                             | 
| api_user                    | string    | User ID of partner account.                                                                 | 
| api_ pass                   | string    | Password for partner account.                                                               | 
| contact_details             | object    |                                                                                             | 
| title                       | string    | Mr, Mrs or Ms.                                                                              |
| name                        | string    | Name of partner.                                                                            | 
| bank_details                | object    |                                                                                             | 
| account_number              | string    | Account number of bank.                                                                     | 
| bank_name                   | string    | Name of bank.                                                                               | 
| country                     | string    | Country of bank [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)               |

{{% /description %}}