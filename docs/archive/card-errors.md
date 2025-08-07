---
title: "Card errors"
category: 
order: 
---

This page sets out reason codes for common credit card errors returned by <<glossary:issuers>> and recommended actions to take.

Only the cardholder can contact the issuer to find out the specific reason.

If the issue can't be resolved, ask the cardholder for another card number, or to use a different payment method.

---
#### 01: Refer to card issuer
The issuer wants to check the transaction.

Cardholder: Contact the issuer to complete the transaction.

---
#### 02: Refer to card issuer, special condition
The issuer wants to check the transaction.

Cardholder: Contact the issuer to complete the transaction.

---
#### 03: Invalid merchant or service provider
The merchant or service provider is restricted by the issuer.

Cardholder: Contact the issuer.

---
#### 04: Pick up card
The transaction was declined because the cardholder's account is closed or blocked.

Cardholder: Contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 05: Do not honor
The issuer has flagged a problem with the card.

Cardholder: Contact the issuer.

---
#### 07: Pick up card, special conditions
The issuer has detected fraudulent activity on the cardholder's account.

Cardholder: If you have successfully paid with this card before, contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 08: Honor with ID
The issuer needs to verify the cardholder's identity.

Cardholder: Contact the issuer.

---
#### 1A Visa soft decline
Authentication required.

Cardholder: Contact the issuer.

---
#### 10: Partial approval
The issuer can approve an amount less than requested, if supported by the merchant.

---
#### 12: Invalid transaction
Cardholder: Check the payment method type and payment details.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 13: Invalid amount
The payment amount exceeds issuer policies or regulatory limits.

Cardholder: Contact your bank.

---
#### 14: Invalid card/account number
The card may have expired, or the account may be invalid or closed.

Cardholder: Contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 15: Invalid issuer
The first digit of the card number doesn't match any issuer.

Cardholder: Check the first digit of the card number, or contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 19: Re-enter transaction
There was a transaction error, or the issuer was temporarily unavailable.

Merchant: Reattempt. If still unsuccessful after several attempts, email <support@multisafepay.com>

---
#### 28: File temporarily unavailable
Authorization failed due to a temporary error.

Merchant: Reattempt. If still unsuccessful after several attempts, email <support@multisafepay.com>

---
#### 30: Format error
Merchant: Check the transaction data.

---
#### 34: Fraud suspicion
Cardholder: Contact the issuer.

---
#### 41: Lost/blocked/cancelled card
The cardholder has reported this card lost.

Merchant:

- If the cardholder is a new customer, assume fraudulent activity. <br> Do **not** reattempt. The issuer will never approve.
- If a recurring payment, the cardholder may have reported the card lost since the last successful payment. Contact them to ask for a new card number, or another payment method. Update the recurring payment with the new payment details.

---
#### 43: Stolen card
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 46: Closed account
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 51: Insufficient funds/over credit limit
The card is over the holder's credit limit, or will go over if the transaction is processed.

Cardholder: Contact the issuer to increase your credit limit, or pay into your account to make more credit available. Once resolved, reattempt.
Merchant: Consider implementing a partial authorization service to accept a lesser amount than requested.

---
#### 54: Expired card
Cardholder: Check the expiry date or try another card.
Merchant: Do **not** reattempt. Make sure you update any recurring payments with the new card details.

---
#### 55: Invalid PIN
Cardholder: Try again with the correct PIN.
Merchant: Reattempt as a non-PIN transaction, if applicable.

---
#### 57: Transaction not permitted to cardholder
The cardholder isn't permitted to perform this type of transaction, e.g.:

- Product type
- Issuer policy
- Restricted country or across borders
- Card not yet activated

Cardholder: Contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### 58: Transaction not permitted to acquirer/terminal
Merchant: Your MultiSafepay account is not set up for this payment method or type of transaction. Email <support@multisafepay.com>

---
#### 59: Suspected fraud (Visa)
Cardholder: Contact the issuer.
Merchant: If the cardholder confirms that the issue is resolved, reattempt.

---
#### 61: Exceeds withdrawal amount limit
Cardholder: Contact the issuer.
Merchant: Do **not** reattempt on the same day to allow limits to reset.

---
#### 62: Restricted card
The card is restricted, e.g.:

- Deceased cardholder
- Permanently blocked
- Embargoed country

Cardholder: Contact the issuer.
Merchant: If the cardholder confirms the restriction has been removed, reattempt. Do&nbsp;**not** alter the country code or any other transaction data.

---
#### 63: Security violation
There is a security violation, suspected fraud, or the card is temporarily blocked.

Cardholder: Contact the issuer.

---
#### 65: Exceeds withdrawal count limit/authentication requested
The cardholder has exceeded their maximum daily credit limit, or will do if the transaction is processed.

Cardholder: Contact the issuer to increase your credit limit or provide authentication. Once resolved, reattempt.
Merchant: If the cardholder is a new customer, the transaction may be fraudulent. Do&nbsp;**not** reattempt on the same day to allow limits to reset.

---
#### 65: Mastercard soft decline
Authentication required.

Cardholder: Contact the issuer.

---
#### 68: Time out

---
#### 70: Contact card issuer
Cardholder and merchant: Contact the issuer.

---
#### 71: PIN not changed
A PIN change request was not completed successfully.

Cardholder: Contact the issuer.

---
#### 75: Allowable number of PIN tries exceeded
Merchant: Do **not** reattempt on the same day to allow limits to reset.

---
#### 78: Invalid/non-existent account
The account is temporarily blocked. The card may not have been activated yet.

Cardholder: Contact the issuer.
Merchant: If the cardholder confirms the account is unblocked, or the card has been activated, reattempt.

---
#### 82: Negative CAM, dCVV, iCVV, or CVV results
There may have been an issue with the card reader or a voltage spike during the read.

Merchant: Reattempt, but monitor for potential fraud.

---
#### 83: Authentication needed
Merchant: Enable 3D Secure and reattempt.

---
#### 85: Not declined
Used for account status inquiries.

---
#### 86: Cannot verify PIN
Merchant: You can reattempt within the same day, or attempt <<glossary:POS>> transactions as non-PIN transactions, if applicable.

---
#### 87: No cashback allowed

---
#### 88: Cryptographic failure
The issuer cannot authorize the transaction for technical reasons.

---
#### 89: Unacceptable PIN
Cardholder: Reattempt with the correct PIN.

---
#### 91: Authorization/issuer system inoperative
The issuer couldn't be contacted or the authorization timed out.

Merchant: You can reattempt within the same day.

---
#### 92: Unable to route the transaction
There was a technical destination error in the issuer's system.

---
#### 93: Transaction cannot be completed
There is a temporary or permanent restriction on the cardholder's account, e.g.:

- Gambling
- Unauthorized card-not-present transaction
- No two-factor authentication

Cardholder: Contact the issuer.
Merchant: If the cardholder confirms the restriction has been removed, reattempt. Do&nbsp;**not** alter any transaction data.

---
#### 94: Duplicate transmission detected
The same transaction has been sumbitted more than once.

---
#### 96: System error
There is a temporary error in the issuer's system.

Merchant: Reattempt. If still unsuccessful after several attempts, email <support@multisafepay.com>

---
#### CV: Card type verification error

**Either**
The CID or CVV2 code provided doesn't match the card.

Cardholder: Provide the correct code, and then reattempt.
Merchant: You can try again _without_ a code, but be aware that if the cardholder doesn't have the correct code, it may be a fraudulent transaction.

**Or**
Merchant: Your MultiSafepay account may be configured incorrectly. Email&nbsp;<support@multisafepay.com>

---
#### R0: Stop payment order
The cardholder requested the issuer to stop a specific, single recurring payment transaction.

Cardholder: Provide an alternative payment method, or contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### R1: Revocation of authorization order
The cardholder requested the issuer to stop all recurring payment transactions with a specific merchant.

Cardholder: Provide an alternative payment method, or contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### R3: Revocation of all authorizations order
The cardholder requested the issuer to stop all recurring payment transactions for that card.

Cardholder: Provide an alternative payment method, or contact the issuer.
Merchant: Do **not** reattempt. The issuer will never approve.

---
#### N7: Decline for CVV2 failure
CVV2 verification failed in card-not-present transaction.

Merchant: Validate the CVV2 value before reattempting. Monitor reattempts for potential fraud.

---
#### 1A: Additional customer authentication required
The transaction falls within the scope of PSD2 and did not pass 3D Secure.

Merchant: For card-not-present transactions, reattempt with 3D Secure.

This page sets out possible reasons why a credit card payment was declined.

Only the cardholder can contact the <<glossary:issuer>> to find out the specific reason.

---
### Declined by MultiSafepay
Our automated fraud filter flagged the transaction as probably fraudulent.

Email <support@multisafepay.com>

---
### 3D Secure authentication cancelled
Ask the cardholder if they want to try the transaction again.

---
### Merchant only accepts 3D Secure-authenticated cards
Email a request to accept non-3D Secure authenticated cards to <risk@multisafepay.com>
<br>

---

[block:html]
{
"html": "<blockquote className=\"callout callout_info\">\n <h3 className=\"callout-heading false\">\n <span className=\"callout-icon\">💬</span>\n <p>Support</p>\n </h3>\n <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)



