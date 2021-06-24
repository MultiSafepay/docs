---
title: "About Bank Transfer"
breadcrumb_title: 'About Bank Transfer'
weight: 10
meta_title: "About Bank Transfer - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
aliases: 
    - /payment-methods/bank-transfer/what-is-bank-transfer/
---

Bank Transfer, also known as SEPA Credit Transfer, is a secure, trusted, international payment method. Customers can make any type of online payment in euros within the SEPA area.

You can link Bank Transfer directly to your website. When a customer selects Bank Transfer as payment method, they receive MultiSafepay bank account details by email.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Europe (SEPA area)  | |
| **Currencies**  | CZK, EUR, GBP, HUF, PLN | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/banks/bank-transfer/user-guide/processing-refunds) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

**Note:** USD is **not** supported due to extremely high transaction and currency conversion fees for customers.

## MultiSafepay local bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your POST `/orders` request in the `country` parameter, e.g. `"country": "DE",`.

{{< details title="View countries" >}}

* Austria (EUR)
* Belgium (EUR)
* Czech Republic (CZK)   
* France (EUR)  
* Germany (EUR)
* Hungary (HUF)
* Italy (EUR)
* Netherlands (EUR)
* Poland (PLN)
* Portugal (EUR)
* Spain (EUR)
* UK (GBP)

{{< /details >}}


## Product rules

- Bank accounts are always displayed in IBAN format. See also [Unmasking IBAN numbers](/faq/api/masking-iban-numbers/).

- You can [adjust payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/) in emails to customers. Bank Transfer transactions are active for 60 days. By&nbsp;default, payment links expire after 30 days. 

- To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your backend until they complete the payment.  This&nbsp;depends on your ecommerce platform or integration, and your products and/or services.  
**Note:** MultiSafepay bears no responsibility for stock-related issues.

- To change how bank transfers are validated, check whether this is possible in your ecommerce platform backend.

- See also [Emailing payment instructions to the customer yourself](/payment-methods/banks/bank-transfer/user-guide/emailing-payment-instructions/). 

