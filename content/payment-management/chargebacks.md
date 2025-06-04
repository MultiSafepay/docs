---
title: 'Chargebacks'
category: 6278c92bf4ad4a00361431b0
order: 0
hidden: false
slug: 'chargebacks'
---

A chargeback is a dispute process that occurs when a cardholder disagrees with or doesn't recognize a transaction charged to their credit or debit card and requests the <<glossary:issuer>> to reverse it. The <<glossary:card scheme>> notifies MultiSafepay and reclaims your transaction amount.

When a customer requests a chargeback, an alert appears on your dashboard homepage.

To see your chargebacks:

1. Go to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions **and click **Chargebacks**.
3. Here, you will find all new, pending or disputed chargebacks. To learn more about the different statuses, see <a href="https://docs.multisafepay.com/docs/chargebacks#chargeback-statuses" target="_blank">Chargeback statuses</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Credit and debit card chargebacks

### Visa & Mastercard

To dispute a chargeback on a credit or debit card for Visa or Mastercard, see the process flow below. Click to magnify.

#### Initial stage

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Chargeback-1.png" align ="center"/>

<br />

***

<br />

#### Dispute stage

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Chargeback-2.png" align ="center"/>

<br />

***

<br />

#### Final stage

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Chargeback-3.png" align ="center"/>

<br />

***

### American Express

When an American Express cardholder disputes a transaction, the chargeback process is initiated and handled directly by American Express, without an issuing bank acting as an intermediary in the initial and subsequent phases. The steps are generally similar to those of Visa and Mastercard, with MultiSafepay still involved as the payment processor.

***

## How to accept chargebacks

If you want to accept liability for a chargeback, you can do so from your dashboard. To accept a chargeback:

1. Go to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Click **Transactions** and go to **Chargebacks**. Select the relevant chargeback.
3. In the **Transaction summary**, under **Chargeback dispute**, click **Accept chargeback**.
4. A message will appear asking for confirmation. Click **Ok**.

After a chargeback has been accepted, the amount for the order will be refunded to the customer. Do not process a refund after a chargeback has been accepted.

***

## How to dispute chargebacks

MultiSafepay can dispute chargebacks on your behalf.

Consumer protection is the main purpose of chargebacks and card scheme rules. Upload the relevant documentary evidence, and make sure it's valid, up-to-date, and clearly presented. 

- An invoice of the order, with details of the product and customer, and with the location of delivery.
- A **Track & trace** document.
- A signed proof of delivery.
- Evidence of contact with the cardholder (emails, conversations, etc.).
- In the event a cardholder cancels an order, a cancellation or return policy.

**⚠️Note:** All documentation provided **must** be in English.

You can upload your documents:

<details id="msp-dashboard">
  <summary>Via your dashboard</summary>
  <br>

1. Go to your MultiSafepay <a href="https://merchant.multisafepay.com/" target="_blank">dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Click **Transactions** and go to **Chargebacks**. Select the relevant chargeback.
3. In the **Transaction summary**, under **Chargeback dispute**, click **Open dispute**.
4. Click **Choose Files** and upload the corresponding documentation in PDF format.
5. Click **Upload**. Repeat this for every document you want to submit. Optionally, add a comment.
6. Once everything has been uploaded, click **Submit dispute**. 

We will contact you via email if any documents are pending or invalid.

If the documentation has been validated, the chargeback status will change to **Processed**.

</details>

<details id="msp-dashboard">
  <summary>Via API</summary>
  <br>

Send a [Challenge chargebacks](/reference/challengechargeback/) request. Include the following information:

- The `order_id` of the original transaction.
- A  `base64` encoded file that includes the documentary evidence.
- The file type must be set to `PDF`.
- A description of the file and a name.

</details>

The Chargeback Team then assesses the evidence provided and decides whether the chargeback can be disputed.

- For questions about disputes, email [retrieval@multisafepay.com](mailto:retrieval@multisafepay.com)
- For more information about fees, email [support@multisafepay.com](mailto:support@multisafepay.com)

**⚠️Note:** All chargebacks require a response before the **due date** specified on the **Transaction summary** page. If no action is taken by then, the chargeback will be automatically accepted, and the consumer will be refunded.

***

## Dispute statuses

Check the table below to know the meaning of each status:

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "New",
    "0-1": "You have received a new chargeback. You can either accept or dispute it.",
    "1-0": "Opened",
    "1-1": "You have opened the chargeback but haven't accepted or disputed it.",
    "2-0": "Accepted",
    "2-1": "You have accepted the chargeback. The consumer receives a refund.",
    "3-0": "Submitted",
    "3-1": "You have disputed a chargeback and submitted the required supporting documentation. We will review it.  \n**⚠️Note:** Remember to upload the evidence before the **due date**.",
    "4-0": "Ready",
    "4-1": "We have requested additional information, which can be submitted through your dashboard. The due date will also be modified.",
    "5-0": "Processed",
    "5-1": "Your documentation has been validated and forwarded to the scheme."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    "left",
    "left"
  ]
}
[/block]


***

## Reasons and required evidence

When a cardholder requests a chargeback, they must provide a reason. 

The most common reasons for requesting chargebacks are:

- Processing or authorization errors by the merchant
- Customer disputes, e.g.: 
  - The order didn't arrive.
  - The items were defective, damaged, or not as described in the specification.
  - The service was not delivered as expected. 
  - The customer didn't receive the expected credit. 
- Fraud, which may be genuine or "friendly fraud," e.g., if the customer:
  - Doesn't recognize your company name or a specific transaction.
  - Requests a chargeback instead of following your refund or returns process.
  - Regrets the purchase.
  - Forgets to cancel a subscription.

If you have requested MultiSafepay to dispute a chargeback for you, we specify what documentary evidence you need to provide for each chargeback reason. Try to provide as much supporting documentation as possible. 

***

Below are the chargeback reason codes for the major card schemes.

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/visa.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

### Visa

#### Fraud

<details id="reason-code-10-4-card-absent-environment">
<summary>Reason code 10.4: Card absent environment</summary>
<br>

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide the following:

- Evidence the cardholder is in possession of and/or using the product/service, e.g. proof of delivery.
- Evidence that the transaction was completed by a member of the cardholder's household or family.
- Evidence of previous interactions with the cardholder, e.g., other purchases, payment details.
- A transaction receipt.
- An invoice number.
- A track and trace number.
- Photos or emails proving a link between the person who received the product/service and the cardholder.

</details>

#### Processing error

<details id="reason-code-12-2-incorrect-transaction-code">
<summary>Reason code 12.2: Incorrect transaction code</summary>
<br>

The wrong transaction code was used. For example, you meant to send a credit to a customer, but accidentally debited their account instead.

To dispute this type of chargeback, you need to provide the following:

- Invoice with the product description
- Any relevant explanation of transaction type and why it was processed that way.
- Proof the correct transaction was completed (e.g., reversal, corrected transaction).
- If applicable, a screenshot of POS system or logs showing the method selected.
- Communication with the cardholder

</details>

<details id="reason-code-12-5-incorrect-amount">
<summary>Reason code 12.5: Incorrect amount</summary>
<br>

The transaction amount is incorrect, or an error occurred. 

To dispute this type of chargeback, you need to provide the following:

- A transaction receipt.
- An invoice number.
- Evidence that the transaction amount is correct.

</details>

<details id="reason-code-12-6-duplicate-processing-or-paid-by-other-means">
<summary>Reason code 12.6: Duplicate processing or paid by other means</summary>
<br>

The cardholder or authorized person did not receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide proof that:

- Both transactions are independent and separate. 
- The transaction was not paid by other means or separate means.

</details>

#### Customer dispute

<details id="reason-code-13-1-merchandise-or-services-not-received">
<summary>Reason code 13.1: Merchandise or services not received</summary>
<br>

The cardholder or authorized person did not receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide the following:

- A description of the product/service.
- Evidence that the cardholder is in possession of and/or using the product/service, e.g. proof of delivery. 
- Proof of delivery, e.g., cardholder signature.
- An invoice number.
- A track and trace number. 
- Evidence of communications with the cardholder.

</details>

<details id="reason-code-13-2-cancelled-recurring-transaction">
<summary>Reason code 13.2: Cancelled recurring transaction</summary>
<br>

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed.

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account. 
- The product/service was used after the cancellation, e.g., ID and/or login history. 
- The transaction was properly authorized and settled as a recurring transaction.
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions or that they signed a contract agreeing to the terms and conditions

</details>

<details id="reason-code-13-3-not-as-described">
<summary>Reason code 13.3: Not as described</summary>
<br>

The product/service:

- Did not match your description on the transaction receipt or elsewhere when purchased, or 
- Was damaged or defective.

To dispute this type of chargeback, you need to provide the following:

- Proof of delivery of the product/service.
- Your original description of the product/service. 
- An invoice number.
- A track and trace number. 
- Evidence of communications with the cardholder. 
- Evidence that the cardholder did not attempt to return the product/service.

</details>

<details id="reason-code-10-4-card-absent-environment">
<summary>Reason code 13.4: Counterfeit merchandise</summary>
<br>

The merchandise was identified as counterfeit by one or more of the following:

- The owner of the intellectual property or its authorized representative.
- A customs agency, law enforcement agency, or other government agency .
- A third-party expert.

To dispute this type of chargeback, you need to provide the following:

- Proof of authenticity for example: Invoice, and Invoice from authorized suppliers
- Proof of refund
- Communication with the cardholder
- Terms and Conditions, by Click to Accept.
- Proof of delivery of the product/service.
- Shipping and tracking details, and proof of delivery.

</details>

<details id="reason-code-13-5-misrepresentation">
<summary>Reason code 13.5: Misrepresentation</summary>
<br>

The cardholder claims a purchased item or service was misrepresented and alleges false advertising.

</details>

<details id="reason-code-13-6-credit-not-processed">
<summary>Reason code 13.6: Credit not processed</summary>
<br>

The cardholder did not receive the funds for credit or voided transaction receipt. 

To dispute this type of chargeback, you need to provide the following:

- Details about the transaction.
- An invoice number. 
- Evidence of communications with the cardholder.

</details>

<details id="reason-code-13-7-cancelled-service-and-or-merchandise">
<summary>Reason code 13.7: Cancelled service and/or merchandise</summary>
<br>

The cardholder cancelled or returned the product/service. Or, you did not properly disclose or did disclose but did not apply a limited return or cancellation policy at the time of the transaction.

To dispute this type of chargeback, you need to provide the following:

- Evidence of the cardholder using the service. 
- Evidence of delivery of products/services that the cardholder did not return.
- Evidence that the cardholder had to click to accept your cancellation policy and that your policy does not include the right to dispute terms and conditions available on your website. 
- An invoice number.
- A track and trace number.
- Evidence of communications with the cardholder

</details>

***

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/mastercard.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

### Mastercard

#### Authorization

<details id="reason-code-4808-authorization-related">
<summary>Reason code 4808: Authorization-related chargeback</summary>
<br>

The transaction was processed without valid authorization.

To dispute this type of chargeback, you need to provide the following:

- Proof of the service was used
- Proof of delivery merchandise
- Tracking and invoice
- Proof of contact with the cardholder

</details>

#### Fraud

<details id="reason-code-4837-fraud-related-chargeback-or-no-cardholder-authorization">
<summary>Reason code 4837: Fraud related chargeback or no cardholder authorization</summary>
<br>

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide the following:

- Evidence that:
  - The cardholder is in possession of and/or using the product/service, e.g. proof of delivery. 
  - The transaction was completed by a member of the cardholder's household or family. 
- Evidence of previous interactions with the cardholder, e.g., other purchases, payment details. 
- A transaction receipt.
- An invoice number. 
- A track and trace number. 
- Photos or emails proving a link between the person who received the product/service and the cardholder

</details>

<details id="reason-code-4863-potential-fraud-cardholder-does-not-recognize-the-transaction">
<summary>Reason code 4863: Potential fraud, the cardholder does not recognize the transaction</summary>
<br>

The cardholder denies participating in or does not recognize the transaction you processed.

To dispute this type of chargeback, you need to provide the following:

- Evidence that:
  - The cardholder is in possession of and/or using the product/service, e.g. proof of delivery. 
  - The transaction was completed by a member of the cardholder's household or family. 
  - The cardholder is using the product/service. 
- A copy of the cardholder's identification. 
- Evidence of previous interactions with the cardholder, e.g., other purchases, payment details 
- A transaction receipt.
- An invoice number.
- A track and trace number.
- Photos or emails proving a link between the person who received the product/service and the cardholder.

</details>

#### Processing error

<details id="reason-code-4831-dispute-amount-or-an-incorrect-amount">
<summary>Reason code 4831: Dispute amount or an incorrect amount</summary>
<br>

The cardholder claims that you processed an incorrect amount. 

To dispute this type of chargeback, you need to provide the following: 

- A transaction receipt.
- An invoice number.
- Evidence that:
  - The transaction amount was correct. 
  - you have the right to alter the transaction amount without the cardholder's consent after the transaction is completed.

</details>

<details id="reason-code-4834-duplicate-processing">
<summary>Reason code 4834: Duplicate processing</summary>
<br>

The issuer determines that you submitted duplicate transactions.

To dispute this type of chargeback, you need to provide proof that both transactions:

- Are separate
- Are valid
- Were authorized by the cardholder's personal identification number (PIN) 

</details>

#### Customer dispute

<details id="reason-code-4841-digital-goods-cancelled-recurring-transaction">
<summary>Reason code 4841: Digital goods, cancelled recurring transaction</summary>
<br>

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed.

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account. 
- The cardholder used the product/service after the cancellation, e.g., ID and/or login history. 
- The transaction was properly authorized and settled as a recurring transaction.
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions or that they signed a contract agreeing to the terms and conditions.

</details>

<details id="reason-code-4853-cardholder-dispute-goods-or-service-not-delivered-goods-not-as-described">
<summary>Reason code 4853: Cardholder dispute: Goods or service not delivered, Goods not as described</summary>
<br>

- The product/service did not match your description on the transaction receipt or other record at the time of purchase, or
- The transaction was not completed, or
- The product/service the cardholder received was damaged or defective, or
- The cardholder disputes the quality of the product/service received.

To dispute this type of chargeback, you need to provide the following:

- Proof of delivery of the product/service.
- A description of the product/service. 
- An invoice 
- A track and trace number.
- Evidence of communications with the cardholder. 
- Evidence that the cardholder did not attempt to return the product/service.

</details>

***

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/amex.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

### American Express

#### Fraud

<details id="reason-code-4526-missing-signature">
<summary>Reason code 4526: Missing signature</summary>
<br>

The cardholder claims the transaction is fraudulent, and their signature is not on the relevant documents.

To dispute this type of chargeback, you need to provide proof that:

- The receipt is signed, or 
- The cardholder was present at the time of the transaction, or 
- The transaction was verified by [3D Secure](/docs/3ds2/).

</details>

<details id="reason-code-4540-card-not-present">
<summary>Reason code 4540: Card not present</summary>
<br>

The cardholder denies participating in a [MOTO](/docs/moto/) transaction you processed. American Express investigates and confirms that the transaction is fraudulent.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder did participate in the transaction.
- The product/service was delivered to the cardholder's billing address, and the cardholder signed a receipt. 

</details>

<details id="reason-code-4573-fraud-full-recourse">
<summary>Reason code 4573: Fraud, full recourse</summary>
<br>

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**.

To dispute this type of chargeback, you need to provide proof that the transaction is exempt or was authorized by a PIN or [3D Secure](/docs/3ds2/).

</details>

<details id="reason-code-6006-fraud-unrecognized-transaction">
<summary>Reason Code 6006: Fraud, unrecognized transaction</summary>
<br>

The cardholder informs American Express that they believe the transaction is fraudulent.

To dispute this type of chargeback, you need to provide the following:

- Proof that the cardholder agreed to the transaction, made the booking/reservation, and received confirmation. 
- Your website name, URL, IP address, and cancellation policy. 
- Signed proof that the product/service was shipped and delivered, and the delivery address and date.

</details>

#### Processing error

<details id="reason-code-4512-multiple-processing">
<summary>Reason code 4512: Multiple processing</summary>
<br>

You sent multiple transactions for the same amount.

To dispute this type of chargeback, you need to provide the following:

- Proof that you have already processed a corrective card transaction.
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid.

</details>

<details id="reason-code-4513-credit-not-presented">
<summary>Reason code 4513: Credit not presented</summary>
<br>

The cardholder received written acknowledgment from you for a credit, or they cancelled in accordance with your policy but have not yet received the refund.

To dispute this type of chargeback, you need to provide the following:

- Proof that you have already processed a corrective card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid
- Screenshots of your cancellation policy 
- Evidence that:
  - The cardholder clicks to accept the terms and conditions.
  - your cancellation policy does not include the right to dispute the policy. 

</details>

<details id="reason-code-4515-paid-through-other-means">
<summary>Reason code 4515: Paid through other means</summary>
<br>

The cardholder informed American Express that the transaction was:

- Altered after they signed for it, or
- Submitted using an incorrect card number or amount.

To dispute this chargeback, you need to prove that the cardholder's payment was unrelated to the disputed transaction.

</details>

<details id="reason-code-4516-request-for-support-not-fulfilled-and-or-no-reply-to-inquiry-letter">
<summary>Reason code 4516: Request for support not fulfilled and/or no reply to inquiry letter</summary>
<br>

American Express asked you to provide documents to support a charge queried by a cardholder, but you have yet to respond.

To dispute this chargeback, you must provide proof that you have already processed a corrective card transaction.

</details>

<details id="reason-code-4517-insufficient-or-unclear-reply-to-dispute-inquiry-letter">
<summary>Reason code 4517: Insufficient or unclear reply to dispute inquiry letter</summary>
<br>

Fully itemized documents are not clear or complete and do not adequately link the cardholder to the transaction.

To dispute this type of chargeback, you need to provide the following:

- The date and amount of credit and the reason.
- An itemized invoice and/or receipt that directly links the cardholder to the charge. 
- A successfully completed fax transmission report.
- Proof that the documents were sent and received by American Express within the time limit on the dispute inquiry letter.

</details>

<details id="reason-code-4534-multiple-rocs">
<summary>Reason code 4534: Multiple ROCs</summary>
<br>

The cardholder denies participating in the transaction despite your previous successful transactions.

To dispute this chargeback, you must provide fully itemized documents linking the cardholder to each charge processed and proving that all transactions are valid.

</details>

#### Customer dispute

<details id="reason-code-4544-goods-and-services-cancellation-of-recurring-payments">
<summary>Reason code 4544: Goods and services, cancellation of recurring payments</summary>
<br>

You have continued to charge the cardholder's account after they requested cancellation of [Recurring payments](/docs/recurring-payments/).

To dispute this type of chargeback, you need to provide the following:

- A signed letter refuting the cardholder's claim and/or proof that their evidence is incorrect. 
- A copy of your cancellation policy and a statement indicating why the cancellation does not comply with your policy.

</details>

<details id="reason-code-4553-goods-and-services-not-as-described">
<summary>Reason code 4553: Goods and services, not as described</summary>
<br>

The cardholder received a product/service that differs from the written description you provided or is damaged. 

To dispute this type of chargeback, you need to provide the following:

- Proof that the product/service is as originally described.
- A copy of your returns and refunds policies.
- If available, authentication or a written assessment of the product/service.

</details>

<details id="reason-code-4554-goods-and-service-not-received">
<summary>Reason code 4554: Goods and services, not received</summary>
<br>

The cardholder did not receive the product/service or only in part.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder or authorized person did receive the product/service, e.g., proof of delivery. 
- The product/service was delivered to the cardholder's billing address. 
- The cardholder neither cancelled nor returned the product/service.

</details>

<details id="reason-code-4798-american-express-fraud-dispute">
<summary>Reason code 4798: American Express fraud dispute</summary>
<br>

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**

To dispute this type of chargeback, you need to provide proof that the transaction is exempt or was authorized by a PIN or [3D Secure](/docs/3ds2/).

</details>

***

## Chargeback period

Card schemes generally allow cardholders to request chargebacks for up to 120 days after the transaction. Upon receiving a chargeback request, the response window to submit the necessary documentation for the dispute is 23 days for Visa and Mastercard and 20 days for American Express.

By offering card payment methods, you agree to the cardholder rights guaranteed by the card schemes.

***

# Minimizing chargebacks

Card schemes may fine merchants with high chargeback rates. The most effective way to minimize chargebacks is to provide excellent customer service.

Check the key strategies to reduce the most common types of chargebacks:

### Prevent fraud

- Use [3DS2](/docs/3ds2/) for all credit or debit card transactions. Cardholders cannot request chargebacks due to fraud on transaction protected by 3D Secure.  

- Carefully review all [uncleared card payments](/docs/uncleared) flagged by MultiSafepay's fraud filter.

### Deliver goods on time

- Keep customers informed about both expected and actual delivery times.
- Document the delivery process, e.g., use track and trace numbers with customer signatures.
- Refund or cancel transactions if the goods won't arrive within the promised delivery time or at all. 

### Avoid miscommunication

- Offer high-quality items and provide clear, accurate descriptions on your website. 
- Make sure your refund and return policies are transparent, clear, and fair.

### Improve transaction clarity

Include your logo in customers' online bank environments and applications to:

- Enhance brand visibility, recognition, and trust.
- Reduce chargebacks, disputes, and friendly fraud – when customers mistakenly initiate chargebacks because they do not recognize or trust a transaction.

<a href="https://logo.ethoca.com/" target="_blank">Upload your logo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the card scheme to display in all participating banking environments and applications. 

Additionally:

- Always follow the card scheme's payment acceptance guidelines carefully.
- Ensure your <<glossary:backend>> processes payments reliably, with no bugs.
- Make sure your refund and return policies are consistent, clear, and fair.

***

# Other payment methods

## Amazon Pay

If an Amazon customer requests a chargeback from their bank or card issuer for an Amazon Pay payment, Amazon Pay notifies you by email. If you do not respond within 11 calendar days, then Amazon Pay automatically debits the chargeback amount from your Amazon Payments merchant account.

For more information, see Amazon Pay - <a href="https://pay.amazon.eu/help/201749650" target="_blank">Handling chargebacks</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Direct debit

For more information about Direct debit chargebacks, see Chargebacks - <a href="https://docs.multisafepay.com/docs/sepa-direct-debit#chargebacks" target="_blank">SEPA Direct Debit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)