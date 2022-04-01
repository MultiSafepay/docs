---
title : "Testing process"
weight: 10
meta_title: "Testing - Testing process - MultiSafepay Docs"
read_more: "."
url: '/testing/testing-process/'
---

Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your [MultiSafepay test account](https://testmerchant.multisafepay.com/).

If you encounter any issues during testing, see [Understanding and resolving errors](/developer/errors-explained/understanding-and-resolving-errors/).

{{< details title="Methods not available in test environment" >}}

You can't test the following methods in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

- Betaal per Maand
- iDEAL QR
- Paysafecard
- Request to Pay
- TrustPay

{{< /details >}}

For support, email <integration@multisafepay.com>

## Test credentials

For all payment methods **except** AfterPay, you need your [API key](/account/site-id-api-key-secure-code/).

## 1. Initiate a transaction

There are two ways to initiate a transaction:

#### Ready-made integration

To create a test payment through your [ready-made integration](/integrations/):

1. Enter the [API key](/account/site-id-api-key-secure-code/) from your test account in your [backend](/glossaries/multisafepay-glossary/#backend).
2. Place a test order, and then initiate a transaction using the payment method you want to test.

#### Via our API

[Create an order](https://api-docs.multisafepay.com/reference/createorder) via our API to the test endpoint: `https://testapi.multisafepay.com/v1/json/`

See **Examples** for example requests for specific payment methods. 

Make sure you include **all** required parameters in the request.

## 2. Complete the payment

1. Enter the [test payment details](/testing/test-payment-details/) for the payment method you are testing, or select a payment scenario.
2. Complete the test payment.

## 3. Check the transaction details

To check the transaction details in your dashboard:

1. Go to **Transactions** > **Transactions overview**.
2. In the **Transactions overview** list, select the transaction to view the **Transaction details** page. 

## 4. Check your connection with MultiSafepay

To check that you have succesfully connected to our system, follow these steps:

1. Sign in to your [test dashboard](https://testmerchant.multisafepay.com/).
2. Go to **Transactions** > **Transactions overview**.
3. Select the transaction to view the **Transaction details** page.
4. Under **Offline actions**, in the **Status** field, check that you correctly received the MultiSafepay request. For information about errors, see [HTTP errors](/developer/errors-explained/http-errors/).

**Note:** Once your live account is approved, make sure you use the API key from your live account instead of your test account.

## Test cancelling an order

{{< details title="Supported payment methods" >}}

You can test refunds for the following methods:

- Banking methods: Belfius, CBC/KBC, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Wallets: Alipay, PayPal

{{< /details >}}

To test cancelling an order:

1. Create an order in your backend or via the API following the usual instructions.
2. On the **Test platform** page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.


