---
title: Direct debit
category:
  uri: Payment methods
slug: direct-debit
position: 7
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/directdebit-en.svg" width="90" align="right" style={{margin: '20px', maxHeight: '75px'}} />

Direct debits are a European banking method where customers authorize automatic one-off or recurring debits directly from their bank account. It is available in 36 countries and supports Sofort and iDEAL.

Read how direct debits can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/direct-debit" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

<table>
  <thead>
    <tr>
      <th>Supports</th>
      <th>Details</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><p><a href="/docs/payment-methods#payment-methods-by-country">Countries</a></p></td>
      <td><p><a href="https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf" target="_blank">SEPA region</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> <br /> <strong>⚠️ Note:</strong> To avoid declined transactions, non-EEA countries must include name and address in the <code>customer\_object</code>.</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/currencies/">Currencies</a></p></td>
      <td><p>EUR</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/chargebacks/">Chargebacks</a></p></td>
      <td><p>Yes (see below)</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/payment-components/">Payment components</a></p></td>
      <td><p>Yes</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/payment-pages/">Payment pages</a></p></td>
      <td><p>Yes (current and deprecated versions)</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/recurring-payments/">Recurring payments</a></p></td>
      <td><p>Yes</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/refund-payments/">Refunds</a></p></td>
      <td><p>Yes: Full and partial</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/second-chance/">Second Chance</a></p></td>
      <td><p>Yes</p></td>
    </tr>

    <tr>
      <td><p><a href="/docs/virtual-ibans/">Virtual IBANs</a></p></td>
      <td><p>Yes,  to better manage direct debits</p></td>
    </tr>
  </tbody>
</table>

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/sepa-direct-debit-payment-flow.svg" alt="SEPA Direct Debit payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

# Payment statuses

The table below sets out the \<\<glossary:order status>> and \<\<glossary:transaction status>> for payments and refunds.

| Description                                                                                               | Order status | Transaction status |
| --------------------------------------------------------------------------------------------------------- | ------------ | ------------------ |
| MultiSafepay's customer background check was successful and we've generated an [e-mandate](#e-mandates).  | Uncleared    | Initialized        |
| We've sent the e-mandate to the customer's bank. You can no longer cancel.                                | Uncleared    | Uncleared          |
| MultiSafepay has collected payment.                                                                       | Completed    | Completed          |
| The customer cancelled the transaction or requested a chargeback, or their bank declined the transaction. | Void         | Void               |
| The transaction has been declined by your bank or by MultiSafepay.                                        | Declined     | Declined           |
| **Refunds:** Refund initiated.                                                                            | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                                                             | Completed    | Completed          |

# Activation

1. Email a request to [sales@multisafepay.com](mailto:\[sales@multisafepay.com]\(mailto:sales@multisafepay.com\))

   Include in the request the following information:

   * Monthly and annual direct debit volume
   * Minimum and maximum transaction amount
   * Type of products sold using this payment method
   * Whether you want to accept [recurring payments](/docs/recurring-payments/)
   * Whether any subscriptions are monthly, quarterly, or annual
   * Any additional information we request\
     We send you an agreement to sign and email back to us.

   We check your eligibility and if approved, activate the payment method for your account.
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
3. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

4. Select the checkbox for the payment method, and then click **Save changes**.

**⚠️ Note:** By default, Direct Debit payments are limited to one payment per IBAN every 24 hours. This restriction affects recurring payments. To request a change to this limit, email [sales@multisafepay.com](mailto:\[sales@multisafepay.com]\(mailto:sales@multisafepay.com\))

💬  **Support:** If the payment method isn't visible in your dashboard, email [risk@multisafepay.com](mailto:\[risk@multisafepay.com]\(mailto:risk@multisafepay.com\))

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Direct debit direct/redirect**.

    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align="center" />
  </details>

### Ready-made integrations

Supported in all [ready-made integrations](/docs/our-integrations/) (direct).

### Testing

To test direct debits, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).

<br />

***

# User guide

## Chargebacks

Customers can request a [chargeback](/docs/chargebacks/) up to 56 days after their account has been debited. Following this, for a period extending up to 13 months, they can only initiate a chargeback with their bank if the transaction is considered unauthorized (e.g., made without verifiable customer consent).

In contrast to credit or debit card chargebacks, **you cannot dispute** Direct debit chargebacks.

Additionally, customers can initiate a chargeback even after receiving a refund if their bank hasn't registered it. This introduces a significant risk when issuing refunds during active customer disputes.

These chargebacks can result in bank fees of **up to 65 EUR**.

### Chargeback reasons

If you receive a chargeback, a reason code is provided.

If the IBAN or BIC is incorrect, our bank informs us the next business day.

<details id="reason-codes-and-recommended-responses">
  <summary>Direct Debit reason codes</summary>

  <br />

  | Code | Reason                                        | Recommended response                                                                                                                                                                                                |
  | ---- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | AC01 | Incorrect account number                      | Contact the debtor to confirm the IBAN. If there is a mandate amendment, check the data provided by the debtor.                                                                                                     |
  | AC04 | Closed account number                         | Contact the debtor to confirm the new IBAN.                                                                                                                                                                         |
  | AC06 | Blocked account                               | Contact the debtor for another account or means of payment.                                                                                                                                                         |
  | AC13 | Debtor account type is missing or invalid     | Contact the debtor for clarification and to agree another means of payment.                                                                                                                                         |
  | AG01 | Transaction forbidden                         | Contact the debtor for another account or means of payment.                                                                                                                                                         |
  | AG02 | Invalid bank operation code                   | Resubmit the transaction with the correct authorization reference and transaction type: `OOFF` or `RCUR`.                                                                                                           |
  | AM04 | Insufficient funds                            | Contact the debtor to add funds to their account.                                                                                                                                                                   |
  | AM05 | Duplication                                   | Contact your bank to confirm whether collection was duplicated.                                                                                                                                                     |
  | BE04 | Creditor address missing or incorrect         |                                                                                                                                                                                                                     |
  | BE05 | Unrecognised initiating party                 | The creditor ID was incorrect or was changed without an amendment indicator. Check your contract for the correct creditor ID. If in doubt, contact your bank first.                                                 |
  | CNOR | Creditor bank is not registered               | Contact your bank.                                                                                                                                                                                                  |
  | DNOR | Debtor bank is not registered                 | Contact your bank. Contact the debtor for another means of payment.                                                                                                                                                 |
  | ED05 | Settlement failed                             | Depends on the SLA between the debtor's bank and the Clearing and Settlement Mechanism (CSM).                                                                                                                       |
  | FF01 | Invalid file format                           | Repair the XML file.                                                                                                                                                                                                |
  | FF05 | Direct debit type incorrect                   |                                                                                                                                                                                                                     |
  | FOCR | Return following a cancellation request       |                                                                                                                                                                                                                     |
  | MD01 | No mandate                                    | Analyse the characteristics of the SDD collection. Contact the debtor if they request a refund.                                                                                                                     |
  | MD02 | Required infomation missing from mandate      | Amend the mandate.                                                                                                                                                                                                  |
  | MD06 | Customer requested chargeback                 | Contact the debtor.                                                                                                                                                                                                 |
  | MD07 | Customer deceased                             | Close the agreement with the deceased debtor.                                                                                                                                                                       |
  | MS02 | Unspecified reason generated by customer      | Contact the debtor.                                                                                                                                                                                                 |
  | MS03 | Unspecified reason generated by agent         | Contact the debtor.                                                                                                                                                                                                 |
  | RC01 | Incorrect bank identifier                     | Contact the debtor for the correct BIC for a non-EEA collection. Ask your bank to allocate the debtor's bank's correct BIC in the interbank message.                                                                |
  | RR01 | Missing debtor account or identification      | Repair the collection to complete the debtor's account information. Contact your bank.                                                                                                                              |
  | RR02 | Missing debtor name or address                | Repair the collection to complete the debtor's name and/or address. Contact your bank.<br /> **⚠️ Note:** To avoid declined transactions, non-EEA countries must include name and address in the `customer_object`. |
  | RR03 | Missing creditor name or address              | Repair the collection to complete your name. Contact your bank.                                                                                                                                                     |
  | RR04 | Regulatory reason                             | Contact your bank.                                                                                                                                                                                                  |
  | SL01 | Specific service offered by debtor agent      | Contact the debtor.                                                                                                                                                                                                 |
  | TM01 | File received after cut-off time              |                                                                                                                                                                                                                     |
  | CUST | Is used sporadically (known to the collector) | Contact your bank.                                                                                                                                                                                                  |
  | DUPL | Is used sporadically (duplicate payment)      | Contact your bank.                                                                                                                                                                                                  |
</details>

* English, see European Payments Council – <a href="https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2019-05/EPC173-14%20v5.0%20Guidance%20on%20Reason%20Codes%20for%20SDD%20R-transactions.pdf" target="_blank">Guidance on reason codes</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
* Dutch, see Betaal Vereniging – <a href="https://www.betaalvereniging.nl/wp-content/uploads/Reasoncodes-en-vervolgacties-Europese-incasso.pdf" target="_blank">Reasoncodes en vervolgacties</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

## E-mandates

An e-mandate represents an agreement between you and the customer and is required for every direct debit. We create them automatically based on the customer's IBAN and the `site_id`, and specify if it is a one-time, initial, or recurring debit (see [Recurring payments](/docs/recurring-payments)).

E-mandates are needed when resolving customer disputes and [chargebacks](#chargebacks).

We send all e-mandates to our bank at the end of every business day.

## Processing times

Transactions are processed within:

* Amounts less than 500 EUR: 9 days
* Amounts over 500 EUR: 22 days

Processing times can be reduced on request. Email [sales@multisafepay.com](mailto:\[sales@multisafepay.com]\(mailto:sales@multisafepay.com\))

## Refund risk

You might end up paying twice the amount if a customer gets a refund from you and also files a chargeback, even if the chargeback is processed after the refund settled.

<details id="how-to-reduce-refund-risk">
  <summary>How to reduce refund risks</summary>

  <br />

  To reduce the chances of this happening, we strongly recommend:

  * Only processing refunds for trusted, verified customers.
  * Avoiding refunding a customer if you have any ongoing dispute with them.
  * If refunding:
    * First check if the customer has already requested a chargeback.
    * Wait until 7 working days after payment was initiated to be sure payment is now complete.
    * Communicate clearly to the customer that you are sending a refund and that the funds will take a few days to arrive in their account.
</details>

<br />

***

<blockquote>
  <h3>
    <span>💬</span>
    Support
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
