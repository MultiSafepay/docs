---
title : "Testing refunds"
meta_title: "Testing - Testing refunds - MultiSafepay Docs"
read_more: "."
url: '/testing/testing-refunds/'
aliases:
    - /tools/multisafepay-test-environment/test-and-live-refunds/
    - /getting-started/test-your-integration/testing-refunds
---

You can process full refunds in your [MultiSafepay test dashboard](https://testmerchant.multisafepay.com/). 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the [transaction status](/about-payments/multisafepay-statuses/) remains **Reserved** or **Initialized** until the refund is manually approved, since there is no settlement with a bank.

## Test refunding an order

{{< details title="Supported payment methods" >}}

You can test refunds for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

{{< /details >}}

To test refunding an order:

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder). 
2. Wait until the transaction status changes to **Completed**.
3. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **Amount** field the amount to refund.  
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
{{< br >}} A new order is created for the refund, with status **Reserved** or **Initialized**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

## Test an API refund

{{< details title="Supported payment methods" >}}

You can test refunds for the following methods:

- Banking methods: Bancontact (not QR), EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3
- Wallets: PayPal, WeChat Pay

{{< /details >}}

To test refunding an order via the API:

1. [Create an order](https://api-docs.multisafepay.com/reference/createorder). 
2. Make a [refund](https://api-docs.multisafepay.com/reference/refundorder) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved** or **Initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

## Live environment

For some payment methods, refund orders in the live environment are processed automatically.

{{< details title="Supported payment methods" >}}

Refund orders in the live environment are processed automatically for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

{{< /details >}}