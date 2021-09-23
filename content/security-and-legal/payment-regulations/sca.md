---
title : "Strong customer authentication (SCA)"
weight: 30
meta_title: "Payment regulations - Strong customer authentication (SCA) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
url: '/payment-regulations/sca/'
aliases:
    - /faq/payment-regulations/strong-customer-authentication
    - /faq/payment-regulations/about-strong-customer-authentication
    - /security-and-legal/payment-regulations/about-strong-customer-authentication/
---

To help combat financial and data fraud, the [PSD2](/payment-regulations/psd2/) requires strong customer authentication (SCA) for most online payments in Europe. 

Merchants and [PSPs](/getting-started/glossary/#payment-service-provider-psp) must verify customer identity for most transactions using two factor authentication (2FA), that is at least two out of the following three authentication methods:

{{< responsive_svg src="/diagrams/svg/SCA" alt="Strong Customer Authetication methods" align="center" >}}

If transactions aren't appropriately authenticated, banks may have to decline them. 

## Exemptions

Transactions are exempt from SCA requirements if they are:

- Low value payments (LVP), i.e. under 30 EUR
- Subject to transaction risk analysis (TRA)
- Safelisted
- Recurring payments, if the initial transaction was successfully authenticated
- Corporate payments

MultiSafepay supports LVP and TRA exemptions (on request), which can help you optimize [conversion](/getting-started/glossary/#conversion-rate) and minimize risk.

To apply, email the Integration Team at <integration@multisafepay.com>

See also [3D Secure 2.0](/faq/payment-regulations/3d-secure).
