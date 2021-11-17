---
title: "SEPA Direct Debit payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "SEPA Direct Debit payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
url: '/payment-methods/sepa-direct-debit/payment-flow/'
aliases: 
    - /payment-methods/direct-debit/how-does-direct-debit-work/
    - /payment-methods/banks/direct-debit/how-does-direct-debit-work/
    - /payment-methods/sepa-direct-debit/how-does-sepa-direct-debit-work/
    - /payment-methods/sepa-direct-debit/reason-codes/
    - /payments/methods/banks/sepa-direct-debit/payment-flow/
    - /payments/sepa-direct-debit/reason-codes

---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    
    C->>Me: Selects SEPA Direct Debit <br> at checkout
    Me->>Mu: Sends request and <br> customer information
    Mu->>CB: Conducts background check <br> and sends e-mandate
    CB->>Mu: Processes transaction and transfers funds 
    Note over CB,Mu: -500 EUR= 7 business days <br> +500 EUR= 20 business days <br> See reason codes for declined transactions below.
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | A request with the customer's information is sent straight to MultiSafepay. | [API reference](/api/#sepa-direct-debit---direct) |
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/) to confirm their IBAN and account name. {{< br >}} A request with the customer's information is sent to MultiSafepay. {{< br >}} The customer is redirected to your success page. | [API reference](/api/#sepa-direct-debit---redirect) |

### E-mandates

MultiSafepay creates e-mandates automatically based on the customer's IBAN and your site ID, specifying if it is a:

- `first` debit (processed within 5 days), or 
- `recurring` debit (processed within 2 days)

We send all e-mandates to our bank at the end of every business day.  

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| MultiSafepay's customer background check was successful and the transaction is initiated. | Initialized  | Initialized |
| MultiSafepay has sent an e-mandate to the customer's bank. {{< br >}} (You can no longer cancel the transaction.) | Uncleared | Uncleared |
| The customer's bank is processing the transaction and transfering the funds. | Completed | Uncleared |
| The transaction is complete.| Completed | Completed |
| The transaction was cancelled. {{< br >}} The customer's information may have been incorrect. | Cancelled   | Cancelled   |
| The transaction was declined. {{< br >}} See the reason codes below. | Declined | Declined   |

{{< details title="Reason codes for declined transactions">}}

The table below sets out the reason codes for why SEPA Direct Debit transactions might be unsuccessful and suggested actions to take.

If the IBAN or BIC is incorrect, our bank informs us the next business day.

| Code | Reason | |
|-----|-------|---|
|AC01|Incorrect account number| Contact the debtor to confirm the IBAN. If there is a mandate amendment, check the data provided by the debtor. |
|AC04|Closed account number| Contact the debtor to confirm the new IBAN. |
|AC06|Blocked account| Contact the debtor for another account or means of payment. |
|AC13|Debtor account type is missing or invalid | Contact the debtor for clarification and to agree another means of payment. |
|AG01|Transaction forbidden| Contact the debtor for another account or means of payment. |
|AG02|Invalid bank operation code| Resubmit the transaction with the correct authorization reference and transaction type: `OOFF` or `RCUR`. |
|AM04|Insufficient funds| Contact the debtor to add funds to their account. |
|AM05|Duplication| Contact your bank to confirm whether collection was duplicated. |
|BE04|Creditor address missing or incorrect| |
|BE05|Unrecognised initiating party| The creditor ID was incorrect or was changed without an amendment indicator. Check your contract for the correct creditor ID. If in doubt, contact your bank first. |
|CNOR|Creditor bank is not registered | Contact your bank. |
|DNOR|Debtor bank is not registered | Contact your bank. Contact the debtor for another means of payment. |
|ED05|Settlement failed | Depends on the SLA between the debtor's bank and the Clearing and Settlement Mechanism (CSM). |
|FF01|Invalid file format| Repair the XML file. |
|FF05|Direct debit type incorrect| |
|FOCR|Return following a cancellation request| |
|MD01|No mandate| Analyse the characteristics of the SDD collection. Contact the debtor if they request a refund. |
|MD02|Required infomation missing from mandate| Amend the mandate.  |
|MD06|Customer requested chargeback| Contact the debtor. |
|MD07|Customer deceased| Close the agreement with the deceased debtor. |
|MS02|Unspecified reason generated by customer| Contact the debtor. |
|MS03|Unspecified reason generated by agent| Contact the debtor. |
|RC01|Incorrect bank identifier | Contact the debtor for the correct BIC for a non-EEA collection. Ask your bank to allocate the debtor's bank's correct BIC in the interbank message. |
|RR01|Missing debtor account or identification| Repair the collection to complete the debtor's account information. Contact your bank. |
|RR02|Missing debtor name or address| Repair the collection to complete the debtor's name and/or address. Contact your bank. |
|RR03|Missing creditor name or address| Repair the collection to complete your name. Contact your bank. |
|RR04|Regulatory reason| Contact your bank. |
|SL01|Specific service offered by debtor agent| Contact the debtor. |
|TM01|File received after cut-off time| |

For more information in:

- English, see European Payments Council – [Guidance on reason codes](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2019-05/EPC173-14%20v5.0%20Guidance%20on%20Reason%20Codes%20for%20SDD%20R-transactions.pdf). 
- Dutch, see Betaal Vereniging – [Reasoncodes en vervolgacties](https://www.betaalvereniging.nl/wp-content/uploads/Reasoncodes-en-vervolgacties-Europese-incasso.pdf).

{{< /details >}}

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |
| The customer has requested a chargeback. | Chargeback  | Completed | 

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).


