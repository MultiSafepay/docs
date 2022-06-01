---
title: 'SEPA Direct Debit'
weight: 90
meta_title: "Payment methods - SEPA Direct Debit - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/directdebit-en.svg' 
short_description: 'Debit European customers directly from their bank account.'
url: '/payment-methods/sepa-direct-debit/'
aliases:
    - /support-tab/magento2/payment-methods/direct-debit
    - /payment-methods/direct-debit/
    - /payment-methods/banks/direct-debit/
    - /payment-methods/banks/sepa-direct-debit
    - /payments/methods/banks/sepa-direct-debit/
    - /payment-methods/sepa-direct-debit/what-is-sepa-direct-debit/
    - /payment-methods/direct-debit/what-is-direct-debit/
    - /payment-methods/banks/direct-debit/what-is-direct-debit/
    - /payments/methods/banks/sepa-direct-debit/about/
    - /payments/methods/sepa/product-rules/
    - /payment-methods/sepa-direct-debit/product-rules/
    - /payment-methods/sepa-direct-debit/overview/
    - /payment-methods/direct-debit/how-does-direct-debit-work/
    - /payment-methods/banks/direct-debit/how-does-direct-debit-work/
    - /payment-methods/sepa-direct-debit/how-does-sepa-direct-debit-work/
    - /payment-methods/sepa-direct-debit/reason-codes/
    - /payments/methods/banks/sepa-direct-debit/payment-flow/
    - /payments/sepa-direct-debit/reason-codes
    - /payment-methods/sepa-direct-debit/payment-flow/
    - /payment-methods/direct-debit/activate-direct-debit/
    - /payment-methods/banks/direct-debit/activate-direct-debit/
    - /payment-methods/sepa-direct-debit/activate-sepa-direct-debit/
    - /payments/methods/banks/sepa-direct-debit/activation/
    - /payment-methods/sepa-direct-debit/activation/
    - /payment-methods/sepa-direct-debit/sepa-direct-debit-testing
    - /payments/methods/banks/sepa-direct-debit/integration-and-testing/
    - /payment-methods/sepa-direct-debit/integration-testing/
    - /payment-methods/sepa-direct-debit/chargebacks/
    - /payment-methods/sepa-direct-debit/refund-risks/
    - /payment-methods/sepa-direct-debit/reason-codes/
    - /payments/sepa-direct-debit/reason-codes
    - /payment-methods/sepa-direct-debit/reason-codes/
---

SEPA Direct Debit is a European banking payment method where customers authorize automatic one-off or recurring debits directly from their bank account. It is available in 36 countries and supports Sofort and iDEAL.

[See how SEPA Direct Debit can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/direct-debit)

## Overview

|   |   |   |
|---|---|---|
| **Countries**  | [SEPA region](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf)  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | [Yes](/chargebacks/) (see below) | 
| **Refunds** | [Full and partial](/refunds/full-partial/)  |
| **Supports** | [Recurring Payments](/payments/recurring-payments/) <br> [Second Chance](/features/second-chance/) | 

To better manage SEPA Direct Debit payments, see also [Virtual IBANs](/payments/virtual-ibans/).

### Chargebacks

Customers can request a [chargeback](/payments/chargebacks/) within 56 days, or for unauthorized transactions (i.e. without verifiable consent from the customer) within 13 months. This makes SEPA Direct Debit unsuitable for most retail businesses, e.g. clothing.

You cannot dispute chargebacks and there is no facilitated process like there is for credit card chargebacks. Chargebacks can cost up to 65 EUR in bank fees.

### Refund risk

There is a risk that if you refund a customer and they also request a chargeback, you pay their money back twice. Customers can even request a chargeback after successfully receiving a refund.

{{< details title="Reducing refund risk" >}}
To reduce the chances of this happening, we strongly recomend:

- Only processing refunds for trusted, verified customers.
- Avoiding refunding a customer if you have any ongoing dispute with them.
- If refunding:
    - First check if the customer has already requested a chargeback.
    - Wait until 7 working days after payment was initiated to be sure payment is now complete.
    - Communicate clearly to the customer that you are sending a refund and that the funds will take a few days to arrive in their account.

{{< /details >}}

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    
    C->>Me: Selects SEPA Direct Debit at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to confirm their IBAN and account name, <br> then to your success page
    Me->>Mu: [Direct flow] Sends request and customer information
    end
    Mu->>CB: Conducts background check <br> and sends e-mandate
    CB->>Mu: Processes transaction and transfers funds 
    Note over CB,Mu: -500 EUR= 9 days <br> +500 EUR= 22 days <br> Processing time can be reduced on request. <br> Email sales@multisafepay.com
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;   

{{< details title= "E-mandates" >}}
&nbsp;  
MultiSafepay creates e-mandates automatically based on the customer's IBAN and your site ID, specifying if it is a first debit or recurring debit. We send all e-mandates to our bank at the end of every business day.  

{{< /details >}}

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/account/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| MultiSafepay's customer background check was successful and we've generated an e-mandate. | Initialized  | Initialized |
| We've sent the e-mandate to the customer's bank. {{< br >}} You can no longer cancel. | Uncleared | Uncleared |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction or requested a chargeback, or their bank declined the transaction. | Void | Void |
| The customer's bank declined the transaction. {{< br >}} See the [reason codes](/payment-methods/sepa-direct-debit/#declined-transactions) below. | Declined | Declined   |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed | 

{{< /details >}}

### Declined transactions

If a SEPA Direct Debit transaction is declined, a reason code is provided.

If the IBAN or BIC is incorrect, our bank informs us the next business day.

{{< details title="Reason codes and recommended responses" >}}

| Code | Reason | Recommended response |
|---|---|---|
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

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment components](/payment-components/) {{< br >}} [Payment pages](/payment-pages/) ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/))  |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > SEPA Direct Debit direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) (direct). |

