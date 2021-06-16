---
title: 'About E-invoicing'
breadcrumb_title: 'About E-invoicing'
weight: 10
meta_title: "About E-invoicing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

E-Invoicing is a MultiSafepay buy now pay later service with automation tools that gives you full control of credit management, the payment process, and customer contact. Customers pay for orders after receiving them.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Buy now pay later  | |
| **API flow**  | `Direct`/`Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/billing-suite/e-invoicing/faq/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- You cannot [adjust payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

- E-invoicing supports different delivery and invoice addresses. Email a request to your account manager at <sales@multisafepay.com>

{{< details title="Gift cards" >}}
&nbsp;  
Buy now pay later services do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, E-invoicing requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}