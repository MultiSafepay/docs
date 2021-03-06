---
title: "SEPA Direct Debit payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "SEPA Direct Debit payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
aliases: 
    - /payment-methods/direct-debit/how-does-direct-debit-work/
    - /payment-methods/banks/direct-debit/how-does-direct-debit-work/
    - /payment-methods/sepa-direct-debit/how-does-sepa-direct-debit-work/
    - /payment-methods/sepa-direct-debit/reason-codes/

---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | Make a SEPA Direct Debit request to MultiSafepay, providing information about the customer. |  |  |
| 2. | MultiSafepay conducts a background check on the customer's information, and if successful, creates an order. | Initialized  | Initialized |
| 3. | MultiSafepay creates an e-mandate automatically based on the customer's IBAN and your site ID. We specify if it is a `first` debit (processed within 5 days) or `recurring` debit (processed within 2 days). {{< br >}} We send all e-mandates to our bank at the end of every business day. {{< br >}} You can no longer cancel the transaction. | Uncleared | Uncleared |
| 4. | The customer's bank processes the transaction. For reasons why it may not be successful, see cancellation codes below. {{< br >}} If the IBAN or BIC is incorrect, our bank informs us the next business day. |  |  |
| 5. | MultiSafepay collects the funds. {{< br >}} For amounts smaller than 500 EUR, settlement takes 7 business days, and for amounts larger than 500 EUR it takes 20 days. | Completed | Uncleared |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance.| Completed | Completed |

{{< details title="Cancellation codes" >}}

| Code | Reason |
|-----|-------|
|AC01|Incorrect account number|
|AC04|Closed account number|
|AC06|Blocked account|
|AC13|Debtor account type is missing or invalid |
|AG01|Transaction forbidden|
|AG01|Transaction forbidden|
|AG02|Invalid bank operation code|
|AM04|Insufficient funds|
|AM05|Duplication|
|BE01|Inconsistent with customer|
|BE04|Creditor address missing or incorrect|
|BE05|Unrecognised initiating party|
|CNOR|Creditor bank is not registered|
|DNOR|Debtor bank is not registered|
|FF01|Invalid file format|
|FF05|Direct debit type incorrect|
|FOCR|Return following a cancellation request|
|MD01|No mandate|
|MD02|Required infomation missing from mandate|
|MD06|Customer requested chargeback|
|MD07|Customer deceased|
|MS02|Unspecified reason generated by customer|
|MS03|Unspecified reason generated by agent|
|RC01|Incorrect bank identifier |
|RR01|Missing debtor account or identification|
|RR02|Missing debtor name or address|
|RR03|Missing creditor name or address|
|RR04|Regulatory reason|
|SL01|Specific service offered by debtor agent|
|TM01|File received after cut-off time|

{{< /details >}}

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction was declined while **Uncleared**. | Declined | Declined   |
| The transaction has been cancelled or you provided incorrect customer information. | Cancelled   | Cancelled   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |
| The customer requested a chargeback. You cannot dispute this. | Chargeback  | Completed | 




