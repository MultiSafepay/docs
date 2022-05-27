---
title: "Transaction expiration per payment method"
weight: 40
meta_title: "Transaction expiration per payment method - MultiSafepay Docs"
read_more: "."
url: "/developer/transaction-expiration/"
---
Different payment methods set different expiration times for transactions. The time begins:

- For direct requests: When you make the [create order](https://docs-api.multisafepay.com/reference/createorder)  request.
- For redirect requests: When the customer selects the payment method on the [payment page](/payment-pages/). 

The expiration time is set by the payment method and cannot be changed.

{{< blue-notice >}}**Note:** Transaction expiration times are different to session lifetimes of payment pages. {{< /blue-notice >}}

The table below sets out the expiration time per payment method:

| Payment method | Expiration time |
|---|---|
| **Credit and debit cards** {{< br >}} American Express, Cartes Bancaires, Dankort, Maestro, Mastercard, Visa, V Pay | 1 hour |
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

## Exceptions

Transactions do not expire for:

- E-Invoicing
- EPS 
- Giropay 
- Gift cards and Edenred vouchers
- SEPA Direct Debit