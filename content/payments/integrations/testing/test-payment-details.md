---
title : "Test payment details"
weight: 20
meta_title: "Testing - Test payment details - MultiSafepay Docs"

read_more: "."
url: '/testing/test-payment-details/'
aliases:
    - /faq/getting-started/test-payment-details/
    - /getting-started/test-your-integration/test-payment-details
---

This page is for testing payment methods and scenarios in your [MultiSafepay test account](https://testMerchant.MultiSafepay.com/). It provides information about test credentials, sample statuses, possible errors, and valid payment pages. 

## Banking methods

{{< details title="Bancontact" >}}

Test card number: See the table below.

Test card expiry date: Any future date is accepted.

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

CBC doesn't support deprecated payment pages. See [MultiSafepay payment pages](/payment-pages/).

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

KBC doesn't support deprecated payment pages. See [MultiSafepay payment pages](/payment-pages/).

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

To enable [recurring payments](/features/recurring-payments/) in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com> 

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

{{< details title="Sofort" >}}

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

To get a test AfterPay API key, you can either:

- Request one in your implementation ticket with AfterPay, or
- Email <sales@afterpay.nl> 

To force and test a rejected order, use the following email address: <rejection@afterpay.nl>  

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

1. Send a [Direct or redirect](/developer/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with [order status](/payments/multisafepay-statuses/) **Completed**, and [transaction status](/payments/multisafepay-statuses/) **Uncleared**.
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

1. Send a [Direct or redirect](/developer/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay test account.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test account so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay account, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in Klarna.

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payment-methods/klarna).

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

Once activated in your [backend](/getting-started/glossary/#backend), to check the connection, make a small payment from a gift card. 

**Note:** This is a real payment and the amount is actually deducted from the gift card.

{{< /details >}}

{{< details title="Paysafecard" >}}

You cannot test Paysafecard.

For any questions, email the Integration Team at <integration@multisafepay.com>
{{< /details >}}


## Wallets

{{< details title="Apple Pay" >}}

To test Apple Pay, see [Compatibility and testing](/payments/methods/wallet/applepay/#compatibility-and-testing) to learn how to test on supported devices.

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

**Test a PayPal order**

1. Send a [direct](/api/#paypal---direct) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

---

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

---

**Change the order status**

You can change the order status to:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Order was completed |
| **Declined** | Order was declined |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted |
| **Initialized**/ **Declined** | Payment blocked by PayPal, then declined |
| **Cancelled** | Order was cancelled |

To change the order status, on the Test platform page, in the **Test scenario** list, select the relevant order status.

**Test refunding an order**

To refund an order:

1. In your test account, under **Order summary**, click **Refund order**.
2. Under **Refund**, in the **Reason/Description** field, enter a reason for the refund. 
3. In the **Amount** field, enter the amount to refund, and then click **Continue**.
4. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
5. Under **Related transactions**, select the **ID** of the refund order.
6. Under **Order summary**, click **Accept**.
7. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

Alternatively, send a [Refund](/api/#refund-an-order) API request.

---

**Note**: You can't test sending a redirect API request.

{{< /details >}}

## Read more

{{< two-buttons href-2="/getting-started/test-your-integration" header-2="Read more" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/getting-started/test-your-integration/testing-refunds" header-2="Read more" text-2="Testing refunds" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}