---
title: 'Card refunds'
category: 6298bd782d1cf4006032e765
order: 4
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: 'card-refunds'
---
# Refunds

## Cancellation

You can cancel a refund while the status is **Initialized** or **Reserved**. 

For more information, see Refund payments – [Cancellation](/docs/refund-payments#cancellation).

## Amount limit

You **cannot** refund more than the original transaction.

## Processing times

- You can process refunds via MultiSafepay for up to 180 days after payment was completed. 

- MultiSafepay sends refunds to the <<glossary:issuer>> for processing within 1 business day.

- Refunds arrive in the customer's account within **1 to 14 business days**, depending on the issuer. 
  
## Visibility
  
- Whether or not the refund is visible to the customer depends on the issuer's system.
  
- Depending on the issuer, the amount may **not** appear directly on the customer's card. We recommend the customer to contact the issuer. 
    - If a customer needs an acquirer reference number (ARN), you can find this in your <a href="https://merchant.multisafepay.com/" target="_blank">dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> on the relevant **Transaction details** page. 
    - ARNs are **not** provided if the refund is processed within the same day as the transaction.

# Reversals

- If you process a partial refund within the same day as the transaction, this is technically called a <<glossary:reversal>>. For simplicity, reversals are recorded as refunds in your MultiSafepay dashboard. 

- On the customer's card statement, the transaction may either be:
  - Adjusted to the new amount= Partial reversal
  - Not debited at all= Full reversal

- You **cannot** cancel reversals because the funds are returned to the customer immediately.

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)