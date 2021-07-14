---
title: 'About Pay After Delivery'
breadcrumb_title: 'About Pay After Delivery'
weight: 10
meta_title: "About Pay After Delivery - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg'
---

Pay After Delivery is MultiSafepay's own online post-payment method that lets customers pay for orders after receiving them, increasing customer confidence and conversion. Customers are only charged for the items they keep from the order. MultiSafepay bears the risk, based on the customer's history, and guarantees settlement.

### General

|   |   |   |
|---|---|---| 
| **Payment type** | Post-payment method   |  | 
| **API flow** | `Direct`/ `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) | 
| **Countries** | Netherlands |  | 
| **Currencies** | EUR | [More information](/faq/general/supported-currencies) |
| **Refunds** | Full, partial, discount, API | [More information](/payments/refunds-and-chargebacks/refunds/) |
| **Recurring payments** | No | [More information](/payments/about/recurring-payments/) |
| **Chargebacks** | No | [More information](/faq/chargebacks) |

### Product rules

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payments/methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, Pay After Delivery requires very precise order specifications. 

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

{{< details title="Pay After Delivery refund rules" >}}

- If the customer hasn't paid, you can cancel the transaction by performing a full refund.

- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- With full refunds, any additional administration costs for the customer are deducted from the invoice. The customer has a further 14 days to complete the payment. 

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

- Minimum and maximum order amounts apply. For more information, email your account manager at <sales@multisafepay.com>

- The delivery and invoice addresses must be the **same** to prevent fraud. For&nbsp;more information, see MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).

- You cannot [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes).
