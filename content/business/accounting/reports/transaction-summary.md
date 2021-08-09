---
title: "Transaction summary"
weight: 10
meta_title: "Reports - Transaction summary - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 2
aliases:
    - /tools/accounting/reports/transaction-summary/
---

The Transaction summary provides an overview of all transactions within a specific timeframe.

Includes:  

- Currency
- [Transaction status](/api/multisafepay-statuses/)
- Payment method
- Website
- Grouping of costs

Supported formats: Excel or PDF

{{< details title="Report contents" >}}

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number and merchant name
- Date from: the start date of the period the report covers
- Date till: the end date of the report period

Columns:

- Completed: the date the funds were settled in your MultiSafepay balance
- Mt merchant
- Mt description
- Mt customer email: the customer's email address
- Currency: the transaction currency
- Mt orderstatus: the [order status](/api/multisafepay-statuses) at the time the report was generated
- Mt pt code: the payment method
- Modifieddate: the date the transaction was modified
- Mt cust country: the customer's country
- Mt id: your transaction reference number
- Creditdebit: C means credit, D means debit

{{< /details >}}

## Generating a Transaction summary

To generate a Transaction summary, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Transaction summary**.
3. Under **Report settings** > in the **From** and **To** fields, enter the start and end dates of the period you want the report to cover.
4. Under **Extra**, specify any other relevant parameters:  
    - **Currency** field: Select the relevant currency.
    - **Status** field: Select the [order or transaction status](/api/multisafepay-statuses), if relevant
    - **Payment method** field: Select the relevant payment method.
    - **Website** field: Select the relevant website.
    - **Group** field: Specify if you want to group costs by **Site**, **Payment method**, or **Country**.
    - To group all transactions and only show the daily total, select the **Show per day** checkbox.
4. Click **Generate report**.
