---
title: "Payment statuses"
category: 6278c92bf4ad4a00361431b0
order: 2
hidden: false
slug: 'payment-statuses'
---
There are two statuses for each payment that update as it is processed:

* **Order status:** Changes as the customer's order with you progresses towards shipment.\
  API attribute: `status`
* **Transaction status:** Changes as the funds progress towards <Glossary>settlement</Glossary> in your account balance.\
  API attribute: `financial_status`

<details id="how-to-view-statuses">
  <summary>How to view statuses</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
  2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, the statuses appear under **Transaction history**.
</details>

# Payment statuses

The meaning of statuses (or combinations of statuses) varies per payment method. To check specific meanings, see the relevant payment method page.

The table below sets out possible order and transaction statuses and what they commonly mean.

| Description                                                                                                                                       | Order status | Transaction status |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has initiated a transaction.                                                                                                         | Initialized  | Initialized        |
| The customer has successfully completed the transaction.                                                                                          | Completed    | Completed          |
| The transaction has been cancelled.                                                                                                               | Void         | Cancelled          |
| The customer has requested a chargeback.                                                                                                          | Void         | Void               |
| The customer didn't complete payment and the transaction expired. <br /> Transaction expiry times vary per payment method.                        | Expired      | Expired            |
| The <Glossary>issuer</Glossary> or <Glossary>acquirer</Glossary> has declined the transaction. <br /> See also [Card errors](/docs/card-errors/). | Declined     | Declined           |
| Manually [capture or decline the transaction](/docs/uncleared/).                                                                                  | Uncleared    | Uncleared          |
| The order has been shipped and the funds are still pending.                                                                                       | Shipped      | Uncleared          |

# Refund and chargeback statuses

The following statuses apply to [refunds](/docs/refunds/) and [chargebacks](/docs/chargebacks/).

| Description                                                                   | Order status         | Transaction status   |
| ----------------------------------------------------------------------------- | -------------------- | -------------------- |
| Refund initiated.                                                             | Initialized/Reserved | Initialized/Reserved |
| Refund/chargeback complete.                                                   | Completed            | Completed            |
| The refund has been processed successfully.                                   | Refunded             | Refunded             |
| The [partial refund](/docs/refund-payments/) has been processed successfully. | Partial\_refunded    | Partial\_refunded    |
| The refund was declined.                                                      | Declined             | Declined             |

<br />

If the status of the refund is **Reserved**, it may mean:

* The refund hasn't been processed yet. Refunds are passed to the customer's bank at midnight on the day they are initiated, and then the status changes to **Completed**. The bank is now responsible for processing the payment. Refunds may be delayed by the issuing bank.
* The refund cannot be processed due to insufficient funds in your account balance. To top up your balance, see [Topping up your balance](/docs/account-balance/).

# Payout statuses

The following statuses apply to [payouts](/docs/payouts/).

| Description       | Status    |
| ----------------- | --------- |
| Payout initiated. | Reserved  |
| Payout completed. | Completed |
| Payout cancelled. | Void      |

<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)