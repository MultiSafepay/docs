---
title: Transaction expiration
category: 623dacddb0cbdd0394b9f5a9
slug: 'transaction-expiration'
order: 6
hidden: false
---

Different payment methods set different expiration times for transactions. The time begins:

- For direct requests: When you make the [create order](/reference/createorder) request.
- For redirect requests: When the customer selects the payment method on the [payment page](/docs/payment-pages/).

The expiration time is set by the payment method and cannot be changed.

**Note:** Transaction expiration times are different to session lifetimes of payment pages.

The table below sets out the expiration time per payment method:

| Payment method | Expiration time |
|---|---|
| **Cards** <br> American Express, Cartes Bancaires, Dankort, <br> Maestro, Mastercard, Visa, V Pay | 1 hour  |
| AfterPay                                                                                                           | 90 days                                        |
| Alipay                                                                                                             | 5 hours                                        |
| Alipay+                                                                                                            | 10 minutes on Alipay+, after 1 hour in our system |
| Apple Pay                                                                                                          | 1 hour                                         |
| Bancontact                                                                                                         | Banking: 1 hour, QR: Doesn't apply             |
| Bank transfer                                                                                                      | 60 days                                        |
| Belfius                                                                                                            | 5 days                                         |
| Betaal per Maand                                                                                                   | 1 day                                          |
| CBC/KBC                                                                                                            | 5 days                                         |
| Dotpay                                                                                                             | 3 days                                         |
| Google Pay                                                                                                         | 1 hour                                         |
| iDEAL                                                                                                              | 1.5 hours                                      |
| in3                                                                                                                | 2 hours                                        |
| Klarna                                                                                                             | 1 hour                                         |
| MyBank                                                                                                             | 1 hour                                         |
| Pay After Delivery                                                                                                 | 90 days                                        |
| PayPal                                                                                                             | 14 days                                        |
| Paysafecard                                                                                                        | 3 hours                                        |
| Request to Pay                                                                                                     | 1 hour                                         |
| Sofort                                                                                                             | 1 day                                          |
| Trustly                                                                                                            | 2 hours                                        |
| TrustPay                                                                                                           | 10 days                                        |
| WeChat Pay                                                                                                         | 2 hours                                        |

# Exceptions

Transactions do not expire for:

- E-Invoicing
- EPS 
- Giropay 
- Gift cards and Edenred vouchers
- Direct debits