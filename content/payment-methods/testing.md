---
title: 'Testing'
category: 6298bd782d1cf4006032e765
order: 600
hidden: false
slug: 'testing'
excerpt: 'Test payment methods and resolve common issues.'
---
Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your [MultiSafepay test account](https://testmerchant.multisafepay.com/).

# Credentials

For all payment methods **except** AfterPay, you need your site's test [API key](/websites/#site-id-api-key-and-secure-code).

# How to make a test payment

1. Initiate a payment in your [ready-made integration](/integrations/) or via our API:  

    <details id="ready-made-integration">
    <summary>Ready-made integration</summary>
    <br>

    - In your backend, enter your test site [API key](/websites/#site-id-api-key-and-secure-code).
    - Place a test order, and then initiate a transaction with the payment method you are testing. 

    </details>
    <details id="api">
    <summary>API</summary>
    <br>
  
    - [Create an order](https://docs-api.multisafepay.com/reference/createorder) via our API to the test endpoint: `https://testapi.multisafepay.com/v1/json/` 
    - For example requests for specific payment methods, see **Examples**.
        </details>
2. Enter the [test payment details](/#test-payment-details) for the payment method you are testing, or select a payment scenario.
3. Complete the test payment.
4. To check the transaction details, sign in to your [test dashboard](https://testmerchant.multisafepay.com/).
5. Go to **Transactions** > **Transactions overview**.
6. In the **Transactions overview** list, select the transaction to view the **Transaction details** page. 
7. To check that you have succesfully connected to our system, under **Offline actions**, check that you've correctly received the **notifyMerchantTrans** action.  
    For information about errors, see [HTTP errors](/http-errors/).

:warning: Once your live account is approved, make sure you use the site API key from your **live** account instead of your test account. 

# Test payment details

When testing, use the following test payment details for different scenarios. 

<details id="methods-not-available-in-test-environment">
<summary>Methods not available in test environment</summary>
<br>

You can't test the following methods in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

- Betaal per Maand
- iDEAL QR
- Paysafecard
- Request to Pay
- TrustPay

</details>

## Banking methods

<details id="bancontact">
<summary>Bancontact</summary>
<br>

**Test a Bancontact order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order (Example: Bancontact redirect).
2. Open the payment link.
3. In the **Card number** field, enter a card number (see table below).
4. In the **Expiry date** fields, enter any future date.
5. Click **Confirm**.

| Card number| Scenario | Description |
| ---| --- | --- |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled). <br> Also use this card number when creating orders to test [refunds and API refunds](#refunds). |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled). |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed). |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds). |
<br>

You can see the reason the transaction was declined in your MultiSafepay test account under **Notes**.

**Test a Bancontact QR code**
1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: Bancontact QR
2. Open the payment link.
3. Scan the QR code with a general QR reader (**not** the Bancontact app or an error occurs).
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.

</details>

<details id="bank-transfer">
<summary>Bank Transfer</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: Bank Transfer redirect
2. Open the payment link. 
3. In the **Your bank account** field, enter an IBAN (see table below). 
4. From the **Bank's country** list, select a country, and then click **Confirm**.

| IBAN | Scenario | Description |
| ---| ---| ---|
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Completed**. <br> Also use this for [testing refunds](#refunds). |
| NL87ABNA0000000002| **Initialized**/ **Expired** | Transaction is initiated. After 2 minutes, this changes to **Expired**. |
| NL87ABNA0000000004| **Initialized**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Declined**. |
| Any other IBAN | **Initialized**/ **Expired** | Transaction is initiated. After 5 days, this changes to **Expired**. |
<br>

**Note:** You can't test making direct API requests with an IBAN to test different transaction statuses.

</details>

<details id="belfius-cbc-kbc-sofort-trustly">
<summary>Belfius, CBC/KBC, Sofort, Trustly</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order.  
    See also the Examples for the specific payment method.
2. Open the payment link. 
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>

<details id="dotpay">
<summary>Dotpay</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: Dotpay redirect
2. On the Dotpay page, enter in the:
    - **Email address** field: Any email address
    - **Phone number** field: Any phone number
3. Select a bank. (You may see more banks available in the live environment.)
  You are automatically redirected.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
    The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>

<details id="eps">
<summary>EPS</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: EPS redirect   
    Set the `locale` parameter to `at_AT`.
2. On the EPS page, in the **BIC** field, enter any BIC code, e.g. `RZOOAT2L420`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
    The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>

<details id="giropay">
<summary>Giropay</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: Giropay redirect
2. On the Giropay page, in the **BIC** field, enter any BIC code, e.g. `NOLADE22XXX`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>

<details id="ideal">
<summary>iDEAL</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: iDEAL direct/redirect
2. For redirect, select a bank.
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
    The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

You can also test the following scenarios:

| Scenario | Description |
| --- | --- |
| **Declined** | Transaction was declined. |
| **Open** **Completed** | Transaction is initiated. After 1 minute, this changes to **Completed**. |
| **Open** **Declined**  | Transaction is initiated. After 1 minute, this changes to **Declined**. |

</details>

<details id="sepa-direct-debit">
<summary>SEPA Direct Debit</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Banking order  
    Example: SEPA Direct Debit direct/redirect
2. For redirect orders, open the payment link. 
3. Enter in the:
    - **Account holder** field the account holder name.
    - **IBAN** field an IBAN (see table below).
4. Click **Confirm**.

| IBAN | Scenario | Description |
| ---| --- | --- |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Completed**. <br> Also use this IBAN to test [refunds and API refunds](#refunds). |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

</details>

## Credit and debit cards

<details id="credit-debit-cards">
<summary>Credit and debit cards</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Card order.  
    See also the Examples for the specific card scheme.  
    For co-branded cards, see the Credit card redirect example, and set the `locale` parameter:
    - Cartes Bancaires: `fr_FR` 
    - Dankort: `da_DK`
    - Postepay: `it_IT`
2. On the payment page:
    - In the **Card number** field, enter a card number (see table below).
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
    The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

| Card number | Scenario | Description |
| --- | --- | --- |
| Amex: 378282246310005 <br> Maestro: 6759000000005 <br> Mastercard: 5500000000000004 <br> Visa/co-branded: <br> 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| Visa/co-branded: <br> 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| Visa/co-branded: <br> 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |
| Amex: 378734493671000 <br> Visa/co-branded: <br> 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| Amex: 374200000000004 <br> Visa/co-branded: <br> 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| Visa/co-branded: <br> 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |
<br>

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

</details>

## Pay later methods

<details id="afterpay">
<summary>AfterPay</summary>
<br>

**Request an API key**

1. Request a test API key from AfterPay via either:
    - Your implementation ticket with AfterPay, **or**
    - Email <sales@afterpay.nl>

    AfterPay shares the test key with MultiSafepay.

2. To enable AfterPay in your MultiSafepay test account, email <integration@multisafepay.com>

**Test an AfterPay order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order  
    Example: AfterPay direct/redirect
2. For redirect orders, select the checkbox at the bottom of the AfterPay page, and then click **Confirm**.  
The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Test AfterPay rejecting an order**  

To test AfterPay rejecting an order, in your direct or redirect API request, use the following email address: <rejection@afterpay.nl>  
The transaction and order statuses change to **Declined**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update order](https://docs-api.multisafepay.com/reference/updateorder) request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Notes:** 

You can't test:  

- Receiving successful payment notifications from AfterPay
- Changing the transaction status from **Uncleared** to **Completed**
- Processing refunds

</details>

<details id="e-invoicing-pay-after-delivery">
<summary>E-Invoicing, Pay After Delivery</summary>
<br>

**Test an order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order  
    Example: E-Invoicing/Pay After Delivery direct/redirect
2. For redirect orders, open the payment link.
3. Enter in the:
    - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
    - **Bank account** field any 10-digit bank account number.
    - **Email address** field any email address.
    - **Phone number** field any phone number.
4. Click **Confirm**.  
The payment is processed in the test environment as **Successful**, with order and transaction statuses **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The order and transaction statuses change to **Void**.

**Test shipping an E-Invoicing order**  

To test shipping an order, make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

</details>

<details id="in3">
<summary>in3</summary>
<br>

**Test an in3 order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order  
    Example: in3 direct/redirect  
    Use the following customer details:
    - Date of birth: 01-01-1999
    - Postal code: 1234AB
    - House number: 1

    For redirect orders:
    - Enter in the:
      - **Birthdate** field: `01-01-1999`
      - **Phone number** field: Any phone number  
    - Select your title, and then click **Confirm**.
2. Select the checkbox to accept in3's payment terms and privacy statement, and then click **Afronden**.
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**. 
5. On the in3 page, click **Terug naar webshop**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test in3 declining an order**  

Use the following customer details:

- Date of birth: 01-01-2000
- Postal code: 1111AB
- House number: 1 

The order and transaction statuses change to **Declined**.

**Test shipping an in3 order**  

To test shipping an order, either:

- Make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request with status `shipped`, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Receive an in3 invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**Test refunding an in3 order**

To test refunding an order:

1. Create an order. 
2. Change the order status to `shipped`.
3. Click **Refund complete order**, and then click **Save item changes**.
    A new order is created for the refund. The order status for the refund changes to **Completed**.

**Test an in3 API refund**

To test refunding an order via the API:

1. Create an order. 
2. Change the order status to `shipped`.
3. Make a pay later refund API request: [Refund order](https://docs-api.multisafepay.com/reference/) > Pay later refund.
    A new order is created for the refund. The order status for the refund changes to **Completed**.

</details>

<details id="klarna">
<summary>Klarna</summary>
<br>

**Test credentials**

- [Site API key](/websites/#site-id-api-key-and-secure-code)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna order** 

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Pay later order 
    Example: Klarna direct/redirect
2. On the Klarna page, click **Kopen**.
3. In the **Telefoonnummer** field, enter any mobile number, and then click **Ga verder**.
4. In the **Verificatiecode** field, enter any 6-digit number, and then click **Bevestigen**.  
    The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update order](https://docs-api.multisafepay.com/reference/updateorder) API request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Test refunding an order**

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or make a pay later refund API request: [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund.  
    The transaction status changes to **Completed**.

**Receive an invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**Notes:** 

You can't test:

- Receiving successful payment notifications from Klarna
- Changing the transaction status from **Uncleared** to **Completed**, except for refunds

For more information about integrating Klarna with MultiSafepay, see [Klarna](/klarna/).

</details>

## Prepaid cards

<details id="edenred">
<summary>Edenred</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order  
    Example: Edenred redirect
2. On the payment page, click **Add discount**.
3. From the **Test scenario** list, select the relevant discount, and then click **Test**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>

<details id="gift-cards">
<summary>Gift cards</summary>
<br>

**Supported gift cards**

You can test the following gift cards:

- Beauty Cadeau
- Boeken Voordeel
- Huis & Tuin Cadeau
- Klus Cadeau
- Nationale Bioscoopbon
- VVV Cadeaukaart
- Wijn Cadeaukaart

You can't test other gift cards in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. You make a small payment and the amount is actually deducted from the gift card.

**Test a gift card order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order  
    Example: Gift card redirect
2. Open the payment link.
3. Enter in the:
    - **Card number** field `111115`
    - **Security code** field any 4-digit number
4. Click **Add discount**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different gift card balances.

| Card numbers | Balance |
| --- | --- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |
<br>

Any other card number receives an "Invalid card number" error.

</details>

## Wallets

<details id="alipay">
<summary>Alipay</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order  
    Example: Alipay direct/redirect
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

    **Note:** You can't test Alipay declining transactions.

</details>

<details id="apple-pay">
<summary>Apple Pay</summary>
<br>

**Compatible devices**

For compatible devices, see Apple – [Devices compatible with Apple Pay](https://support.apple.com/en-us/HT208531).

If you don't own an Apple device, we recommend using the [Appetize.io](https://appetize.io) emulator. When you try to complete a test payment on the payment page, you get a _This device is not supported_ error. But the emulator creates an order with the Apple Pay gateway preselected to check if there is an existing connection to our server. However, you can't fully complete the test transaction.

**Prerequisites**

- Use a [compatible device](https://support.apple.com/en-us/HT208531)
- Use Safari browser
- Activate Maestro for your MultiSafepay account

If these requirements are not met, Apple Pay doesn't appear on the checkout page.

**Testing Apple Pay redirect**

To test your Apple Pay redirect integration, there are two ways:

- If you have an Apple account with at least one credit card in your wallet, you can use your own account and card details in our test environment without incurring any costs.
- Alternatively, you can use an [Apple Developer account](https://developer.apple.com/apple-pay/sandbox-testing) configured for Apple Pay, with at least one Apple Pay test card in your wallet.

To test, follow these steps:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order  
    Example: Apple Pay redirect
2. On the payment page, click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
3. Sign in to your Apple Developer account and select your test card.
4. Authorize the payment.
  The transaction is completed.

**Testing Apple Pay direct**

See Apple Pay direct integration – [Test your integration](/payment-methods/apple-pay/direct/#test-your-integration).

</details>

<details id="google-pay">
<summary>Google Pay</summary>
<br>

To test Google Pay payments, follow these steps:

1. In your checkout, click the **Google Pay** button.  
2. Complete payment using your Google account. 

    Your real card details are never processed in our testing environment, but you must add at least one chargeable card to your Google account.

    Depending on your card's authentication method, you may or may not be redirected to authenticate:

    - **PAN only**: Authentication method for cards stored on file in your Google Account. Returned payment data includes your personal account number (PAN), expiration month, and expiration year. You are redirected to a test 3D Secure page to authenticate the payment.
    - **Cryptogram 3DS**: Authentication method for cards stored as Android device tokens. Returned payment data includes a 3D Secure cryptogram generated on the device. You are not redirected to authenticate the payment.  
    For more information about testing, see Google Pay – [Test with sample tokens](https://developers.google.com/pay/api/web/guides/resources/sample-tokens).
 
3. Check the status of the payment in your [test dashboard](https://testmerchant.multisafepay.com/).

</details>

<details id="paypal">
<summary>PayPal</summary>
<br>

**Test a PayPal order**

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order  
    Example: PayPal direct
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

**Change the order status**

You can change the order status to:

| Status | Description | Test scenario |
| --- | --- | --- |
| **Completed** | Order was completed | Completed  |
| **Void** | Order was cancelled | Cancelled  |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted after 2 minutes | Initialized completed |
<br>

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant test scenario.

</details>

<details id="wechat-pay">
<summary>WeChat Pay</summary>
<br>

1. [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order  
    Example: WeChat direct/redirect
2. Scan the QR code with a general QR reader (**not** the WeChat app or an error occurs).
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Completed**.

</details>
<br>

---

# User guide

## Cancellations

<details id="how-to-test-cancelling-order">
<summary>How to test cancelling an order</summary>
<br>

1. Create an order in your backend or via the API as above.
2. On the **Test platform** page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
    The order status changes to **Void**.

You can process full refunds in your [MultiSafepay test dashboard](https://testmerchant.multisafepay.com/). 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the [transaction status](/payment-statuses/) remains **Reserved** or **Initialized** until the refund is manually approved, since there is no settlement with a bank.

**Supported payment methods**

You can test cancelling orders for the following methods:

- Banking methods: Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Wallets: Alipay, PayPal

</details>

## Live environment

For some payment methods, refund orders in the live environment are processed automatically.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

Refund orders in the live environment are processed automatically for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

</details>

## Refunds

<details id="how-to-test-refunding-order">
<summary>How to test refunding an order</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder). 
2. Wait until the transaction status changes to **Completed**.
3. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **Amount** field the amount to refund.  
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
    A new order is created for the refund, with status **Reserved** or **Initialized**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
    The order status changes to **Completed**.

**Supported payment methods**

You can test refunds for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

</details>

<details id="how-to-test-refunding-api-order">
<summary>How to test refunding an API order</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder). 
2. Make a [refund](https://docs-api.multisafepay.com/reference/refundorder) API request.
    A new order is created for the refund. The order status for the refund changes to **Reserved** or **Initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
    The order status changes to **Completed**.

**Supported payment methods**

You can test refunds for the following methods:

- Banking methods: Bancontact (not QR), EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3
- Wallets: PayPal, WeChat Pay

</details>

<br>

> 💬  Support
> If you encounter any issues during testing, see [Handling errors](/handling-errors/).
>
> For more information or support, email <integration@multisafepay.com>