---
title: "Payment statuses"
category: 6278c92bf4ad4a00361431b0
order: 500
hidden: false
slug: 'payment-statuses'
---
There are two statuses for each payment that update as it is processed:

- **Order status:** Changes as the customer's order with you progresses towards shipment.  
API attribute: `status`
- **Transaction status:** Changes as the funds progress towards settlement in your account balance.  
API attribute: `financial_status`

<details id="how-to-view-statuses">
<summary>How to view statuses</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Transaction overview**, and then select the relevant transaction to open the **Transaction details** page. 
3. Under **Status history**, you can see the statuses.

</details>

# Status meanings

The meaning of statuses (or combinations of statuses) varies per payment method. To check specific meanings, see the relevant payment method page. 

The table below sets out possible order and transaction statuses and what they commonly mean.

| Description | Order | Transaction |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The transaction has been cancelled. | Void | Cancelled |
| The customer has requested a chargeback. | Void | Void |
| The customer didn't complete payment and the transaction expired. <br> Transaction expiry times vary per payment method. | Expired | Expired |
| The <<glossary:issuer>> or <<glossary:acquirer>> has declined the transaction. <br> See also [Card errors](/card-errors/). | Declined | Declined |
| Manually [capture or decline the transaction](/uncaptured/). | Uncleared | Uncleared |
| Manually change the order status to shipped. | Shipped | Uncleared |

## Refunds and chargebacks

| Description | Order | Transaction |
|---|---|---|
| Refund initiated.| Initialized/Reserved | Initialized/Reserved |
| Refund/chargeback complete. | Completed | Completed |
| The refund has been processed successfully.| Refunded | Refunded |
| The [partial refund](/refunds/) has been processed successfully.| Partial_refunded | Partial_refunded |
| The refund was declined. | Declined | Declined |
<br>

If the status of the refund  is **reserved**, it may mean: 

- The refund hasn't been processed yet. Refunds are passed to the customer's bank at midnight on the day they are initiated, and then the status changes to **Completed**. The bank is now responsible for processing the payment. Refunds may be delayed by the issuing bank.
- The refund cannot be processed due to insufficient funds in your account balance. To top up your balance, see [Topping up your balance](/account-balance/).

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
