---
title: "Financial report"
meta_title: "Financial report - MultiSafepay Docs"
read_more: "."
weight: 3
url: "/reports/financial-report/"
aliases:
    - /tools/accounting/reports/financial-report/
    - /accounting/reports/financial-report/
---
The financial report provides an overview of:

- Transactions within a specific timeframe and grouping of costs  
- Paid transactions
- Refunds
- Chargebacks/reversals
- Payouts
- Currency conversions

Supported formats: Excel or CSV

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

## Generating financial reports

To generate a financial report, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Reports** > **Financial report**.
3. In the **Between** and **And** fields, enter the start and end dates of the period you want the report to cover.
4. In the **Cost grouping** list:  
    - **No grouping:** Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **Single entry for all costs:** List each MultiSafepay fee below the matching transaction.
5. Click **Generate report**.