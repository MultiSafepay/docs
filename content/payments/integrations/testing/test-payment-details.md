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

{{< details title="Bank Transfer" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Bank Transfer order**

1. To test a Bank Transfer order, send a [redirect](/api/#bank-transfer---redirect) API request.
2. Open the payment link. 
3. In the **Your bank account** field, enter an IBAN. 
4. From the **Bank's country** list, select a country, and then click **Confirm**.

Use the following IBANs to test different transaction statuses.

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Expired** | Transaction is initialized. After 2 minutes, this changes to **Expired**. |
| NL87ABNA0000000004| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| Any other IBAN | **Initialized**/ **Expired** | Transaction is initialized. After 5 days, this changes to **Expired**. |

**Test cancelling an order**

To test cancelling an order, either:

- Send an [update an order](/api/#update-an-order) API request with status **Cancelled**, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Cancel**.  
The transaction status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order using IBAN: NL87ABNA0000000001. 
2. Wait until the transaction status changes to **Completed**.
3. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
5. In the **IBAN** field, enter the IBAN of the account you want to refund to.
6. In the **Reason/Description** field, enter a reason for the refund. 
7. In the **Amount** field, enter the amount to refund, and then click **Continue**.
8. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
9. Under **Related transactions**, select the **ID** of the refund order.
10. Under **Order summary**, click **Accept**.
11. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** You can't test the following:
- Sending a refund API request
- Sending a direct API request with an IBAN to test different transaction statuses

{{< /details >}}

{{< details title="Belfius" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Belfius order**

1. To test a Belfius order, send a [direct](/api/#belfius---direct) or [redirect](/api/#belfius---redirect) API request.
2. On the Test platform page, from the **Test Scenario** list, select **Completed**, and then click **Test**.  
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling an order. 
- You can't test sending a refund API request.
- In the live environment you can't accept a refund order. This is done automatically.

{{< /details >}}

{{< details title="CBC" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a CBC order**

1. To test a CBC order, send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test Scenario** list, select **Completed**, and then click **Test**.  
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling an order. 
- You can't test sending a refund API request.
- In the live environment you can't accept a refund order. This is done automatically.

{{< /details >}}

{{< details title="Dotpay" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Dotpay order**

1. To test a Dotpay order, send a [redirect](/api/#dotpay) API request.
2. On the Dotpay page, in the **E-mail address** field, enter any email address.
3. In the **Phone number** field, enter any phone number.
4. Select a bank.  
  You are automatically redirected.
5. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.
6. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

---

**Note:** You may see more banks available in the live environment.

---

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling an order. 
- You can't test sending a refund API request.
- In the live environment you can't accept a refund order. This is done automatically.

{{< /details >}}

{{< details title="EPS" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test an EPS order**

1. To test an EPS order, send a [redirect](/api/#eps) API request.
2. On the EPS page, in the **BIC** field, enter any BIC code. For example, `RZOOAT2L420`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#eps) API request.
2. On the EPS page, in the **BIC** field, enter any BIC code. For example, `RZOOAT2L420`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**, and then click **Test**.  
  The transaction status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test refunding an order with an API request**

To test refunding an order with an API request:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- In the live environment you can't accept a refund order. This is done automatically.
- In the live environment, EPS only appears if you set `customer.locale` for Austria `at_AT` in your API request.

{{< /details >}}

{{< details title="Giropay" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Giropay order**

1. To test a Giropay order, send a [redirect](/api/#giropay) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code. For example, `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#eps) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code. For example, `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**, and then click **Test**.  
  The transaction status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test refunding an order with an API request**

To test refunding an order with an API request:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- In the live environment you can't accept a refund order. This is done automatically.
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

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a KBC order**

1. To test a KBC order, send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test Scenario** list, select **Completed**, and then click **Test**.  
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling an order. 
- You can't test sending a refund API request.
- In the live environment you can't accept a refund order. This is done automatically.

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

AfterPay shares the test AfterPay API key with MultiSafepay so that MultiSafepay can configure this for you.

**Test an AfterPay order**

1. Send a [direct or redirect](/api/#afterpay) API request. For more information, see [Difference between direct and redirect API requests](/developer/api/difference-between-direct-and-redirect).
2. If you send a redirect API request, select the checkbox at the bottom of the AfterPay page, and then click **Confirm**.
3. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**. The transaction and order statuses change to **Void**.

**Test AfterPay rejecting an order**  

To test AfterPay rejecting an order, in your direct or redirect API request, use the following email address: <rejection@afterpay.nl>

The transaction and order statuses change to **Declined**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Send an [update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

---

**Note:** You can't test:  

- Receiving a successful payment notification from AfterPay
- Changing the transaction status from **Uncleared** to **Completed**
- Processing a refund

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
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna order**  
1. Send a [direct or redirect](/api/#klarna) API request. For more information, see [Difference between direct and redirect API requests](/developer/api/difference-between-direct-and-redirect).
2. On the Klarna page, click **Kopen**.
3. In the **Telefoonnummer** field, enter any mobile number, and then click **Ga verder**.
4. In the **Verificatiecode** field, enter any 6-digit number, and then click **Bevestigen**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**. The transaction and order statuses change to **Void**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Send an [update an order](/api/#update-an-order) API request, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

**Test refunding an order**

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or send a [refund with shopping cart](/api/#refund-with-shopping-cart) API request.  
  The transaction status changes to **Completed**.

**Receive an invoice**  

You can only test the invoice process in your live MultiSafepay account. To do this, change the order status to **Shipped**.

---

**Note:** You can't test:

- Receiving a successful payment notification from Klarna
- Changing the transaction status from **Uncleared** to **Completed**, except for refunds

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payments/methods/billing-suite/klarna).
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

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant order status.

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