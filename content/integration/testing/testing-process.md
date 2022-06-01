---
title : "Testing process"
weight: 10
meta_title: "Testing - Testing process - MultiSafepay Docs"
read_more: "."
url: "/testing/testing-process/"
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

For all payment methods **except** AfterPay, you need your site's test [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).

## Make a test payment

1. Initiate a payment in your [ready-made integration](/integrations/) or via our API:  

    {{< details title="Ready-made integration" >}}

- In your backend, enter your test site [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
- Place a test order, and then initiate a transaction with the payment method you are testing. 

    {{< /details >}}
    {{< details title="API" >}}
  
- [Create an order](https://docs-api.multisafepay.com/reference/createorder) via our API to the test endpoint: `https://testapi.multisafepay.com/v1/json/` 
- For example requests for specific payment methods, see **Examples**.
    {{< /details >}}
2. Enter the [test payment details](/testing/test-payment-details/) for the payment method you are testing, or select a payment scenario.
3. Complete the test payment.
4. To check the transaction details, sign in to your [test dashboard](https://testmerchant.multisafepay.com/).
5. Go to **Transactions** > **Transactions overview**.
6. In the **Transactions overview** list, select the transaction to view the **Transaction details** page. 
7. To check that you have succesfully connected to our system, under **Offline actions**, check that you've correctly received the **notifyMerchantTrans** action. For information about errors, see [HTTP errors](/developers/http-errors/).

{{< blue-notice >}} Once your live account is approved, make sure you use the site API key from your **live** account instead of your test account. {{< /blue-notice >}}

## Test cancelling an order

{{< details title="Supported payment methods" >}}

You can test cancelling orders for the following methods:

- Banking methods: Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Wallets: Alipay, PayPal

{{< /details >}}

To test cancelling an order:

1. Create an order in your backend or via the API as above.
2. On the **Test platform** page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.


