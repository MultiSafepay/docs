---
title: "About Paysafecard"
breadcrumb_title: 'About Paysafecard'
weight: 10
meta_title: "About Paysafecard - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases: 
    - /payment-methods/paysafecard/what-is-paysafecard
---

Paysafecard lets customers make online payments using secure prepaid vouchers, available for purchase locally. Customers enter the voucher code, without providing any personal payment details. Vouchers for different amounts are available in the local currency in 46 countries.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Prepaid card  | |
| **API flow**  | `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | Go to [paysafecard.com](https://www.paysafecard.com/en-gb/), and click the globe icon in the banner. |
| **Currencies**  | EUR, GBP, USD | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Only payments with Paysafecard **and** another payment method  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- When buying a Paysafecard voucher, the customer chooses an amount: 10, 25, 50 or 100 EUR
- The funds are available immediately.
- If the customer doesn't use the full amount in the first payment, the outstanding balance remains available for 12 months free of charge. After 12 months, they are charged a monthly administration fee of 3 EUR, which is deducted from the outstanding balance.

{{< details title="Paysafecard refund rules" >}}

- You can refund more than original amount. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Transactions paid with Paysafecard in full: You can't refund these from your MultiSafepay balance because we don't receive any payment details or bank account details from the customer to refund to. You can refund these transactions in your own online banking environment. 

- Transactions paid with Paysafecard **and** another payment method (e.g. iDEAL): You can refund these in full from your MultiSafepay balance. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Refunding mixed payments" >}}

To refund a transaction paid with a gift card **and** another payment method, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

{{< /details >}}



