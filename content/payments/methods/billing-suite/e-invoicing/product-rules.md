---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "E-Invoicing product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
url: '/payments/methods/e-invoicing/product-rules/'
aliases:
    - /payments/methods/billing-suite/e-invoicing/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  | 
| **Payment flow**  | [Direct](/api/#e-invoicing-direct) / [Redirect](/api/#e-invoicing-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | Doesn't apply | |
| **Adjust payment link lifetimes**  | No | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- Full and partial refunds, discounts, and API refunds are supported. See [Refunds](/payments/refunds/).

- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payments/methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, E-Invoicing requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

- E-Invoicing supports different delivery and invoice addresses. Email a request to your account manager at <sales@multisafepay.com>

- See also MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).
