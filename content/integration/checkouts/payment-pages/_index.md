---
title: 'Payment pages'
weight: 10
meta_title: "Payment pages - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/Payment pages.svg'
short_description: 'Activate and customize hosted payment pages.'
url: '/payment-pages/'
aliases:
    - /tools/payment-pages/what-is-payv2
    - /faq/general/languages-supported/
    - /faq/general/which-languages-are-supported-by-multisafepay
    - /payments/checkout/payment-pages/activating-payv2/
    - /payments/checkout/payment-pages/requirements-for-visa/
    - /tools/payment-pages/visa-shows-address
    - /faq/errors-explained/csrf
    - /faq/errors-explained/csrf-errors
    - /developer/errors-explained/csrf-errors/
    - /payment-pages/activation/
    - /tools/payment-pages/Difference between V1 and V2
    - /payments/checkout/payment-pages/classic-payment-page/
    - /payments/checkout/payment-pages/classic-payment-page/
    - /payment-pages/deprecated/
    - /tools/payment-pages/show-all-methods
    - /payments/checkout/payment-pages/displaying-all-payment-methods/
    - /payment-pages/displaying-payment-methods/
    - /payment-pages/hiding-shopping-cart/
    - /tools/payment-pages/payment-page-templates/
    - /payments/checkout/payment-pages/dynamic-styling-payment-pages/
    - /payments/checkout/payment-pages/styling-payment-pages/
    - /payment-pages/styling/
---

Payment pages are hosted by MultiSafepay and are the easiest way to integrate all payment methods. 

They are completely secure, fully mobile responsive, and can be styled to fit the look and feel of your website.

## How they work

A customer selects a payment method at checkout, and is redirected to a secure page to complete payment with a URL starting with `payv2.multisafepay.com`.

If you specify a payment method gateway, the page is tailored for that payment method. For example, for Visa, the page includes fields for the customer to enter their credit card details.  

If you don't specify a gateway, all payment methods enabled in your account appear on the payment page.

## Activating payment pages

You can activate payment pages yourself in your dashboard.

{{< details title="Activating payment pages" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Select the **Use new payment pages** checkbox.

**Note:** If the **Use new payment pages** checkbox is not visible, email <integration@multisafepay.com>
{{< /details >}}

## Integrating payment pages 

See API recipe – [Create a payment page](https://docs-api.multisafepay.com/recipes/create-a-payment-pagelink).

{{< details title="Known errors" >}}

A cross-site request forgery (CSRF) warning appears on payment pages when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a [create order](https://docs-api.multisafepay.com/reference/createorder) request.
 
- `https://api.multisafepay.com` accepts `POST` and `GET` requests.
- `https://payv2.multisafepay.com` only accepts `GET` requests.
{{< /details >}}

## Styling payment pages

We recommend styling payment pages to be consistent with the look and feel of your website.

{{< details title="In your dashboard" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings** > **Website**.
3. Click the **Template** button. 
4. Use the WYSIWYG editor to style the payment page template.  

    **Choosing colors**  
    In the left menu, a color chart appears when you click on the field of a page element. You can also enter a [Hex color](https://www.w3schools.com/colors/colors_picker.asp) in the input field next to it.  

    **Selecting a logo or header image**  
    In **Settings** > **Payment page templates**, upload files for logos or header backgrounds. They may take up to 5 minutes to process, and then automatically appear in the list in the editor.  

    **Setting a default template**  
    If you have more than one template and want to set one as your default template, use the **Set default** option. You can also give this template a name, which is used as the `template_id`.   

    **Editing saved templates**  
    Click **Edit template** (top-left corner).  

    **Duplicating styling to another template**  
    Click **Apply style from** (top-right corner). Save the template to the relevant website.  

5. To save the finished template to the relevant website, click **Submit website**. 

{{< /details >}}

{{< details title="Via the API" >}}

You can dynamically style the payment page template for specific transaction requests via our API. 

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Payment page/link > `payment_options` object. 

{{< /details >}}

## User guide

### Deprecated version

The deprecated version of the payment page (URL: `pay.multisafepay.com`) is still fully supported, but we strongly recommend upgrading to the current version.

{{< details title="Unsupported payment methods" >}}

We cannot guarantee that the deprecated version will support any new payment methods we add to our platform.

It does **not** support the following methods:

| | |
|---|---|
| **Pay later** | AfterPay, Betaal per Maand, in3, Klarna |
| **Wallets** | Alipay, Apple Pay, WeChat Pay |
| **Banking** | Bancontact QR, Belfius, CBC/KBC, EPS, iDEAL QR, Request to Pay, Sofort, Trustly |
| **Prepaid cards** | PaySafecard |

{{< /details >}}

### Google Analytics tracking

You can track the behavior of customers on payment pages through Google Analytics tracking. When the customer is redirected to the payment page, the UA-code is generated and appears in the HTML.

### Languages

{{< details title="Supported languages" >}}

Payment pages support the following languages:

* Arabic
* Czech
* Danish
* Dutch
* English
* Finnish
* French
* German
* Hebrew
* Italian
* Japanese
* Mandarin
* Norwegian
* Polish
* Portuguese
* Russian
* Spanish
* Swedish
* Turkish

{{< /details >}}

### Payment links

You can manually generate a link to a payment page to send to a customer to complete payment. See [Payment links](/account/payment-links/).

### Payment methods

{{< details title="Displaying all payment methods" >}}

If a customer's country is unclear or your integration doesn't let you provide the correct country code, consider displaying all your enabled payment methods on the payment page. This is not supported for the deprecated version.

To display all payment methods on the payment page, follow these steps:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) to retrieve the payment link.
2. Add `&methods=all` at the end of the payment link, e.g.: `https://testpayv2.multisafepay.com/connect/822LtiM8RjN313Yo5C46E2cjqmuL5qVfc7w/?lang=en_NL&methods=all`
3. Redirect the customer to the adapted link.

**Note:** This is not a standard option in our [ready-made integrations](/integrations/ready-made/).

{{< /details >}}

### Requirements for Visa

{{< details title="Requirements for Visa" >}}

When customers select Visa as payment method, Visa requires us to display on the payment page the city and country where your webshop is located. This measure aims to increase reliability, transparency, and safety for customers.

{{< /details >}}

### Shopping cart

If you include a `shopping_cart` object when you [create an order](https://docs-api.multisafepay.com/reference/createorder), the cart details are displayed on the payment page by default. That is, all items in the customer's order, with the price and VAT for each.

{{< details title="Hiding the shopping cart on payment pages" >}}

1. To request to enable **Advanced website templates** for your MultiSafepay account, email <integration@multisafepay.com>
2. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/). 
3. Go to **Settings** > **New payment pages**.
4. Next to the relevant website, click **Template**.
5. Under **Configure page style**, click **Settings**, and then select the **Hide cart details** checkbox. 

{{< /details >}}

## Support
 
Email <integration@multisafepay.com>