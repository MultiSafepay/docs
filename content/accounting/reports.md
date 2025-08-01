---
title: 'Reports'
category: 62962dee7af1c800355771a1
order: 2
hidden: false
slug: 'reports'
---
Reports can be generated via your Merchant Dashboard, or received in a [subscription](/docs/reports#set-up-automated-reports).

Note: You can only retrieve data from approximately two years back.

# Accountant export

The accountant export lists all successful incoming and outgoing transactions, including the:

* Amount
* Payment method
* Current <Glossary>transaction status</Glossary>

<details id="supported-formats">
  <summary>Supported formats</summary>

  <br />

  * CAMT053
  * CODA
  * CSV
  * MT940
  * XLS
  * XLSX
</details>

<details id="report-contents">
  <summary>Report contents</summary>

  <br />

  | Headers                  | Description                                                                           |
  | ------------------------ | ------------------------------------------------------------------------------------- |
  | Report created           | The date the report was generated                                                     |
  | Merchant ID              | Your MultiSafepay account number                                                      |
  | Date from                | The start date of the reporting period                                                |
  | Date till                | The end date of the reporting period                                                  |
  | Currency                 | The currency of transactions                                                          |
  | Opening balance          | The balance at the start date                                                         |
  | Total credit             | The amount credited in the report period                                              |
  | Total debit              | The amount debited in the report period                                               |
  | Closing balance          | The balance at the end date                                                           |
  | **Columns**              | **Description**                                                                       |
  | Completed date/time      | The date and time the transaction was completed                                       |
  | Amount                   | The transaction amount                                                                |
  | Creditdebit              | C means credit, D means debit                                                         |
  | Typetransaction          | See [N-codes for identifying payment methods](/docs/reports#filter-by-payment-method) |
  | Paymenttype              | A MultiSafepay fee, or the payment method                                             |
  | Description 2-4          | Descriptions of the order                                                             |
  | Tr status                | The <Glossary>transaction status</Glossary>                                           |
  | Ms description           | The website name, or name of the terminal group                                       |
  | Mt merchanttransactionid | Your unique identifier for the order                                                  |
  | Mt cust firstname        | The customer’s first name                                                             |
  | Mt cust lastname         | The customer’s last name                                                              |
  | Mt cust city             | The customer's city                                                                   |
  | Mt cust country          | The customer's country                                                                |
  | Invoice ID               | Your internal invoice ID                                                              |
</details>

<details id="paypal-transactions">
  <summary>PayPal transactions</summary>

  <br />

  MultiSafepay does not collect funds for PayPal, therefore these transactions don't appear in accountant exports.

  You can view them in your dashboard under **Transaction overview**.
</details>

<details id="how-to-generate-accountant-exports">
  <summary>How to generate accountant exports</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">live</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> or <a href="https://testmerchant.multisafepay.com" target="_blank">test</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> dashboard.
  2. Go to **Reports** > **Accountant export**.
  3. From the **Date selection** list, select the relevant timeframe (last 2 years only), and then click **Apply**.
  4. From the **Currency** list, select the relevant currency.
  5. From the **Report type** list, select the relevant export format.
  6. For the **Group costs in 1 record** toggle, set to:
     * **Yes:** Show only the total of all MultiSafepay transaction fees for the selected timeframe.
     * **No:** List each MultiSafepay fee below the matching transaction.
  7. Click **Generate report**.
</details>

You can import accountant exports into a range of third-party [accounting platforms](/docs/accounting-integrations/).

***

# Financial report

This report provides an overview (in Excel or CSV format) of:

* Paid/unpaid transactions within a specific timeframe and transaction fees
* Refunds, chargebacks, <Glossary>reversals</Glossary>
* <Glossary>Payouts</Glossary>
* Currency conversions

<details id="financial-report-contents">
  <summary>Report contents</summary>

  <br />

  | Columns        | Description                                             |
  | -------------- | ------------------------------------------------------- |
  | ID             | MultiSafepay's transaction reference number             |
  | Merchant ref   | Your transaction reference number                       |
  | Created        | The date the transaction was initiated                  |
  | Completed      | The date the funds were settled in your account balance |
  | Site           | The website where the customer placed the order         |
  | First name     | The customer's first name                               |
  | Last name      | The customer's last name                                |
  | Description    | A description of the order                              |
  | Currency       | The currency of the transaction                         |
  | Amount         | The amount of the transaction                           |
  | Payment type   | A MultiSafepay fee, or the payment method               |
  | Payment status | The <Glossary>transaction status</Glossary>             |
</details>

<details id="how-to-generate-financial-reports">
  <summary>How to generate financial reports</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Financial report**.
  3. To specify the period you want the report to cover, click the date selector under **Period**.
  4. From the **Cost grouping** list, select:
     * **No grouping**: Show only the total of all MultiSafepay transaction fees for the selected timeframe.
     * **Single entry for all costs**: List each MultiSafepay fee below the matching transaction.
  5. Click **Generate report**.
</details>

***

# Conversion reports

This report provides insight (in Excel format) into your conversion rate. You can filter by:

* Customer country and device
* Day
* Payment method
* Website

<details id="how-to-generate-conversion-reports">
  <summary>How to generate conversion reports</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Advanced reporting**.
     * Under **Date**, select the date range you want the report to cover.
     * Under **Currency**, select the relevant currency.
     * Under **Website** and **Site 2**, specify one or two websites (if relevant).
  3. To download, click **XLS** or **XLSX**.
  4. Click **Execute report**.
</details>

***

# Financial summary

This report provides an overview (in Excel or PDF format) of revenue and fees for:

* Payment methods
* Refunds, chargebacks, <Glossary>reversals</Glossary>
* Transactions

<details id="financial-summary-contents">
  <summary>Report contents</summary>

  <br />

  | Headers        | Description                                                                                    |
  | -------------- | ---------------------------------------------------------------------------------------------- |
  | Report created | The date the report was generated                                                              |
  | Merchant ID    | Your MultiSafepay account number and merchant name                                             |
  | Currency       | The currency of transactions                                                                   |
  | Date from      | The start date of the period the report covers                                                 |
  | Date till      | The end date of the report period                                                              |
  | Group refunds  | Whether you have grouped refunds together                                                      |
  | **Columns**    | **Description**                                                                                |
  | Description    | Payment method/refunds/chargebacks/reversals/transaction fees, broken down by revenue and cost |
  | Column 1       | The transaction fee                                                                            |
  | Number         | The number of transactions                                                                     |
  | Debit          | The total amount debited                                                                       |
  | Credit         | The total amount credited                                                                      |
  | Net income     | The total revenue minus costs                                                                  |

  **Exclusions**

  The report does **not** include:

  * <Glossary>Payouts</Glossary> (see [Payout report](#payout-report))
  * Monthly transaction fees
  * VAT (see [VAT invoices](/docs/invoices/))
</details>

<details id="how-to-generate-financial-summaries">
  <summary>How to generate financial summaries</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Financial summary**.
  3. Under **Options**, in the **Date** field, enter the start and end dates of the period you want the report to cover.
  4. From the **Currency** list, select the relevant currency.
  5. Click **Generate report**.
</details>

***

# Payout report

This report provides an overview (in Excel format) of the specific transactions and fees per <Glossary>payout</Glossary>. It is helpful for matching payouts to specific orders or invoices for accounting purposes. See also [Payouts](/docs/payouts/).

<details id="report-contents">
  <summary>Report contents</summary>

  <br />

  | Headers             | Description                                                                                                           |
  | ------------------- | --------------------------------------------------------------------------------------------------------------------- |
  | Report created      | The date the report was generated                                                                                     |
  | Merchant ID         | Your MultiSafepay account number and merchant name                                                                    |
  | Payout ID           | The reference number for this payout                                                                                  |
  | Logic               | What time the payout was made                                                                                         |
  | Date from           | The start date of the reporting period                                                                                |
  | Date till           | The end date of the reporting period                                                                                  |
  | Payout currency     | The currency the payout was paid in                                                                                   |
  | **Columns**         | **Description**                                                                                                       |
  | Created date        | The date the transaction was initiated                                                                                |
  | Completed date/time | The date and time the transaction was completed                                                                       |
  | Mt status           | The <Glossary>transaction status</Glossary>                                                                           |
  | Mt order status     | The <Glossary>order status</Glossary>                                                                                 |
  | PSP ID              | MultiSafepay's transaction reference number                                                                           |
  | Amount              | The transaction amount in whole currency                                                                              |
  | Amount cents        | The transaction amount in cents                                                                                       |
  | Creditdebit         | C means credit, D means debit                                                                                         |
  | N code              | See [N-codes for identifying payment methods](/docs/reports#filter-by-payment-method)                                 |
  | Payment type        | A MultiSafepay fee, or the payment method                                                                             |
  | Mt description      | A description of the transaction                                                                                      |
  | Sub description     | A description of a component of the transaction, e.g. an <Glossary>issuer</Glossary>  fee or currency conversion cost |
  | Sub status          | The <Glossary>transaction status</Glossary>                                                                           |
  | Sub ID              | MultiSafepay's transaction reference number                                                                           |
  | Ms description      | The website name                                                                                                      |
  | Order ID            | Your unique identifier for the order                                                                                  |
  | Var1/Var2/Var3      | Additional information                                                                                                |
</details>

<details id="how-to-generate-payout-reports">
  <summary>How to generate payout reports</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Daily balance**.
  3. Under **Payout ID** for the relevant date, click the green **Export** icon.

    **💡 Tip!** You must have completed at least one payout to generate a payout report.
</details>

***

# Sales report

This report provides an overview (in Excel format) of the total revenue and/or number of transactions per:

* Customer country and device
* Day
* Payment method
* Website

<details id="how-to-generate-sales-reports">
  <summary>How to generate sales reports</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Advanced reporting** > **Website**.
  3. Under **Date**, select the date range you want the report to cover.
  4. If relevant, specify one or two websites under **Website** and **Site 2**.
  5. To download, click **XLS** or **XLSX**.
</details>

***

# Second Chance report

This report provides an overview (in Excel format) of all transactions:

* By payment method or country
* Declined, retried and completed, retried and completed with a different payment method
* Completed with [Second Chance](/docs/second-chance/)

To request a Second Chance report, email \<[sales@multisafepay.com](mailto:sales@multisafepay.com)>

<details id="report-contents">
  <summary>Report contents</summary>

  <br />

  | Column                             | Description                                                                         |     |
  | ---------------------------------- | ----------------------------------------------------------------------------------- | --- |
  | Report created                     | The date the report was generated                                                   |     |
  | Merchant ID                        | Your MultiSafepay account number                                                    |     |
  | Date from                          | The start date of the reporting period                                              |     |
  | Date till                          | The end date of the reporting period                                                |     |
  | **By payment method or country**   |                                                                                     |     |
  | Paymentmethod                      | The payment method                                                                  |     |
  | Country                            | The country where the transaction took place                                        |     |
  | Completed                          | The number of completed transactions                                                |     |
  | Declined                           | The number of declined transactions                                                 |     |
  | Retry completed                    | The number of transactions that were completed after retrying                       |     |
  | Retry completed diff paymentmethod | The number of transactions completed after retrying with a different payment method |     |
  | Perc completed                     | The percentage of all transactions that were successfully completed                 |     |
  | **Other sections**                 |                                                                                     |     |
  | Created                            | The time the transaction was created                                                |     |
  | Maintransaction                    | MultiSafepay's transaction reference number                                         |     |
  | Paymenttype                        | The payment method                                                                  |     |
  | Country                            | The country where the transaction took place                                        |     |
  | Email                              | The customer's email address                                                        | All |
  | Merchant ID                        | Your unique identifier for the order                                                |     |
  | **Declined:**                      |                                                                                     |     |
  | Reason                             | Any reason why the transaction was declined                                         |     |
  | **Retried and completed:**         |                                                                                     |     |
  | Result                             | Any additional information about the transaction                                    |     |
  | **Different payment method:**      |                                                                                     |     |
  | Original                           | The original payment method                                                         |     |
  | Retry                              | The payment method used to retry                                                    |     |
  | Result                             | Any additional information about the transaction                                    |     |
  | **Completed with Second Chance:**  |                                                                                     |     |
  | Amount                             | The amount paid                                                                     |     |
  | Totals                             | The total number of transactions, and total amount paid                             |     |
</details>

***

# Transaction summary

This report provides an overview (in Excel or PDF format) of all transactions within a specific timeframe, including:

* Fees
* Amount and currency
* Websites

<details id="how-to-generate-transaction-summaries">
  <summary>How to generate transaction summaries</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Reports** > **Transaction summary**.
  3. Under **Report settings** > in the **From** and **To** fields, enter the start and end dates of the period you want the report to cover.
  4. Under **Extra**, specify any other relevant parameters:
     * **Currency** field: Select the relevant currency.
     * **Status** field: Select the <Glossary>order status</Glossary>  or <Glossary>transaction status</Glossary> , if relevant
     * **Payment method** field: Select the relevant payment method.
     * **Website** field: Select the relevant website.
     * **Grouping method** field: Specify if you want to total fees together per **Website**, **Payment method**, or **Country**, or not at all.
     * To group all transactions and only show the daily total, select the **Show per day** checkbox.
  5. Click **Generate report**.
</details>

***

# Set up automated reports

You can automate generation of accountant exports and payout reports.

<details id="how-to-request-automated-exports">
  <summary>How to request automated exports</summary>

  <br />

  To request automated accountant exports, email the following information to \<[support@multisafepay.com](mailto:support@multisafepay.com)>:

  * Your account ID (top-right corner of your MultiSafepay dashboard)
  * Method: SFTP Pull or Push request
  * Frequency: Daily, weekly, or monthly
  * Preferred time after 05:29 (based on Central European (Summer) Time (CET/CEST))
  * Accountant export:
    * File format: CAMT053, CODA, CSV, MT940, XLS, or XLSX
    * MultiSafepay transaction fees: Total or listed separately

  To view the autogenerated reports in your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, click the **Messages** icon in the top-right corner.
</details>

<details id="SFTP-requests-and-requirements">
  <summary>SFTP requests and requirements</summary>

  <br />

  * SFTP:
    * Pull request: We give you access to a MultiSafepay SFTP server.
    * Push request: You give us access to your SFTP server.

  * We support SFTP with username/password and username/SSH keys.

  * For SFTP connections, we only support ports **22** and **2222**.

  * Make sure our IP address is on your allow list. For a list of MultiSafepay IP addresses, email \<[support@multisafepay.com](mailto:support@multisafepay.com)>

  * To deliver the report using SFTP Push requests, you must support the following protocols on your SFTP server:

    `sh-ed25519`,
    `rsa-sha2-512`,
    `rsa-sha2-256`,
    `ecdsa-sha2-nistp521`,
    `ecdsa-sha2-nistp384`,
    `ecdsa-sha2-nistp256`,
    `ssh-rsa`
</details>

***

# Filter by payment method

To identify transactions in reports by payment method, use the following N-codes.

| N-Code | Transaction type                      |
| ------ | ------------------------------------- |
| N001   | [MASTERCARD](/docs/card-payments/)    |
| N002   | [VISA](/docs/card-payments/)          |
| N003   | [MAESTRO](/docs/card-payments/)       |
| N004   | WALLET                                |
| N006   | [DANKORT](/docs/card-payments/)       |
| N016   | [ALIPAY](/docs/alipay/)               |
| N017   | [DOTPAY](/docs/dotpay/)               |
| N018   | [POSTEPAY](/docs/card-payments/)      |
| N021   | [IDEAL](/docs/ideal/)                 |
| N031   | [GIROPAY](/docs/giropay/)             |
| N081   | [BANKTRANS](/docs/bank-transfer/)     |
| N085   | [AMEX](/docs/card-payments/)          |
| N086   | [KLARNA](/docs/klarna/)               |
| N088   | [PAYAFTER](/docs/pay-after-delivery/) |
| N089   | [SANTANDER](/docs/betaal-per-maand/)  |
| N090   | [in3](/docs/in3/)                     |
| N092   | [DIRECTBANK](/docs/sofort/)           |
| N093   | CURRENCY CONVERSION                   |
| N094   | [MISTERCASH](/docs/bancontact/)       |
| N095   | [CHARGEBACK](/docs/chargebacks/)      |
| N096   | WITHDRAWAL                            |
| N097   | Refund                                |
| N098   | [COUPON](/docs/gift-cards/)           |
| N101   | [DIRDEB](/docs/direct-debit/)         |
| N102   | [iDEAL QR](/docs/ideal/)              |
| N102   | [BELFIUS](/docs/belfius/)             |
| N103   | [EPS](/docs/eps/)                     |
| N104   | [EINVOICE](/docs/e-invoicing/)        |
| N105   | [Riverty](/docs/riverty/)             |
| N107   | FERBUY                                |
| N108   | [TRUSTLY](/docs/trustly/)             |
| N109   | [KBC](/docs/cbc-kbc/)                 |
| N913   | FEE                                   |

<br />

## Troubleshooting

### Data range not applied

In some cases, the custom range selected for your report is not applied immediately. This can usually be solved by either accessing from a different browser, or deleting your cookies / cache data.

### Payout report not generated

**⚠️Note:** The payout report is only available for automated withdrawals.

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>
[Top of page](#)