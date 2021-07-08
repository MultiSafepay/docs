---
title : "Chargeback reasons and required evidence"
weight: 60
meta_title: "Credit card user guide - Chargeback reasons and required evidence - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/chargebacks/dispute-chargeback
    - /faq/chargebacks/disputing-chargebacks/
---

When a [cardholder](/payment-methods/credit-and-debit-cards/user-guide/glossary/#cardholder) requests a [chargeback](/payment-methods/credit-and-debit-cards/user-guide/glossary/#chargeback), they must provide a reason. This page sets out the chargeback reason codes for the major [card schemes](/payment-methods/credit-and-debit-cards/user-guide/glossary/#card-scheme). 

If you have asked MultiSafepay to dispute a chargeback on your behalf, we have specified what documentary proof you need to provide for each chargeback reason. Try to provide as much proof as possible. 

## Visa

### Fraud 
{{< details title="Reason code 10.4: Card absent environment" >}}

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide:

- Evidence the cardholder is in possession of and/or using the product/service, e.g. proof of delivery
- Evidence that the transaction was completed by a member of the cardholder's household or family
- Evidence of previous interactions with the cardholder, e.g. other purchases, payment details
- A transaction receipt
- An invoice number
- A Track & Trace number
- Photos or emails proving a link between the person who received the product/service and the cardholder

{{< /details >}}

### Processing error
{{< details title="Reason Code 12.5: Incorrect amount" >}}

The transaction amount is incorrect or an error occurred. 

To dispute this type of chargeback, you need to provide:

* A transaction receipt 
* An invoice 
* Evidence that the transaction amount is correct

{{< /details >}}

{{< details title="Reason code 12.6: Duplicate processing or paid by other means" >}}

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide proof that:

- Both transactions are independent and separate 
- The transaction was not paid by other means or separate means

{{< /details >}}

### Customer dispute

{{< details title="Reason code 13.1: Merchandise or services not received" >}}

The cardholder or authorized person didn't receive the product/service because you were unwilling or unable to provide it.

To dispute this type of chargeback, you need to provide:

- A description of the product/service
- Evidence that the cardholder is in possession of and/or using the product/service, e.g. proof of delivery 
- Proof of delivery, e.g. cardholder signature 
- An invoice 
- A Track & Trace number 
- Evidence of communications with the cardholder

{{< /details >}}

{{< details title="Reason code 13.2: Cancelled recurring transaction" >}}

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account 
- The product/service was used after the cancellation, e.g. ID and/or login history 
- The transaction was properly authorized and settled as a recurring transaction
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions, or that they signed a contract agreeing to the terms and conditions

{{< /details >}}

{{< details title="Reason code 13.3: Not as described" >}}

The product/service:

- Did not match your description on the transaction receipt or elsewhere when purchased, or 
- Was damaged or defective

To dispute this type of chargeback, you need to provide:

- Proof of delivery of the product/service 
- Your original description of the product/service 
- An invoice number
- A Track & Trace number 
- Evidence of communications with the cardholder 
- Evidence that the cardholder did not attempt to return the product/service

{{< /details >}}

{{< details title="Reason code 13.6: Credit not processed" >}}

The cardholder didn't receive the funds for a credit or voided transaction receipt. 

To dispute this type of chargeback, you need to provide:

- Details about the transaction 
- An invoice  
- Evidence of communications with the cardholder

{{< /details >}}

{{< details title="Reason code 13.7: Cancelled service and/or merchandise" >}}

The cardholder canceled or returned the product/service. Or, you did not properly disclose, or did disclose but did not apply, a limited return or cancellation policy at the time of the transaction.

To dispute this type of chargeback, you need to provide:

- Evidence of the cardholder using the service 
- Evidence of delivery of products/services that the cardholder didn't return
- Evidence that the cardholder had to click to accept your cancellation policy, and that your policy doesn't include the right to dispute terms and conditions available on your website 
- An invoice number 
- A Track & Trace number
- Evidence of communications with the cardholder

{{< /details >}}

## Mastercard 

### Fraud

{{< details title="Reason code 4837: Fraud related chargeback or no cardholder authorization" >}}

The cardholder denies participating in the transaction you processed.

To dispute this type of chargeback, you need to provide:

- Evidence that:
    - the cardholder is in possession of and/or using the product/service, e.g. proof of delivery 
    - the transaction was completed by a member of the cardholder's household or family 
- Evidence of previous interactions with the cardholder, e.g. other purchases, payment details 
- A transaction receipt
- An invoice 
- A Track & Trace number 
- Photos or emails proving a link between the person who received the product/service and the cardholder

{{< /details >}}

{{< details title="Reason code 4863: Potential fraud, cardholder does not recognize the transaction" >}}

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
- A Track & Trace number
- Photos or emails proving a link between the person who received the product/service and the cardholder

{{< /details >}}

### Processing error

{{< details title="Reason code 4834: Duplicate processing" >}}

The issuer determines that you submitted duplicate transactions.

To dispute this type of chargeback, you need to provide proof that both transactions:

- Are separate
- Are valid
- Were authorized by the cardholder's personal identification number (PIN) 

{{< /details >}}

{{< details title="Reason code 4831: Dispute amount or an incorrect amount" >}}

The cardholder claims that you processed an incorrect amount. 

To dispute this type of chargeback, you need to provide: 

- A transaction receipt
- An invoice 
- Evidence that:
    - the transaction amount was correct 
    - you have the right to alter the transaction amount without the cardholder's consent after the transaction is completed

{{< /details >}}

### Customer dispute 

{{< details title="Reason code 4855: Goods or services not delivered" >}}

You have debited the cardholder's account for a transaction but they didn't receive the product/service you were to ship, deliver, or otherwise provide by the expected delivery date.

To dispute this type of chargeback, you need to provide:

- A description of the product/service 
- Evidence that the cardholder is in possession of and/or using the product/service, e.g. proof of delivery
- Proof of delivery of the product/service, e.g. signed by the cardholder
- An invoice 
- A Track & Trace number
- Evidence of communications with the cardholder

{{< /details >}}

{{< details title="Reason code 4853: Cardholder dispute, not as described" >}}

- The product/service did not match your description on the transaction receipt or other record at the time of purchase, or
- The transaction was not completed, or
- The product/service the cardholder received was damaged or defective, or
- The cardholder disputes the quality of the product/service received

To dispute this type of chargeback, you need to provide:

- Proof of delivery of the product/service 
- A description of the product/service 
- An invoice 
- A Track & Trace number
- Evidence of communications with the cardholder 
* Evidence that cardholder didn't attempt to return the product/service

{{< /details >}}

{{< details title="Reason code 4841: Digital goods, cancelled recurring transaction" >}}

The cardholder:

- Withdrew permission to charge their bank account for a recurring transaction or installment transaction, or
- Notified you before the transaction was processed that their account was closed

To dispute this type of chargeback, you need to provide evidence that:

- You have previously completed successful transactions from that bank account 
- The cardholder used the product/service after the cancellation, e.g. ID and/or login history 
- The transaction was properly authorized and settled as a recurring transaction
- The transaction was a recurring transaction, including proof that the cardholder had to click to accept the terms and conditions of recurring transactions, or that they signed a contract agreeing to the terms and conditions

{{< /details >}}

## American Express 

### Fraud
{{< details title="Reason code 4573: Fraud, full recourse" >}}

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**.

To dispute this type of chargeback, you need to provide proof that the transaction is exempt, or was authorized by a PIN, or [3D Secure](/payment-methods/credit-and-debit-cards/user-guide/glossary/#3d-secure).

{{< /details >}}

{{< details title="Reason code 4526: Missing signature" >}}

The cardholder claims that the transaction is fraudulent and their signature is not on the relevant documents.

To dispute this type of chargeback, you need to provide proof that:

- The receipt is signed, or 
- The cardholder was present at the time of the transaction, or 
- The transaction was verified by [3D Secure](/payment-methods/credit-and-debit-cards/user-guide/glossary/#3d-secure)

{{< /details >}}

{{< details title="Reason code 4540: Card not present" >}}

The cardholder denies participating in a [MOTO](/tools/mail-order-telephone-order) transaction you processed. American Express investigates and confirms that the transaction is fraudulent.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder did participate in the transaction.
- The product/service was delivered to the cardholder's billing address and that the cardholder signed a receipt. 

{{< /details >}}

{{< details title="Reason Code 6006: Fraud, unrecognized transaction" >}}

The cardholder informs American Express that they believe the transaction is fraudulent.

To dispute this type of chargeback, you need to provide:

- Proof that the cardholder agreed to the transaction, made the booking/reservation, and received confirmation 
- Your website name, URL, IP address, and cancellation policy 
- Signed proof that the product/service was shipped and delivered, and the delivery address and date

{{< /details >}}

### Processing errors

{{< details title="Reason code 4512: Multiple processing" >}}

You sent multiple transactions for the same amount.

To dispute this type of chargeback, you need to provide:

- Proof that you have already processed a corrective credit card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid

{{< /details >}}

{{< details title="Reason code 4513: Credit not presented" >}}

The cardholder received written acknowledgement from you for a credit or they canceled in line with your policy, but they haven't received the credit in their account.

To dispute this type of chargeback, you need to provide:

- Proof that you have already processed a corrective credit card transaction 
- A fully itemized document that links the cardholder to each charge processed and proves that all transactions are valid
- Screenshots of your cancellation policy 
- Evidence that:
    - the cardholder clicks to accept the terms and conditions
    - your cancellation policy doesn't include the right to dispute the policy 

{{< /details >}}

{{< details title="Reason code 4515: Paid through other means" >}}

The cardholder informed American Express that the transaction was:

- Altered after they signed for it, or
- Submitted using an incorrect card number or amount

To dispute this type of chargeback, you need to provide proof that the cardholder's payment was not related to the disputed transaction.

{{< /details >}}

{{< details title="Reason code 4516: Requested for support not fulfilled and/or no reply to inquiry letter" >}}

American Express asked you to provide documents to support a charge queried by a cardholder but you didn't respond.

To dispute this type of chargeback, you need to provide proof that you have already processed a corrective credit card transaction.

{{< /details >}}

{{< details title="Reason code 4517: Insufficient or unclear reply to dispute inquiry letter" >}}

Fully itemized documents aren't clear or complete and directly link the cardholder to the transaction.

To dispute this type of chargeback, you need to provide:

* The date and amount of credit and the reason 
* An itemized invoice and/or receipt that directly links the cardholder to the charge 
* A successfully completed fax transmission report 
* Proof that the documents were sent and received by American Express within the time limit on the dispute inquiry letter

{{< /details >}}

{{< details title="Reason code 4534: Multiple ROCs" >}}

The cardholder denies participating in the transaction, despite previous successful transactions with you.

To dispute this type of chargeback, you need to provide fully itemized documents that link the cardholder to each charge processed and prove that all transactions are valid.

{{< /details >}}

### Customer disputes
{{< details title="Reason code 4544: Goods and services, cancellation of recurring payments" >}}

You have continued to charge the cardholder's account after they notified you to cancel or revoke consent for recurring payments.

To dispute this type of chargeback, you need to provide:

- A signed letter refuting the cardholder's claim, and/or proof that their evidence is incorrect 
- A copy of your cancellation policy and a statement indicating why the cancellation doesn't comply with your policy

{{< /details >}}

{{< details title="Reason code 4553: Goods and services, not as described" >}}

The cardholder received a product/service that differs from the written description you provided, or is damaged. 

To dispute this type of chargeback, you need to provide:

- Proof that the product/service is as originally described
- A copy of your returns and refunds policies
- If available, authentication or a written assessment of the product/service

{{< /details >}}

{{< details title="Reason code 4554: Goods and services, not received" >}}

The cardholder didn't receive the product/service or only in part.

To dispute this type of chargeback, you need to provide evidence that:

- The cardholder or authorized person did receive the product/service, e.g. proof of delivery 
- The product/service was delivered to the cardholder's billing address 
- The cardholder neither canceled nor returned the product/service 

{{< /details >}}

{{< details title="Reason code 4798: American Express fraud dispute" >}}

The cardholder denies authorizing the charge, and your business has been placed in the fraud full recourse program: **Investigation confirms fraud**

To dispute this type of chargeback, you need to provide proof that the transaction is exempt, or was authorized by a PIN, or [3D Secure](/payment-methods/credit-and-debit-cards/user-guide/glossary/#3d-secure).

{{< /details >}}