---
title: 'Payment pages'
category: 62bd999547298d001abc714c
order: 3
hidden: false
slug: 'payment-pages'
---
Payment pages are hosted by MultiSafepay and are the easiest way to integrate all payment methods. 

They are completely secure, [Fuhrmann-2 compliant](/docs/fuhrmann2/), fully mobile responsive, and can be styled to fit the look and feel of your site.

# How it works

A customer selects a payment method at checkout, and is redirected to a secure page to complete payment with a URL starting with `payv2.multisafepay.com`.

If you specify a payment method <<glossary:gateway>>, the page is tailored for that payment method. For example, for Visa, the page includes fields for the customer to enter their card details.  

If you don't specify a gateway, all payment methods enabled in your account appear on the payment page.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/payment-pages.svg" alt="Payment pages" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Activation

Payment pages are automatically activated when you [add a site](/docs/sites/) to your account.

# Integration 

See Recipes – <a href="https://docs.multisafepay.com/recipes/create-a-payment-pagelink" target="_blank">Create a payment page</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

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
| **BNPL** | Betaal per Maand, in3, Klarna, Riverty |
| **Wallets** | Alipay, Apple Pay, WeChat Pay |
| **Banking** | Bancontact QR, Belfius, CBC/KBC, EPS, iDEAL QR, Request to Pay, Sofort, Trustly |
| **Prepaid cards** | PaySafecard |

</details>

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

The first parameter taken into account is the `country` parameter. Secondly, `locale` is checked.
If `country`is not sent, the decision is based on `locale`.


See API reference > [Create order](/reference/createorder) > `customer` object > `country` and `locale` parameters.

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

**⚠️ Note:** This is not a standard option in our [ready-made integrations](/docs/our-integrations/).

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

We recommend styling payment pages to be consistent with the look and feel of your website.

### Via the dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

2. Go to **Websites**, and then click the relevant website.

3. On the **Website profile** page, under **Style your checkout solution** > **Hosted Payment Page V2**, click **Edit**. 

4. On the **Payv2 settings** page, under **Configure page style**, you can customize the appearance of various elements on your payment page. Click on the sections below to expand them and view the available options:  

   <details id="how-to-change-the-logo">
   <summary>How to change the logo</summary>
   <br>

   - If you haven't added a new logo, go to **Settings** > **Files**, and upload your logo file.
   - On the **Payv2 settings** page, under **Configure page style**, from the **Logo** list, select the logo file.
   - To hide the logo, under **Configure page style** > **Settings**, select the **Hide main logo** checkbox. 

   <br />

   </details>

   <details id="how-to-style-the-header">
   <summary>How to style the header</summary>
   <br>

   Under **Configure page style** > **Header**, you can:

   - Set the header **Background** color. 
   - Select a **Background image** that you have uploaded under **Settings** > **Files**.

   <br />

   </details>

   <details id="how-to-style-the-body">
   <summary>How to style the body</summary>
   <br>

   Under **Configure page style** > **Body**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text, and links on the page and when the user hovers over them.

   <br />

   </details>

   <details id="how-to-style-the-body-container">
   <summary>How to style the body container</summary>
   <br>

   Under **Configure page style** > **Container**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text, labels, and links. 

   <br />

   </details>

   <details id="how-to-style-the-cart">
   <summary>How to style the cart</summary>
   <br>

   Under **Configure page style** > **Cart**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text, and labels. 

   <br />

   </details>

   <details id="how-to-style-the-payment-form">
   <summary>How to style the payment form</summary>
   <br>

   Under **Configure page style** > **Payment form**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text, input border, and input labels. 

   <br />

   </details>

   <details id="how-to-style-the-buttons">
   <summary>How to style the buttons</summary>
   <br>

   Under **Configure page style** > **Buttons**, you can set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, border, text on the page and when hovered over. 

   <br />

   </details>

   <details id="how-to-set-a-default-template">
   <summary>How to set a default template</summary>
   <br>

   If you have multiple templates, you can set one as your default:

   - Under **Configure page style**, click **Set as default template**.
   - Enter a name for your template. This will define the `template_id`.
   - Click **Submit settings**.

   <br />

   </details>

   <details id="how-to-edit-saved-templates">
   <summary>How to edit saved templates</summary>
   <br>

   To select a specific template you want to edit:

   - Click **Edit template** at the top-right corner.
   - Select the relevant template you want to edit.
   - You can change the settings, name, reset to default settings or delete your template.

   <br />

   </details>

   <details id="how-to-duplicate-styling-to-another-template">
   <summary>How to duplicate styling to another template</summary>
   <br>

   - Select the template you want to apply the style to.
   - Click **Apply style from** at the top-right corner.
   - Select the relevant template.
   - Click **Submit settings**.

   <br />

   </details>

5. To save the finished template to the relevant website, enter a name in the **Save template as** field, and then click **Submit template**. 

### Via the API

You can dynamically style the payment page for specific order requests via our API. 

See:

- API reference – [Create order](/reference/createorder/) > Payment page/link > `payment_options` object
- Recipes – <a href="https://docs.multisafepay.com/recipes/style-the-payment-page" target="_blank">Style the payment page</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

The `items` parameter is an HTML string for displaying order items on the payment page, instead of including a `shopping_cart`. 

Some HTML tags and elements are supported and all others are stripped out.

<details id="supported-html-tags-and-elements">
<summary>Supported HTML tags and elements</summary>
<br>

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

***

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
