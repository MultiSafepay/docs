---
title: 'American Express product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "American Express product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/amex/product-rules/'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-additional-information
    - /payments/methods/credit-and-debit-cards/american-express/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR, GBP, USD | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | Yes | See below.  |
| **Payment flow**  | [Redirect](/api/#american-express) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="American Express MerchantID" >}}

If you use your American Express MerchantID (MID):
    
- American Express settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported.  
  
For more information, email the Support Team at <support@multisafepay.com>

{{< /details >}}

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

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
    
**Note:** All transactions higher than 30 EUR require Safekey.


