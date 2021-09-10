---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "AfterPay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
aliases:
    - /payments/methods/billing-suite/afterpay/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands, Belgium  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  | 
| **Payment flow**  | [Direct](/api/#afterpay-direct) / [Redirect](/api/#afterpay-redirect)| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 90 days | |
| **Adjust payment link lifetimes**  | No | [More information](/api/#adjust-payment-link-lifetimes)  |


{{< details title="Refunds" >}}

- Full and partial refunds, discounts, API refunds are supported. See [Refunds](/payments/refunds/).

- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payments/methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, AfterPay requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

- AfterPay requires an additional API key for Belgium. Contact AfterPay.

- You must [activate MultiSafepay payment pages](/payments/methods/billing-suite/afterpay/faq/activating-payv2/) at website level in your MultiSafepay account. 

- Customers can provide different invoice and delivery addresses, but the customer's first and last name must share at least two characters. The **Transaction details** page in your MultiSafepay account only shows the invoice address. To retrieve other transaction details, make a `GET /orders` request. See API Reference – [Retrieve an order](/api/#retrieve-an-order). 

- See also MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).
