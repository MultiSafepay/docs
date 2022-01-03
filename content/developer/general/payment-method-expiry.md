---
title: "Payment method expiry periods"
weight: 40
meta_title: "Payment method expiry periods - MultiSafepay Docs"
read_more: "."
url: '/developer/payment-method-expiry-periods/'
---
Different payment methods set different expiry periods for transactions. The period begins:

- For direct requests: When you make the `POST /orders` request.
- For redirect requests: When the customer selects the payment method on the [MultiSafepay payment page](/payment-pages/). 

This does **not** apply to:

- E-Invoicing
- EPS 
- Giropay 
- Gift cards and Edenred vouchers
- SEPA Direct Debit

For all [credit and debit cards](/payments/methods/credit-and-debit-cards/), transaction sessions expire after 1 hour.

The table below sets out the expiry period for all other payment methods:

| Payment method | Expiry period |
|---|---|
| AfterPay | 90 days |
| Alipay | 5 hours |
| Apple Pay | 1 hour |
| Bancontact | Banking: 1 hour, QR: Doesn't apply |
| Bank Transfer | 60 days |
| Belfius | 5 days |
| Betaal per Maand | 1 day |
| CBC/KBC | 5 days |
| Dotpay | 3 days |
| Google Pay | 1 hour |
| iDEAL | 1.5 hours |
| in3 | 2 hours |
| Klarna | 1 hour |
| Pay After Delivery | 90 days |
| PayPal | 14 days |
| Paysafecard | 3 hours |
| Request to Pay | 1 hour |
| Sofort | 1 day |
| Trustly | 2 hours |
| TrustPay | 10 days |
| WeChat Pay| 2 hours |

