---
title : 'Refunds'
category: 6278c92bf4ad4a00361431b0
order: 700
hidden: false
slug: 'refunds'
---
This page provides information about processing refunds with MultiSafepay. 

- Refunds can only be processed for payments linked to transactions, otherwise the customer receives credit on their invoice instead.
- Refunds are only processed if there are enough funds in your MultiSafepay balance.
- Customers receive refunds in the bank account they originally paid from.

# Full and partial refunds

You can process refunds:

- Via our API – [Refund order](https://docs-api.multisafepay.com/reference/refundorder)
- In most of our [ready-made integrations](/integrations/ready-made/)
- Via your dashboard

<details id="how-to-refund-via-your-dashboard">
<summary>How to refund via your dashboard</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.  
3. Under **Order summary**, click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
4. Click **Continue**, and then click **Confirm**.

The refund becomes a new transaction, which you can find on the original **Transaction details** page under **Related transactions**.

The status of the refund starts as **reserved**, and changes to **completed** at midnight. 

</details>

# Pay later refunds 

You can refund [pay later](/pay-later/) orders via:

- API – [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund
- Your dashboard

<details id="full-amount-via-dashboard">
<summary>Full amount via dashboard</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.
3. Under **Order summary**, click **Refund order**, and then click **Refund complete order**.
4. Add any relevant comments in the **Description** field.
5. Click **Save item changes**.  
  The order status changes to **void**.

</details>

<details id="partial-amount-via-dashboard">
<summary>Partial amount via dashboard</summary>
<br>

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
  A new refund transaction is generated and the order status is **completed**.

</details>
<br>

---

# User guide

## Batches

You can process refunds in batches using our PHP refund script. 

<details id="how-to-batch-refunds">
<summary>How to batch refunds</summary>
<br>

Make sure you have a PHP interpreter installed.

For instructions and to download, see MultiSafepay GitHub – [Refund script](https://github.com/MultiSafepay/refund-script).

Provide your [site API key](/account/websites/#viewing-the-site-id-api-key-and-secure-code) and a .csv file specifying the order ID, amount, and a description of all the transactions in the batch.

</details>

## Cancellation

<details id="how-to-cancel-refunds">
<summary>How to cancel refunds</summary>
<br>

- You can cancel a refund via MultiSafepay while the status is **Initialized** or **Reserved**, which is until midnight on the day the refund was initiated. 
- At midnight, the transaction is passed to the customer's bank to process. 
- Then the status changes to **Completed** and you can no longer cancel it via MultiSafepay.

</details>

## Live refunds

For some payment methods, refund orders in the live environment are processed automatically.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

Refund orders in the live environment are processed automatically for the following methods:

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Wallets: Alipay, PayPal, WeChat Pay

</details>

## Processing time

- Banking methods and credit cards: 1 business day 
- Bank Transfer: 2 to 3 business days, depending on the customer's bank

## Refunding more than the original amount

You can refund customers more than the amount of the original transaction, e.g. if you want to cover the customer's postage costs when returning an order. A maximum amount applies.

<details id="how-to-refund-more-than-original-amount">
<summary>How to refund more than the original amount</summary>
<br>

**Supported payment methods** 

- All banking methods, except EPS and SEPA Direct Debit
- Gift cards
- Paysafecard
- Alipay

**Activation**

Email a request to <sales@multisafepay.com>

The Risk Team assesses your request. Once approved, we enable it for your account.

</details>

## Testing

<details id="how-to-test-refunds-via-your-dashboard">
<summary>How to test refunds via your dashboard</summary>
<br>

You can process full refunds in your [MultiSafepay test dashboard](https://testmerchant.multisafepay.com/). 

Partial refunds are not enabled by default. To enable this, email <integration@multisafepay.com>

If you refund a payment in your MultiSafepay test dashboard, the [transaction status](/payment-statuses/) remains **reserved** or **initialized** until the refund is manually approved, since there is no settlement with a bank.

Follow these steps:

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder). 
2. Wait until the transaction status changes to **completed**.
3. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **Amount** field the amount to refund.  
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
    A new order is created for the refund, with status **reserved** or **initialized**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **completed**.

**Supported payment methods**

- Banking methods: Bancontact (not QR), Bank Transfer, Belfius, CBC/KBC, Dotpay, EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3, Klarna
- Wallets: Alipay, PayPal, WeChat Pay

</details>

<details id="how-to-test-refunds-via-api">
<summary>How to test refunds via API</summary>
<br>

1. [Create an order](https://docs-api.multisafepay.com/reference/createorder). 
2. Make a [refund](https://docs-api.multisafepay.com/reference/refundorder) API request.
    A new order is created for the refund. The order status for the refund changes to **reserved** or **initialized**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
    The order status changes to **completed**.

**Supported payment methods**

- Banking methods: Bancontact (not QR), EPS, Giropay, iDEAL (not QR), SEPA Direct Debit, Sofort, Trustly
- Credit and debit cards
- Pay later: in3
- Wallets: PayPal, WeChat Pay

</details>

## Time limits

There is a limit on how long after payment was completed that you can refund via MultiSafepay. After this time, we recommend using a Bank Transfer (no time limit, so long as the receiving bank can process the refund).

<details id="multiSafepay-time-limits">
<summary>MultiSafepay time limits</summary>
<br>

| Refund period   | Payment methods  |
|---|---|
| 60 days | PayPal |
| 180 days | All credit and debit cards, Bancontact, Paysafecard |
| 365 days | Alipay, Trustly, WeChat Pay |
| 730 days | All pay later methods, all banking methods except Trustly |

</details>

<br>

> 📘 **More info**
> For more information or support, email <integration@multisafepay.com>