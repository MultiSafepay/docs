---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Pay After Delivery product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg'
url: '/payments/methods/pay-after-delivery/product-rules/'
aliases:
    - /payments/methods/billing-suite/pay-after-delivery/about/
---

|   |   |   |
|---|---|---| 
| **Countries** | Netherlands |  | 
| **Currencies** | EUR | [More information](/faq/general/supported-currencies) |
| **Chargebacks** | No | [More information](/payments/chargebacks/) |
| **Payment flow** | [Direct](/api/#paypal-direct) / [Redirect](/api/#paypal-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) | 
| **Recurring Payments** | No | [More information](/payments/features/recurring-payments/) |
| **Transactions expire after**  | Doesn't apply | |
| **Adjust payment link lifetimes**  | No | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- Full, partial, and API refunds and discounts are supported. See [Refunds](/payments/refunds/).

- You cannot refund more than the amount of the original transaction.

- You can't process refunds after the invoice is transfered to a collection agency (usually 6 weeks after shipping the order). **Shipped** status is not visible in your MultiSafepay account. To check the date of shipment, email <support@multifactor.nl>

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- You can't see whether the customer has paid the invoice. If they have already paid, they receive a refund. If not, they receive an adjusted payment request or the invoice is cancelled.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- For both full and partial refunds, any additional administration costs for the customer are deducted from the invoice. The customer has a further 14 days to complete the payment. 

-  You cannot reverse full refunds.

- If a refund fails, email the Support Team at <support@multifactor.nl> 

{{< /details >}}

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

- Minimum and maximum order amounts apply. For more information, email your account manager at <sales@multisafepay.com>

- The delivery and invoice addresses must be the **same** to prevent fraud. For&nbsp;more information, see MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).

