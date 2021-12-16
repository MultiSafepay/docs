---
title: "Bank Transfer overview"

breadcrumb_title: 'Overview'
weight: 10
meta_title: "Bank Transfer overview - MultiSafepay Docs"
short_description: "Key information, supported countries, currencies, and features"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
url: '/payment-methods/bank-transfer/overview/'
aliases: 
    - /payment-methods/bank-transfer/what-is-bank-transfer/
    - /payments/methods/banks/bank-transfer/about/
    - /payments/methods/bank-transfer/product-rules/
    - /payment-methods/bank-transfer/product-rules/
---
Bank Transfer, also known as SEPA Credit Transfer, is a secure, trusted, international banking method. Customers can make any type of online payment in euros within the SEPA area. 

|   |   |   
|---|---|
| **Countries** | Europe (SEPA area) | 
| **Currencies** | EUR, CZK, GBP, HUF, PLN {{< br >}} USD is **not** supported due to extremely high transaction and currency conversion fees for customers. |
| **Chargebacks**  | No – See [Chargebacks](/payments/chargebacks/). | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Transactions expire after**  | 60 days | 

## MultiSafepay local bank accounts

You can link Bank Transfer directly to your website. When a customer selects Bank Transfer as payment method, they receive MultiSafepay bank account details by email.

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your `POST /orders` request in the `country` parameter, e.g. `"country": "DE",`.

{{< details title="Countries with a local MultiSafepay bank account" >}} 

- Austria (EUR)
- Belgium (EUR)
- Czech Republic (CZK)
- France (EUR)
- Germany (EUR)
- Hungary (HUF)
- Italy (EUR)
- Netherlands (EUR)
- Poland (PLN)
- Portugal (EUR)
- Spain (EUR)
- UK (GBP)

{{< /details >}}

## Notes 

- Bank accounts are always displayed in IBAN format. See also [Unmasking IBAN numbers](/developer/api/masking-iban-numbers/).

- To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your [backend](/glossaries/multisafepay-glossary/#backend) until they complete the payment.  This&nbsp;depends on your ecommerce platform or integration, and your products and/or services.  
**Note:** MultiSafepay bears no responsibility for stock-related issues.

- To change how bank transfers are validated, check whether this is possible in your backend.






