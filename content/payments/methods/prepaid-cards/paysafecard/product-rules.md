---
title: "Paysafecard product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Paysafecard product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/paysafecard/product-rules/'
aliases: 
    - /payments/methods/prepaid-cards/paysafecard/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | Go to [paysafecard.com](https://www.paysafecard.com/en-gb/), and click the globe icon in the banner. |
| **Currencies**  | EUR, GBP, USD | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | Redirect | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 3 hours | |
| **Adjust payment link lifetimes**  | No | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- You can refund more than original amount. See [Refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Transactions paid with Paysafecard in full: You can't refund these from your MultiSafepay balance because we don't receive any payment details or bank account details from the customer to refund to. You can refund these transactions in your own online banking environment. 

- Transactions paid with Paysafecard **and** another payment method (e.g. iDEAL): You can refund these in full from your MultiSafepay balance. Follow these steps:

    1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
    2. Go to **Transactions** > **Transaction overview**.
    3. Search for the transaction and click to open the **Transaction details** page.
    4. Click **Refund order** > **Full refund**.
    5. Click **Save**.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

- When buying a Paysafecard voucher, the customer chooses an amount: 10, 25, 50 or 100 EUR.

- The funds are available immediately.

- If the customer doesn't use the full amount in the first payment, the outstanding balance remains available for 12 months free of charge. After 12 months, they are charged a monthly administration fee of 3 EUR, which is deducted from the outstanding balance.

