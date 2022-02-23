---
title : "Activating MultiSafepay payment pages"
weight: 10
meta_title: "Activating MultiSafepay payment pages - MultiSafepay Docs"
read_more: '.'
url: '/payment-pages/activation/'
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
---

MultiSafepay payment pages (URL: `payv2.multisafepay.com`):

- Are easy to integrate, completely secure, and fully mobile responsive
- Support all payment methods
- Can be styled to fit the look and feel of your website

To activate payment pages, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Select the **Use new payment pages** checkbox.

**Note:** If the **Use new payment pages** checkbox is not visible, email the Integration Team at <integration@multisafepay.com>

{{< details title="Supported languages" >}}

MultiSafepay payment pages support the following languages:

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

{{< details title="Requirements for Visa" >}}

When customers select Visa as payment method, Visa requires us to display on the payment page the city and country where your webshop is located. This measure aims to increase reliability, transparency, and safety for customers.

{{< /details >}}

## Integration

See API reference – [Create a redirect order](/api/#create-a-redirect-order).

### Known errors
A cross-site request forgery (CSRF) warning appears on payment pages when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a `POST /orders` request.
 
* `https://api.multisafepay.com` accepts `POST` and `GET` requests.
* `https://payv2.multisafepay.com` only accepts `GET` requests.
 
For support, email the Integration Team at <integration@multisafepay.com>