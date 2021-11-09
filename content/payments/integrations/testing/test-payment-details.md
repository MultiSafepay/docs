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

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Bancontact order**

1. To test a Bancontact order, send a [redirect](/api/#bancontact) API request.
2. Open the payment link.
3. In the **Card number** field, enter a 16-digit card number.
4. In the **Expiry date** fields, enter any future date, and then click **Confirm**.

Use the following card numbers to test different transaction statuses.

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

---

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

---

**Test a Bancontact QR code**
1. Send a [redirect](/api/#bancontact-qr) API request.
2. Open the payment link.
3. Scan the QR code with a general QR reader (**not** the Bancontact app - an error occurs).
4. On the Test platform page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.

**Test refunding an order**

To test refunding an order:

1. Create an order using card number `67034500054620008`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order using card number `67034500054620008`. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling orders. 
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Bank Transfer" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

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

To test cancelling an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Cancel**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order using IBAN: NL87ABNA0000000001. 
2. Wait until the transaction status changes to **Completed**.
3. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test:
  - Refunding via the API
  - Sending direct API requests with an IBAN to test different transaction statuses
- In the live environment, you can't accept refund orders. These are done automatically.
{{< /details >}}

{{< details title="Belfius" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Belfius order**

1. To test a Belfius order, send a [direct](/api/#belfius---direct) or [redirect](/api/#belfius---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#belfius---direct) or [redirect](/api/#belfius---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="CBC" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a CBC order**

1. To test a CBC order, send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Dotpay" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Dotpay order**

1. To test a Dotpay order, send a [redirect](/api/#dotpay) API request.
2. On the Dotpay page, enter in the:
    - **E-mail address** field: Any email address
    - **Phone number** field: Any phone number
3. Select a bank.  
  You are automatically redirected.
4. On the Test platform page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

---

**Note:** You may see more banks available in the live environment.

---

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#dotpay) API request.
2. On the Dotpay page, enter in the:
    - **E-mail address** field: Any email address
    - **Phone number** field: Any phone number
3. Select a bank.  
  You are automatically redirected.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
5. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="EPS" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an EPS order**

1. To test an EPS order, send a [redirect](/api/#eps) API request with the `locale` set to `at_AT`.
2. On the EPS page, in the **BIC** field, enter any BIC code, e.g. `RZOOAT2L420`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#eps) API request with the `locale` set to `at_AT`.
2. On the EPS page, in the **BIC** field, enter any BIC code, e.g. `RZOOAT2L420`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**. 
5. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Giropay" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Giropay order**

1. To test a Giropay order, send a [redirect](/api/#giropay) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code, e.g. `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#eps) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code, e.g. `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
5. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.
{{< /details >}}

{{< details title="iDEAL" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an iDEAL order**

1. To test an iDEAL order, send a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you send a redirect API request, select a bank.
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you send a redirect API request, select a bank. 
3. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
4. Click **Test**.  
  The order status changes to **Void**.

Use the following test scenarios on the Test platform page to test different transaction statuses.

| Status                | Description              |
| --------------------- | ------------------------ |
| **Declined**              | Transaction was declined |
| **Open** **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Open** **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="iDEAL QR" >}}

You can't test iDEAL QR in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

{{< /details >}}

{{< details title="ING Home'Pay" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an ING Home'Pay order**

1. To test an ING Home'Pay order, send a [direct](/api/#ing-homepay---direct) or [redirect](/api/#ing-homepay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test declining an order**

To test declining an order:

1. Send a [direct](/api/#ing-homepay---direct) or [redirect](/api/#ing-homepay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The transaction status changes to **Declined**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test:
  - Cancelling orders
  - Refunding via the API
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="KBC" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a KBC order**

1. To test a KBC order, send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Request to Pay" >}}

You can't test Request to Pay in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

{{< /details >}}

{{< details title="Recurring payments" >}}

To enable [recurring payments](/features/recurring-payments/) in your MultiSafepay test account, email the Integration Team at <integration@multisafepay.com> 

{{< /details >}}

{{< details title="SEPA Direct Debit" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a SEPA Direct Debit order**

1. To test a SEPA Direct Debit order, send a [direct](/api/#sepa-direct-debit---direct) or [redirect](/api/#sepa-direct-debit---redirect) API request.
2. If you send a redirect API request, enter in the:
    - **Account holder** field the account holder name.
    - **IBAN** field the IBAN.
4. Click **Confirm**.

Use the following IBANs to test different transaction statuses.

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

**Test refunding an order**

To test refunding an order:

1. Create an order with IBAN `NL87ABNA0000000001`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order with IBAN `NL87ABNA0000000001`. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling orders.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Sofort" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Sofort order**

1. To test a Sofort order, send a [direct](/api/#sofort---direct) or [redirect](/api/#sofort---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#sofort---direct) or [redirect](/api/#sofort---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Trustly" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Trustly order**

1. To test a Trustly order, send a [direct](/api/#trustly---direct) or [redirect](/api/#trustly---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#trustly---direct) or [redirect](/api/#trustly---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- In the live environment, you can't accept refund orders. These are done automatically.
- You can't test Trustly declining transactions.

{{< /details >}}

{{< details title="TrustPay" >}}

You can't test TrustPay in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

{{< /details >}}

## Pay later methods

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

- Receiving successful payment notifications from AfterPay
- Changing transaction statuses from **Uncleared** to **Completed**
- Processing refunds

{{< /details >}}

{{< details title="Betaal per Maand" >}}

You can't test Betaal per Maand in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

{{< /details >}}

{{< details title="E-Invoicing" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an E-Invoicing order**

To test an E-Invoicing order, send a [direct](/api/#e-invoicing---direct) or [redirect](/api/#e-invoicing---redirect) API request.  
The payment is processed in the test environment as **Successful**, with order and transaction statuses **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#e-invoicing---direct) API request.
2. Either:
    - Send an [update an order](/api/#update-an-order) API request with status `"cancelled"`, or 
    - In your MultiSafepay test account, go to **Order summary**, click **Order status**.
    - From **Change status to**, select **cancelled**, in the **memo** field enter a reason, and then click **Ok**.  
  The transaction status changes to **Void** and the order status changes to **Cancelled**.

**Test shipping an order**  

To test shipping an order, send an [update an order](/api/#update-an-order) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

---

**Note:** You can't test processing refunds.

{{< /details >}}

{{< details title="in3" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an in3 order**

1. To test an in3 order, send a [direct](/api/#in3---direct) or [redirect](/api/#in3---redirect) API request with the following customer details.
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |

- If you send a redirect API request, enter in the:
    - **Birthdate** field `01-01-1999`.
    - **Phone number** field any phone number.  
  Select your title, and then click **Confirm**.
2. Select the checkbox confirming that you accept in3's payment terms and privacy statement, and then click **Afronden**.
3. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**. 
4. On the in3 page, click **Terug naar webshop**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test in3 declining an order**  

To test in3 declining an order, send a [direct](/api/#in3---direct) or [redirect](/api/#in3---redirect) API request with the following customer details:

| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-2000 | 1111AB | 1 |

The transaction and order statuses change to **Declined**.

**Test shipping an order**  
To test shipping an order, either:

- Send an [update an order](/api/#update-an-order) API request with status `shipped`, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Order status**.

**Receive an invoice**  

You can only test the invoice process in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. Change the order status to `shipped`.
3. Click **Refund complete order** and then click **Save item changes**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Change the order status to `shipped`.
3. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

---

**Note:** 
You can't test cancelling orders.

{{< /details >}}

{{< details title="Klarna" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna order**  
1. Send a [direct](/api/#klarna) API request. 
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

You can only test the invoice process in your MultiSafepay live account. To do this, change the order status to **Shipped**.

---

**Note:** You can't test:

- Receiving successful payment notifications from Klarna
- Changing transaction statuses from **Uncleared** to **Completed**, except for refunds
- Sending redirect API requests

For more information about integrating Klarna with MultiSafepay, see Payment methods – [Klarna](/payments/methods/billing-suite/klarna).
{{< /details >}}

{{< details title="Pay After Delivery (Betaal na Ontvangst)" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Pay After Delivery order**

1. To test a Pay After Delivery order, send a [direct](api/#pay-after-delivery---direct) or [redirect](api/#pay-after-delivery---redirect) API request.
2. If you send a redirect API request, click **Pay After Delivery**.
3. Enter in the:
    - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
    - **Bank account** field any bank account number.
    - **E-mail address** field any email address.
    - **Phone number** field any phone number.
4. Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**. The transaction and order statuses change to **Void**.

**Test cancelling an order**

To test cancelling an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, click **Order status**.
3. From **Change status to**, select **cancelled**, in the **memo** field enter a reason, and then click **Ok**.  
  The transaction status changes to **Void** and the order status changes to **Cancelled**.

---

**Note:** 
You can't test:  
  - Processing refunds
  - Changing the statuses of orders to shipped

{{< /details >}}

## Credit and debit cards

{{< details title="Cartes Bancaires / Dankort / V Pay" >}}
You can test the following cards using the Visa test instructions. To display these cards on MultiSafepay payment pages, you must set the `locale` parameter in the redirect API request to a specific locale.

| Card             | `locale` |
|------------------|----------|
| Cartes Bancaires | `fr_FR`  |
| Dankort          | `da_DK`  |
| V Pay            | `it_IT`  |

{{< /details >}}

{{< details title="Visa" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a VISA order**  

1. Send a [redirect](/api/#visa) API request.
2. On the payment page:
    - In the **Card number** field, enter `4111111111111111`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

---

**Note:** 
- You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.
- You can't test cancelling orders. 

{{< /details >}}

{{< details title="Maestro" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

Testing Maestro is similar to Visa. For extensive testing, see [Visa](#details-visa). 

**Test a Maestro order**  

1. Send a [redirect](/api/#maestro) API request.
2. On the payment page:
    - In the **Card number** field, enter `6759000000005`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Mastercard" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

Testing Mastercard is similar to Visa. For extensive testing, see [Visa](#details-visa). 

**Test a Mastercard order**  

1. Send a [redirect](/api/#mastercard) API request.
2. On the payment page:
    - In the **Card number** field, enter `5500000000000004`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**. 
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="American Express" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an American Express order**  

1. Send a [redirect](/api/#american-express) API request.
2. On the payment page:
    - In the **Card number** field, enter `378282246310005`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 374200000000004| **Declined**  | Transaction was declined |
| 378734493671000| **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |

{{< /details >}}

{{< details title="Refunding credit and debit card orders" >}}
**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

## Prepaid cards

{{< details title="Edenred" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an Edenred order**

1. Send a [redirect](/api/#edenred) API request.
2. On the payment page, click **Add discount**.
3. From the **Test scenario** list, select the relevant discount, and then click **Test**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Gift cards" >}}

You can test the following gift cards:

- Beauty Cadeau
- Boeken Voordeel
- Huis & Tuin Cadeau
- Klus Cadeau
- Nationale Bioscoopbon
- VVV Cadeaukaart
- Wijn Cadeaukaart

**Test a gift card order**

Test credentials: [API key](/account/site-id-api-key-secure-code/)

1. Send a [redirect](/api/#gift-cards) API request.
2. On the payment page:
    - In the **Card number** field, enter `111115`.
    - In the **Security code** field, enter any 4-digit number.
    - Click **Add discount**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different gift card balances.

| Card numbers     | Balance    |
| ------- | --------- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |

Any other card number receives an "Invalid card number" error.

**Other gift cards** 

You can't test other gift cards in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. You make a small payment and the amount is actually deducted from the gift card.

{{< /details >}}

{{< details title="Paysafecard" >}}

You can't test Paysafecard in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

For any questions, email the Integration Team at <integration@multisafepay.com>
{{< /details >}}

{{< details title="Postepay" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Postepay order**  
1. Send a [redirect](/api/#postepay) API request with the `locale` set to `it_IT`.
2. On the payment page:
    - In the **Numero carta** field, enter `4111111111111111`.
    - In the **Titolare carta** field, enter any name.
    - From the **Data di scadenza** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Conferma**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

---

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

---

**Test refunding an order**

To test refunding an order:

1. Create an order using card number `4012001038443335`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order using card number `4012001038443335`. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.
---

**Note:**

- You can't test cancelling orders. 
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

## Wallets

{{< details title="Alipay" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

**Test an Alipay order**

1. Send a [direct](/api/#alipay---direct) or [redirect](/api/#alipay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#alipay---direct) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Initialized**.
4. In your MultiSafepay test account, under **Order summary**, click **Cancel**.
5. In the **Add transaction comment** field, add a comment, and then click **Ok**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note**:  

- You can't test:
    - Refunding via the API.
    - Alipay declining transactions.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="Apple Pay" >}}

To test Apple Pay, see [Testing](/payment-methods/apple-pay/integration-testing/#testing) to learn how to test on supported devices.

{{< /details >}}

{{< details title="Google Pay" >}}

To test Google Pay, see [Testing](/payment-methods/google-pay/integration-testing/#testing).

{{< /details >}}

{{< details title="PayPal" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

**Test a PayPal order**

1. Send a [direct](/api/#paypal---direct) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

---

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

---

**Change the order status**

You can change the order status to:

| Status    | Description              | Test scenario     |
| --------- | ------------------------ | ----------------- |
| **Completed** | Order was completed | Completed  |
| **Void** | Order was cancelled | Cancelled  |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted after 2 minutes | Initialized completed |

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant test scenario.

**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

Alternatively, send a [Refund](/api/#refund-an-order) API request.

---

**Note**:  

- You can't test sending redirect API requests.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

{{< details title="WeChat Pay" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

**Test a WeChat Pay order**

1. Send a [direct](/api/#wechat-pay---direct) or [redirect](/api/#wechat-pay---redirect) API request.
2. Scan the QR code with a general QR reader (**not** the WeChat app - an error occurs).
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note**:  

- You can't test cancelling orders.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

## Read more

{{< two-buttons href-2="/getting-started/test-your-integration" header-2="Read more" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/getting-started/test-your-integration/testing-refunds" header-2="Read more" text-2="Testing refunds" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
