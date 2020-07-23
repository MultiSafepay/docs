---
title : "Test Payment Details"
meta_title: "FAQ Getting Started - Test payment details - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

For thoroughly testing your payment integration with MultiSafepay, you can use the following payment credentials in the TEST environment to simulate different payment scenarios.

Testing with our test credentials can only be done in you MultiSafepay Test Control. Create your [MultiSafepay Test Account](https://testmerchant.multisafepay.com/signup) free of charge.

With a successful connection with your test or staging environment, you can immediately start testing.

{{< alert-notice >}} Outgoing payments and additional payment methods (e.g. American Express) are disabled by default in a MultiSafepay test account. As a result, a refund cannot be processed successfully. Contact our Integration Team to enable outgoing payments or additional payment methods in your MultiSafepay Test Control. {{< /alert-notice >}} 

If assistance is required, contact our Integration Team at <integration@multisafepay.com>


## AfterPay

Contact our [Integration Team](<mailto:integration@multisafepay.com>) to enable AfterPay as payment method in your MultiSafepay Test Control.

## Alipay

MultiSafepay provides a test platform for Alipay transactions. During the payment process you will be able to simulate the outcome of the transaction.

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled |

## American Express

MultiSafepay provides a test platform for American Express transactions. By entering a test card number, you will be able to simulate the outcome of the transaction.

* CVC 123
* Select a date in the future for the expiry date

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 378282246310005  | Completed | Transaction is Completed (not 3D enrolled) |
| 374200000000004  | Declined  | Transaction is Declined |
| 378734493671000  | Uncleared | Transaction is Uncleared (after 3 minutes it is changed to Void) |

## Apple Pay

If you would like to test Apple Pay, we kindly invite you to read our page about [Compatibility and Testing](/payment-methods/wallet/applepay/#compatibility-and-testing) which explains how you will be able to execute tests on supported devices.

## Bancontact

MultiSafepay provides a test platform for Bancontact transactions. By entering a test card number, you will be able to simulate the outcome of the transaction.

| Card number           | Status    | Description              |
| --------------------- | --------- | ------------------------ |
| 67034500054610005 | Completed | Transaction is Completed (3D enrolled) |
| 67034500054610009 | Declined  | Transaction is Declined (card needs to be 3D enrolled) |
| 67039902990000045 | Declined  | Transaction is Declined (failed 3D authentication) |
| 67039902990000011	| Declined  | Transaction is Declined (3D authentication successful, but insufficient funds) |

## BankTransfer

MultiSafepay provides a test platform for bank transfer transactions. By entering a test IBAN you will be able to simulate the outcome of the transaction.

| IBAN               | Status    | Description              |
| ------------------ | --------- | ------------------------ |
| NL87ABNA0000000001 | Initialized/Completed | Transaction is Initialized (after 1 minute it is Completed) |
| NL87ABNA0000000002 | Initialized/Expired/Completed | Transaction is Initialized ( after 1 minute it is Expired, and 1 minute later it is Completed) |
| NL87ABNA0000000003 | Initialized/Expired | Transaction is Initialized ( after 1 minute it is Expired) |
| NL87ABNA0000000004 | Initialized/Declined | Transaction is Initialized ( after 1 minute it is Declined) |

## Belfius

MultiSafepay provides a test platform for Belfius transactions. During the payment process you will be able to simulate the outcome of the transaction.

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled |

## Cartes Bancaires

MultiSafepay provides the Visa test credentials to test the payment method Cartes Bancaires.

Cartes Bancaires is shown as a payment option on the payment page of MultiSafepay only after:

1. The Visa gateway is enabled; and
2. The locale is set to fr_FR (France) in the transaction call received by MultiSafepay.

## CBC

The payment method CBC can only be processed on our new payment page starting with PayV2.

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is completed |
| Cancelled | Transaction is void / cancelled |


## Dankort

MultiSafepay provides the Visa test credentials to test the payment method Dankort.

Dankort is shown as a payment option on the Payment page of MultiSafepay only after:

1. The Visa gateway is enabled; and
2. The locale is set to da_DK (Denmark) in the transaction call received by MultiSafepay.

## SEPA Direct Debit

MultiSafepay provides a test platform for SEPA Direct Debit transactions. By entering a test IBAN you will be able to simulate the outcome of the transaction.

| IBAN               | Status    | Description              |
| ------------------ | --------- | ------------------------ |
| NL87ABNA0000000001 | Initialized/Completed | Transaction is Initialized (after 2 minutes it is Completed) |
| NL87ABNA0000000002 | Initialized/Declined | Transaction is Initialized (after 2 minutes it is Declined) |
| NL87ABNA0000000003 | Initialized/Uncleared/Completed | Transaction is Initialized ( after 2 minutes it is Uncleared, and 1 minute later it is Completed) |
| NL87ABNA0000000004 | Initialized/Uncleared/Declined | Transaction is Initialized ( after 2 minutes it is Uncleared, and 1 minute later it is Declined) |

## Dotpay

MultiSafepay provides a test platform for Dotpay transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Declined | Transaction is Declined |

## E-invoicing

MultiSafepay provides a test platform for Betaal na Ontvangst / Pay After Delivery transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Address               | Status    | Description              |
| ------------------ | --------- | ------------------------ |
| Kraanspoor 39C - 1033SC Amsterdam | Completed | Transaction is Completed |


## Gift cards

Currently no test data available for the payment method gift cards.

When activating a gift card as payment method in a live MultiSafepay Control, the payment method will be tested before release.

## Giropay / EPS

MultiSafepay provides a test platform for Giropay/EPS transactions. During the payment process you will be able to simulate the outcome of the transaction.

| BIC     | Status    | Description              |
| ------- | --------- | ------------------------ |
| Any BIC | Completed | Transaction is Completed |
| Any BIC | Declined  | Transaction is Declined |

Note: Giropay is a German payment method and can only be tested if the country code for Germany (DE) is sent in the pre-transaction request. For EPS, you can also use the Giropay gateway in TEST. In the LIVE environment EPS will display only when you use Austria (AT) as country code.

## iDEAL

MultiSafepay provides a test platform for iDEAL transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Status                | Description              |
| --------------------- | ------------------------ |
| Completed             | Transaction is Completed |
| Declined              | Transaction is Declined |
| Cancelled             | Transaction is Cancelled |
| Initialized/Completed | Transaction is Initialized (after 1 minute it is changed to Completed) |
| Initialized/Declined  | Transaction is Initialized (after 1 minute it is changed to Declined) |


## ING Home'Pay 

MultiSafepay provides a test platform for ING Home'Pay transactions. During the payment process you will be able to simulate the outcome of the transaction.

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled |


## KBC

The payment method KBC can only be processed on our new payment page starting with PayV2.

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is completed |
| Cancelled | Transaction is void / cancelled |

## Klarna

Klarna provides their own test credentials. For a complete guide, check out [Klarna's documentation](https://developers.klarna.com/en/gb/kco-v3/test-credentials)

## Maestro

MultiSafepay provides a test platform for Maestro transactions. The simulation is similar to the Visa test platform. For extensive testing please use the Visa test platform. By entering a test card number, you will be able to simulate the outcome of the transaction.

| Card number      | Status    | Description              |
| -----------------| --------- | ------------------------ |
| 6759000000005 | Completed | Transaction is Completed (3D enrolled)


## Mastercard

MultiSafepay provides a test platform for Mastercard transactions. The simulation is similar to the Visa test platform. For extensive testing please use the Visa test platform. By entering a test card number, you will be able to simulate the outcome of the transaction.


* CVC 123
* Select a date in the future for the expiry date

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 5500000000000004 | Completed | Transaction is Completed (not 3D enrolled) |

## Nexi
MultiSafepay provides the Visa test credentials to test the payment method Nexi.

Nexi is shown as a payment option on the payment page of MultiSafepay only after:

1. The Visa gateway is enabled; and
2. The locale is set to it_IT (Italy) in the transaction call received by MultiSafepay.

## Pay After Delivery (Betaal na Ontvangst)

MultiSafepay provides a test platform for Betaal na Ontvangst / Pay After Delivery transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Address               | Status    | Description              |
| ------------------ | --------- | ------------------------ |
| Kraanspoor 39C - 1033SC Amsterdam | Completed | Transaction is Completed |
| Vlierweg 12D - 1032LG Amsterdam | Declined | Transaction is Declined |


## PayPal

MultiSafepay provides a test platform for PayPal transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Declined | Transaction is Declined |
| Initialized / Completed | Payment blocked by PayPal (then accepted) |
| Initialized / Declined | Payment blocked by PayPal (then declined) |
| Cancelled | Transaction is Cancelled |


## Recurring payment

Contact us at <integration@multisafepay.com> to enable recurring payment in your MultiSafepay Test Control. [Full documentation on recurring payments](/tools/recurring-payments/)


## Santander Betaalplan

Currently no test data available for the payment method Santander.

When activating Santander Betaalplan as payment method in a live MultiSafepay Control, the payment method will be tested before release.

## SOFORT Banking

MultiSafepay provides a test platform for SOFORT Banking transactions. During the payment process you will be able to simulate the outcome of the transaction.

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled |

## Trustly 

MultiSafepay provides a test platform for Trustly transactions. During the payment process you will be able to simulate the outcome of the transaction.

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled |

## Visa

MultiSafepay provides a test platform for Visa transactions. By entering a test card number you will be able to simulate the outcome of the transaction.

* CVC 123
* Select a date in the future for the expiry date

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | Completed | Transaction is Completed (3D enrolled) |
| 4012001038443335 | Completed | Transaction is Completed (not 3D enrolled) |
| 4917300000000008 | Uncleared | Transaction is Uncleared (after 3 minutes it is changed to Void) |
| 4462000000000003 | Uncleared | Transaction is Uncleared (after 3 minutes it is changed to Completed) |
| 4012001037461114 | Declined  | Transaction is Declined (failed 3D authentication) |
| 4012001038488884 | Declined  | Transaction is Declined (3D authentication successful, but insufficient funds) |
