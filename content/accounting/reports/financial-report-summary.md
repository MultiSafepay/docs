---
title: "Financial report and summary"
meta_title: "Financial report and summary - MultiSafepay Docs"
read_more: '.'
weight: 3
url: '/reports/financial-report-summary/'
aliases:
    - /tools/accounting/reports/financial-report/
    - /accounting/reports/financial-report/
    - /tools/reports/financial-summary
    - /tools/accounting/reports/financial-summary/
    - /accounting/reports/financial-summary/
    - /reports/financial-summary/
    - /reports/financial-report/
    - /tools/reports/financial-summary
    - /tools/accounting/reports/financial-summary/
    - /accounting/reports/financial-summary/
    - /reports/financial-summary/
---
This page describes the financial report and financial summary.

## Financial report
This report provides an overview (in Excel or CSV format) of:

- Paid/unpaid transactions within a specific timeframe and transaction fees
- Refunds, chargebacks, reversals
- Payouts
- Currency conversions

{{< details title="Report contents" >}}
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

{{< /details >}}

{{< details title="Generating financial reports" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial report**.
3. In the **Between** and **And** fields, enter the start and end dates of the period you want the report to cover.
4. In the **Cost grouping** list:  
    - **No grouping:** Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **Single entry for all costs:** List each MultiSafepay fee below the matching transaction.
5. Click **Generate report**.

{{< /details >}}

## Financial summary

This report provides an overview (in Excel or PDF format) of revenue and fees for:

- Payment methods
- Refunds, chargebacks, reversals 
- Transactions

{{< details title="Report contents" >}}
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

{{< /details >}}

{{< details title="Exclusions" >}}

The report does **not** include:

- Payouts (see [payout report](/reports/payout-report/))
- Monthly transaction fees 
- VAT (see [VAT invoices](/account/vat-invoices/))

{{< /details >}}

{{< details title="Generating financial summaries" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial summary**.
3. Under **Options** > in the **Date** field, enter the start and end dates of the period you want the report to cover.
4. Under **Currency**, select the relevant currency.
5. Click **Generate report**.

{{< /details >}}