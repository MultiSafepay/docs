---
title : "Refunds"
weight: 20
meta_title: "Refunds - MultiSafepay Docs"
layout: 'single'
read_more: '.'
block-range-pages: '.'
url: '/refunds/'
logo: '/svgs/Refunds.svg'
short_description: 'Process refunds in your dashboard, from your ready-made integration, or via our API'
aliases:
    - /faq/refunds
    - /faq/refunds/initiating-refunds/
    - /faq/refunds/initiating-refunds-in-batches/
    - /faq/refunds/cancelling-refunds/
    - /faq/refunds/refund-period-for-payment-methods/
    - /faq/refunds/refund-processing-time/
    - /faq/refunds/delays-in-processing-refunds/
    - /faq/refunds/using-the-refund-script
    - /faq/refunds/refund-an-order
    - /faq/finance/how-can-i-perform-a-refund
    - /faq/finance/paying-refunds
    - /faq/refunds/initiating-refunds
    - /faq/refunds/refund-period-payment-methods
    - /faq/refunds/
    - /faq/refunds/how-long-does-a-refund-take-to-process
     - /faq/refunds/can-i-cancel-an-initiated-refund
    - /faq/finance/paying-out-funds-from-your-multisafepay-control
    - /faq/finance/refund-more-than-original-amount
    - /tools/multisafepay-control/processing-refunds
    - /payments/refunds/
    - /refunds/about/
    - /refunds/full-partial/
    - /refunds/pay-later/
    - /tools/multisafepay-test-environment/test-and-live-refunds/
    - /getting-started/test-your-integration/testing-refunds
    - /testing/testing-refunds/
---

This page provides information about processing refunds with MultiSafepay. 

- Refunds can only be processed for payments linked to transactions, otherwise the customer receives credit on their invoice instead.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Customers receive refunds in the bank account they originally paid from.

## Full and partial refunds

You can process refunds:

- Via our API – [Refund order](https://docs-api.multisafepay.com/reference/refundorder)
- In most of our [ready-made integrations](/integrations/ready-made/)
- Via your dashboard

{{< details title="Refunding via your dashboard" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.  
3. Under **Order summary**, click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
4. Click **Continue**, and then click **Confirm**.

The refund becomes a new transaction, which you can find on the original **Transaction details** page under **Related transactions**.

The status of the refund starts as **Reserved**, and changes to **Completed** at midnight. 
{{< /details >}}

## Pay later refunds 

You can refund [pay later](/payment-methods/pay-later/) orders via:

- API – [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund
- Your dashboard

{{< details title="Full amount via dashboard" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.
3. Under **Order summary**, click **Refund order**, and then click **Refund complete order**.
4. Add any relevant comments in the **Description** field.
5. Click **Save item changes**.  
  The order status changes to **Void**.
{{< /details >}}

{{< details title="Partial amount via dashboard" >}}

To refund part of the amount:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.
3. Under **Order summary**, click **Change order**.
    - In the **Quantity** field, enter the number of units to refund.
    - In the **Name** field, enter the name of the item to refund.
    - In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
4. Click **Add**, and then check that the **New total** amount is correct. 
5. To display a field to enter add any relevant comments, click **Description**.
6. Click **Save item changes**.  
  A new refund transaction is generated and the order status is **Completed**.
{{< /details >}}

## Processing times

Refund processing time per payment method:

- Banking methods and credit cards: 1 business day 
- Bank Transfer: 2 to 3 business days, depending on the customer's bank

## MultiSafepay time limit

There is a limit on how long after payment was completed that you can refund via MultiSafepay. After this time, we recommend using a bank transfer (no time limit, so long as the receiving bank can process the refund).

{{< details title="MultiSafepay time limits" >}}

| Refund period   | Payment methods  |
|---|---|
| 60 days | PayPal |
| 180 days | All credit and debit cards, Bancontact, Paysafecard |
| 365 days | Alipay, Trustly, WeChat Pay |
| 730 days | All pay later methods, all banking methods except Trustly |

{{< /details >}}

## Refunding more than the original order amount

You can refund customers more than the amount of the original transaction, e.g. if you want to cover the customer's postage costs when returning an order. A maximum amount applies.

{{< details title="Refunding more than the original amount" >}}

**Supported payment methods** 

- All banking methods, except EPS and SEPA Direct Debit
- Gift cards
- Paysafecard
- Alipay

**Activation**

Email a request to <sales@multisafepay.com>

The Risk Team assesses your request. Once approved, we enable it for your account.

{{< /details >}}

## Cancelling refunds

You can cancel refunds via your dashboard. 

{{< details title="Cancelling refunds" >}}

- You can cancel a refund via MultiSafepay while the status is **Initialized** or **Reserved**, which is until midnight on the day the refund was initiated. 
- At midnight, the transaction is passed to the customer's bank to process. 
- Then the status changes to **Completed** and you can no longer cancel it via MultiSafepay.

{{< /details >}}

## Testing refunds

{{< details title="Testing refunds via your dashboard" >}}

**Payment methods**

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

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
{{< br >}} A new order is created for the refund, with status **Reserved** or **Initialized**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

{{< /details >}}

{{< details title="Testing refunds via API" >}}

**Payment methods**

- Banking methods: Bancontact (not QR), EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3
- Wallets: PayPal, WeChat Pay

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder). 
2. Make a [refund](https://docs-api.multisafepay.com/reference/refundorder) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved** or **Initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

{{< /details >}}

## Batching refunds

You can process refunds in batches using our PHP refund script. 

{{< details title="Batching refunds" >}}

Make sure you have a PHP interpreter installed.

For instructions and to download, see MultiSafepay GitHub – [Refund script](https://github.com/MultiSafepay/refund-script).

Provide your [site API key](/account/websites/#viewing-the-site-id-api-key-and-secure-code) and a .csv file specifying the order ID, amount, and a description of all the transactions in the batch.

{{< /details >}}

You can process full refunds in your [MultiSafepay test dashboard](https://testmerchant.multisafepay.com/). 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the [transaction status](/about-payments/multisafepay-statuses/) remains **Reserved** or **Initialized** until the refund is manually approved, since there is no settlement with a bank.

## Live refunds

For some payment methods, refund orders in the live environment are processed automatically.

{{< details title="Payment methods" >}}

Refund orders in the live environment are processed automatically for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

{{< /details >}}

{{< blue-notice >}} **Support** <br> Email <integration@multisafepay.com> {{< /blue-notice >}}




