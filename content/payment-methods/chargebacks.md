---
title: 'Chargebacks'
category: 6298bd782d1cf4006032e765
order: 29
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: 'chargebacks'
---

Chargebacks arise when a cardholder disagrees with or doesn't recognize a transaction charged to their credit card, and requests the <<glossary:issuer>> to reverse it. The <<glossary:card scheme>> notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying chargebacks.

When a customer requests a chargeback, an alert to review it appears on your dashboard homepage. 

# Disputing chargebacks

The table below sets out the process for disputing chargebacks.

| Step  | Who  | Action  |   
|---|---|---|
| 1. | Cardholder  | To find out more about a transaction, the cardholder can file a free retrieval request for more information. This can help identify and clarify transactions and avoid chargebacks. <br> You can still refund the transaction at this stage.  |   
| 2.  | Cardholder  | If the cardholder still disagrees with the transaction, they request a chargeback.  | 
| 3.  | Issuer  | The issuer usually refunds the cardholder as soon as they request the chargeback. <br> We don't support refunding chargeback transactions from this point, because then the cardholder likely receives the refund twice. |
| 4.  | Merchant  | MultiSafepay can dispute the chargeback on your behalf. <br> You must provide evidence that the chargeback is unjustified. <br> A separate transaction for the chargeback, connected to the original transaction, is created under your MultiSafepay account.  | 
| 5.  | Cardholder  | If the cardholder disagrees with the outcome of the dispute, the chargeback process continues.  | 
| 6.  | Merchant  | You can dispute again, but the potential costs involved are significant. <br> The card scheme may charge fees. <br> You need to present strong **new** evidence not provided already.  | 
| 7.  | Card scheme | The card scheme makes the final decision about the chargeback.  | 
| 8.  | Card scheme  | If the chargeback is unsuccessful, the card scheme reclaims the amount from MultiSafepay directly.  |  
| 9.  | MultiSafepay  | We debit the amount from your account balance.  |  

### MultiSafepay disputing chargebacks on your behalf

MultiSafepay can dispute chargebacks on your behalf. 

You need to upload relevant documentary evidence:

- In the **Transaction details** page of the original transaction in your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, **or**
- Via our API - see [Challenge chargebacks](/reference/challengechargeback/), **or**


<details id=“how-to-upload-files”>
<summary>How to upload files</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Settings** > **Files**.
3. Under **Upload a new file**, click **Choose file**.<br> **Note:** You must upload files in PDF format.
4. Select the relevant file(s), and then click **Open**.
5. Under **Upload queue**, to upload:
    - A specific file, click **Upload**.
    - A batch of files, click **Upload all**.

</details>

The Chargeback Team then assesses the evidence provided and decides whether the chargeback can be disputed.

- For questions about disputes, email <retrieval@multisafepay.com>
- For more information about fees, email <support@multisafepay.com>

# Chargeback reasons

The most common reasons for requesting chargebacks are:

- Processing or authorization errors by the merchant
- Customer disputes, e.g.: 
    - The order didn't arrive.
    - The items were defective, damaged, or not as described in the specification.
    - A service wasn't performed as expected. 
    - The customer didn't receive an expected credit. 
- Fraud, which may be genuine or "friendly fraud", e.g. if the customer:
    - Doesn't recognize your company name or a specific transaction
    - Requests a chargeback instead of following your refund or returns process
    - Regrets the purchase
    - Forgets to cancel a subscription 

# Chargeback period

Card schemes generally allow cardholders to request chargebacks for up to 180 days after the transaction. If you require a longer period (e.g. for annual subscriptions paid in advance), you may be able to negotiate this with the card scheme.

By offering credit card payment methods, you agree to the cardholder rights guaranteed by the card schemes.

# Amazon Pay chargebacks

If an Amazon customer requests a chargeback from their bank or credit card issuer for an Amazon Pay payment, Amazon Pay notifies you by email. If you do not respond within 11 calendar days, then Amazon Pay automatically debits the chargeback amount from your Amazon Payments merchant account.

For more information, see Amazon Pay - <a href="https://pay.amazon.eu/help/201749650" target="_blank">Handling chargebacks</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Direct debit chargebacks

Customers can request a chargeback within 56 days, or for unauthorized transactions (i.e. without verifiable consent from the customer) within 13 months. Chargebacks can cost up to 65 EUR in bank fees.

You cannot dispute chargebacks and there is no facilitated process like there is for credit card chargebacks. 

# Chargeback reasons and required evidence

When a cardholder requests a chargeback, they must provide a reason. Below are the chargeback reason codes for the major card schemes. 

If you have asked MultiSafepay to dispute a chargeback on your behalf, we specify what documentary evidence you need to provide for each chargeback reason. Try to provide as much evidence as possible. 

---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/amex.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

### American Express 

#### Fraud
<details id="reason-code-4573-fraud-full-recourse">
<summary>Reason code 4573: Fraud, full recourse</summary>
<br>

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**.

To dispute this type of chargeback, you need to provide proof that the transaction is exempt, or was authorized by a PIN, or [3D Secure](/docs/3ds2/).

</details>

<details id="reason-code-4526-missing-signature">
<summary>Reason code 4526: Missing signature</summary>
<br>

The cardholder claims that the transaction is fraudulent and their signature is not on the relevant documents.

To dispute this type of chargeback, you need to provide proof that:

- The receipt is signed, or 
- The cardholder was present at the time of the transaction, or 
- The transaction was verified by [3D Secure](/docs/3ds2/)

</details>

<details id="reason-code-4540-card-not-present">
<summary>Reason code 4540: Card not present</summary>
<br>

The cardholder denies participating in a [MOTO](/docs/moto/) transaction you processed. American Express investigates and confirms that the transaction is fraudulent.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder did participate in the transaction.
- The product/service was delivered to the cardholder's billing address and that the cardholder signed a receipt. 

</details>

<details id="reason-code-6006-fraud-unrecognized-transaction">
<summary>Reason Code 6006: Fraud, unrecognized transaction</summary>
<br>

The cardholder informs American Express that they believe the transaction is fraudulent.

To dispute this type of chargeback, you need to provide:

- Proof that the cardholder agreed to the transaction, made the booking/reservation, and received confirmation 
- Your site name, URL, IP address, and cancellation policy 
- Signed proof that the product/service was shipped and delivered, and the delivery address and date

</details>

#### Processing error

<details id="reason-code-4512-multiple-processing">
<summary>Reason code 4512: Multiple processing</summary>
<br>

You sent multiple transactions for the same amount.

To dispute this type of chargeback, you need to provide:

- Proof that you have already processed a corrective credit card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid

</details>

<details id="reason-code-4513-credit-not-presented">
<summary>Reason code 4513: Credit not presented</summary>
<br>

The cardholder received written acknowledgement from you for a credit or they cancelled in line with your policy, but they haven't received the credit in their account.

To dispute this type of chargeback, you need to provide:

- Proof that you have already processed a corrective credit card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid
- Screenshots of your cancellation policy 
- Evidence that:
    - the cardholder clicks to accept the terms and conditions
    - your cancellation policy doesn't include the right to dispute the policy 

</details>

<details id="reason-code-4515-paid-through-other-means">
<summary>Reason code 4515: Paid through other means</summary>
<br>

The cardholder informed American Express that the transaction was:

- Altered after they signed for it, or
- Submitted using an incorrect card number or amount

To dispute this type of chargeback, you need to provide proof that the cardholder's payment was not related to the disputed transaction.

</details>

<details id="reason-code-4516-request-for-support-not-fulfilled-and-or-no-reply-to-inquiry-letter">
<summary>Reason code 4516: Request for support not fulfilled and/or no reply to inquiry letter</summary>
<br>

American Express asked you to provide documents to support a charge queried by a cardholder but you didn't respond.

To dispute this type of chargeback, you need to provide proof that you have already processed a corrective credit card transaction.

</details>

<details id="reason-code-4517-insufficient-or-unclear-reply-to-dispute-inquiry-letter">
<summary>Reason code 4517: Insufficient or unclear reply to dispute inquiry letter</summary>
<br>

Fully itemized documents aren't clear or complete and directly link the cardholder to the transaction.

To dispute this type of chargeback, you need to provide:

- The date and amount of credit and the reason 
- An itemized invoice and/or receipt that directly links the cardholder to the charge 
- A successfully completed fax transmission report 
- Proof that the documents were sent and received by American Express within the time limit on the dispute inquiry letter

</details>

<details id="reason-code-4534-multiple-rocs">
<summary>Reason code 4534: Multiple ROCs</summary>
<br>

The cardholder denies participating in the transaction, despite previous successful transactions with you.

To dispute this type of chargeback, you need to provide fully itemized documents that link the cardholder to each charge processed and prove that all transactions are valid.

</details>

#### Customer dispute
<details id="reason-code-4544-goods-and-services-cancellation-of-recurring-payments">
<summary>Reason code 4544: Goods and services, cancellation of recurring payments</summary>
<br>

You have continued to charge the cardholder's account after they notified you to cancel or revoke consent for [Recurring payments](/docs/recurring-payments/).

To dispute this type of chargeback, you need to provide:

- A signed letter refuting the cardholder's claim, and/or proof that their evidence is incorrect 
- A copy of your cancellation policy and a statement indicating why the cancellation doesn't comply with your policy

</details>

<details id="reason-code-4553-goods-and-services-not-as-described">
<summary>Reason code 4553: Goods and services, not as described</summary>
<br>

The cardholder received a product/service that differs from the written description you provided, or is damaged. 

To dispute this type of chargeback, you need to provide:

- Proof that the product/service is as originally described
- A copy of your returns and refunds policies
- If available, authentication or a written assessment of the product/service

</details>

<details id="reason-code-4554-goods-and-service-not-received">
<summary>Reason code 4554: Goods and services, not received</summary>
<br>

The cardholder didn't receive the product/service or only in part.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder or authorized person did receive the product/service, e.g. proof of delivery 
- The product/service was delivered to the cardholder's billing address 
- The cardholder neither cancelled nor returned the product/service 

</details>

<details id="reason-code-4798-american-express-fraud-dispute">
<summary>Reason code 4798: American Express fraud dispute</summary>
<br>

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**

To dispute this type of chargeback, you need to provide proof that the transaction is exempt, or was authorized by a PIN, or [3D Secure](/docs/3ds2/).

</details>

---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/mastercard.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

### Mastercard 

#### Fraud

<details id="reason-code-4837-fraud-related-chargeback-or-no-cardholder-authorization">
<summary>Reason code 4837: Fraud related chargeback or no cardholder authorization</summary>
<br>

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide:

- Evidence that:
    - the cardholder is in possession of and/or using the product/service, e.g. proof of delivery 
    - the transaction was completed by a member of the cardholder's household or family 
- Evidence of previous interactions with the cardholder, e.g. other purchases, payment details 
- A transaction receipt
- An invoice 
- A track & trace number 
- Photos or emails proving a link between the person who received the product/service and the cardholder

</details>

<details id="reason-code-4863-potential-fraud-cardholder-does-not-recognize-the-transaction">
<summary>Reason code 4863: Potential fraud, cardholder does not recognize the transaction</summary>
<br>

The cardholder denies participating in or doesn't recognize the transaction you processed.

To dispute this type of chargeback, you need to provide:

- Evidence that:
    - the cardholder is in possession of and/or using the product/service, e.g. proof of delivery 
    - the transaction was completed by a member of the cardholder's household or family 
    - the cardholder is using the product/service 
- A copy of the cardholder's identification 
- Evidence of previous interactions with the cardholder, e.g. other purchases, payment details 
- A transaction receipt
- An invoice 
- A track & trace number
- Photos or emails proving a link between the person who received the product/service and the cardholder

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

To dispute this type of chargeback, you need to provide: 

- A transaction receipt
- An invoice 
- Evidence that:
    - the transaction amount was correct 
    - you have the right to alter the transaction amount without the cardholder's consent after the transaction is completed

</details>

#### Customer dispute 

<details id="reason-code-4853-cardholder-dispute-goods-or-service-not-delivered-goods-not-as-described">
<summary>Reason code 4853: Cardholder dispute: Goods or service not delivered, Goods not as described</summary>
<br>

- The product/service did not match your description on the transaction receipt or other record at the time of purchase, or
- The transaction was not completed, or
- The product/service the cardholder received was damaged or defective, or
- The cardholder disputes the quality of the product/service received

To dispute this type of chargeback, you need to provide:

- Proof of delivery of the product/service 
- A description of the product/service 
- An invoice 
- A track & trace number
- Evidence of communications with the cardholder 
- Evidence that cardholder didn't attempt to return the product/service

</details>

<details id="reason-code-4841-digital-goods-cancelled-recurring-transaction">
<summary>Reason code 4841: Digital goods, cancelled recurring transaction</summary>
<br>

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account 
- The cardholder used the product/service after the cancellation, e.g. ID and/or login history 
- The transaction was properly authorized and settled as a recurring transaction
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions, or that they signed a contract agreeing to the terms and conditions

</details>

---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/visa.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

### Visa

#### Fraud 
<details id="reason-code-10-4-card-absent-environment">
<summary>Reason code 10.4: Card absent environment</summary>
<br>

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide:

- Evidence the cardholder is in possession of and/or using the product/service, e.g. proof of delivery
- Evidence that the transaction was completed by a member of the cardholder's household or family
- Evidence of previous interactions with the cardholder, e.g. other purchases, payment details
- A transaction receipt
- An invoice number
- A track & trace number
- Photos or emails proving a link between the person who received the product/service and the cardholder

</details>

#### Processing error
<details id="reason-code-12-5-incorrect-amount">
<summary>Reason code 12.5: Incorrect amount</summary>
<br>

The transaction amount is incorrect or an error occurred. 

To dispute this type of chargeback, you need to provide:

- A transaction receipt 
- An invoice 
- Evidence that the transaction amount is correct

</details>

<details id="reason-code-12-6-duplicate-processing-or-paid-by-other-means">
<summary>Reason code 12.6: Duplicate processing or paid by other means</summary>
<br>

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide proof that:

- Both transactions are independent and separate 
- The transaction was not paid by other means or separate means

</details>

#### Customer dispute

<details id="reason-code-13-1-merchandise-or-services-not-received">
<summary>Reason code 13.1: Merchandise or services not received</summary>
<br>

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide:

- A description of the product/service
- Evidence that the cardholder is in possession of and/or using the product/service, e.g. proof of delivery 
- Proof of delivery, e.g. cardholder signature 
- An invoice 
- A track & trace number 
- Evidence of communications with the cardholder

</details>

<details id="reason-code-13-2-cancelled-recurring-transaction">
<summary>Reason code 13.2: Cancelled recurring transaction</summary>
<br>

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account 
- The product/service was used after the cancellation, e.g. ID and/or login history 
- The transaction was properly authorized and settled as a recurring transaction
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions, or that they signed a contract agreeing to the terms and conditions

</details>

<details id="reason-code-13-3-not-as-described">
<summary>Reason code 13.3: Not as described</summary>
<br>

The product/service:

- Did not match your description on the transaction receipt or elsewhere when purchased, or 
- Was damaged or defective

To dispute this type of chargeback, you need to provide:

- Proof of delivery of the product/service 
- Your original description of the product/service 
- An invoice number
- A track & trace number 
- Evidence of communications with the cardholder 
- Evidence that the cardholder did not attempt to return the product/service

</details>

<details id="reason-code-13-6-credit-not-processed">
<summary>Reason code 13.6: Credit not processed</summary>
<br>

The cardholder didn't receive the funds for a credit or voided transaction receipt. 

To dispute this type of chargeback, you need to provide:

- Details about the transaction 
- An invoice  
- Evidence of communications with the cardholder

</details>

<details id="reason-code-13-7-cancelled-service-and-or-merchandise">
<summary>Reason code 13.7: Cancelled service and/or merchandise</summary>
<br>

The cardholder cancelled or returned the product/service. Or, you did not properly disclose, or did disclose but did not apply, a limited return or cancellation policy at the time of the transaction.

To dispute this type of chargeback, you need to provide:

- Evidence of the cardholder using the service 
- Evidence of delivery of products/services that the cardholder didn't return
- Evidence that the cardholder had to click to accept your cancellation policy, and that your policy doesn't include the right to dispute terms and conditions available on your site 
- An invoice number 
- A track & trace number
- Evidence of communications with the cardholder

</details>

---

# Minimizing chargebacks

Card schemes may fine merchants that have high rates of chargebacks.

The best way of minimizing chargebacks is to provide good customer service.

Ways to minimize the most common types of chargeback include: 

<details id="fraud">
<summary>Fraud</summary>
<br>

Use [3DS2](/docs/3ds2/) for all credit card transactions. 

Cardholders are not allowed to request chargebacks due to fraud for 3D Secure-protected transactions.  

Carefully review all [uncaptured card payments](/docs/uncaptured) flagged by MultiSafepay's fraud filter.
</details>

<details it="non-delivery">
<summary>Non-delivery</summary>
<br>

- Inform customers of both expected and actual delivery times
- Document the delivery process, e.g. use track & trace with signature
- Refund or cancel transactions if the goods won't arrive within the stated delivery time or not at all. 
</details>

<details id="goods-not-as-described">
<summary>Goods not as described</summary>
<br>  

Offer quality items and provide clear descriptions on your site. 

Make sure your refund and return policies are clear and fair. 
</details>

<details id="transaction-not-recognized">
<summary>Transaction not recognized</summary>
<br>

Including your logo in customer's online bank environments and applications can help:

- Increase brand presence, recognition, and trust.
- Reduce chargebacks, disputes, and friendly fraud – when customers mistakenly initiate chargebacks because they don't recognize or trust a transaction.

<a href="https://logo.ethoca.com/" target="_blank">Upload your logo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the card scheme to display in all participating banking environments and applications. 
</details>
<br>

Additional guidance:

- Always follow the card scheme's payment acceptance guidelines carefully.
- Ensure there are no bugs for processing card payments in your <<glossary:backend>>.
- Make sure your refund and return policies are clear and fair. 

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
