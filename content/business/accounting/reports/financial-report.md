---
title: "Financial report"
weight: 20
meta_title: "Reports - Financial report - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 3
aliases:
    - /tools/accounting/reports/financial-report/
---
The Financial report provides an overview of:

- Transactions within a specific timeframe and grouping of costs
- The following types of completed transactions:  
    - Paid transactions
    - Refunds
    - Chargebacks/reversals
    - Payouts
    - Currency conversions

Supported formats: Excel or CSV

{{< details title="Report contents" >}}

- ID: MultiSafepay's transaction reference number
- Merchant ref: your transaction reference number
- Created: the date the transaction was initiated
- Completed: the date the funds were settled in your MultiSafepay balance
- Site: the website where the customer placed the order
- First name: the customer's first name
- Last name: the customer's last name
- Description: a description of the order
- Currency: the currency of the transaction
- Amount: the amount of the transaction
- Payment status: the [transaction status](/api/multisafepay-statuses)

{{< /details >}}

## Generating Financial reports

To generate a Financial report, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial report**.
3. In the **Between** and **And** fields, enter the start and end dates of the period you want the report to cover.
4. In the **Cost grouping** dropdown menu:  
    - **No grouping:** Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **Single entry for all costs:** List each MultiSafepay fee below the matching transaction.
5. Click **Generate report**.