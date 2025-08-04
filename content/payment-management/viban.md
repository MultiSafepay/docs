---
title: Virtual IBANs
category:
  uri: Payment management
slug: virtual-ibans
position: 8
privacy:
  view: public
content:
  excerpt: Collect bank transfers and direct debits in your own bank account.
---
A virtual international bank account number (VIBAN) in your company name improves the customer experience for [bank transfers](/docs/bank-transfer/) and [SEPA direct debits](/docs/direct-debit/):

* Customers appear to pay your company directly, instead of a collecting party.
* Customers receive refunds in your name rather than from MultiSafepay.
* You can resolve unmatched bank transfers yourself.

# How it works

A VIBAN isn't connected to an actual bank account. It simply routes incoming funds to MultiSafepay's account to collect as normal.

### Improve customer experience

Customers are not always aware of the role of a payment service provider, and may be confused by seeing MultiSafepay's name in payment instructions and on their bank statement.

With a VIBAN, bank transfer instructions on [payment pages](/docs/payment-pages/) and in emails display your name and VIBAN instead of MultiSafepay's.

Descriptors on bank statements for both payments and refunds display "\[Merchant name] by MultiSafepay", making it easier for your customers to recognize you.

Increasing brand recognition helps reduce your customer support load and potential [chargebacks](/docs/direct-debit#chargebacks).

### Match payments

With a VIBAN, you gain access to a dedicated tool in your dashboard to resolve unmatched bank transfers yourself. See [Matching payments](#matching-payments) below.

### Other benefits

VIBANs are quick and easy to set up, compared to bank accounts. This makes them particularly suitable for processing payments abroad.

They are also beneficial for B2B and B2C cases, where manual bank transfers and direct debits are frequently used.

# Activation

You can apply for a VIBAN for all websites under your MultiSafepay account, or for a specific website.

Email a request for a VIBAN to [sales@multisafepay.com](mailto:sales@multisafepay.com)

Include in the request:

* The company name you want to display to customers
* The payment methods you want to use the VIBAN for: bank transfers, SEPA direct debits, or both
* Whether you want the bank transfer matching tool
* Whether you want to use the VIBAN to receive payments only, or also to process refunds

# Integration

Once activated, no integration is required.

***

# User guide

## Currencies

VIBANs can only be used for transactions in EUR.

## Matching payments

Most incoming payments are automatically matched to the relevant `{order}` in your account. However, if the customer accidentally provides incorrect information or pays the wrong amount, MultiSafepay matches them manually. See Bank transfer – [Matching payments](/docs/bank-transfer#matching-payments).

With a VIBAN, you can resolve unmatched payments yourself in your MultiSafepay dashboard. You need to request this functionality when applying for your VIBAN.

Once activated, an alert appears on your dashboard home page when you have unmatched payments to resolve. A new section appears under **Transactions**, called **Unmatched payments**. With this tool, you can perform the following actions:

| Unmatched payment | Action                                              | Outcome                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Correct amount    | Match to order                                      | The `{order status}` changes to **Completed**. <br /> An explanation appears on the **Transaction details** page under **Notes**.                                                                                                                                                                                                                                                                    |
| Amount too high   | Match and refund the excess                         | The order status changes to **Completed**. <br /> A new refund order linked to the original order is created for the excess amount, and an explanation appears on the **Transaction details** page under **Notes**.                                                                                                                                                                                  |
|                   | Partially match and reserve the excess              | The order status changes to **Completed**. <br /> The excess amount is reserved for future orders.                                                                                                                                                                                                                                                                                                   |
|                   | Match and keep the excess                           | The order status changes to **Completed**. <br /> A new order (status **Completed**) linked to the original order is created to credit the excess to your account balance. <br /> - An explanation appears on the **Transaction details** page under **Notes**.                                                                                                                                      |
| Amount too low    | Match and make up deficit from your account balance | The order status changes to **Completed**. <br /> The deficit is debited from your balance as a transaction fee. <br /> - An explanation appears on the **Transaction details** page under **Notes**.                                                                                                                                                                                                |
|                   | Match and collect deficit                           | The order status changes to **Completed**. <br /> A new bank transfer order (linked to the original order) is created with a payment link for the customer to pay the outstanding amount.                                                                                                                                                                                                            |
| Refund requested  | Refund in full                                      | A refund order linked to the original order is created and the payment is refunded.                                                                                                                                                                                                                                                                                                                  |
| Lump payment      | Match the payment to multiple orders                | Divide the payment across multiple orders and their status changes to **Completed**. <br /> If there is any excess after all relevant orders are matched, you can refund, reserve, or keep the excess (see above). <br /> If there are not enough funds for all relevant orders, you can make up the deficit from your account balance or create a new order for the outstanding amount (see above). |

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
