---
title: 'Virtual IBANs'
weight: 95
meta_title: "Virtual IBANs - MultiSafepay Docs"
logo: '/svgs/Banks.svg'
layout: 'single'
short_description: "Collect bank transfers and direct debits in your own bank account."
url: '/features/virtual-ibans/'
---
A virtual international bank account number (IBAN) routes incoming [Bank Transfer](/payment-methods/bank-transfer/) and [SEPA Direct Debit](/payment-methods/sepa-direct-debit/) payments into your business bank account, instead of MultiSafepay collecting them on your behalf. It is not itself connected to an actual bank account.   

## How it works

You can link a virtual IBAN to your MultiSafepay account, or to a specific site.

Virtual IBANs can only be used for transactions in EUR. 

### Bank Transfer

Customers are provided your virtual IBAN to make the transfer to (instead of MultiSafepay's IBAN) in:

- [MultiSafepay payment pages](/payment-pages/)
- Emails containing payment instructions (including for the [direct flow](/payment-methods/bank-transfer/payment-flow/))

### SEPA Direct Debit 

There is no change for the customer, as they don't see your virtual IBAN when completing payment. But your company name displays on their bank statement instead of MultiSafepay's name. This increases brand recognition and trust, which can reduce [chargebacks](/payment-methods/sepa-direct-debit/overview/#chargebacks).

## Matching payments

Most incoming payments are automatically matched the relevant order in your account. However, if the customer accidentally provides incorrect information or pays the wrong amount, payments need to be matched manually. 

With a virtual IBAN, you can resolve unmatched payments in your MultiSafepay dashboard, instead of MultiSafepay doing it on your behalf (see [Resolving unmatched Bank Transfer payments](/bank-transfer/unmatched-payments/)).

Once activated, an alert appears on your dashboard home page when you have unmatched payments to resolve. 

A new section appears under **Transactions**, called **Unmatched payments**. In this tool, you can perform the following actions: 

| Unmatched payment | Action | Outcome |
|---|---|---|
| Correct amount | Match to order | The order status changes to **Completed**. {{< br >}} An explanation appears on the **Transaction details** page under **Notes**.|
| Amount too high | Match and refund the excess | The order status changes to **Completed**. {{< br >}} A new refund order linked to the original order is created for the excess amount, and an explanation appears on the **Transaction details** page under **Notes**. |
|  | Partially match and reserve the excess | The order status changes to **Completed**. {{< br >}} The excess amount is reserved for future orders. |
|  | Match and keep the excess | The order status changes to **Completed**. {{< br >}} A new Bank Transfer order (status **Completed**) linked to the original order is created to credit the excess to your MultiSafepay balance: {{< br >}} - The order is flagged as `viban-fund-balance`. {{< br >}} - An explanation appears on the **Transaction details** page under **Notes**. |
| Amount too low | Match and make up deficit from your MultiSafepay balance | The order status changes to **Completed**. {{< br >}} A new order linked to the original order is created to debit the deficit from your balance: {{< br >}} - The order is flagged as `viban-charge-balance`. {{< br >}} - An explanation appears on the **Transaction details** page under **Notes**. |
|  | Match and collect deficit | The order status changes to **Completed**. {{< br >}} A new order linked to the original order is created for the outstanding amount. |
| Refund requested | Refund in full | A refund order linked to the original order is created and the payment is refunded. |
| Lump payment | Match the payment to multiple orders | Divide the payment across multiple orders and their status changes to **Completed**. {{< br >}} If there is any excess after all relevant orders are matched, you can refund, reserve, or keep the excess (see above). {{< br >}} If there are not enough funds for all relevant orders, you can make up the deficit from your MultiSafepay balance or create a new order for the outstanding amount (see above).| 

## Refunds and payouts

You can also make [refunds](/refunds/) and [payouts](/account/payouts/) via Bank Transfer using your virtual IBAN, managed from your MultiSafepay dashboard. Your company name appears on bank statements instead of MultiSafepay's name.

## Activation

Email a request for a virtual IBAN to <sales@multisafepay.com>

Include in the request:

- Whether you want to use the refunds and matching tool in your dashboard
- What company name you want to appear on bank statements
- Which direction of funds to enable: credit, debit, or both