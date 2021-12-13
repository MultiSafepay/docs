---
title: "Accountant export"
meta_title: "Reports - Accountant export - MultiSafepay Docs"

read_more: '.'
weight: 1
aliases:
    - /tools/reports/accountant-report-export/
    - /tools/reports/report-validity/
    - /tools/reports/n-codes/
    - /tools/reports/automatic-reports/
---

The Accountant export lists all successful incoming and outgoing transactions, including the:

- Amount
- Payment method
- [Transaction status](/payments/multisafepay-statuses/) (at the time the report was generated)

{{< details title="Supported formats" >}}

* CAMT053
* CODA
* CSV
* MT940
* XLS
* XLSX

{{< /details >}}

{{< details title="Exclusions" >}}
&nbsp;  
MultiSafepay does not collect funds for PayPal. Therefore, PayPal transactions don't automatically appear in the Accountant export. To include them, in your [backend](/getting-started/glossary/#backend), make sure the transaction status is set to **Completed**.

{{< /details >}}

{{< details title="Report contents" >}}
&nbsp; 

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number
- Date from: the start date of the reporting period
- Date till: the end date of the reporting period
- Currency: the currency of transactions
- Opening balance: the balance at the start date
- Total credit: the amount credited in the report period
- Total debit: the amount debited in the report period
- Closing balance: the balance at the end date

Columns:

- Completed date/time: the date and time the transaction was completed
- Amount: the transaction amount
- Creditdebit: C means credit, D means debit
- Typetransaction: see [N-codes for identifying payment methods](/reports/n-codes/)
- Paymenttype: a MultiSafepay fee, or the payment method
- Description/Description2/Description3/Description4: descriptions of the order
- Tr status: the [transaction status](/payments/multisafepay-statuses/)
- Ms description: website name
- Mt merchanttransactionid: your unique identifier for the order
- Mt cust firstname: the customer’s first name
- Mt cust lastname: the customer’s last name
- Mt cust city: the customer's city
- Mt cust country: the customer's country
- Invoice id: your internal invoice ID

{{< /details >}}

## Generating Accountant exports

To generate an Accountant export, follow these steps:

1. Sign in to your live [MultiSafepay account](https://merchant.multisafepay.com), or for test reports, your [MultiSafepay test account](https://testmerchant.multisafepay.com).
2. Go to **Reports** > **Accountant export**.
3. From the **Date selection** dropdown, select the relevant timeframe (last 2 years only), and then click **Apply**.
4. From the **Currency** dropdown, select the relevant currency.
5. From the **Report type** dropdown, select the relevant export format. 
6. **Group costs in 1 record** toggle:   
    - **Yes**: Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **No**: List each MultiSafepay fee below the matching transaction.
7. Click **Generate report**.

To filter transactions in the Accountant export (e.g. by payment method), see [N-codes for identifying payment methods](/reports/n-codes/).

## Automating Accountant exports

To request automated Accountant exports, email the following information to the Integration Team at <integration@multisafepay.com>:

- Your account ID: Top-right corner of your MultiSafepay account
- Method: SFTP Pull or Push request
- Frequency: Daily, weekly, or monthly
- File format: CAMT053, CODA, CSV, MT940, XLS, or XLSX
- Desired time: Based on Central European (Summer) Time (CET/CEST)
- MultiSafepay transaction fees: Total or listed separately

{{< details title="View SFTP requests and requirements" >}} 

- SFTP:  
  - Pull request: We give you access to a MultiSafepay SFTP server.
  - Push request: You give us access to your SFTP server.

- We support SFTP with username/password and username/SSH keys.
- For SFTP connections, we only support ports **22** and **2222**.
- Make sure our IP address is on your allow list. For more information, see [MultiSafepay IP ranges](/developer/errors-explained/multisafepay-ip-ranges/).
- To deliver the report using SFTP Push requests, you must support the following protocol on your SFTP server:

  sh-ed25519,
  rsa-sha2-512,
  rsa-sha2-256,
  ecdsa-sha2-nistp521,
  ecdsa-sha2-nistp384,
  ecdsa-sha2-nistp256,
  ssh-rsa

{{< /details >}}

For support, email the Support Team at <support@multisafepay.com>

## See also

- [Reconciliation through API](/accounting/api-reconciliation/) 
- [Accounting integrations](/business/accounting/integrations/)
