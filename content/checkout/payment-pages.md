---
title: 'Payment pages'
category: 62bd999547298d001abc714c
order: 30
hidden: false
slug: 'payment-pages'
---
Payment pages are hosted by MultiSafepay and are the easiest way to integrate all payment methods. 

They are completely secure, [Fuhrmann-2 compliant](/docs/fuhrmann2/), fully mobile responsive, and can be styled to fit the look and feel of your site.

# How it works

A customer selects a payment method at checkout, and is redirected to a secure page to complete payment with a URL starting with `payv2.multisafepay.com`.

If you specify a payment method <<glossary:gateway>>, the page is tailored for that payment method. For example, for Visa, the page includes fields for the customer to enter their credit card details.  

If you don't specify a gateway, all payment methods enabled in your account appear on the payment page.

# Activation

Payment pages are automatically activated when you [add a site](/docs/sites/) to your account.

# Integration 

See Recipes – [Create a payment page](/recipes/create-a-payment-pagelink).

<details id="known-errors">
<summary>Known errors</summary>
<br>

A cross-site request forgery (CSRF) warning appears on payment pages when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a [create order](/reference/createorder/) request.
 
- `https://api.multisafepay.com` accepts `POST` and `GET` requests.
- `https://payv2.multisafepay.com` only accepts `GET` requests.
</details>
<br>

---

# User guide

## Deprecated version

The deprecated version of the payment page (URL: `pay.multisafepay.com`) is still fully supported, but we strongly recommend upgrading to the current version.

<details id="unsupported-payment-methods">
<summary>Unsupported payment methods</summary>
<br>

We cannot guarantee that the deprecated version will support any new payment methods we add to our platform.

It does **not** support the following methods:

| Method type | Unsupported methods |
|---|---|
| **BNPL** | AfterPay, Betaal per Maand, in3, Klarna |
| **Wallets** | Alipay, Apple Pay, WeChat Pay |
| **Banking** | Bancontact QR, Belfius, CBC/KBC, EPS, iDEAL QR, Request to Pay, Sofort, Trustly |
| **Prepaid cards** | PaySafecard |

</details>

## Google Analytics tracking

You can track the behavior of customers on payment pages through Google Analytics tracking. When the customer is redirected to the payment page, the UA-code is generated and appears in the HTML.

## iframes

An inline frame (iframe) is an HTML document embedded inside another HTML document on a site. 
 
Although MultiSafepay doesn't prohibit embedding payment pages as an `<iframe>`, we do **not** recommend it. This is because:

- Some payment methods may not work for privacy and security reasons. 
- Some banks use scripts that can't run within `<iframe>` elements.
- Modern browsers can block them due to stricter security checks.

Instead, we recommend using [payment components](/docs/payment-components/) to embed payments into your site. 

## Localization

Payment pages are supported in 19 languages. 

<details id="supported-languages">
<summary>Supported languages</summary>
<br>

Payment pages support the following languages:

| Supported languages | Supported languages |
|---|---|
| Arabic | Japanese |
| Czech | Mandarin |
| Danish | Norwegian |
| Dutch | Polish |
| English | Portuguese |
| Finnish | Russian |
| French | Spanish |
| German | Swedish |
| Hebrew | Turkish |
| Italian ||

</details>

You can also localize payment pages to automatically filter out payment methods that are not available in the customer's country, and to display local variants. 

See API reference > [Create order](/reference/createorder) > `customer` object > `locale` parameter.

<details id="locale-codes">
<summary>Locale codes per language and country</summary>
<br>

| Code | Language & country |
|---|---|
| cs_CZ | Czech |
| de_AT | German (Austria) |
| de_DE | German (Germany) |
| en_US | American English |
| fi_FI | Finnish |
| fr_BE | French (Belgium) |
| fr_FR | French (France) |
| it_IT | Italian |
| nl_BE | Dutch (Belgium) |
| nl_NL | Dutch (Netherlands) |
| pl_PL | Polish |
| es_ES | Spanish |
| sv_SE | Swedish |
| zh_CN | Chinese |

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

## Payment links

You can manually generate a [link to a payment page](/docs/payment-links/) to send to a customer to complete payment. 

## Payment methods

If a customer's country is unclear or your integration doesn't let you provide the correct country code, consider displaying **all** your enabled payment methods on the payment page. This is not supported for the deprecated version.

<details id="how-to-display-all-payment-methods">
<summary>How to display all payment methods</summary>
<br>

To display all payment methods on the payment page, follow these steps:

1. [Create an order](/reference/createorder/) to retrieve the payment link.
2. Add `&methods=all` at the end of the payment link, e.g. `https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL&methods=all`
3. Redirect the customer to the adapted link.

**Note:** This is not a standard option in our [ready-made integrations](/docs/our-integrations/).


</details>

## Shopping cart

If you include a `shopping_cart` object when you [create an order](/reference/createorder/), the cart details are displayed on the payment page by default. That is, all items in the customer's order, with the price and VAT for each.

<details id="how-to-hide-shopping-cart">
<summary>How to hide the shopping cart</summary>
<br>

1. To request to enable **Advanced website templates** for your MultiSafepay account, email <integration@multisafepay.com>
2. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
3. Go to **Settings** > **New payment pages**.
4. Next to the relevant site, click **Template**.
5. Under **Configure page style**, click **Settings**, and then select the **Hide cart details** checkbox. 

</details>

## Styling 

We recommend styling payment pages to be consistent with the look and feel of your site.

<details id="in-your-dashboard">
<summary>In your dashboard</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Integrations** > **Sites**, and then click the relevant site.
3. On the **Site profile** page, under **Functionality**, click **Edit template**. 
4. On the **Payment page styling** page:  

    **Style the logo**  
    - Go to **Settings** > **Files**, and upload your logo file.
    - On the **Payment page styling** page, under **Configure page style**, from the **Logo** list, select the logo file.
    - To hide the logo, under **Configure page style** > **Settings**, select the **Hide main logo** checkbox. 

    **Style the header**  
    Under **Configure page style** > **Header**, you can:
    - Set the header **Background** color. 
    - Select a **Background image** that you have uploaded under **Settings** > **Files**.

    **Style the body**  
    Under **Configure page style** > **Body**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text, and links on the page and when the user mouses over them.

    **Style the body container**
    Under **Configure page style** > **Container**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text, labels, and links. 
      
    **Style the cart**
    Under **Configure page style** > **Cart**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text, and labels. 

    **Style the payment form**
    Under **Configure page style** > **Payment form**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text, input border, and input labels. 

    **Style the buttons**
    Under **Configure page style** > **Buttons**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text on the page and when moused over. 

    **Set a default template**  
    If you have more than one template and want to set one as your default template, use the **Set default** option. You can also give this template a name, which is used as the `template_id`.   

    **Edit saved templates**  
    Click **Edit template** (top-right corner).  

    **Duplicate styling to another template**  
    - Click **Apply style from** (top-right corner). 
    - Select the relevant template. 

    **Set as default template**
    To set this as the default template for this site, under **Configure page style**, click **Set as default template**. 

5. To save the finished template to the relevant site, enter a name in the **Save template as** field, and then click **Save template**. 

</details>

<details id="via-the-api">
<summary>Via the API</summary>
<br>

You can dynamically style the payment page template for specific transaction requests via our API. 

See API reference – [Create order](/reference/createorder/) > Payment page/link > `payment_options` object. 

The `items` parameter is an HTML string for displaying order items on the payment page, instead of including a `shopping_cart`. The following HTML tags and elements are supported (all others are stripped out):

- b, br
- div (align)
- em
- font (color, face, size)
- h1, h2, h3, h4, h5, h6, hr
- i, img (width, height, alt, scale, border, align)
- li
- nobr
- ol
- p
- small, span, strong
- table (width, border, bordercolor, cellpadding, cellspacing), thead, tbody, tfoot, th (width, scope, colspan, align), td (height, width, align, valign, colspan, bgcolor), tr (bgcolor, valign)
- u, ul

</details>

## Requirements for Visa

When customers select Visa as payment method, Visa requires us to display on the payment page the city and country where your webshop is located. This measure aims to increase reliability, transparency, and safety for customers.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
