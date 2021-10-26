---
title: 'PayPal product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "PayPal product rules - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payment-methods/paypal/product-rules/'
aliases:
    - /payments/methods/wallet/paypal/about/
    - /payments/methods/paypal/product-rules/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](https://developer.paypal.com/docs/payouts/reference/country-and-currency-codes/) | 
| **Chargebacks**  | Yes | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#paypal-direct) / [Redirect](/api/#paypal-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 14 days | |
| **Adjust payment link lifetimes**  | Links are valid for 14 days. The lifetime is set by PayPal. | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="PayPal Seller Protection" >}}

PayPal Seller Protection covers you in the event of claims, chargebacks, or reversals due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. For a list of the countries, see PayPal API – [State codes](https://developer.paypal.com/docs/nvp-soap-api/state-codes).

For more information, see PayPal – [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156). 

{{< /details >}}

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 60 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your PayPal business account. Otherwise, PayPal issues an [eCheck](https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082). To avoid PayPal cancelling the refund, in your PayPal account authorize PayPal to withdraw funds from another bank account instead. For any questions, contact PayPay – [Help Center Home](https://www.paypal.com/us/smarthelp/home).

- The customer receives the refund in the bank account they originally paid from within the next business day.

{{< /details >}}

You can only decline or authorize **Uncleared** transactions in your PayPal account.