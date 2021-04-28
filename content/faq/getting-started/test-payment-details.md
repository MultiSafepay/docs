---
title : "Test payment details"
weight: 8
meta_title: "FAQ Getting Started - Test payment details - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

Use the following test payment credentials when testing different payment scenarios in your [MultiSafepay Test Control](https://testMerchant.MultiSafepay.com/).

**Note:** You cannot process test refunds. 

## Banks

### AfterPay

To enable AfterPay in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com>

### Alipay
Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction was cancelled |

### American Express

#### Test credentials
You will need a test:

- Card number: See Sample statuses below
- CVC code: 123
- Expiry date in the future

#### Sample statuses

| Card number| Status    | Description              |
| --------- | --------- | ------------------------ |
| 378282246310005| Completed | Transaction was completed (not 3D enrolled) |
| 374200000000004| Declined  | Transaction was declined |
| 378734493671000| Uncleared | Transaction is uncleared. After 3 minutes, this changes to Void. |

### Apple Pay

To test Apple Pay, see [Compatibility and testing](/payment-methods/wallet/applepay/#compatibility-and-testing).

### Bancontact

#### Test credentials
You will need a test card number. See Sample statuses below.

#### Sample statuses

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | Completed | Transaction was completed (3D enrolled) |
| 67034500054610009| Declined  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| Declined  | Transaction was declined (3D authentication failed) |
| 67039902990000011| Declined  | Transaction was declined (3D authentication successful, but insufficient funds) |

#### Possible errors

The test QR codes can only be read with a general QR code application. If you scan the code using the Bancontact app, an error occurs.

### Banktransfer


#### Test credentials
You will need a test IBAN. See Sample statuses below.

#### Sample statuses

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000002| Initialized/Declined | Transaction is initialized. After 1 minute, this changes to declined. |
| NL87ABNA0000000003| Initialized/Uncleared/Completed | Transaction is initialized. After 1 minute, this changes to Uncelared. After 1 more minute, it changes to Completed. |
| NL87ABNA0000000004| Initialized/Uncleared/Declined | Transaction is initialized. After 1 minute, this changes to Uncleared. After 1 more minute, it changes to Declined. |

### Belfius

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled 


### CBC

CBC can only be processed on our new payment page starting with PayV2.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction wass completed |
| Cancelled | Transaction is void / cancelled |


### Dankort

MultiSafepay provides Visa test credentials for Dankort.

Dankort only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` is set to `da_DK` (Denmark) in the transaction request sent to MultiSafepay.

### Dotpay

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Declined | Transaction was declined |

### Giropay / EPS

- Giropay is a German payment method. To test it, you must include the country code for Germany `DE` in the pre-transaction request. 
- For EPS, you can also use the Giropay gateway in your MultiSafepay Test Control. In your live MultiSafepay Control, EPS only appears ifyou provide the Austria `AT` country code.

#### Test credentials
You will need a test BIC.

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Declined  | Transaction was declined |

### iDEAL

Sample statuses:

| Status                | Description              |
| --------------------- | ------------------------ |
| Completed             | Transaction was completed |
| Declined              | Transaction was declined |
| Cancelled             | Transaction was cancelled |
| Initialized/Completed | Transaction is initialized. After 1 minute, this changes to Completed. |
| Initialized/Declined  | Transaction is initialized. After 1 minute, this changes to Declined. |


### iDEAL QR

You cannot test the iDEAL QR payment method in your MultiSafepay Test Control. You can only place test payments in your live MultiSafepay Control.

### ING Home'Pay 

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction was cancelled |

### KBC

KBC can only be processed on our new payment page starting with PayV2.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction is void / cancelled |

### Request to Pay

You can test Request to Pay transactions though Deutsche Bank. In the **Bank** field, select **Demo Bank**. 
To get:

- **Completed_** status, follow the steps from Deutsche Bank.
- **Canceled** status, click the **Close** button at the top right of the screen.

#### Sample statuses  

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Canceled | Transaction was canceled |


### Recurring payments

To enable [recurring payments](/tools/recurring-payments) in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com> 

### SEPA Direct Debit

#### Test credentials
You will need a test IBAN. See Sample statuses below.

#### Sample statuses

| IBAN | Status    | Description              |
|| --------- | ------------------------ |
| NL87ABNA0000000001| Initialized/Completed | Transaction is initialized. After 2 minutes, this changes to Completed. |
| NL87ABNA0000000002| Initialized/Declined | Transaction is initialized. After 2 minutes, this changes to Declined. |
| NL87ABNA0000000003| Initialized/Uncleared/Completed | Transaction is initialized. After 2 minutes, this changes to Uncleared. After 1 more minute, it changes to Completed. |
| NL87ABNA0000000004| Initialized/Uncleared/Declined | Transaction is initialized. After 2 minutes, this changes to Uncleared. After 1 more minute, it changes to Declined. |

### SOFORT Banking

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction was cancelled |

### Trustly 

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction was cancelled |

## Billing suites

### AfterPay

To enable AfterPay as payment method in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com>

### Betaal per Maand

You cannot test Betaal per Maand in MultiSafepay Test Control. 

When activating Betaal per Maand as payment method in your live MultiSafepay Control, you can test it before go live.

### E-invoicing

#### Test credentials
You will need a test address: Kraanspoor 39C - 1033SC Amsterdam

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |

### in3

#### Test credentials
You will need a test [API key](.com/tools/multisafepay-control/get-your-api-key/).

To test in3, follow these steps:

1. Place a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in the live control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in in3.

You can also test in3 transactions by entering the following details on the in3 checkout page:
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |
| 01-01-2000 | 1111AB | 1 |


#### Sample statuses

| Status            | 
| ---------------- | 
| Approved             | 
| Declined              |

### Klarna

#### Test credentials 
You will need:

- An [API key](/tools/multisafepay-control/get-your-api-key/)
- [Klarna's test credentials](https://developers.klarna.com/en/gb/kco-v3/test-credentials)

To test Klarna, follow these steps:

1. Place a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in the live control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in Klarna.

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payment-methods/billing-suite/klarna).


## Debit and credit cards

### American Express

#### Test credentials
You will need a test:

- Card number: See Sample statuses below.
- CVC code: 123
- Expiry date in the future

#### Sample statuses

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 378282246310005| Completed | Transaction is Completed (not 3D enrolled) |
| 374200000000004| Declined  | Transaction is Declined |
| 378734493671000| Uncleared | Transaction is Uncleared (after 3 minutes it is changed to Void) |

### Cartes Bancaires

MultiSafepay provides Visa test credentials to test Cartes Bancaires.

Cartes Bancaires only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` parameter is set to `fr_FR` (France) in the transaction API request.


### Maestro

Testing Maestro is similar to Visa. For extensive testing, use Visa. 

#### Test credentials
You will need a test card number: 6759000000005

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed (3D enrolled)|


### Mastercard

Testing Mastercard is similar to Visa. For extensive testing, use Visa. 

#### Test credentials
You will need a test:

- Card number: 5500000000000004
- CVC code: 123
- Expiry date in the future

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed (3D enrolled)|


### Pay After Delivery (Betaal na Ontvangst)

#### Test credentials
You will need test addresses:

- Kraanspoor 39C - 1033SC Amsterdam
- Vlierweg 12D - 1032LG Amsterdam

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Declined | Transaction was declined |

### Visa

#### Test credentials
You will need a test: 

- Card number: See Sample statuses below
- CVC code: 123
* Expiry date in the future

#### Sample statuses

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | Completed | Transaction was completed (3D enrolled) |
| 4012001038443335 | Completed | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | Uncleared | Transaction is Uncleared. After 3 minutes, this changes to Void. |
| 4462000000000003 | Uncleared | Transaction is Uncleared. After 3 minutes, this changes to Completed. |
| 4012001037461114 | Declined  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | Declined  | Transaction was declined (3D authentication was successful, but insufficient funds) |

## Wallets

### Apple Pay

To test Apple Pay, first read [Compatibility and testing](/payment-methods/wallet/applepay/#compatibility-and-testing) to learn how to test on supported devices.

### Alipay

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Cancelled | Transaction was cancelled |

### PayPal

#### Test credentials
You will need an [API key](/tools/multisafepay-control/get-your-api-key/).

To test PayPal transactions, follow these steps:

1. Place a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in MultiSafepay Test Control as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. Since MultiSafepay does not collect payments on behalf of PayPal, the financial (transaction) status remains **Initialized** and cannot be changed to **Completed**.

#### Sample statuses

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction was completed |
| Declined | Transaction was declined |
| Initialized / Completed | Payment blocked by PayPal, then accepted |
| Initialized / Declined | Payment blocked by PayPal, then declined |
| Cancelled | Transaction was cancelled |


## Prepaid cards

### Gift cards

You can test Intersolve gift cards. 

When activating a gift card as payment method in your live MultiSafepay Control, you can test it before go live.

#### Test credentials

| Balance     | Coupon code    |
| ------- | --------- |
| € 100 | 111115 |
| € 5 | 111112  |
| No balance | 111110  |


#### Possible errors
Any other card number receives the error **Invalid card number**.

### Paysafecard

You cannot test Paysafecard.

For any questions, email the Integration Team at <integration@multisafepay.com>
