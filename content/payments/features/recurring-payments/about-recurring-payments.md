---
title : "About Recurring Payments"
weight: 51
meta_title: "About Recurring Payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: '.'
url: '/recurring-payments/about/'
aliases:
    - /tools/recurring-payments/what-is-recurring-payments
    - /payments/features/recurring-payments/about-recurring-payments/
---

Recurring Payments is a MutiSafepay solution let you automatically charge a customer's bank account or credit card on a regular basis, e.g. for a monthly or annual subscription. The customer must initiate the first payment.

## Supported payment methods

- Credit cards: Visa, Mastercard, American Express
- SEPA Direct Debit: SOFORT Banking, iDEAL
- Optionally, you can use iDEAL, Bancontact, or SOFORT Banking for the initial payment and continue with recurring direct debits.

We offer a work-around option to use Bancontact for the initial payment. For more information, email your account manager at <sales@multisafepay.com>

If you already process Recurring Payments for SEPA Direct Debit customers with another PSP, you cannot use Recurring Payments for the same customers with MultiSafepay. 

For these customers, you can use a [SEPA Direct Debit](/api/#direct-sepa-direct-debit) using the retrieved IBAN and account holder name.

## Requirements

You are responsible for scheduling recurring payments and optional retries.

You must inform customers about Recurring Payments and stored mandates:

- During the checkout process and/or in your general terms and conditions which the customer must agree to before checkout.
- Before each transaction, e.g. by email.
 
## Terminology

| Term    | Description  |
|---|---|
| Initial payment  | The first payment initiated by a customer having understood and approved Recurring Payments.  |
| Subsequent payments  | All payments after the initial payment.  |
| Single Euro Payments Area (SEPA)  | All countries within the European Union and Norway, Iceland, Liechtenstein, Switzerland, and Monaco.  |
| SEPA Direct Debit  | International SEPA Direct Debit  |
|Single SEPA Direct Debit   | A SEPA Direct Debit the customer approved for a single withdrawal.  |
| Recurring SEPA Direct Debit  | A recurring SEPA Direct Debit the customer approved for regular withdrawals.  |
| Chargeback  | When the customer revokes a recurring payment.  |

