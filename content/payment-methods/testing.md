---
title: 'Testing payment methods'
category: 6298bd782d1cf4006032e765
order: 6
hidden: false
slug: 'testing'
excerpt: 'Test payment methods and resolve common issues.'
---
Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your <a href="https://testmerchant.multisafepay.com/" target="_blank">MultiSafepay test account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Credentials

For all payment methods **except** Riverty, you need your site's test [API key](/docs/sites#site-id-api-key-and-security-code).

# How to make a test payment

1. Initiate a payment:  

    <details id="in-your-ready-made-integration">
    <summary>In your ready-made integration</summary>
    <br>

    - In your <<glossary:backend>>, enter your test site [API key](/docs/sites#site-id-api-key-and-security-code).
    - Place a test order, and then initiate a transaction with the payment method you are testing. 
    
    <br>

    </details>
    <details id="via-our-api">
    <summary>Via our API</summary>
    <br>
  
    - [Create an order](/reference/createorder/) via our API to the test endpoint: `https://testapi.multisafepay.com/v1/json/` 
    - For example requests for specific payment methods, see **Examples**.

    <br>

    </details>
2. Enter the [test payment details](/docs/testing#test-payment-details) for the payment method you are testing, or select a payment scenario.
3. Complete the test payment.
4. To check the transaction details, sign in to your <a href="https://testmerchant.multisafepay.com/" target="_blank">test dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
5. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
6. On the **Transaction details** page, under **Notification history**, to see if you have successfully connected to our system, check that you've correctly received the **notifyMerchantTrans** action.  
    For information about errors, see [HTTP errors](/docs/http-errors/).

✅ **Success!** Once your live account is approved, make sure you use the site API key from your **live** account instead of your test account. 

---
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

## PSP ID

> ⚠️ Note
> 
> We are currently updating the format of our PSP ID to consist of 16 digits.

Testing this new format is possible on both our TEST and LIVE environment:

- Create a transaction with customer_email '[enable-pspid-encoding@multisafepay.com](mailto:enable-pspid-encoding@multisafepay.com)''.  
  You will receive a response in the new 16-digit format.
- Review if your integration supports the longer ID:  
  Check for example your offline actions, and any related operational processes.
- Review if your reconciliation and accounting process supports this longer ID.


</details>

---
## Banking methods

<details id="bancontact">
<summary>How to test Bancontact</summary>
<br>

**Test a Bancontact order**

**⚠️ Note:** Bancontact doesn't support **direct** requests.

1. [Create an order](/reference/createorder/) > Banking order (Example: Bancontact redirect).
2. Open the payment link.
3. In the **Card number** field, enter a card number (see table below).
4. In the **Expiry date** fields, enter any future date.
5. Click **Confirm**.

| Card number| Scenario | Description |
| ---| --- | --- |
| 67034500054620008 | **Completed** | The transaction was completed (3D enrolled). <br> Also use this card number when creating orders to test [refunds and API refunds](#refunds). |
| 67034500054610009| **Declined**  | The transaction was declined (card must be 3D enrolled). |
| 67039902990000045| **Declined**  | The transaction was declined (3D authentication failed). |
| 67039902990000011| **Declined**  | The transaction was declined (3D authentication successful, but insufficient funds). |
<br>

You can see the reason the transaction was declined in your MultiSafepay test account under **Notes**.

**Test a Bancontact QR code**
1. [Create an order](/reference/createorder/) > Banking order (Example: Bancontact QR)
2. Open the payment link.
3. Scan the QR code with a general QR reader (**not** the Bancontact app or an error occurs).
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.

</details>

<details id="bank-transfer">
<summary>How to test bank transfers</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: Bank transfer redirect)
2. Open the payment link. 
3. In the **Your bank account** field, enter an IBAN (see table below). 
4. From the **Bank's country** list, select a country, and then click **Confirm**.

| IBAN | Scenario | Description |
| ---| ---| ---|
| NL87ABNA0000000001| **Completed** | The transaction is initiated. <br> After 2 minutes, this changes to **Completed**. <br> Also use this for [testing refunds](#refunds). |
| NL87ABNA0000000002| **Expired** | The transaction is initiated. <br> After 2 minutes, this changes to **Expired**. |
| NL87ABNA0000000004| **Declined** | The transaction is initiated. <br> After 2 minutes, this changes to **Declined**. |
| Any other IBAN | **Expired** | The transaction is initiated. <br> After 5 days, this changes to **Expired**. |
<br>

**⚠️ Note:** You cannot test making <<glossary:direct>> API requests with an IBAN to test different <<glossary:transaction statuses>>.

</details>

<details id="belfius-cbc-kbc-sofort-trustly">
<summary>How to test Belfius, CBC/KBC, Sofort & Trustly</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order.  
    See also the Examples for the specific payment method.
2. Open the payment link. 
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>

<details id="dotpay">
<summary>How to test Dotpay</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: Dotpay redirect)
2. On the Dotpay page, enter in the:
    - **Email address** field: Any email address
    - **Phone number** field: Any phone number
3. Select a bank. (You may see more banks available in the live environment.)
  You are automatically redirected.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
    The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>

<details id="eps">
<summary>How to test EPS</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: EPS redirect)
    In the `customer` object, set the `locale` parameter to `at_AT`.
2. On the EPS page, in the **BIC** field, enter any BIC code, e.g. `RZOOAT2L420`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
    The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>

<details id="giropay">
<summary>How to test Giropay</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: Giropay redirect)
2. On the Giropay page, in the **BIC** field, enter any BIC code, e.g. `NOLADE22XXX`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>

<details id="ideal">
<summary>How to test iDEAL</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: iDEAL direct/redirect)
2. For <<glossary:redirect>> orders, open the payment link.
3. On the **Test platform** page, from the **Test scenario** list, select the desired transaction scenario. Refer to the table below for details.
4. Click **Test**.

| Scenario      | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| **Success**   | The transaction is initiated. <br> Transaction will show as **Completed**. |
| **Failure**   | The transaction is initiated. <br> Transaction will show as **Declined**.  |
| **Cancelled** | The transaction is initiated. <br> Transaction will show as **Void**.      |
| **Expired**   | The transaction is initiated. <br> Transaction will show as **Expired**.   |

</details>

<details id="MBWAY-and-multibanco">
<summary>How to test Multibanco & MB WAY</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order.  
   See also the Examples for the specific payment method.
2. For <<glossary:redirect>> orders, open the payment link.
3. Set the `amount` parameter according to the desired transaction scenario. Refer to the table below for details. 
4. For **MB WAY** direct orders, in the `customer` object, fill the `phone` parameter. For redirect orders, enter a phone number on the payment link and click **Confirm**.

| Amount                  | Scenario      | Description                                                                                                              |
| ----------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 9.99 and below          | **Declined**  | The transaction is initiated. <br> Transaction will show as **Declined**.                                                |
| Between 10.00 and 20.00 | **Completed** | The transaction is initiated. <br> Transaction will show as **Completed**.                                               |
| Above 20.00             | **Expired**   | The transaction is initiated. <br> The status will show as **Initialized**. After 84 hours, this changes to **Expired**. |

</details>

<details id="direct-debit">
<summary>How to test direct debits</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: Direct debit direct/redirect)
2. For <<glossary:redirect>> orders, open the payment link. 
3. Enter in the:
    - **Account holder** field the account holder name.
    - **IBAN** field an IBAN (see table below).
4. Click **Confirm**.

| IBAN | Scenario | Description |
| ---| --- | --- |
| NL87ABNA0000000001| **Completed** | The transaction is initiated. <br> After 2 minutes, this changes to **Completed**. <br> Also use this IBAN to test [refunds and API refunds](#refunds). |
| NL87ABNA0000000002| **Declined** | The transaction is initiated. <br> After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Uncleared** > **Completed** | The transaction is initiated. <br> After 2 minutes, this changes to **Uncleared**. <br> After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Uncleared** > **Declined** | The transaction is initiated. <br> After 2 minutes, this changes to **Uncleared**. <br> After 1 more minute, it changes to **Declined**. |

</details>

<details id="mybank">
<summary>How to test MyBank</summary>
<br>

1. [Create an order](/reference/createorder/) > Banking order (Example: MyBank direct/redirect)
    In the `customer` object, set the `locale` parameter to `it_IT`.
2. For <<glossary:redirect>> orders, open the payment link. 
3. Select the bank/payment scenario below.
4. Click **Continua sull'online banking**.

| Bank | Scenario | Description |
| ---| --- | --- |
| Allianz Bank FA SPA | **Completed** | The transaction is initiated. <br> After 2 minutes, this changes to **Completed**. <br> Also use this IBAN to test [refunds and API refunds](#refunds). |
| Banca di Cesena - Credito Coop. | **Declined** | The transaction is initiated. <br> After 2 minutes, this changes to **Declined**. |
| Credito Artigiano | **Cancelled** | The transaction is initiated. <br> After 2 minutes, this changes to **Cancelled**.  |
| Volksbank - Banca Popolare | **Expired** | The transaction is initiated. <br> After 2 minutes, this changes to **Expired**.  |

</details>

---
## Credit and debit cards

<details id="credit-debit-cards">
<summary>How to test cards</summary>
<br>

1. [Create an order](/reference/createorder/) > Card order.  
    See also the Examples for the specific <<glossary:card scheme>>.  
    For co-branded cards, see the Card payment redirect example. In the `customer` object, set the `locale` parameter:
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
    The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

| Card number | Scenario | Description |
| --- | --- | --- |
| Amex: 374500000000015 <br> Maestro: 6799990000000000011 <br> Mastercard: 5500000000000004 <br> Visa/co-branded: <br> 4111111111111111 <br>  4761340000000019| **Completed** | The transaction was completed (3D enrolled). |
| Visa/co-branded: <br> 4917300000000008 | **Uncleared** | The transaction is uncleared. <br> After 3 minutes, this changes to **Void**. |
| Amex: 378734493671000 <br> Visa/co-branded: <br> 4462000000000003 | **Uncleared** | The transaction is uncleared. <br> After 3 minutes, this changes for Amex to **Void** and for Visa to **Completed**. |
| Amex: 374200000000004 <br> Visa/co-branded: <br> 4012001037461114 | **Declined**  | The transaction was declined (3D authentication failed). |
| Visa/co-branded: <br> 4012001038488884 | **Declined**  | The transaction was declined (3D authentication was successful, but insufficient funds). |
<br>

&nbsp; **💡 Tip!** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

</details>

---
## BNPL methods

<details id="e-invoicing-pay-after-delivery">
<summary>How to test E-Invoicing & Pay After Delivery</summary>
<br>

**Test an order**

1. [Create an order](/reference/createorder/) > BNPL order  
    Example: E-Invoicing/Pay After Delivery direct/redirect
2. For <<glossary:redirect>> orders, open the payment link.
3. Enter in the:
    - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
    - **Bank account** field any 10-digit bank account number.
    - **Email address** field any email address.
    - **Phone number** field any phone number.
4. Click **Confirm**.  
The payment is processed in the test environment as **Successful**, with order and transaction statuses **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The <<glossary:order status>> and <<glossary:transaction status>> change to **Void**.

**Test shipping an E-Invoicing order**  

To test shipping an order, make an [update order](/reference/updateorder/) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

</details>

<details id="in3">
<summary>How to test in3</summary>
<br>

**Test an in3 order**

1. [Create an order](/reference/createorder/) > BNPL order  
    Example: in3 direct/redirect  
    Use the following customer details:
    - Date of birth: 01-01-1999
    - Postal code: 1234AB
    - House number: 1

    For <<glossary:redirect>> orders:
    - Enter in the:
      - **Birthdate** field: `01-01-1999`
      - **Phone number** field: Any phone number  
    - Select your title, and then click **Confirm**.
2. Select the checkbox to accept in3's payment terms and privacy statement, and then click **Afronden**.
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**. 
5. On the in3 page, click **Terug naar webshop**.  
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and transaction status **Uncleared**.

**Test in3 declining an order**  

Use the following customer details:

- Date of birth: 01-01-2000
- Postal code: 1111AB
- House number: 1 

The <<glossary:order status>> and <<glossary:transaction status>> change to **Declined**.

**Test shipping an in3 order**  

To test shipping an order, either:

- Make an [update order](/reference/updateorder/) API request with status `shipped`, or 
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
3. Make a BNPL refund API request: [Refund order](/reference/refundorder/) > BNPL refund.
    A new order is created for the refund. The order status for the refund changes to **Completed**.

</details>

<details id="klarna">
<summary>How to test Klarna</summary>
<br>

**Test credentials**

- [Site API key](/docs/sites#site-id-api-key-and-security-code)
- <a href="https://docs.klarna.com/resources/test-environment/" target="_blank">Klarna's test credentials</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

**Test a Klarna order** 

1. [Create an order](/reference/createorder/) > BNPL order 
    Example: Klarna direct/redirect
2. On the Klarna page, click **Kopen**.
3. In the **Telefoonnummer** field, enter any mobile number, and then click **Ga verder**.
4. In the **Verificatiecode** field, enter any 6-digit number, and then click **Bevestigen**.  
    The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update order](/reference/updateorder/) API request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Test refunding an order**

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or make a BNPL refund API request: [Refund order](/reference/refundorder/) > BNPL refund.  
    The <<glossary:transaction status>> changes to **Completed**.

**Receive an invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**⚠️ Note:** You can't test:
- Receiving successful payment notifications from Klarna
- Changing the <<glossary:transaction status>> from **Uncleared** to **Completed**, except for refunds

ℹ More information
To learn more about integrating Klarna with MultiSafepay, see [Klarna](/docs/klarna/).

</details>

<details id="riverty">
<summary>How to test Riverty</summary>
<br>

**Request an API key**

1. Request a test API key from Riverty via either:
    - Your implementation ticket with Riverty, **or**
    - Email <sales@riverty.com>

    Riverty shares the test key with MultiSafepay.

2. To enable Riverty in your MultiSafepay test account, email <integration@multisafepay.com>

**Test an Riverty order**

1. [Create an order](/reference/createorder/) > BNPL order  
    Example: Riverty direct/redirect
2. For <<glossary:redirect>> orders, select the checkbox at the bottom of the Riverty page, and then click **Confirm**.  
The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The transaction and order statuses change to **Void**.

**Test Riverty rejecting an order**  

To test Riverty rejecting an order, in your <<glossary:direct>> or <<glossary:redirect>> API request, use the following email address: <rejection@afterpay.nl>  
The transaction and order statuses change to **Declined**.

**Change the order status**  

You can change the order status to **Shipped** or **Cancelled**.
To change the order status, either:  

- Make an [update order](/reference/updateorder/) request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**⚠️ Note:** You can't test:  
 - Receiving successful payment notifications from Riverty
 - Changing the <<glossary:transaction status>> from **Uncleared** to **Completed**
 - Processing refunds

</details>

---
## Prepaid cards

<details id="edenred">
<summary>How to test Edenred</summary>
<br>

1. [Create an order](/reference/createorder/) > Prepaid card order  
    Example: Edenred redirect
2. On the payment page, click **Add discount**.
3. From the **Test scenario** list, select the relevant discount, and then click **Test**.
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>

<details id="gift-cards">
<summary>How to test gift cards</summary>
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

1. [Create an order](/reference/createorder/) > Prepaid card order  
    Example: Gift card redirect
2. Open the payment link.
3. Enter the following details:
    - In the **Card number** field, `111115`
    - In the **Security code** field, any 4-digit number
4. Click **Add discount**.  
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

Use the following card numbers to test different gift card balances:

| Card numbers | Balance |
| --- | --- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |
<br>

Any other card number receives an "Invalid card number" error.

</details>

<details id="monizze">
<summary>How to test Monizze</summary>
<br>

1. [Create an order](/reference/createorder/) > Prepaid card order  
    Example: Monizze redirect
2. Open the payment link.
3. Enter the following details:
    - In the **Card number** field, `111115`
    - In the **Security code** field, any 4-digit number
4. Click **Add discount**.
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

 Use the following card numbers to test different gift card balances:

| Card numbers | Balance |
| --- | --- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110  | € 0 |

  </details>

<details id="sodexo">
<summary>How to test Sodexo</summary>
<br>

1. [Create an order](/reference/createorder/) > Prepaid card order  
    Example: Sodexo redirect
2. Open the payment link.
3. Enter the following details:
    - In the **Card number** field, `111115`
    - In the **Security code** field, any 4-digit number
4. Click **Add discount**.  
  The payment is processed in the test environment as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

Use the following card numbers to test different gift card balances:

| Card numbers | Balance |
| --- | --- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110  | € 0 |
<br>

Any other card number receives an "Invalid card number" error.

</details>

---
## Wallets

<details id="alipay">
<summary>How to test Alipay</summary>
<br>

1. [Create an order](/reference/createorder/) > Wallet order  
    Example: Alipay direct/redirect
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with <<glossary:order status>> **Completed**, and transaction status **Initialized**.

**⚠️ Note:** You can't test Alipay declining transactions.

</details>

<details id="amazon-pay">
<summary>How to test Amazon Pay</summary>
<br>

1. [Create an order](/reference/createorder/) > Wallet order.
    Example: Amazon Pay direct/redirect
2. On the **Test platform** page, wait for 5 seconds or click **Amazon Pay**.
3. From the **Test scenario** list, select **Completed**.
4. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Initialized**.

</details>

<details id="apple-pay">
<summary>How to test Apple Pay</summary>
<br>

**Compatible devices**

For compatible devices, see Apple – <a href="https://support.apple.com/en-us/HT208531" target="_blank">Devices compatible with Apple Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

If you don't own an Apple device, we recommend using the <a href="https://appetize.io" target="_blank">Appetize.io</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> emulator. When you try to complete a test payment on the payment page, you get a _This device is not supported_ error. But the emulator creates an order with the Apple Pay <<glossary:gateway>> pre-selected to check if there is an existing connection to our server. However, you can't fully complete the test transaction.

**Prerequisites**

- Use a <a href="https://support.apple.com/en-us/HT208531" target="_blank">compatible device</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- Use Safari browser
- Activate Maestro for your MultiSafepay account

If these requirements are not met, Apple Pay doesn't appear on the checkout page.

**Testing Apple Pay redirect**

To test your Apple Pay <<glossary:redirect>> integration, there are two ways:

- If you have an Apple account with at least one card in your wallet, you can use your own account and card details in our test environment without incurring any costs.
- Alternatively, you can use an <a href="https://developer.apple.com/apple-pay/sandbox-testing" target="_blank">Apple Developer account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> configured for Apple Pay, with at least one Apple Pay test card in your wallet.

To test, follow these steps:

1. [Create an order](/reference/createorder/) > Wallet order  
    Example: Apple Pay redirect
2. On the payment page, click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
3. Sign in to your Apple Developer account and select your test card.
4. Authorize the payment.
  The transaction is completed.

**Testing Apple Pay direct**

See Apple Pay direct integration – [Test your integration](/docs/apple-pay-direct#6-test-your-integration).

</details>

<details id="google-pay">
<summary>How to test Google Pay</summary>
<br>

To test Google Pay payments, follow these steps:

1. In your checkout, click the **Google Pay** button.  
2. Complete payment using your Google account. 

    Your real card details are never processed in our testing environment, but you must add at least one chargeable card to your Google account.

    Depending on your card's authentication method, you may or may not be redirected to authenticate:

    - **PAN only**: Authentication method for cards stored on file in your Google Account. Returned payment data includes your personal account number (PAN), expiration month, and expiration year. You are redirected to a test 3D Secure page to authenticate the payment.
    - **Cryptogram 3DS**: Authentication method for cards stored as Android device tokens. Returned payment data includes a 3D Secure cryptogram generated on the device. You are not redirected to authenticate the payment.  
    For more information about testing, see Google Pay – <a href="https://developers.google.com/pay/api/web/guides/resources/sample-tokens" target="_blank">Test with sample tokens</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
 
3. Check the status of the payment in your <a href="https://testmerchant.multisafepay.com/" target="_blank">test dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>

<details id="paypal">
<summary>How to test PayPal</summary>
<br>

**Test a PayPal order**

PayPal must be activated via your <a href="https://testmerchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

To test, follow these steps:

1. [Create an order](/reference/createorder/) > Wallet order  
   Example: PayPal direct
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
   The payment is processed in your MultiSafepay test account as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Initialized**.

**⚠️ Note:** Since MultiSafepay does not collect payments on behalf of PayPal, the <<glossary:transaction status>> remains **Initialized** and can't be changed to **Completed**.

**Change the order status**

You can change the order status to:

| Status        | Description         | Test scenario |
| ------------- | ------------------- | ------------- |
| **Completed** | Order was completed | Approved      |
| **Void**      | Order was cancelled | Cancelled     |
| **Expired**   | Order not completed | Closed        |

<br>

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant test scenario.

</details>

<details id="wechat-pay">
<summary>How to test WeChat Pay</summary>
<br>

1. [Create order](/reference/createorder/) > Wallet order  
    Example: WeChat direct/redirect
2. Scan the QR code with a general QR reader (**not** the WeChat app or an error occurs).
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Completed**.

</details>
<br>

---

# User guide

## Cancellations

<details id="how-to-test-cancelling-order">
<summary>How to test cancelling an order</summary>
<br>

1. Create an order in your <<glossary:backend>> or via the API as above.
2. On the **Test platform** page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
    The order status changes to **Void**.

You can process full refunds in your <a href="https://testmerchant.multisafepay.com/" target="_blank">MultiSafepay test dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the [transaction status](/docs/payment-statuses/) remains **Reserved** or **Initialized** until the refund is manually approved, since there is no involvement with a bank.

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

- Banking methods: Bancontact (not QR), bank transfers, Belfius, CBC/KBC, direct debits, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

</details>

## Refunds

<details id="how-to-test-refunding-order">
<summary>How to test refunding an order</summary>
<br>

1. [Create an order](/reference/createorder/). 
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

- Banking methods: Bancontact (not QR), bank transfers, Belfius, CBC/KBC, direct debits, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- <<glossary:BNPL>>: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

</details>

<details id="how-to-test-refunding-api-order">
<summary>How to test refunding an API order</summary>
<br>

1. [Create an order](/reference/createorder/). 
2. Make a [refund](/reference/refundorder/) API request.
    A new order is created for the refund. The order status for the refund changes to **Reserved** or **Initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
    The order status changes to **Completed**.

**Supported payment methods**

You can test refunds for the following methods:

- Banking methods: Bancontact (not QR), direct debits, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- <<glossary:BNPL>>: in3
- Wallets: PayPal, WeChat Pay

</details>

<br>

---

> ℹ See also
>
> If you encounter any issues during testing, see [Troubleshooting](/docs/troubleshooting/).

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
