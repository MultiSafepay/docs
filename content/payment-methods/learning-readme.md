---
title: 'Learning Readme'
category: 6298bd782d1cf4006032e765
order: 800
hidden: true
slug: learning-readme
---
> ✅ Success!
>
> This is a message about great success!

> ✅ Success! This is a message about great success!

> ✅ Success!
> This is a message about great success!

> ⚠️ Warning
> 
> The situation is dire!

> ❗️ Error
> 
> You need to do something fast!

| Header 1| Header 2|
|---|---|
| Something | Something else|
| More | Even more |

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/InesScreenshot.png" align ="center"/>

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/test-mermaid.svg" alt="Our first diagram" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

  ```javascript
      var ApplePayRequest = {
        "countryCode": "NL",
        "currencyCode": "EUR",
        "merchantCapabilities": [
            "supports3DS"
        ], 
        "supportedNetworks": [
        "amex",
        "maestro",
        "masterCard",
        "visa",
        "vPay"
        ],
        "requiredBillingContactFields":[
            "postalAddress",
            "billingAddress"
        ],
        "total":{
            "label": "Your Merchant Name",
            "type": "final",
            "amount": 15.95
        }
    };
    ```
<br>

``` json
{
  "customer": {
    "first_name": "John",
    "last_name": "Doe",
    "house_number": "39",
    "address1": "Kraanspoor",
    "address2": "",
    "city": "Amsterdam",
    "zip_code": "1033 SC",
    "state": "Noord-Holland",
    "country": "NL",
    "locale": "nl_NL", // Set the language and country code
    "phone": "0208500500",
    "email": "example@multisafepay.com",
    "gender": "M",
    "birthday": "1980-12-31",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "referrer": "http://test.com",
    "ip_address": "123.123.123.123",
    "forwarded_ip": "",
    "reference": ""
  }
}
```

# Heading 1

## Heading 2
 
### Heading 3

#### Heading 4

[Hyperlink](/docs/payment-pages/)

- Bullet list
- Bullet 2

1. Numbered list 1
2. Numbered list 2


External link

1. Sign in to your <a href="https://live.actuals.io" target="_blank">Actuals account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<details id="our-first-details-element">
<summary>Our first details element</summary>
<br>

Here is the content of this details element.

---

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)