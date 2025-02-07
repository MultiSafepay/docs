---
title: 'Refunds'
category: 6278c92bf4ad4a00361431b0
order: 4
hidden: false
slug: 'refund-payments'
---
This page provides information about processing refunds with MultiSafepay. 

- Refunds can only be processed for payments linked to transactions, otherwise the customer receives credit on their invoice instead.
- Refunds are only processed if there are enough funds in your account balance.
- Customers receive refunds in the bank account they originally paid from.

For information about credit and debit card refunds and reversals, see [Card refunds](/docs/card-refunds/).

# Full and partial refunds

You can process refunds:

- Via our API – [Refund order](/reference/refundorder/)
- In most of our [ready-made integrations](/docs/our-integrations/)
- Via your dashboard

<details id="how-to-refund-via-your-dashboard">
<summary>How to refund via your dashboard</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.  
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.  
3. On the **Transaction details** page, under **Order summary**, click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
4. Click **Continue**, and then click **Confirm**.

The refund becomes a new transaction, which you can find on the original **Transaction details** page under **Related transactions**.

The status of the refund starts as **Reserved**, and changes to **Completed** at midnight. 

</details>

# BNPL refunds 

You can refund <<glossary:BNPL>> orders via:

- API – [Refund order](/reference/refundorder/) > BNPL refund
- Your dashboard

<details id="full-amount-via-dashboard">
<summary>Full amount via dashboard</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction. 
3. On the **Transaction details** page, under **Order summary**, click **Refund order** > **Refund whole order**.
4. Add any relevant comments in the **Description** field.
5. Click **Save changes**.  
  The <<glossary:order status>> changes to **Void**.

</details>

<details id="partial-amount-via-dashboard">
<summary>Partial amount via dashboard</summary>
<br>

To refund part of the amount:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction. 
3. On the **Transaction details** page, under **Order details**, click **Edit order**.
    - In the **Quantity** field, enter the number of units to refund.
    - In the **Name** field, enter the name of the item to refund.
    - In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
4. Click **Add**, and then check that the **Total** amount is correct. 
5. To display a field to enter add any relevant comments, click **Description**.
6. Click **Save changes**.  
  A new refund transaction is generated and the <<glossary:order status>> is **Completed**.

</details>

# Card refunds

For information about credit and debit card refunds and reversals, see [Card refunds](/docs/card-refunds/).

<br>

---

# User guide

## Amount limits

You can refund customers more than the amount of the original transaction, e.g. if you want to cover the customer's postage costs when returning an order. A maximum amount applies.

<details id="how-to-refund-more-than-original-amount">
<summary>How to refund more than the original amount</summary>
<br>

**Supported payment methods** 

- All banking methods, except direct debit and EPS
- Gift cards
- Paysafecard
- Alipay

**Activation**

Email a request to <sales@multisafepay.com>

The Risk Team assesses your request. Once approved, we enable it for your account.

</details>

## Batches

You can process refunds in batches using our PHP refund script. 

<details id="how-to-batch-refunds">
<summary>How to batch refunds</summary>
<br>

Make sure you have a PHP interpreter installed.

For instructions and to download, see MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/refund-script" target="_blank">Refund script</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

Provide your [website API key](/docs/sites#site-id-api-key-and-security-code) and a .csv file specifying the order ID, amount, and a description of all the transactions in the batch.

</details>

## Cancellation

You can cancel a refund via MultiSafepay while the status is **Initialized** or **Reserved**, which is until midnight on the day the refund was initiated. At midnight, the transaction is passed to the customer's bank to process. Then the status changes to **Completed** and you can no longer cancel it via MultiSafepay.

You can't cancel <<glossary:reversals>>. For more information, see [Card payments - Reversals](/docs/card-payments#reversals).

## Live refunds

For some payment methods, refund orders in the live environment are processed automatically.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

Refund orders in the live environment are processed automatically for the following methods:

- Banking methods: Bancontact (not QR), bank transfers, Belfius, CBC/KBC, direct debits, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

</details>

## Processing times

- Banking methods: 1 business day 
- Bank transfers: 2 to 3 business days, depending on the customer's bank
- Cards: 1 to 14 business days, depending on the <<glossary:issuer>>

## Refund receipts

If a customer wants a receipt for a refund, you can download a PDF version from your dashboard. This is supported for all payment methods except <<glossary:BNPL>>.

<details id="how-to-download-refund-receipt">
<summary>How to download a refund receipt</summary>
<br>

To download a refund receipt:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**.
3. In the **Keyword** search box, enter "refund", and then click **Search** (or press **Enter**).
4. Click the relevant transaction. 
5. On the **Transaction details** page, under **Transaction summary**, click the **PDF icon** next to **Payment method: Refund**
     The receipt PDF is downloaded.

</details>

For how to add your header or logo to the receipt, see [Logos and icons](/docs/sites#logos-and-icons).

## Testing

<details id="how-to-test-refunds-via-your-dashboard">
<summary>How to test refunds via your dashboard</summary>
<br>

You can process full refunds in your <a href="https://testmerchant.multisafepay.com/" target="_blank">MultiSafepay test dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the <<glossary:transaction status>> remains **reserved** or **Initialized** until the refund is manually approved, since there is no involvement with a bank.

Follow these steps:

1. [Create an order](/reference/createorder/). 
2. Wait until the <<glossary:transaction status>> changes to **Completed**.
3. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **Amount** field the amount to refund.  
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
    A new <<glossary:order>> is created for the refund, with status **reserved** or **Initialized**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The <<glossary:order status>> changes to **Completed**.

**Supported payment methods**

- Banking methods: Bancontact (not QR), bank transfers, Belfius, CBC/KBC, direct debits, Dotpay, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- <<glossary:BNPL>>: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

</details>

<details id="how-to-test-refunds-via-api">
<summary>How to test refunds via API</summary>
<br>

1. [Create an order](/reference/createorder/). 
2. Make a [refund](/reference/refundorder/) API request.
    A new order is created for the refund. The <<glossary:order>> status for the refund changes to **reserved** or **Initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
    The <<glossary:order status>> changes to **Completed**.

**Supported payment methods**

- Banking methods: Bancontact (not QR), direct debits, EPS, Giropay, iDEAL (not QR), Sofort, Trustly
- Credit and debit cards
- <<glossary:BNPL>>: in3
- Wallets: PayPal, WeChat Pay

</details>

## Time limits

There is a limit on how long after payment was completed that you can refund via MultiSafepay. After this time, we recommend doing a bank transfer (no time limit, so long as the receiving bank can process the refund).

<details id="multiSafepay-time-limits">
<summary>MultiSafepay time limits</summary>
<br>

| Refund period   | Payment methods  |
|---|---|
| 60 days | PayPal |
| 180 days | All credit and debit cards, Bancontact, Paysafecard |
| 365 days | Alipay, Trustly, WeChat Pay |
| 730 days | All <<glossary:BNPL>> methods, all banking methods except Trustly |

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
