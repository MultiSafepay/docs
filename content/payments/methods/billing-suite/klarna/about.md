---
title: 'About Klarna'
breadcrumb_title: 'About Klarna'
weight: 10
meta_title: "About Klarna - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

Klarna is an online post-payment method that lets customers pay for orders after receiving them. Customers are only charged for the items they keep from the order. Klarna bears the risk and guarantees settlement.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Post-payment method  | |
| **API flow**  | `Direct`/`Redirect` {{< br >}} Both direct to the Klarna payment page| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Austria, Belgium, Denmark, France, Germany, Italy, Norway, Spain, Sweden, Netherlands  | |
| **Currencies**  | EUR, SEK, NOK, DKK | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full, partial, discounts, API | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

{{< details title="Klarna refund rules" >}}
- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payments/methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, Klarna requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

{{< details title="Discounts" >}}

Discounts are processed as a **negative amount** instead of a **negative quantity**. This method of adding discounts only applies to successful transactions. 

**API**  
For how to add a discount in your transaction request via our API, see API Reference – [Discount](/api/#discount):

- Discount added as a unit price
- Discount added as an order rule (non-refundable)

**MultiSafepay account**  
Instead of deleting an item in the checkout editor, you may want to add a discount. Follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Add the discount as a new page in the checkout editor.  
    Example: quantity (1) > discount (item or name) > amount (as negative) > VAT
6. To deduct the amount of the discount, add a new line to the order.
7. Click **Save**.

   The discount is added to the transaction. 
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}
