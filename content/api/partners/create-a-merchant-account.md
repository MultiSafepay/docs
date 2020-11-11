---
weight: 710
meta_title: "API - Create a Partner account - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}

> POST - /partners

```shell 

{
    "product": "connect300",
    "company_name": "Company name Partner",
    "address1": "Kraanspoor",
    "address2": "",
    "house_number": "39C"
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


> JSON Response 


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

__Please note: This API call currently only works in a 'Live' environment. The functioning of this API call in the 'Test' environment will follow.__ 

If you have any questions, please contact <integration@multisafepay.com>

**Parameters**

----------------
__product__ | string

Select the desired MultiSafepay subscription: Connect 300, Connect 1000 or FastCheckout. 

----------------
__company_name__ | string

Company name of partner. 

----------------
__address1__ | string

First line of customer’s provided address.   

----------------
__address2__ | string

Second line of customer’s provided address.   

----------------
__zip_code__ | string

Customer’s provided zip / postal code.

----------------
__city__ | integer

Customer’s provided city.                                                                   

----------------
__email__ | string

Customer’s provided email address. Used to send Second Chance emails and in fraud checks.   

----------------
__country__ | string

Customer’s provided country code [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)

----------------
__phone__ | string

Customer’s provided phone number.

----------------
__password__ | string

Supply a password for creating credentials for partner account.   

----------------
__address_apartment__ | string

----------------
__software_partner__ | string

Put on "Anders".

----------------
__partner__ | object

Supply a password for creating credentials for partner account.  

----------------
__api_user__ | string

User ID of partner account.   

----------------
__api_pass__ | string

Password for partner account.

----------------
__contact_details__ | object

----------------
__title__ | string

Mr, Mrs or Ms.   

----------------
__name__ | string

Name of partner.     

----------------
__bank_details__ | object

----------------
__account_number__ | string

Account number of bank. 

----------------
__bank_name__ | string

Name of bank.    

----------------
__country__ | string

Country of bank [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)  

{{% /description %}}