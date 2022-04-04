---
title : "Test payment details"
weight: 20
meta_title: "Test payment details - MultiSafepay Docs"
read_more: "."
url: '/testing/test-payment-details/'
aliases:
    - /faq/getting-started/test-payment-details/
    - /getting-started/test-your-integration/test-payment-details
---

This page provides test payment details for different scenarios. 

## Banking methods

{{< details title="Bancontact" >}}

**Test a Bancontact order**

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: Bancontact redirect).
2. Open the payment link.
3. In the **Card number** field, enter a card number (see table below).
4. In the **Expiry date** fields, enter any future date.
5. Click **Confirm**.

| Card number| Scenario | Description |
| ---| --- | --- |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled). <br> Also use this card number when creating orders to test [refunds](/testing/testing-refunds/#test-refunding-an-order) and [API refunds](/testing/testing-refunds/#test-an-api-refund). |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled). |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed). |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds). |

You can see the reason the transaction was declined in your MultiSafepay test account under **Notes**.

---

**Test a Bancontact QR code**
1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: Bancontact QR).
2. Open the payment link.
3. Scan the QR code with a general QR reader (**not** the Bancontact app or an error occurs).
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.

{{< /details >}}

{{< details title="Bank Transfer" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: Bank Transfer redirect).
2. Open the payment link. 
3. In the **Your bank account** field, enter an IBAN (see table below). 
4. From the **Bank's country** list, select a country, and then click **Confirm**.

| IBAN | Scenario | Description |
| ---| ---| ---|
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Completed**. <br> Also use this for [testing refunds](/testing/testing-refunds/#test-refunding-an-order). |
| NL87ABNA0000000002| **Initialized**/ **Expired** | Transaction is initiated. After 2 minutes, this changes to **Expired**. |
| NL87ABNA0000000004| **Initialized**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Declined**. |
| Any other IBAN | **Initialized**/ **Expired** | Transaction is initiated. After 5 days, this changes to **Expired**. |

**Note:** You can't test making direct API requests with an IBAN to test different transaction statuses.
{{< /details >}}

{{< details title="Belfius, CBC/KBC, Sofort, Trustly" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order. <br> See also the Examples for the specific payment method.
2. Open the payment link. 
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Dotpay" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: Dotpay redirect).
2. On the Dotpay page, enter in the:
    - **Email address** field: Any email address
    - **Phone number** field: Any phone number
3. Select a bank. (You may see more banks available in the live environment.)
  You are automatically redirected.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="EPS" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: EPS redirect). <br> Set the `locale` parameter to `at_AT`.
2. On the EPS page, in the **BIC** field, enter any BIC code, e.g.&nbsp;`RZOOAT2L420`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Giropay" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: Giropay redirect). 
2. On the Giropay page, in the **BIC** field, enter any BIC code, e.g. `NOLADE22XXX`.
3. Click **Confirm**.
4. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
5. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="iDEAL" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: iDEAL direct/redirect).
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

{{< /details >}}

{{< details title="SEPA Direct Debit" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Banking order (Example: SEPA Direct Debit direct/redirect).
2. For redirect orders, open the payment link. 
3. Enter in the:
    - **Account holder** field the account holder name.
    - **IBAN** field an IBAN (see table below).
4. Click **Confirm**.

| IBAN | Scenario | Description |
| ---| --- | --- |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Completed**. <br> Also use this IBAN to test [refunds](/testing/testing-refunds/#test-refunding-an-order) and [API refunds](/testing/testing-refunds/#test-an-api-refund). |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initiated. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initiated. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

{{< /details >}}

## Pay later methods

{{< details title="AfterPay" >}}

**1.** Request a test API key from AfterPay via either:

- Your implementation ticket with AfterPay, **or**
- Email <sales@afterpay.nl>

AfterPay shares the test key with MultiSafepay.

**2.** To enable AfterPay in your MultiSafepay test account, email <integration@multisafepay.com>

**Test an AfterPay order**

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Pay later order (Example: AfterPay direct/redirect).
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

- Make an [update order](https://api-docs.multisafepay.com/reference/updateorder) request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

---

**Notes:** 

You can't test:  

- Receiving successful payment notifications from AfterPay
- Changing the transaction status from **Uncleared** to **Completed**
- Processing refunds

{{< /details >}}

{{< details title="E-Invoicing, Pay After Delivery" >}}

**Test an order**

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Pay later order (Example: E-Invoicing/Pay After Delivery direct/redirect).
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

To test shipping an order, make an [update order](https://api-docs.multisafepay.com/reference/updateorder) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

{{< /details >}}

{{< details title="in3" >}}

**Test an in3 order**

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Pay later order (Example: in3 direct/redirect). Use the following customer details:
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

**Test shipping an order**  

To test shipping an order, either:

- Make an [update order](https://api-docs.multisafepay.com/reference/updateorder) API request with status `shipped`, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Receive an invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. Change the order status to `shipped`.
3. Click **Refund complete order**, and then click **Save item changes**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Change the order status to `shipped`.
3. Make a pay later refund API request: [Refund order](https://api-docs.multisafepay.com/reference/) > Pay later refund.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Completed**.

{{< /details >}}

{{< details title="Klarna" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)
- [Klarna's test credentials](https://docs.klarna.com/resources/test-environment/)

**Test a Klarna order**  
1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Pay later order (Example: Klarna direct/redirect).
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

- Make an [update order](https://api-docs.multisafepay.com/reference/updateorder) API request, or 
- In your MultiSafepay test dashboard, go to **Order summary**, and then click **Order status**.

**Test refunding an order**

To refund an order:

1. Change the order status to **Shipped**.
2. Under **Order summary**, click **Refund order**, or make a pay later refund API request: [Refund order](https://api-docs.multisafepay.com/reference/refundorder) > Pay later refund.  
  The transaction status changes to **Completed**.

**Receive an invoice**  

You can only test invoicing in your MultiSafepay live account. To do this, change the order status to **Shipped**.

---

**Notes:** 

You can't test:

- Receiving successful payment notifications from Klarna
- Changing the transaction status from **Uncleared** to **Completed**, except for refunds

For more information about integrating Klarna with MultiSafepay, see [Klarna](/payment-methods/klarna/).
{{< /details >}}

## Credit and debit cards

{{< details title="Credit and debit cards" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Card order. See also the Examples for the specific card scheme.  
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

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.
{{< /details >}}

## Prepaid cards

{{< details title="Edenred" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Prepaid card order (Example: Edenred redirect).
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

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Prepaid card order (Example: Gift card redirect).
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

Any other card number receives an "Invalid card number" error.

**Other gift cards** 

You can't test other gift cards in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. You make a small payment and the amount is actually deducted from the gift card.

{{< /details >}}

## Wallets

{{< details title="Alipay" >}}

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Wallet order (Example: Alipay direct/redirect).
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

**Note:** You can't test Alipay declining transactions.

{{< /details >}}

{{< details title="Apple Pay" >}}

**Compatible devices**

For compatible devices, see Apple – [Devices compatible with Apple Pay](https://support.apple.com/en-us/HT208531).

If you don't own an Apple device, we recommend using the [Appetize.io](https://appetize.io) emulator. When you try to complete a test payment on the payment page, you get a _This device is not supported_ error. But the emulator creates an order with the Apple Pay gateway preselected to check if there is an existing connection to our server. However, you can't fully complete the test transaction.

**Testing prerequisites**

- Use a [compatible device](https://support.apple.com/en-us/HT208531)
- Use Safari browser
- Activate Maestro for your MultiSafepay account

If these requirements are not met, Apple Pay doesn't appear on the checkout page.

**Testing Apple Pay redirect**

To test your Apple Pay redirect integration, there are two ways:

- If you have an Apple account with at least one credit card in your wallet, you can use your own account and card details in our test environment without incurring any costs.
- Alternatively, you can use an [Apple Developer account](https://developer.apple.com/apple-pay/sandbox-testing) configured for Apple Pay, with at least one Apple Pay test card in your wallet.

To test, follow these steps:

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Wallet order (Example: Apple Pay redirect).
2. On the payment page, click the **Apple Pay** button.  
    You can ignore the "This device is not supported" error.
3. Sign in to your Apple Developer account and select your test card.
4. Authorize the payment.
  The transaction is completed.

**Testing Apple Pay direct**

See Apple Pay direct integration – [Test your integration](/payment-methods/apple-pay/direct/#test-your-integration).

{{< /details >}}

{{< details title="Google Pay" >}}

To test Google Pay payments, follow these steps:

1. In your checkout, click the **Google Pay** button.  
2. Complete payment using your Google account. 

    Your real card details are never processed in our testing environment, but you must add at least one chargeable card to your Google account.

    Depending on your card's authentication method, you may or may not be redirected to authenticate:

    - **PAN only**: Authentication method for cards stored on file in your Google Account. Returned payment data includes your personal account number (PAN), expiration month, and expiration year. You are redirected to a test 3D Secure page to authenticate the payment.
    - **Cryptogram 3DS**: Authentication method for cards stored as Android device tokens. Returned payment data includes a 3D Secure cryptogram generated on the device. You are not redirected to authenticate the payment.  
    &nbsp;  
    For more information about testing, see Google Pay – [Test with sample tokens](https://developers.google.com/pay/api/web/guides/resources/sample-tokens).
&nbsp;  
3. Check the status of the payment in your [test dashboard](https://testmerchant.multisafepay.com/).

For support, email <integration@multisafepay.com>

{{< /details >}}

{{< details title="PayPal" >}}

**Test a PayPal order**

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder) > Wallet order (Example: PayPal direct).
2. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

---

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

---

**Change the order status**

You can change the order status to:

| Status | Description | Test scenario |
| --- | --- | --- |
| **Completed** | Order was completed | Completed  |
| **Void** | Order was cancelled | Cancelled  |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted after 2 minutes | Initialized completed |

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant test scenario.

{{< /details >}}

{{< details title="WeChat Pay" >}}

1. [Create order](https://api-docs.multisafepay.com/reference/createorder) > Wallet order (Example: WeChat direct/redirect).
2. Scan the QR code with a general QR reader (**not** the WeChat app or an error occurs).
3. On the **Test platform** page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

## Read more

{{< two-buttons href-2="/getting-started/test-your-integration" header-2="Read more" text-2="Test your integration" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/getting-started/test-your-integration/testing-refunds" header-2="Read more" text-2="Testing refunds" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
