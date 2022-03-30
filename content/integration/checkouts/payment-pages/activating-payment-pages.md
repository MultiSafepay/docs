---
title : "Activating payment pages"
weight: 10
meta_title: "Activating payment pages - MultiSafepay Docs"
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

Payment pages are hosted by MultiSafepay (URL: payv2.multisafepay.com) and are the easiest way to connect to all payment methods. 

They are completely secure, fully mobile responsive, and can be styled to fit the look and feel of your website.

## How it works

A customer selects a payment method at checkout, and is redirected to a secure page to complete payment.

If you specify a payment method gateway, the page is tailored for that payment method. For example, for Visa, the page includes fields for the customer to enter their credit card details.  

If you don't specify a gateway, all payment methods enabled in your account appear on the payment page.

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

### Requirements for Visa

When customers select Visa as payment method, Visa requires us to display on the payment page the city and country where your webshop is located. This measure aims to increase reliability, transparency, and safety for customers.

### Google Analytics tracking

You can track the behavior of customers on payment pages through Google Analytics tracking.  

When the customer is redirected to the payment page, the UA-code is generated and appears in the HTML.

## Activation

To activate payment pages, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Click the relevant website.
4. Select the **Use new payment pages** checkbox.

**Note:** If the **Use new payment pages** checkbox is not visible, email the Integration Team at <integration@multisafepay.com>

## Integration

See API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder): Payment page.

### Known errors
A cross-site request forgery (CSRF) warning appears on payment pages when you use an HTML form to send customers to `https://payv2.multisafepay.com` with a `POST /orders` request.
 
- `https://api.multisafepay.com` accepts `POST` and `GET` requests.
- `https://payv2.multisafepay.com` only accepts `GET` requests.
 
For support, email <integration@multisafepay.com>