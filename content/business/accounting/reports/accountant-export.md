---
title: "Accountant export"
weight: 40
meta_title: "Reports - Accountant export - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
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

## Generating Accountant exports

To generate an Accountant export, follow these steps:

1. Sign in to your live [MultiSafepay account](https://merchant.multisafepay.com), or for test reports, your [MultiSafepay test account](https://testmerchant.multisafepay.com).
2. Go to **Reports** > **Accountant export**.
3. From the **Date selection** dropdown, select the relevant timeframe (last 2 years only), and then click **Apply**.
4. From the **Report type** dropdown, select the relevant export format. 
5. **Group costs in 1 record** toggle:   
    - **Yes**: Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **No**: List each MultiSafepay fee below the matching transaction.
6. Click **Generate report**.

To filter transactions in the Accountant export (e.g. by payment method), see [N-codes for identifying payment methods](/reports/n-codes/).

## Automating Accountant exports

To request automated Accountant exports, email the following information to the Integration Team at <integration@multisafepay.com>:

- Your account ID: Top-right corner of your MultiSafepay account
- Method: SFTP Pull or Push request, or email
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
- Make sure our IP address is on your allow list. For more information, see [MultiSafepay IP ranges](/faq/general/ip-ranges).
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

- [Transactions API endpoint](/business/accounting/transactions-api-endpoint/) 
- [Accounting integrations](/business/accounting/integrations/)
