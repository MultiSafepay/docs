---
title : "Financial summary"
weight: 30
meta_title: "Reports - Financial summary - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 4
aliases:
    - /tools/reports/financial-summary
    - /tools/accounting/reports/financial-summary/
---

The Financial summary provides an overview of revenue and costs for:

- Each payment method
- Refunds
- Chargebacks
- Reversals 
- Transaction fees

Supported formats: Excel or PDF

{{< details title="Report contents" >}}

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number and merchant name
- Currency: the currency of transactions
- Date from: the start date of the period the report covers
- Date till: the end date of the report period
- Group refunds: whether you have grouped refunds together

Columns:

- Description: Payment method/refunds/chargebacks/reversals/transaction fees, broken down by revenue and cost
- Column 1: The transaction fee
- Number: The number of transactions
- Debit: The total amount debited
- Credit: The total amount credited 
- Net income: The total revenue minus costs

{{< /details >}}

{{< details title="Exclusions" >}}

The report does **not** include:

- Payouts – see [Payout report](/reports/payout-report/)
- Monthly transaction costs and VAT – see your monthly [VAT invoice](/account/multisafepay-account/multisafepay-vat/)

{{< /details >}}

## Generating a Financial summary

To generate a Financial summary, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial summary**.
3. Under **Options** > in the **Date** field, enter the start and end dates of the period you want the report to cover.
4. Click **Generate report**.