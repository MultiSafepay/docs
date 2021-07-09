---
title : "Test payment details"
weight: 14
meta_title: "FAQ Getting Started - Test payment details - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/getting-started/test-payment-details/
---

This page is for testing payment methods and scenarios in your [MultiSafepay test account](https://testMerchant.MultiSafepay.com/). It provides information about test credentials, sample statuses, possible errors, and valid payment pages. 

## Banks

{{< details title="Bancontact" >}}

Test card number: See the table below.

Possible errors: The test QR codes can only be read with a general QR code application. If you scan the code using the Bancontact app, an error occurs.

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

{{< /details >}}

{{< details title="Banktransfer" >}}

Test IBANs: See the table below.

Sample statuses:

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 1 minute, this changes to declined. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 1 minute, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 1 minute, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

{{< /details >}}

{{< details title="Belfius" >}}

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled 

{{< /details >}}

{{< details title="CBC" >}}

Payment page: CBC can only be processed on our new payment page starting with PayV2.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction is void / cancelled |

{{< /details >}}

{{< details title="Dotpay" >}}

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |

{{< /details >}}

{{< details title="Giropay/EPS" >}}

- Giropay is a German payment method. To test it, you must include the country code for Germany `DE` in the pre-transaction request. 
- For EPS, you can also use the Giropay gateway in your MultiSafepay test account. In your live MultiSafepay account, EPS only appears if you provide the country code for Austria `AT`.

Test credentials: You will need a test BIC.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined**  | Transaction was declined |

{{< /details >}}

{{< details title="iDEAL" >}}

Sample statuses:

| Status                | Description              |
| --------------------- | ------------------------ |
| **Completed**             | Transaction was completed |
| **Declined**              | Transaction was declined |
| **Cancelled**             | Transaction was cancelled |
| **Initialized**/ **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Initialized**/ **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

{{< /details >}}

{{< details title="iDEAL QR" >}}

You cannot test iDEAL QR in your MultiSafepay test account. You can only make test payments in your live MultiSafepay account.

{{< /details >}}

{{< details title="ING Home'Pay" >}}

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}

{{< details title="KBC" >}}

Payment page: KBC can only be processed on our new payment page starting with PayV2.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction is void / cancelled |

{{< /details >}}

{{< details title="Request to Pay" >}}

Testing environment: You can test Request to Pay transactions through Deutsche Bank. In the **Bank** field > **Fill-in Demo Bank**. 

Sample statuses:

| Status    | Testing instructions | Description              |
| --------- | ----------------------- | ----------------------- |
| **Completed** | Follow the steps from Deutsche Bank. | Transaction was completed |
| Canceled | Click the **Close** button at the top right of the screen. | Transaction was cancelled |

{{< /details >}}

{{< details title="Recurring payments" >}}

To enable [recurring payments](/tools/recurring-payments) in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com> 

{{< /details >}}

{{< details title="SEPA Direct Debit" >}}

Test IBANs: See the table below.

Sample statuses:

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

{{< /details >}}

{{< details title="SOFORT Banking" >}}

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}

{{< details title="Trustly" >}}

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}

{{< details title="TrustPay" >}}

It is not possible to test TrustPay payments.

{{< /details >}}

## Billing Suite

{{< details title="AfterPay" >}}

To enable AfterPay in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com>

To generate a test API key from AfterPay for authentication, create an AfterPay Sandbox account. See AfterPay - [Sign in](https://developer.afterpay.io/auth/login). 

The API key appears on the AfterPay **Account** page, which also specifies how long it is valid. The key is generated immediately, but you may need to refresh the page after a few seconds to display it. 

{{< /details >}}

{{< details title="Betaal per Maand" >}}

You cannot test Betaal per Maand in MultiSafepay test account. 

When activating Betaal per Maand as a payment method in your live MultiSafepay account, you can test it before going live.

{{< /details >}}

{{< details title="E-Invoicing" >}}

Test address: Kraanspoor 39C - 1033SC Amsterdam

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |

{{< /details >}}

{{< details title="in3" >}}

Test credentials: [API key](.com/tools/multisafepay-control/get-your-api-key/)

To test in3 transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay test account.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test account so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay account, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in in3.

You can also test in3 transactions by entering the following details on the in3 checkout page:
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |
| 01-01-2000 | 1111AB | 1 |

Sample statuses:

- **Approved**
- **Declined**

{{< /details >}}

{{< details title="Klarna" >}}

Test credentials:

- [API key](/tools/multisafepay-control/get-your-api-key/)
- [Klarna's test credentials](https://developers.klarna.com/en/gb/kco-v3/test-credentials)

To test Klarna transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay test account.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test account so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay account, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in Klarna.

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payment-methods/billing-suite/klarna).

{{< /details >}}

{{< details title="Pay After Delivery (Betaal na Ontvangst)" >}}

Test addresses:

- Kraanspoor 39C, 1033SC Amsterdam
- Vlierweg 12D, 1032LG Amsterdam

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |

{{< /details >}}

## Credit and debit cards

{{< details title="American Express" >}}

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

{{< /details >}}

{{< details title="Cartes Bancaires" >}}

Test credentials: MultiSafepay provides Visa test credentials to test Cartes Bancaires.

Payment page: Cartes Bancaires only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` parameter is set to `fr_FR` (France) in the transaction API request.

{{< /details >}}

{{< details title="Dankort" >}}

Test credentials: MultiSafepay provides Visa test credentials for Dankort.

Payment page: Dankort only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` is set to `da_DK` (Denmark) in the transaction request sent to MultiSafepay.

{{< /details >}}

{{< details title="Maestro" >}}

Testing Maestro is similar to Visa. For extensive testing, use Visa. 

Test card number: 6759000000005

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed (3D enrolled)|

{{< /details >}}

{{< details title="Mastercard" >}}

Testing Mastercard is similar to Visa. For extensive testing, use Visa. 

Test card details: 

- Card number: 5500000000000004
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed (3D enrolled)|

{{< /details >}}

{{< details title="Visa" >}}

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

{{< /details >}}

## Prepaid cards

{{< details title="Gift cards" >}}

**Intersolve gift cards**

You can only test gift cards that use the Intersolve connection. 

| Test coupon code     | Balance    |
| ------- | --------- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |

Any other coupon code receives an "Invalide card number" error.

**Other gift cards** 

Once activated in the backend of your ecommerce platform, to check the connection, make a small payment from a gift card. 

**Note:** This is a real payment and the amount is actually deducted from the gift card.

{{< /details >}}

{{< details title="Paysafecard" >}}

You cannot test Paysafecard.

For any questions, email the Integration Team at <integration@multisafepay.com>
{{< /details >}}


## Wallets

{{< details title="Apple Pay" >}}

To test Apple Pay, see [Compatibility and testing](/payment-methods/wallet/applepay/#compatibility-and-testing) to learn how to test on supported devices.

{{< /details >}}

{{< details title="Alipay" >}}

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}

{{< details title="PayPal" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

To test PayPal transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. Since MultiSafepay does not collect payments on behalf of PayPal, the financial (transaction) status remains **Initialized** and cannot be changed to **Completed**.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted |
| **Initialized**/ **Declined** | Payment blocked by PayPal, then declined |
| **Cancelled** | Transaction was cancelled |

{{< /details >}}

## Read more

{{< two-buttons href-2="/getting-started/test-your-integration" header-2="Read more" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/getting-started/test-your-integration/testing-refunds" header-2="Read more" text-2="Testing refunds" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}