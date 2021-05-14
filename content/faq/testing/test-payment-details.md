---
title : "Test payment details"
meta_title: "Testing - Test payment details - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

To test payment methods with your ecommerce integration or custom-built integration, test payment details can be entered on the checkout page to simulate a transaction. Alternativley, some payment methods require you select test scenarios from a list.

The test payment details and scenarios can only be tested in the [MultiSafepay Test Control](https://testmerchant.multisafepay.com/). If you do not have an account yet, see [Onboarding](/guides/getting-started/#step-1-create-a-test-account)

{{< alert-notice >}} Outgoing payments and additional payment methods (e.g. American Express) are disabled by default in a MultiSafepay Test Control. As a result, a refund cannot be processed successfully. Contact our Integration Team at <integration@multisafepay.com> to enable outgoing payments or additional payment methods in your MultiSafepay Test Control. {{< /alert-notice >}} 

This page assumes you have followed the steps on [Getting started](/guides/getting-started) and are ready to test different payment methods and scenarios in your [MultiSafepay Test Control](https://testMerchant.MultiSafepay.com/).

It provides information about test credentials, sample statuses, possible errors, and valid payment pages.

**Note:** By default, you cannot process test refunds. To enable outgoing payments, email the Integration Team at <integration@multisafepay.com>  


## Banks

### Bancontact

MultiSafepay provides test details for Bancontact transactions. To simulate the outcome of a transaction, enter:

* A test card number
* Any expiry date in the future

Possible errors: The test QR codes can only be read with a general QR code application. If you scan the code using the Bancontact app, an error occurs.

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

MultiSafepay provides a test details for Bank transfer transactions. To simulate the outcome of a transaction, enter:

* A test IBAN number

| IBAN               | Status    | Description              |
| ------------------ | --------- | ------------------------ |
| NL87ABNA0000000001 | Initialized/Completed | Transaction is Initialized/Initialized (after 1 minute it is Completed) |
| NL87ABNA0000000002 | Initialized/Expired/Completed | Transaction is Initialized (after 1 minute it is Expired, and 1 minute later it is Completed) |
| NL87ABNA0000000003 | Initialized/Expired | Transaction is Initialized (after 1 minute it is Expired) |
| NL87ABNA0000000004 | Initialized/Declined | Transaction is Initialized (after 1 minute it is Declined) |

### Belfius


 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Cancelled (Order status will first be Void) 


### CBC

The payment method CBC can only be processed on our new payment page starting with [PayV2](/tools/payment-pages/difference-between-v1-and-v2/).

MultiSafepay provides test scenarios for Belfius transactions. To simulate the outcome of a transaction, select one of the following statuses:

| Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Cancelled | Transaction is Void / Cancelled |


### Dankort

MultiSafepay provides [Visa test credentials](/faq/getting-started/test-payment-details/#visa) to test the payment method Dankort.

Dankort is shown as a payment option on the payment page of MultiSafepay only after:

1. The Visa gateway is enabled; and
2. The locale is set to da_DK (Denmark) in the transaction call received by MultiSafepay.

Contact our Integration Team at <integration@multisafepay.com> to enable the Visa gateway.

### Dotpay

MultiSafepay provides test scenarios for Dotpay transactions. To simulate the outcome of a transaction, select one of the following statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |

### Giropay / EPS

MultiSafepay provides a testing environment for Giropay/EPS transactions. To simulate the outcome of a transaction, enter the following:

* Any BIC

Test credentials: You will need a test BIC.

Note: Giropay is a German payment method and can only be tested if the country code for Germany (DE) is sent in the pre-transaction request. For EPS, you can also use the Giropay gateway in test environment. In the live environment, EPS will display only when you use Austria (AT) as country code.

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined**  | Transaction was declined |

### iDEAL

MultiSafepay provides test scenarios for iDEAL transactions. To simulate the outcome of a transaction, select one of the following scenarios:

| Status                | Description              |
| --------------------- | ------------------------ |
| **Completed**             | Transaction was completed |
| **Declined**              | Transaction was declined |
| **Cancelled**             | Transaction was cancelled |
| **Initialized**/ **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Initialized**/ **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

### iDEAL QR

You cannot test iDEAL QR in your MultiSafepay Test Control. You can only make test payments in your live MultiSafepay Control.

### ING Home'Pay 

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

### KBC

Payment page: KBC can only be processed on our new payment page starting with PayV2.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction is void / cancelled |

### Request to Pay

MultiSafepay provides a test platform for Request to Pay transactions through Deutsche Bank.

You can simulate the following scenarios:  

Sample statuses:

Select 'Demo Bank' in the Bank field and go through the steps with the information provided in the description in order to get a _Completed_ status.

In order to get a _Cancel_ status you need to click on the _Close_ button at the top right of the screen.


### Recurring payments

To enable [recurring payments](/tools/recurring-payments) in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com> 

### SEPA Direct Debit

Test IBANs: See the table below.

Sample statuses:

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

### SOFORT Banking

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

### Trustly 

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

## Billing suites

### AfterPay

To enable AfterPay in your MultiSafepay Test Control, email the Integration Team at <integration@multisafepay.com>

### Betaal per Maand

MultiSafepay provides a test platform for Betaal per Maand transactions. During the payment process you will be able to simulate the outcome of the transaction.

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed (Order status will first go to Uncleared) |
| Declined | Transaction is Declined (Order status will first go to Uncleared) |

### E-invoicing

MultiSafepay provides a test platform for E-invoicing transactions. During the payment process you will be able to simulate the outcome of the transaction.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |

### in3

MultiSafepay provides a test platform for in3 transactions. To simulate the outcome of a transaction, select one of the following scenarios in the test environment:

 Status    | Description              |
| --------- | ------------------------ |
| Completed | Transaction is Completed |
| Declined | Transaction is Declined |
| Open Completed | Transaction remains initialized until the Bank provides a final completed status. (after 1 minute) |
| Open Declined | Transaction remains initialized until the Bank provides a final declined status. (after 1 minute) |
| Cancelled | Transaction is Cancelled |

### Klarna

Test credentials:

- [API key](/tools/multisafepay-control/get-your-api-key/)
- [Klarna's test credentials](https://developers.klarna.com/en/gb/kco-v3/test-credentials)

To test Klarna transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay Control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in Klarna.

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payment-methods/billing-suite/klarna).

### Pay After Delivery (Betaal na Ontvangst)

Test addresses:

- Kraanspoor 39C, 1033SC Amsterdam
- Vlierweg 12D, 1032LG Amsterdam

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |

## Debit and credit cards

### American Express

Test card details:

- Card number: See the table below.
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 378282246310005| **Completed** | Transaction was completed (not 3D enrolled) |
| 374200000000004| **Declined**  | Transaction was declined |
| 378734493671000| **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |

### Cartes Bancaires

Test credentials: MultiSafepay provides Visa test credentials to test Cartes Bancaires.

Payment page: Cartes Bancaires only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` parameter is set to `fr_FR` (France) in the transaction API request.

### Dankort

Test credentials: MultiSafepay provides Visa test credentials for Dankort.

Payment page: Dankort only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` is set to `da_DK` (Denmark) in the transaction request sent to MultiSafepay.

### Maestro

Testing Maestro is similar to Visa. For extensive testing, use Visa. 

Test card number: 6759000000005

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed (3D enrolled)|


### Mastercard

Testing Mastercard is similar to Visa. For extensive testing, use Visa. 

Test card details: 

- Card number: 5500000000000004
- CVC code: 123
- Expiry date in the future

MultiSafepay provides a test platform for Betaal na Ontvangst / Pay After Delivery transactions. During the payment process you will be able to simulate the outcome of the transaction by filling in the following information:

* Any random date of birth
* Any random bank account number (do not enter your own bank account number)
* Any random Email address
* Any random phone 

### Visa

Test card details: 

- Card number: See the table below.
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

## Wallets

### Apple Pay

To test Apple Pay, see [Compatibility and testing](/payment-methods/wallet/applepay/#compatibility-and-testing) to learn how to test on supported devices.

### Alipay

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

### PayPal

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

To test PayPal transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in MultiSafepay Test Control as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. Since MultiSafepay does not collect payments on behalf of PayPal, the financial (transaction) status remains **Initialized** and cannot be changed to **Completed**.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted |
| **Initialized**/ **Declined** | Payment blocked by PayPal, then declined |
| **Cancelled** | Transaction was cancelled |


## Prepaid cards

### Gift cards

You can test Intersolve gift cards. 

Testing environment: When activating a gift card as a payment method in your live MultiSafepay Control, you can test it before going live.

Possible errors: Any other coupon code receives the error **Invalid card number**.

Test coupon codes:

| Coupon code     | Balance    |
| ------- | --------- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |

### Paysafecard

You cannot test Paysafecard.

For any questions, email the Integration Team at <integration@multisafepay.com>
