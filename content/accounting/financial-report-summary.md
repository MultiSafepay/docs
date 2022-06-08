---
title: "Financial report and summary"
category: 62962dee7af1c800355771a1
order: 102
hidden: false
parentDoc: 629f40b87c755200870646a0
---
This page describes the financial report and financial summary.

# Financial report
This report provides an overview (in Excel or CSV format) of:

- Paid/unpaid transactions within a specific timeframe and transaction fees
- Refunds, chargebacks, reversals
- Payouts
- Currency conversions

<details id="financial-report-contents">
<summary>Report contents</summary>
<br>

| Columns | Description |
|---|---|
| ID | MultiSafepay's transaction reference number |
| Merchant ref | Your transaction reference number |
| Created | The date the transaction was initiated |
| Completed | The date the funds were settled in your MultiSafepay balance |
| Site | The website where the customer placed the order |
| First name | The customer's first name |
| Last name | The customer's last name |
| Description | A description of the order |
| Currency | The currency of the transaction |
| Amount | The amount of the transaction |
| Payment type | A MultiSafepay fee, or the payment method |
| Payment status | The [transaction status](/about-payments/multisafepay-statuses/) |

</details>

<details id="generating-financial-reports">
<summary>Generating financial reports</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial report**.
3. In the **Between** and **And** fields, enter the start and end dates of the period you want the report to cover.
4. In the **Cost grouping** list:  
    - **No grouping:** Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **Single entry for all costs:** List each MultiSafepay fee below the matching transaction.
5. Click **Generate report**.

</details >

# Financial summary

This report provides an overview (in Excel or PDF format) of revenue and fees for:

- Payment methods
- Refunds, chargebacks, reversals 
- Transactions

<details id="financial-summary-contents">
<summary>Report contents</summary>
<br>

| Headers | Description |
|---|---|
| Report created | The date the report was generated |
| Merchant ID | Your MultiSafepay account number and merchant name |
| Currency | The currency of transactions |
| Date from | The start date of the period the report covers |
| Date till | The end date of the report period |
| Group refunds | Whether you have grouped refunds together |
| **Columns** | **Description** |
| Description | Payment method/refunds/chargebacks/reversals/transaction fees, broken down by revenue and cost |
| Column 1 | The transaction fee |
| Number | The number of transactions |
| Debit | The total amount debited |
| Credit | The total amount credited |
| Net income | The total revenue minus costs |

</details >

<details id="exclusions" >
<summary>Exclusions</summary>
<br>

The report does **not** include:

- Payouts (see [payout report](/reports/payout-report/))
- Monthly transaction fees 
- VAT (see [VAT invoices](/account/vat-invoices/))

</details >

<details id="generating-financial-summaries" >
<summary>Generating financial summaries</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial summary**.
3. Under **Options** > in the **Date** field, enter the start and end dates of the period you want the report to cover.
4. Under **Currency**, select the relevant currency.
5. Click **Generate report**.

</details >

> 📘 **Support**
> Email <support@multisafepay.com>