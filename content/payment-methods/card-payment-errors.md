---
title: "Card payment errors"
category: 6298bd782d1cf4006032e765
order: 1
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: "card-payment-errors"
---
This page lists card error codes you may encounter in authentication and authorization responses or statuses and descriptions.

**Authentication errors** occur when the person introducing the card details cannot demonstrate that they are the cardholder. Authentication errors can be either technical or non-technical, for example 3DS code inserted incorrectly.
**Authorization errors** occur when the issuer bank, schemes or other intermediates reject the authorization (this is possible for both 3DS-verified and non-verified transactions).

## Authentication errors

This table lists the most common 3DS authentication failed errors response and descriptions.

In these cases, neither MultiSafepay nor the merchant can take specific actions to unblock the transaction. Advise the cardholder to contact their bank if the reason for the error is unclear to them.

| Code     | Card error                                                         |
| :-------- | :----------------------------------------------------------------------- |
| **3001** | 3DS Authentication Failed / Card authentication failed.                  |
| **3002** | 3DS Authentication Failed / Unknown device.                              |
| **3003** | Authentication Failed / Unsupported device.                              |
| **3004** | 3DS Authentication Failed / Exceeds authentication frequency limit.      |
| **3005** | 3DS Authentication Failed / Expired card.                                |
| **3006** | 3DS Authentication Failed / Invalid card number.                         |
| **3007** | 3DS Authentication Failed / Invalid transaction.                         |
| **3008** | 3DS Authentication Failed / No Card record.                              |
| **3009** | 3DS Authentication Failed / Security failure.                            |
| **3010** | 3DS Authentication Failed / Stolen card.                                 |
| **3011** | 3DS Authentication Failed / Suspected fraud.                             |
| **3012** | 3DS Authentication Failed / Transaction not permitted to the cardholder. |
| **3100** | 3DS Authentication Failed / Initiation Failed. |

## Authorization errors

The table below lists common card errors returned by <<glossary:issuers>> and recommended actions.

If the issue can't be resolved, ask the cardholder for another card number or to use a different payment method.

| Code | Card error | Description| Action recommended|
| :-------- | :--------| :--------|:---------- |
| **4001** | Do not honor |The issuer has flagged a problem with the card.|**Cardholder:** Contact the issuer.|
| **4002** | Insufficient funds | The cardholder has exceeded their maximum daily credit limit.| **Cardholder:** Contact the issuer to increase your credit limit or pay into your account to make more credit available. Once resolved, reattempt.<br> **Merchant:** Consider implementing a partial authorization service to accept a lesser amount than requested. |
| **4003** | Suspected fraud | There is a security violation, suspected fraud, or the card is temporarily blocked. | **Cardholder:**  Contact the issuer. |
| **4004** | Soft decline | Authentication required.| **Cardholder:**  Contact the issuer. |
| **4005** | Expired card, **or** Invalid Account Number | The card may have expired, or the account may be invalid or closed. |**Cardholder:**  Check the expiry date or try another card.<br> **Merchant:**  Do not reattempt. Make sure you update any recurring payments with the new card details. |
| **4999** | Declined | See below for a description. | See below for the action required. |

<details>

<summary>  Specific reason codes for <b>4999</b> Declined error</summary>
 <br>

| Card error | Description | Action |
|:---|:---| :--- |
| **Refer to the card issuer** | The issuer wants to check the transaction. | **Cardholder:** Contact the issuer to complete the transaction. |
| **Invalid merchant or service provider** | The issuer restricts the merchant or service provider.| **Cardholder:** Contact the issuer.|
| **Pick up the card** | The transaction was declined because the cardholder's account was closed or blocked.|  **Cardholder:**  Contact the issuer to complete the transaction |
|  **Pick up the card, special conditions** | The issuer wants to check the transaction.| **Cardholder:** Contact the issuer to complete the transaction |
| **Cardholder not enrolled in service** | The cardholder is not enrolled in 3DS service. | **Cardholder**:  Contact the issuer. <br> **Merchant**: card not enrolled in 3DS service. Not possible to authenticate |
| **Transaction timed out (ACS)** | The transaction expired in the authentication stage | **Cardholder**: In next transaction, complete authentication |
| **Invalid merchant or service provider** | The merchant or service provider is restricted by the issuer.| **Cardholder:** Contact the issuer. |
|  **Invalid transaction** | The transaction is invalid. |**Cardholder:** Check the payment method type and payment details <br>**Merchant:** Do not reattempt. The issuer will never approve.|
| **Invalid amount** | The payment amount exceeds issuer policies or regulatory limits.| **Cardholder:** Contact your bank. |
| **Invalid card, or account number** | The card may have expired, or the account may be invalid or closed. | **Cardholder:** Contact the issuer. |
| **Invalid issuer** | The first digit of the card number doesn't match any issuer. | **Cardholder:** Check the first digit of the card number, or contact the issuer.<br> **Merchant:** Do not reattempt. The issuer will never approve. |
| **Re-enter transaction** | There was a transaction error, or the issuer was temporarily unavailable. |  **Merchant:** Reattempt if still unsuccessful after several attempts, email [support@multisafepay.com](mailto:support@multisafepay.com)|
| **File temporarily unavailable** | Authorization failed due to a temporary error. | **Merchant:** Reattempt if still unsuccessful after several attempts, email [support@multisafepay.com](mailto:support@multisafepay.com) |
| **Format error** | The format may be incorrect. | **Merchant:** Check the transaction data. |
| **Insufficient funds or over credit limit** | The card exceeds the holder's credit limit or will go over if the transaction is processed. | **Cardholder:** Contact the issuer to increase your credit limit or pay into your account to make more credit available. Once resolved, reattempt.<br>  **Merchant:**  Consider implementing a partial authorization service to accept a less than requested.| 
| **Invalid PIN** | The PIN may be incorrect. |**Cardholder:**  Try again with the correct PIN. |
| **Transaction not permitted to cardholder** | The cardholder isn't permitted to perform this type of transaction, e.g.: <br> - Product type  <br> - Issuer policy <br> - Restricted country or across borders <br>- Card has not yet been activated | **Cardholder:** Contact the issuer. <br> **Merchant:** Do **not** reattempt. The issuer will never approve.|
| **Transaction not permitted to acquirer or terminal** | Your MultiSafepay account is not set up for this payment method or type of transaction. | **Merchant:** Email [support@multisafepay.com](mailto:support@multisafepay.com) |
| **Restricted card** | The card is restricted, e.g.: <br>- Deceased cardholder <br> - Permanently blocked <br>- Embargoed country|**Cardholder:** Contact the issuer.<br> **Merchant:** Reattempt if the cardholder confirms the restriction has been removed. Do **not** alter the country code or any other transaction data.|
| **PIN not changed** | A PIN change request was not completed successfully. | **Cardholder:** Contact the issuer. |
| **PIN tries exceeded** | The number of PIN tries exceeded. | **Merchant:** Do **not** reattempt on the same day to allow limits to reset. |
| **Invalid or non-existent account** | The account is temporarily blocked. The card may not have been activated yet. | **Cardholder:** Contact the issuer.<br> **Merchant:**  Reattempt. If the cardholder confirms the account is unblocked or the card has been activated.|
| **Negative CAM, dCVV, iCVV, or CVV results** | There may have been an issue with the card reader or a voltage spike during the read. | **Merchant:**  Reattempt, but monitor for potential fraud. |
| **Cannot verify PIN** | An issue with card verification. | **Merchant:** You can reattempt within the same day, or attempt <<glossary:POS>> transactions as non-PIN transactions, if applicable. |
|  **Cryptographic failure** | Technical issues. | The issuer cannot authorize the transaction for technical reasons. |
| **Authorization or issuer system inoperative** | The issuer couldn't be contacted, or the authorization timed out. | **Merchant:** You can reattempt within the same day. |
| **Unable to route the transaction** | There was a technical destination error in the issuer's system. | **Cardholder:** You can reattempt. |
| **Transaction cannot be completed** | There is a temporary or permanent restriction on the cardholder's account, e.g.:<br>- Gambling <br> - Unauthorized card-not-present transaction  <br>- No two-factor authentication | **Cardholder:** Contact the issuer.<br>**Merchant:** Reattempt if the cardholder confirms the restriction has been removed. Do **not** alter any transaction data.|
| **Duplicate transmission detected** | The same transaction has been submitted more than once.| **Cardholder:** Do **not** reattempt. |
| **System error** | There is a temporary error in the issuer's system. | **Merchant:** Reattempt if it still unsuccessful, email [support@multisafepay.com](mailto:support@multisafepay.com) |
| **Card type verification error** | The CID or CVV2 code provided doesn't match the card. | **Cardholder:** Provide the correct code, and then reattempt.<br> **Merchant:** You can try again without a code, but be aware that it may be a fraudulent transaction if the cardholder doesn't have the correct code, **or** Your MultiSafepay account may be configured incorrectly. Email [support@multisafepay.com](mailto:support@multisafepay.com) |
| **Stop payment order** | The cardholder has requested that the issuer stop a recurring payment transaction. | **Cardholder:** Provide an alternative payment method, or contact the issuer. <br> **Merchant:** Do **not** reattempt. The issuer will never approve. |
| **Revocation of authorization order** | The cardholder requested that the issuer stop recurring payment transactions with a specific merchant. | **Cardholder:** Provide an alternative payment method, or contact the issuer.<br> **Merchant:** Do **not** reattempt. The issuer will never approve. |
| **Revocation of all authorizations order** | The cardholder requested the issuer to stop all recurring payment transactions for that card. | **Cardholder:** Provide an alternative payment method, or contact the issuer.<br>  **Merchant:** Do **not** reattempt. The issuer will never approve. |
| **Decline for CVV2 failure** | CVV2 verification failed in a card-not-present transaction. | **Merchant:** Validate the CVV2 value before reattempting. Monitor reattempts for potential fraud. |
| **Additional customer authentication required** | The transaction falls within the scope of PSD2 and did not pass 3D Secure. |**Merchant:**  For card-not-present transactions, reattempt with 3D Secure. |
| **Declined by MultiSafepay** | Our automated fraud filter flagged the transaction as probably fraudulent. | Email [support@multisafepay.com](mailto:support@multisafepay.com) |
| **3D Secure authentication cancelled** | 3DS authentication was cancelled. | Ask the cardholder to reattempt. |
| **3D Secure-authenticated cards** | Merchant only accepts 3D Secure-authenticated cards | Email a request to accept non-3D Secure authenticated cards to [risk@multisafepay.com](mailto:risk@multisafepay.com) |

 <br>

 </details>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)

