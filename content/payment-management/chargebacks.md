---
title: 'Chargebacks'
category: 6278c92bf4ad4a00361431b0
order: 0
hidden: false
slug: 'chargebacks'
---

Chargeback is a process of dispute that occurs when a cardholder disagrees with or doesn't recognize a transaction charged to their credit or debit card and requests the <<glossary:issuer>> to reverse it. The <<glossary:card scheme>> notifies MultiSafepay and reclaims your transaction amount.

When a customer requests a chargeback, an alert to review it appears on your dashboard homepage.

If you receive a chargeback, you can find it if you: 

1. Go to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions **and click **Chargebacks**.
3. Here, you will find any new, pending or disputed chargebacks. To know more about the different statuses, see <a href="https://docs.multisafepay.com/docs/chargebacks-test#chargeback-statuses" target="_blank">Chargeback statuses</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Credit or debit card chargebacks

To dispute a chargeback on a credit or debit card, see the process flow below. Click to magnify.

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

<br />

## Accept a chargeback

If you want to accept liability for a chargeback, you can do it from your dashboard. To accept a chargeback:

1. Go to your MultiSafepay <a href="https://merchant.multisafepay.com/" target="_blank">dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Click **Transactions** and go to **Chargebacks**. Select the relevant chargeback.
3. In the **Transaction summary**, under **Chargeback dispute**, click **Accept chargeback**.
4. A message will appear asking for confirmation. Click **Ok**.

The amount for the order will be refunded to the customer.

## Disputing chargebacks

MultiSafepay can dispute chargebacks on your behalf. You must upload the relevant documentary evidence:

- An invoice of the order, with details of the product and customer, and with the location of delivery.
- A **Track & trace** document.
- A signed proof of delivery.
- Evidence of contact with the cardholder (emails, conversations, etc).
- In case of cancellation of the order by the cardholder, a cancellation or return policy.

You can upload your documents:

<details id="msp-dashboard">
  <summary>Via your dashboard</summary>
  <br>

1. Go to your MultiSafepay <a href="https://merchant.multisafepay.com/" target="_blank">dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Click **Transactions** and go to **Chargebacks**. Select the relevant chargeback.
3. In the **Transaction summary**, under **Chargeback dispute**, click **Open dispute**.
4. Click **Choose Files** and upload the corresponded documentation in PDF format.
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
- Type must be set to `PDF`.
- A description of the file and a name.

</details>

The Chargeback Team then assesses the evidence provided and decides whether the chargeback can be disputed.

- For questions about disputes, email [retrieval@multisafepay.com](mailto:retrieval@multisafepay.com)
- For more information about fees, email [support@multisafepay.com](mailto:support@multisafepay.com)

**⚠️Note:** You must respond to any chargeback before the specified due date, which can be found on the **Transaction summary** page. If no action is taken by the due date, the chargeback will be automatically accepted, and a refund will be issued to the consumer.

## Chargeback reasons and required evidence

When a cardholder requests a chargeback, they must provide a reason. 

The most common reasons for requesting chargebacks are:

- Processing or authorization errors by the merchant
- Customer disputes, e.g.: 
  - The order didn't arrive.
  - The items were defective, damaged, or not as described in the specification.
  - Service wasn't performed as expected. 
  - The customer didn't receive the expected credit. 
- Fraud, which may be genuine or "friendly fraud," e.g., if the customer:
  - Doesn't recognize your company name or a specific transaction.
  - Requests a chargeback instead of following your refund or returns process.
  - Regrets the purchase.
  - Forgets to cancel a subscription.

If you have asked MultiSafepay to dispute a chargeback for you, we specify what documentary evidence you need to provide for each chargeback reason. Try to provide as much evidence as possible. 

***

Below are the chargeback reason codes for the major card schemes.

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/amex.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

### American Express

#### Fraud

<details id="reason-code-4573-fraud-full-recourse">
<summary>Reason code 4573: Fraud, full recourse</summary>
<br>

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**.

To dispute this type of chargeback, you need to provide proof that the transaction is exempt or was authorized by a PIN or [3D Secure](/docs/3ds2/).

</details>

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

The cardholder received written acknowledgment from you for credit, or they cancelled in line with your policy but have yet to receive the credit in their account.

To dispute this type of chargeback, you need to provide the following:

- Proof that you have already processed a corrective card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid
- Screenshots of your cancellation policy 
- Evidence that:
  - The cardholder clicks to accept the terms and conditions.
  - your cancellation policy doesn't include the right to dispute the policy. 

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

Fully itemized documents aren't clear or complete and directly link the cardholder to the transaction.

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

You have continued to charge the cardholder's account after they notified you to cancel or revoke consent for [Recurring payments](/docs/recurring-payments/).

To dispute this type of chargeback, you need to provide the following:

- A signed letter refuting the cardholder's claim and/or proof that their evidence is incorrect. 
- A copy of your cancellation policy and a statement indicating why the cancellation doesn't comply with your policy.

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

The cardholder didn't receive the product/service or only in part.

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

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/mastercard.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

### Mastercard

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

The cardholder denies participating in or doesn't recognize the transaction you processed.

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

<details id="reason-code-4834-duplicate-processing">
<summary>Reason code 4834: Duplicate processing</summary>
<br>

The issuer determines that you submitted duplicate transactions.

To dispute this type of chargeback, you need to provide proof that both transactions:

- Are separate
- Are valid
- Were authorized by the cardholder's personal identification number (PIN) 

</details>

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

#### Customer dispute

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
- Evidence that the cardholder didn't attempt to return the product/service.

</details>

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

***

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/visa.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

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

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide proof that:

- Both transactions are independent and separate. 
- The transaction was not paid by other means or separate means.

</details>

#### Customer dispute

<details id="reason-code-13-1-merchandise-or-services-not-received">
<summary>Reason code 13.1: Merchandise or services not received</summary>
<br>

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

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

<details id="reason-code-13-6-credit-not-processed">
<summary>Reason code 13.6: Credit not processed</summary>
<br>

The cardholder didn't receive the funds for credit or voided transaction receipt. 

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
- Evidence of delivery of products/services that the cardholder didn't return.
- Evidence that the cardholder had to click to accept your cancellation policy and that your policy doesn't include the right to dispute terms and conditions available on your website. 
- An invoice number.
- A track and trace number.
- Evidence of communications with the cardholder

</details>

***

## Chargeback period

Card schemes generally allow cardholders to request chargebacks for up to 180 days after the transaction. However, if you require a longer period (e.g., for annual subscriptions paid in advance), you may be able to negotiate this with the card scheme.

By offering card payment methods, you agree to the cardholder rights guaranteed by the card schemes.

***

# Chargeback statuses

Check the table below to know the meaning of each status:

| Status    | Description                                                                                                                                                       |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New       | You have received a new chargeback. You can either accept or dispute it.                                                                                          |
| Opened    | You have opened the chargeback but haven't accepted or disputed it.                                                                                               |
| Accepted  | You have accepted the chargeback. The consumer receives a refund.                                                                                                 |
| Submitted | You have disputed chargeback and submitted the required supporting documentation. We will review it.                                                              |
| Ready     | Action is required from your side. Additional information or clarification is requested. Check the chargeback for more information. The due date will be modified |
| Processed | Your documentation has been validated and forwarded to the scheme.                                                                                                |

***

# Minimizing chargebacks

Card schemes may fine merchants that have high rates of chargebacks.

The best way of minimizing chargebacks is to provide good customer service.

Ways to minimize the most common types of chargeback include: 

<details id="fraud">
<summary>Fraud</summary>
<br>

Use [3DS2](/docs/3ds2/) for all credit or debit card transactions. 

Cardholders are not allowed to request chargebacks due to fraud for 3D Secure-protected transactions.  

Carefully review all [uncleared card payments](/docs/uncleared) flagged by MultiSafepay's fraud filter.

</details>

<details it="non-delivery">
<summary>Non-delivery</summary>
<br>

- Inform customers of both expected and actual delivery times.
- Document the delivery process, e.g., use track and trace number with signature.
- Refund or cancel transactions if the goods won't arrive within the stated delivery time or not at all. 
  </details>

<details id="goods-not-as-described">
<summary>Goods not as described</summary>
<br>  

Offer quality items and provide clear descriptions on your website. 

Make sure your refund and return policies are clear and fair. 

</details>

<details id="transaction-not-recognized">
<summary>Transaction not recognized</summary>
<br>

Including your logo in customer's online bank environments and applications can help:

- Increase brand presence, recognition, and trust.
- Reduce chargebacks, disputes, and friendly fraud – when customers mistakenly initiate chargebacks because they don't recognize or trust a transaction.

<a href="https://logo.ethoca.com/" target="_blank">Upload your logo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the card scheme to display in all participating banking environments and applications. 

Additional guidance:

- Always follow the card scheme's payment acceptance guidelines carefully.
- Ensure there are no bugs in processing card payments in your <<glossary:backend>>.
- Make sure your refund and return policies are clear and fair.

</details>

***

# Other payment methods

## Amazon Pay chargebacks

If an Amazon customer requests a chargeback from their bank or card issuer for an Amazon Pay payment, Amazon Pay notifies you by email. If you do not respond within 11 calendar days, then Amazon Pay automatically debits the chargeback amount from your Amazon Payments merchant account.

For more information, see Amazon Pay - <a href="https://pay.amazon.eu/help/201749650" target="_blank">Handling chargebacks</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Direct debit chargebacks

Customers can request a chargeback within 56 days or for unauthorized transactions (i.e., without verifiable consent from the customer) within 13 months. Chargebacks can cost up to 65 EUR in bank fees.

You cannot dispute chargebacks, and there is no facilitated process like there is for credit or debit card chargebacks. 

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)
