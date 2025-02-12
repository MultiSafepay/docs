---
title: 'FastCheckout'
category: 62bd999547298d001abc714c
order: 0
hidden: true
slug: 'fastcheckout'
---

<blockquote class="callout callout_warning">
    <h3 class="callout-heading false">Closed beta phase</h3>
</blockquote>

<style>
blockquote.callout_warning div.heading-text {
font-size: 5 rem;
color: rgb(241, 173, 0) !important;
}
</style>

FastCheckout is MultiSafepay's own complete checkout solution for a fast, frictionless checkout experience and increased <<glossary:conversion>>.

# How it works

FastCheckout is highly flexible and fully customizable. It consists of modular checkout steps (billing, shipping, and payment) that let you create a tailored experience for each customer. 

New features and payment methods are made available automatically. No updates or upgrades are required. FastCheckout is optimized for both mobile and desktop.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOExample.png" align ="center"/>
<br>

The FastCheckout page comprises 4 elements that can be displayed or hidden, and configured per <<glossary:order>>.

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
- Saves space by bundling all available cards in a single gateway that auto-detects the card type
- Is [Fuhrmann-2 compliant](/docs/fuhrmann2/)

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
  <summary>Example of single card payment gateway</summary>
  <br>

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/FCOCard.png" align ="center"/>

  </details>

#### Shopping cart element

- Provides clear breakdown of price and taxes, with no hidden costs
- Updates automatically when different shipping options are selected
- Supports discounts

#### Sequence

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/fastcheckout.svg" alt="FastCheckout flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Activation

Email a request to activate FastCheckout for specific websites under your account to <sales@multisafepay.com>

Specify in your request the relevant [website IDs](/docs/sites#site-id-api-key-and-security-code). 

# Integration

To integrate FastCheckout as a hosted page via our API, see:

- API reference – [Create order](/reference/createorder) > FastCheckout order
- Recipes – <a href="https://docs.multisafepay.com/recipes/create-a-fastcheckout-page" target="_blank">Create a FastCheckout page</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 

To embed FastCheckout into your website, see [FastCheckout JavaScript integration](/docs/fastcheckout-integration/).

If you cannot send your available shipping options for the shipping element in your [create order](/reference/createorder) request, see [FastCheckout shipping options request](/docs/fastcheckout-shipping-options/).

<br>

---
# User guide

## Branding

You can add your brand's logo at the top of the FastCheckout page.

<details id="how-to-add-logo">
<summary>How to add your logo to the FastCheckout page</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**, and then click the relevant website.
3. On the **Website profile** page, under **Functionality**, from the **FastCheckout logo** list, select the relevant logo. 
4. Click **Save changes**.

---

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

---

</details>

The customer can change the page to their preferred language using the flag toggle.

You can also localize FastCheckout pages to automatically hide payment methods that are not available in the customer's country, and to display local variants. 

See API reference > [Create order](/reference/createorder) > FastCheckout order > `customer` object > `locale` parameter.

❗️ **Note:** The `locale` parameter can be overriden on initializing the JavaScript application, or when the customer changes the flag toggle.  

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

---

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

---

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Bancontact
- Bank transfers
- Cards
- Google Pay
- iDEAL

---

</details>

## Second Chance

You can follow up abandoned FastCheckout pages with [Second Chance](/docs/second-chance/).

## Split payments

[Split payment](/docs/split-payments/) are supported for FastCheckout.

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)