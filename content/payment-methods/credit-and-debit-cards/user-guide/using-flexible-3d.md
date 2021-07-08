---
title : "Using Flexible 3D"
weight: 90
meta_title: "Credit card user guide - Using Flexible 3D - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
logo: '/svgs/Flexible 3D.svg'
short_description: 'Use 3D Secure verification to provide an extra layer of security to credit card payments.'
aliases: 
    - /tools/flexible_3d
---

{{< alert-notice >}}
**Note:** MultiSafepay no longer supports Flexible 3D for merchants in Europe due to PSD2 regulations. If you are a European merchant with a lot of customers outside Europe and you need a more flexible setup, email your account manager at <sales@multisafepay.com>
{{< /alert-notice >}}

Flexible 3D lets you enable and disable mandatory [3D Secure](/payment-methods/credit-and-debit-cards/user-guide/glossary/) verification of credit card transactions via our API.

For more information about 3D Secure, see [About 3D Secure](/faq/payment-regulations/about-3d-secure).

Setting Flexible 3D to:

- `false` disables 3D Secure verification and overrides [Dynamic 3D](/tools/server2server/3d-dynamics) rules. The payment is classified as **"Not Enrolled, Liability".**

- `true` enables 3D Secure verification and the payment is classified as **3D Secure Result: Enrolled Liability**.

See API Reference:

- [3D disabled or NON 3D transaction](/api/#3d-disabled-or-non-3d-transaction)
- [Direct, Flexible 3D set to false](/api/#direct-flexible-3d-set-on-_false_)
- [Direct Server to Server, Flexible 3D set to true](/api/#direct-server-to-server-flexible-3d-set-on-_true_)
- [Redirect, Flexible 3D set to false](/api/#redirect-flexible-3d-set-on-_false_)


