---
title : "Financial summary"
meta_title: "Financial summary - MultiSafepay Docs"
read_more: '.'
weight: 4
url: '/reports/financial-summary/'
aliases:
    - /tools/reports/financial-summary
    - /tools/accounting/reports/financial-summary/
    - /accounting/reports/financial-summary/
---

The financial summary provides an overview of revenue and costs for:

- Each payment method
- Refunds
- Chargebacks
- Reversals 
- Transaction fees

Supported formats: Excel or PDF

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
- Monthly transaction costs and VAT (see your monthly [VAT invoice](/account/vat-invoices/))

{{< /details >}}

## Generating a financial summary

To generate a financial summary, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial summary**.
3. Under **Options** > in the **Date** field, enter the start and end dates of the period you want the report to cover.
4. Under **Currency**, select the relevant currency.
5. Click **Generate report**.