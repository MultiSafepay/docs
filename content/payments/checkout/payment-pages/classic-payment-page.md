---
title : "Classic payment page"
weight: 42
meta_title: "Payment pages - Classic payment page - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/payment-pages/Difference between V1 and V2
---

PayV1 is the classic MultiSafepay payment page, starting with `pay.multisafepay.com`. It is still fully supported, but we strongly recommend upgrading to PayV2 to enjoy the following benefits: 

### Payment methods
Some payment methods are only supported on PayV2 pages. When we add new payment methods to our platform, we cannot guarantee that they will work on PayV1 pages.

PayV1 does **not** support the following payment methods:

| Payment method category   | Payment methods     |
|----------------|-------------------|
|  Bank | Belfius, CBC, EPS, iDEALQR, ING Home'Pay, KBC, Request to Pay, Santander, SOFORT Banking, Trustly     |
|  Billing Suite | AfterPay, in3, Klarna     |
|  Wallet | Alipay, Apple Pay, JCB    |
|  Prepaid cards | PaySafecard   |  

**Note:** Bancontact QR codes only work on PayV2 pages.

### Faster request processing 
Requests to and responses from the MultiSafepay server are processed much faster on PayV2 pages.

### Responsive design
We designed PayV2 pages to work responsively across different devices and browsers to give customers a seamless experience.

### Dynamic templates
With PayV2, you can use dynamic templates to style payment pages through our API. For more information, see [Dynamic styling for payment pages](/payments/checkout/payment-pages/dynamic-styling-for-payment-pages/).

### Languages
PayV2 supports 5 more languages. For a list of supported languages, see FAQ - [Languages supported](/faq/general/languages-supported/).

To activate PayV2, see [Activating PayV2](https://docs.multisafepay.com/payments/checkout/payment-pages/activating-payv2).
