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
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to refund and click to open the **Transaction details** page.  
4. Click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
5. Click **Continue**, and then click **Confirm**.

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

- Click **Change order**.
- In the **Quantity** field, enter the number of units to refund.
- In the **Name** field, enter the name of the item to refund.
- In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
- From the **Tax** list, select **None (0.0%)**. 
- Click **Add**.
- Check that the **New total** amount is correct. 
- To display a field to enter add any relevant comments, click **Description**.
- Click **Save item changes**.  
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

## Batching refunds

You can process refunds in batches using our PHP refund script. 

{{< details title="Batching refunds" >}}

Make sure you have a PHP interpreter installed.

For instructions and to download, see MultiSafepay GitHub – [Refund script](https://github.com/MultiSafepay/refund-script).

Provide your [site API key](/account/websites/#viewing-the-site-id-api-key-and-secure-code) and a .csv file specifying the order ID, amount, and a description of all the transactions in the batch.

{{< /details >}}

{{< blue-notice >}} **Support** <br> Email <integration@multisafepay.com> {{< /blue-notice >}}




