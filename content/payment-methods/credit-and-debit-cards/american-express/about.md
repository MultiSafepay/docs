---
title: 'About American Express'
breadcrumb_title: 'About American Express'
weight: 10
meta_title: "About American Express - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/American_Express.svg'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-additional-information
---

American Express is one of the biggest global credit card schemes, accepted in more than 160 countries. An additional layer of security is provided by Safekey (the American Express-branded version of [3D Secure](/faq/general/glossary/#3d-secure)), which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR, GBP, USD | [More information](/faq/general/supported-currencies) {{< br >}} Email requests to support a different currency to the Support Team at <support@multisafepay.com> | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/credit-and-debit-cards/american-express/user-guide/processing-refunds/) | 
| **Recurring payments**  | Yes | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks) {{< br >}} You are solely liable for paying chargebacks.  |

## Product rules

- You can [adjust payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/).

- All transactions higher than 30 EUR require Safekey.

{{< details title="American Express MerchantID" >}}

If you use your American Express MerchantID (MID):
    
- American Express settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported.  
  
For more information, email the Support Team at <support@multisafepay.com>

{{< /details >}}


    



