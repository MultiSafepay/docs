---
title : "Payout report"
meta_title: "Reports - Payout report - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 5
url: '/reports/payout-report/'
---

The Payout report provides an overview of the specific transactions and fees included in a [payout](/account/payouts/).

It is helpful for matching payouts to specific orders or invoices for accounting purposes. 

Supported format: Excel

{{< details title="Report contents" >}}
&nbsp; 

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number and merchant name
- Payout ID: the reference number for this payout
- Logic: what time the payout was made
- Date from: the start date of the reporting period
- Date till: the end date of the reporting period
- Payout currency: the currency the payout was paid in

Columns:

- Created date: the date the transaction was initiated
- Completed date/time: the date and time the transaction was completed
- Mt status: the [transaction status](/payments/multisafepay-statuses/)
- Mt order status: the [order status](/payments/multisafepay-statuses/)
- Psp id: MultiSafepay's transaction reference number
- Amount: the transaction amount in whole currency
- Amount cents: the transaction amount in cents
- Creditdebit: C means credit, D means debit
- N code: see [N-codes for identifying payment methods](/reports/n-codes/)
- Payment type: a MultiSafepay fee, or the payment method
- Mt description: description of the transaction 
- Sub description: description of a component of the transaction. For example, an issuer fee or currency conversion cost.
- Sub status: the [transaction status](/payments/multisafepay-statuses/)
- Sub id: MultiSafepay's transaction reference number
- Ms description: website name
- Order id: your unique identifier for the order
- Var1/Var2/Var3: additional information

{{< /details >}}

## Generating Payout reports

**Note:** You must have completed at least one payout to generate a Payout report.

To generate a Payout report, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Finance** > **Daily balance**.
3. In the **Daily balance overview** page, under **Payout transaction** for the relevant date, click the green Excel icon.

