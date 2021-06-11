---
title: "Accountant export"
weight: 40
meta_title: "Reports - Accountant export - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
weight: 1
aliases:
    - /tools/reports/accountant-report-export
    - /tools/reports/report-validity
    - /tools/reports/N-codes
    - /tools/reports/automatic-reports
---

The Accountant export lists all successful incoming and outgoing transactions, including the amount, payment method, and transaction status (at the time the report was generated).

{{< details title="View export formats" >}}
You can generate the report in the following formats:

* CAMT053
* CODA
* CSV
* MT940
* XLS
* XLSX

{{< /details >}}

{{< details title="View exclusions" >}}
&nbsp;  
MultiSafepay does not collect funds for PayPal. Therefore, PayPal transactions don't automatically appear in the Accountant export. To include them, in your backend, make sure the financial status for PayPal transactions is set to **Completed**.

{{< /details >}}

For support, email the Support Team at <support@multisafepay.com>

## Generating Accountant exports

To generate an Accountant export, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com), or for test reports, your [MultiSafepay Test Control](https://testmerchant.multisafepay.com).
2. Go to **Reports** > **Accountant export**.
3. From the **Date selection** dropdown, select the relevant timeframe (last 2 years only), and then click **Apply**.
4. From the **Report type** dropdown, select the relevant export format. 
5. **Group costs in 1 record** toggle:   
    - **Yes**: Show only the total of all MultiSafepay transaction fees for the selected timeframe.
    - **No**: List each MultiSafepay fee below the matching transaction.
6. Click **Generate report**.

{{< details title="View N-Codes to filter transactions" >}}

To filter transactions in the Accountant export (e.g. by payment method), use the following **N-Codes**:

| N-Code | Transaction type                                        |   |
|--------|---------------------------------------------------------|---|
| N001   | [MASTERCARD](/payment-methods/credit-and-debit-cards/mastercard)             |   |
| N002   | [VISA](/payment-methods/credit-and-debit-cards/mastercard)                   |   |
| N003   | [MAESTRO](/payment-methods/credit-and-debit-cards/maestro)                    |   |
| N004   | WALLET                                                  |   |
| N006   | [DANKORT](/payment-methods/credit-and-debit-cards/dankort)       |   |
| N016   | [ALIPAY](/payment-methods/wallet/alipay)                      |   |
| N017   | [DOTPAY](/payment-methods/banks/dotpay)                      |   |
| N018   | [POSTEPAY](/payment-methods/credit-and-debit-cards/postepay)      |   |
| N021   | [IDEAL](/payment-methods/banks/ideal)                        |   |
| N031   | [GIROPAY](/payment-methods/banks/giropay)                    |   |
| N081   | [BANKTRANS](/payment-methods/banks/bank-transfer)            |   |
| N085   | [AMEX](/payment-methods/credit-and-debit-cards/american-express)                   |   |
| N086   | [KLARNA](/payment-methods/billing-suite/klarna)                      |   |
| N088   | [PAYAFTER](/payment-methods/billing-suite/pay-after-delivery)        |   |
| N089   | [SANTANDER](/payment-methods/billing-suite/betaalpermaand)               |   |
| N092   | [DIRECTBANK](/payment-methods/banks/sofort-banking)          |   |
| N093   | CURRENCY CONVERSION                                     |   |
| N094   | [MISTERCASH](/payment-methods/banks/bancontact)              |   |
| N095   | [CHARGEBACK](/faq/chargebacks) |   |
| N096   | WITHDRAWAL                                              |   |
| N097   | Refund                                                  |   |
| N098   | [COUPON](/payment-methods/prepaid-cards/gift-cards)                  |   |
| N101   | [DIRDEB](/payment-methods/banks/sepa-direct-debit)                |   |
| N102   | [iDEAL QR](/payment-methods/banks/idealqr)                   |   |
| N102   | [BELFIUS](/payment-methods/banks/belfius)                    |   |
| N103   | [EPS](/payment-methods/banks/eps)                            |   |
| N104   | [EINVOICE](/payment-methods/billing-suite/e-invoicing)               |   |
| N105   | [AFTERPAY](/payment-methods/billing-suite/afterpay)                  |   |
| N106   | [INGHOME](/payment-methods/banks/ing-home-pay)               |   |
| N107   | FERBUY                                                  |   |
| N108   | [TRUSTLY](/payment-methods/banks/trustly)                    |   |
| N109   | [KBC](/payment-methods/banks/kbc)                            |   |
| N913   | FEE                                                     |   |

{{< /details >}}

## Automating Accountant exports


To request automated Accountant exports, email the following information to the Integration Team at <integration@multisafepay.com>:

- Your account ID: Top-right corner of your MultiSafepay Control
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

## See also

- [Transactions API endpoint](/tools/transactions-api-endpoint/) 
- [Accounting integrations](/tools/accounting/accounting-integrations/)

