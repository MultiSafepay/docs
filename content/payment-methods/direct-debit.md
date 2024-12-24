---
title: 'Direct debit'
category: 6298bd782d1cf4006032e765
order: 7
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'direct-debit'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/directdebit-en.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

Direct debits are a European banking method where customers authorize automatic one-off or recurring debits directly from their bank account. It is available in 36 countries and supports Sofort and iDEAL.

Read how direct debits can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/direct-debit" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | <a href="https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf" target="_blank">SEPA region</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> <br> **⚠️ Note:** To avoid declined transactions, non-EEA countries must include name and address in the `customer_object`.  | 
| [Currencies](/docs/currencies/)  | EUR | 
| [Chargebacks](/docs/chargebacks/)  | Yes (see below) |
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions)  |
| [Recurring payments](/docs/recurring-payments/) | Yes |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial  |
| [Second Chance](/docs/second-chance/) | Yes |
| [Virtual IBANs](/docs/virtual-ibans/) | Yes,  to better manage direct debits | 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/sepa-direct-debit-payment-flow.svg" alt="SEPA Direct Debit payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| MultiSafepay's customer background check was successful and we've generated an [e-mandate](#e-mandates). | Uncleared  | Initialized |
| We've sent the e-mandate to the customer's bank. You can no longer cancel. | Uncleared | Uncleared |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction or requested a chargeback, or their bank declined the transaction. | Void | Void |
| The customer's bank declined the transaction. See the [reason codes](#declined-transactions) below. | Declined | Declined   |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed | 

# Activation 

1. Email a request to <sales@multisafepay.com> 
    
    Include in the request the following information:
    - Monthly and annual direct debit volume
    - Minimum and maximum transaction amount
    - Type of products sold using this payment method
    - Whether you want to accept [recurring payments](/docs/recurring-payments/)
    - Whether any subscriptions are monthly, quarterly, or annual
    - Any additional information we request
    We send you an agreement to sign and email back to us.

   We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <risk@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Direct debit direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (direct).

### Testing
To test direct debits, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).
<br>

---

# User guide

## Chargebacks

Customers can request a [chargeback](/docs/chargebacks/) within 56 days, or for unauthorized transactions (i.e. without verifiable consent from the customer) within 13 months. This makes direct debits unsuitable for most retail businesses, e.g.&nbsp;clothing.

You cannot dispute chargebacks and there is no facilitated process like there is for credit or debit card chargebacks. Chargebacks can cost up to 65 EUR in bank fees.

## Declined transactions

If a direct debit is declined, a reason code is provided.

If the IBAN or BIC is incorrect, our bank informs us the next business day.

<details id="reason-codes-and-recommended-responses">
<summary>Reason codes and recommended responses</summary>
<br>

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
|RR02|Missing debtor name or address| Repair the collection to complete the debtor's name and/or address. Contact your bank.<br> **⚠️ Note:** To avoid declined transactions, non-EEA countries must include name and address in the `customer_object`. |
|RR03|Missing creditor name or address| Repair the collection to complete your name. Contact your bank. |
|RR04|Regulatory reason| Contact your bank. |
|SL01|Specific service offered by debtor agent| Contact the debtor. |
|TM01|File received after cut-off time| |
|CUST|Is used sporadically (known to the collector)| Contact your bank. |
|DUPL|Is used sporadically (duplicate payment)| Contact your bank. |
<br>
For more information in:

- English, see European Payments Council – <a href="https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2019-05/EPC173-14%20v5.0%20Guidance%20on%20Reason%20Codes%20for%20SDD%20R-transactions.pdf" target="_blank">Guidance on reason codes</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
- Dutch, see Betaal Vereniging – <a href="https://www.betaalvereniging.nl/wp-content/uploads/Reasoncodes-en-vervolgacties-Europese-incasso.pdf" target="_blank">Reasoncodes en vervolgacties</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>

## E-mandates

An e-mandate represents an agreement between you and the customer and is required for every direct debit. We create them automatically based on the customer's IBAN and the `site_id`, and specify if it is a one-time, initial, or recurring debit (see [Recurring payments](/docs/recurring-payments)). 

E-mandates are needed when resolving customer disputes and [chargebacks](#chargebacks).

We send all e-mandates to our bank at the end of every business day. 

## Processing times

Transactions are processed within:

- Amounts less than 500 EUR: 9 days
- Amounts over 500 EUR: 22 days

Processing times can be reduced on request. Email <sales@multisafepay.com>

## Refund risk

There is a risk that if you refund a customer and they also request a chargeback, you pay their money back twice. Customers can even request a chargeback after successfully receiving a refund.

<details id="how-to-reduce-refund-risk">
<summary>How to reduce refund risks</summary>
<br>

To reduce the chances of this happening, we strongly recomend:

- Only processing refunds for trusted, verified customers.
- Avoiding refunding a customer if you have any ongoing dispute with them.
- If refunding:
    - First check if the customer has already requested a chargeback.
    - Wait until 7 working days after payment was initiated to be sure payment is now complete.
    - Communicate clearly to the customer that you are sending a refund and that the funds will take a few days to arrive in their account.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
