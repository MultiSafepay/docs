---
title: "iDEAL product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "iDEAL product rules - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/iDeal.svg'
url: '/payment-methods/ideal/product-rules/'
aliases: 
    - /payment-methods/ideal/what-is-ideal/
    - /payments/methods/banks/ideal/about/
    - /payments/methods/ideal/product-rules/
    - /payments/methods/ideal-qr/product-rules/
---
 
|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Payment flow**  | Banking: [Direct](/api/#ideal---direct) / [Redirect](/api/#ideal---redirect) {{< br >}} QR: [Redirect](/api/#ideal-qr) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | Banking: Yes {{< br >}} QR: No | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Transactions expire after**  | 1.5 hours | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}
- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

To increase transparency for customers, the name of your website appears on the iDEAL payment page and "Your-website-name by MultiSafepay" on the customer's bank statement.

## iDEAL QR

iDEAL QR has a wide range of applications. Customers can scan QR codes off screens or paper, e.g. invoices, receipts. This makes it particularly suitable for hospitality, charity collectors, and home deliveries. 

For more information, see iDEAL – [Offer iDEAL QR](https://www.ideal.nl/en/businesses/offer-ideal-qr/).

- iDEAL QR is supported in all our [ready-made integrations](/payments/integrations/). 

- Not all Dutch banking apps support iDEAL QR yet, so we recommend that customers scan QR codes with their camera or a general QR reader. This redirects to the ideal.nl payment page, which works for all banks. 

- You can specify whether the same QR code can be used more than once.

- You can let customers change the amount to pay, e.g. for donations. 






