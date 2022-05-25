---
title : "About refunds"
weight: 10
layout: 'single'
meta_title: "About refunds - MultiSafepay Docs"
short_description: "Refund rules, processing times, and cancelling refunds."
read_more: "."
url: '/refunds/about/'
---

This page provides information about processing refunds with MultiSafepay. 

For support with refunds, email <support@multisafepay.com>

## Refund rules

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions, otherwise the customer receives credit on their invoice instead.

- Customers receive refunds in the bank account they originally paid from.

## Processing times

Refund processing time per payment method:

- Banking methods: 1 business day 
- Bank Transfer: 2 to 3 business days, depending on the customer's bank
- Credit cards: 1 business day 

## MultiSafepay time limit

There is a limit on how long after payment was completed that you can refund via MultiSafepay. After this time, we recommend using a bank transfer (no time limit, so long as the receiving bank can process the refund).

| Refund period   | Payment methods  |
|---|---|
| 60 days | PayPal |
| 180 days | All credit and debit cards, Bancontact, Paysafecard |
| 365 days | Alipay, Trustly, WeChat Pay |
| 730 days | All pay later methods, all banking methods except Trustly |

## Refunding more than the original amount amount
Applies to: 

- All banking methods, except EPS and SEPA Direct Debit
- Gift cards
- Paysafecard
- Alipay

You can refund customers more than the amount of the original transaction, e.g. if you want to cover the customer's postage costs when returning an order. A maximum amount applies. 

To apply, follow these steps:

1. Email a request to <sales@multisafepay.com>
2. The Risk Team assesses your request. 
3. Once approved, the Risk Team enables the **Allow more than original** function for your MultiSafepay account.

## Cancelling refunds

- You can cancel a refund via MultiSafepay while the status is **Initialized** or **Reserved**, which is until midnight on the day the refund was initiated. 
- At midnight, the transaction is passed to the customer's bank to process. 
- Then the status changes to **Completed** and you can no longer cancel it via MultiSafepay.

## Batching refunds

You can process refunds in batches using our refund script. 

Provide:

- A .csv file specifying the order ID, amount, and description of all the transactions
- Your [API key](/glossaries/multisafepay-glossary/#api-key)

The script is written in PHP, so make sure you have a PHP interpreter installed.

For how to use the script and to download, see MultiSafepay GitHub – [Refund script](https://github.com/MultiSafepay/refund-script).

For support, email <integration@multisafepay.com>
