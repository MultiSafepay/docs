---
title: 'About American Express'
breadcrumb_title: 'About American Express'
weight: 10
meta_title: "About American Express - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-additional-information
---

American Express is one of the biggest global credit card schemes, accepted in more than 160 countries. An additional layer of security is provided by Safekey (the American Express-branded version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/)), which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | [Redirect](/api/#american-express) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR, GBP, USD | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/payments/chargebacks)  |

## Product rules

- You can [adjust payment link lifetimes](/api/#adjust-payment-link-lifetimes).

- All transactions higher than 30 EUR require Safekey.

{{< details title="American Express MerchantID" >}}

If you use your American Express MerchantID (MID):
    
- American Express settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported.  
  
For more information, email the Support Team at <support@multisafepay.com>

{{< /details >}}

{{< details title="Refunds" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- Depending on the customer's issuer, the amount may not appear directly on their card. We recommend that they contact the issuer. If they need an [acquirer reference number (ARN)](/credit-and-debit-cards/glossary/#acquirer-reference-number-arn), they can email the Support Team at <support@multisafepay.com> 

- If you process a partial refund on the same day, this is technically called a "reversal", but for simplicity is logged as a refund in your MultiSafepay account. On customer credit card statements, the transaction may either be adjusted to the new amount (partial reversal) _or_ not debited at all (full reversal).

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask American Express to raise a dispute. American Express then notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying chargebacks.

American Express gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/chargebacks).

To help reduce chargebacks, see [Your logo in online banking](/payments/methods/credit-and-debit-cards/user-guide/your-logo-online-banking).

{{< /details >}}
    



