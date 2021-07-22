---
title : "Payout report"
meta_title: "Reports - Payout report - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 60
url: '/reports/payout-report/'
---

Payout reports let you:

- See the specific transactions and fees included in a payout.
- Match payouts to specific orders or invoices for accounting purposes. 

{{< details title="Report contents" >}}
&nbsp; 
The Payout report lists:

- Report created: the date the report was generated
- Payout ID: the reference number for this payout
- Logic: what time the payout was made
- Continue on error:
- Target hash:
- Date from: the start date of the period the report covers
- Date till: the end date of the report period
- Payout currency: the currency the payout was paid in

For each transaction:

- created date: the date the transaction was initiated
- completed date/time: the date and time the transaction was completed
- mt status: the [transaction status](/api/multisafepay-statuses/)
- mt order status: the [order status](/api/multisafepay-statuses/)
- psp id: 
- amount: the transaction amount in whole currency
- amount cents: the transactio amount in cents
- creditdebit: C means credit, D means debit
- n code: see [N-codes for identifying payment methods](/reports/n-codes/)
- payment type: a MultiSafepay fee, or the payment method
- mt description: your description of the transaction 

{{< /details >}}

## Downloading Payout reports

**Note:** You must have completed at least one payout to download a Payout report.

To download a Payout report to Microsoft Excel, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Finance** > **Daily balance**.
3. In the **Daily balance overview** page, under **Payout transaction** for the relevant date, click the green Excel icon.

