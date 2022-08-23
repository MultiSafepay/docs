---
title: 'FastCheckout'
category: 62bd999547298d001abc714c
order: 5
hidden: false
slug: 'fastcheckout'
---

FastCheckout is MultiSafepay's own complete checkout solution for a fast, frictionless checkout experience and increased <<glossary:conversion>>.

## How it works

FastCheckout is highly flexible and fully customizable. It consists of modular checkout steps (billing, shipping, and payment) that let you create a tailored experience for each customer. 

New features and payment methods are made available automatically. No updates or upgrades are required. FastCheckout is optimized for both mobile and desktop.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOExample.png" align ="center"/>
<br>

The FastCheckout page comprises 4 elements that can be displayed or hidden, and configured per transaction.

You can also include custom fields, e.g. terms and conditions, newsletter signup.

#### Billing element

- Gathers the customer's billing information
- Auto-highlights any incorrect or incomplete details

#### Shipping element

- Gathers the customer's shipping address
- Displays available shipping options
- Supports multiple carriers, pickup locations, and standard and express options
- Automatically updates the order total with any shipping fee 

#### Payment element

- Dynamically displays payment methods based on the customer's country, device, and the order amount
- Styles how <<glossary:issuers>> are displayed and how to connect to their environment
- Validates input instantly and suggests actionable errors
- Saves space by bundling all available credit cards in a single gateway that auto-detects the card type

  <details id="issuer-example">
  <summary>Examples of how issuers can be displayed</summary>
  <br>

  <div style="text-align: center">List</div>
  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOIssuersList.png" align ="center"/>
  <br>

  <div style="text-align: center">Dropdown</div>
  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOIssuersDropdown.png" align ="center"/>
  <br>

  <div style="text-align: center">Buttons</div>
  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOIssuersButtons.png" align ="center"/>

  </details>

  <details id="cards-example">
  <summary>Example of single credit card gateway</summary>
  <br>

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOCreditCards.png" align ="center"/>

  </details>

#### Shopping cart element

- Provides clear breakdown of price and taxes, with no hidden costs
- Updates automatically when different shipping options are selected
- Supports discounts

## Activation

Email a request to activate FastCheckout for specific sites under your account to <sales@multisafepay.com>

Specify in your request the relevant [site IDs](/docs/sites#site-id-api-key-and-security-code). 

## Integration

To integrate FastCheckout as a hosted page via our API, see:

- API reference – [Create order](/reference/createorder) > FastCheckout order
- Recipes – [Create a FastCheckout page](/recipes/create-a-fastcheckout-page).

To embed FastCheckout into your site, see [FastCheckout JavaScript integration](/docs/fastcheckout-integration/).

<br>

---
# User guide

## Branding

You can add your brand's logo at the top of the FastCheckout page.

<details id="how-to-add-logo">
<summary>How to add your logo to the FastCheckout page</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Settings** > **Website settings**.
3. From the **Payment logo (FastCheckout)** list, select the relevant logo. 

</details>

## Language

FastCheckout pages are supported in 6 languages.

<details id="supported-languages">
<summary>Supported languages</summary>
<br>

- Dutch
- English
- French
- German
- Italian
- Spanish

</details>

The customer can also change the page to their preferred language using the flag toggle.

You can also localize FastCheckout pages to automatically hide payment methods that are not available in the customer's country, and to display local variants. 

See API reference > [Create order](/reference/createorder) > FastCheckout order > `customer` object > `locale` parameter.

❗️ The `locale` parameter can be overriden on initializing the JavaScript application, or when the customer changes the flag toggle.  

<details id="locale-codes">
<summary>Locale codes per language and country</summary>
<br>

| Code | Language & country |
|---|---|
| de_AT | German (Austria) |
| de_DE | German (Germany) |
| en_US | American English |
| fr_BE | French (Belgium) |
| fr_FR | French (France) |
| it_IT | Italian |
| nl_BE | Dutch (Belgium) |
| nl_NL | Dutch (Netherlands) |
| es_ES | Spanish |

</details>

<details id="locale-example">
<summary>Locale example</summary>
<br>

```json
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

</details>

## Payment methods

FastCheckout supports all payment methods, including QR codes, **except** for Pay After Delivery and E-Invoicing.

## Second Chance

You can follow up abandoned FastCheckout pages with [Second Chance](/features/second-chance/).

## Split payments

[Split payment](/docs/split-payments/) are supported for FastCheckout.

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)