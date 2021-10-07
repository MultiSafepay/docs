---
title: "Bank transfer product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Bank transfer rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
url: '/payments/methods/bank-transfer/product-rules/'
aliases: 
    - /payment-methods/bank-transfer/what-is-bank-transfer/
    - /payments/methods/banks/bank-transfer/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Europe (SEPA area)  | |
| **Currencies**  | CZK, EUR, GBP, HUF, PLN | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#bank-transfer-direct) / [Redirect](/api/#bank-transfer-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 60 days | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}
- [Full and partial refunds](/payments/refunds/) are supported.

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

## Other rules
- USD is **not** supported due to extremely high transaction and currency conversion fees for customers.

- Bank accounts are always displayed in IBAN format. See also [Unmasking IBAN numbers](/developer/api/masking-iban-numbers/).

- To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your [backend](/getting-started/glossary/#backend) until they complete the payment.  This&nbsp;depends on your ecommerce platform or integration, and your products and/or services.  
**Note:** MultiSafepay bears no responsibility for stock-related issues.

- To change how bank transfers are validated, check whether this is possible in your backend.

- See also [Emailing payment instructions to the customer yourself](/payments/methods/banks/bank-transfer/user-guide/emailing-payment-instructions/). 



## MultiSafepay local bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your `POST /orders` request in the `country` parameter, e.g. `"country": "DE",`.

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


