---
title: Card refunds
category:
  uri: Payment methods
slug: card-refunds
position: 4
privacy:
  view: public
parent:
  uri: cards
---
# Refunds

## Cancellation

You can cancel a refund while the status is **Initialized** or **Reserved**.

For more information, see Refund payments – [Cancellation](/docs/refund-payments#cancellation).

## Amount limit

You **cannot** refund more than the original transaction.

## Processing times

* You can process refunds via MultiSafepay for up to 180 days after payment was completed.

* MultiSafepay sends refunds to the <Glossary>issuer</Glossary> for processing within 1 business day.

* Refunds arrive in the customer's account within **1 to 14 business days**, depending on the issuer.

## Visibility

* Whether or not the refund is visible to the customer depends on the issuer's system.
* Depending on the issuer, the amount may **not** appear directly on the customer's card. We recommend the customer to contact the issuer.
  * If a customer needs an acquirer reference number (ARN), you can find this in your <a href="https://merchant.multisafepay.com/" target="_blank">dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> on the relevant **Transaction details** page.
  * ARNs are **not** provided if the refund is processed within the same day as the transaction.

# Reversals

* If you process a partial refund within the same day as the transaction, this is technically called a <Glossary>reversal</Glossary>. For simplicity, reversals are recorded as refunds in your MultiSafepay dashboard.

* On the customer's card statement, the transaction may either be:
  * Adjusted to the new amount = Partial reversal
  * Not debited at all = Full reversal

* You **cannot** cancel reversals because the funds are returned to the customer immediately.

**⚠️Note:** If you have processed a reversal or a refund, but the customer hasn't received their funds, you can send them a receipt of the transaction. For more information, see <a href="https://docs.multisafepay.com/docs/refund-payments#refund-receipts" target="_blank">Refund receipts</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
