---
title : "Declined credit card payments"
weight: 70
meta_title: "Declined credit card payments - MultiSafepay Docs"
read_more: "."
short_description: "Reason codes for why a card payment was declined."
url: '/about-payments/declined-status/'
aliases: 
    - /payment-methods/creditcards/creditcard-status-declined-what-does-this-mean-/
    - /payment-methods/credit-and-debit-cards/creditcards/creditcard-status-declined-what-does-this-mean-/
    - /faq/general/declined-status/
    - /payments/methods/credit-and-debit-cards/user-guide/declined-status/
    - /credit-cards-user-guide/declined-status/
---

This page sets out possible reasons why a credit card payment was declined. 

Only the cardholder can contact the [issuer](/glossaries/credit-cards/#issuer) to find out the specific reason.

## MultiSafepay errors

### Transaction declined by MultiSafepay 
Our automated fraud filter declined the transaction.  

Email <support@multisafepay.com> 

### 3D Secure authentication cancelled 
Ask the cardholder if they want to try the transaction again. 

### Merchant only accepts 3D Secure-authenticated cards 
Email a request to accept non-3D Secure authenticated cards to <risk@multisafepay.com> 

## Issuer errors

### 01: Refer to card issuer 
The issuer won't authorize the transaction.  

- Ask the cardholder to contact the issuer. Once resolved, try again.
- If not resolved, ask the cardholder for another card, or to use a different payment method.

### 04: Pick up card 
The issuer won't authorize the transaction.  

- Ask the cardholder to contact the issuer. Once resolved, try again.
- If not resolved, ask the cardholder for another card, or to use a different payment method.

### 05: Do not honour / Card declined by issuer 
The issuer has flagged a problem with the card and advises you not to accept it.  

- Ask the cardholder to contact the issuer. Once resolved, try again.
- If not resolved, ask the cardholder for another card, or to use a different payment method. 

### 07: Pick up card, special conditions
The issuer has detected fraudulent activity on the cardholder's account and won't authorize the transaction.  

- If the cardholder has successfully paid with this card before, suggest they try a different card or payment method and advise them to contact the issuer. 
- If the cardholder is a new customer, assume fraudulent activity. Do **not** attempt to run the card again. 

### 12: Invalid transaction
Correct the payment method type and payment details, and then try again.

### 13: Invalid amount
The payment amount is negative or non-numeric.  

Correct the amount, and then try again. 

### 14: Invalid card number 
- Correct the card number, and then try again.  
- Pauze any scheduled recurring payments or you will incur an authorization fee for each attempt with the invalid card number. 

### 15: No such issuer, decline
The first digit of the card number doesn't match any issuer.  

Correct the first digit of the card number, and then try again. 

### 19: Re-enter transaction
There was an unknown error.  

Try again. If still unsuccessful after several attempts, email <support@multisafepay.com>

### 28: File update file locked
Authorization failed due to a temporary error.  

Try again. If still unsuccessful after several attempts, email <support@multisafepay.com>

### 41: Lost card, pick up
The cardholder has reported this card lost or stolen. The issuer won't authorize any attempted transactions. 

- If the cardholder is a new customer, assume fraudulent activity. Do **not** attempt to run the card again.
- If a recurring payment, the cardholder may have reported the card lost or stolen since the last successful payment. Contact them to ask for a new card number, or another payment method. Update the recurring payment with the new payment details. 

### 51: Insufficient funds
The card is over the holder's credit limit, or will go over if the transaction is processed.   

- Ask the cardholder to contact the issuer to increase their credit limit, or pay into their account to make more credit available. Once resolved, try again. 
- If not resolved, ask the cardholder for another card number, or use a different payment method. 

### 54: Expired card
- Ask the cardholder for a new card number, and process the payment again. 
- Make sure you update any recurring payments with the new card details. 

### 57: Transaction not permitted to cardholder
The card doesn't allow this type of transaction. 

- Ask the cardholder to contact the issuer and request permission for this type of transaction. Once resolved, try again. 
- If not resolved, ask the cardholder for another card, or to use a different payment method. 

### 58: Transaction not permitted to terminal
Your MultiSafepay account is not set up for this payment method or type of transaction.  

Email <support@multisafepay.com>

### 62: Restricted card
**Either** your MultiSafepay account is not set up for this payment method or type of transaction.  

Email <support@multisafepay.com>

**Or** the card has restrictions for online or international payments.  

- Ask the cardholder to contact the issuer. Once resolved, try again.  
- If not resolved, ask the cardholder for another card, or to use a different payment method. 

### 63: Security violation on credit card or machine
The CID or CVV2 code provided doesn't match the card.

- Ask the cardholder for the correct code, and then try again. 
- You can try again _without_ a code, but be aware that if the cardholder doesn't have the correct code, it may be a fraudulent transaction.

### 65: Exceeds withdrawal frequency limit
The cardholder has exceeded their maximum daily credit limit, or will do if the transaction is processed. 

- If the cardholder is a new customer, the transaction may be fraudulent. 
- Ask the cardholder to contact the issuer to increase their credit limit. Once resolved, try again. 
- If not resolved, ask the cardholder for another card, or to use a different payment method.

### 85 or 00: Issuer system unavailable
Authorization failed due to a temporary communication error with the issuer's system. 

Try again. If still unsuccessful after several attempts, email <support@multisafepay.com>

### 91: Issuer or switch is inoperative
The issuer couldn't be contacted or the authorization timed out. 

Try again. If still unsuccessful after several attempts, email <support@multisafepay.com>

### 93: Transaction cannot be completed
There is a violation on the cardholder's account and the issuer declined the transaction. 

- Ask the cardholder to contact the issuer. Once resolved, try again. 
- If not resolved, ask the cardholder for another card, or to use a different payment method.

### 96: System malfunction
Authorization failed due to a temporary error in the issuer's system. 

Try again. If still unsuccessful after several attempts, email <support@multisafepay.com>

### CV: Card type verification error
**Either** the CID or CVV2 code provided doesn't match the card.  

- Ask the cardholder for the correct code, and then try again. 
- You can try again _without_ a code, but be aware that if the cardholder doesn't have the correct code, it may be a fraudulent transaction. 

**Or** your MultiSafepay account may be configured incorrectly.  

Email <support@multisafepay.com>

### R0 or R1: Stop recurring transaction
The cardholder requested the issuer to cancel a recurring payment.

To avoid a [chargeback](/chargebacks/), cancel the recurring payment immediately. Then, ask the cardholder what they want to do. If they want to continue the recurring payment with:

- The current card, ask them to contact the issuer to remove the stop order against you.
- Updated card details or a different payment method, get their consent and then update the recurring payment.

## Support
Email <support@multisafepay.com>