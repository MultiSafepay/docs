---
title: "Test and live refunds"
weight: 71
meta_title: "Test and live refunds - MultiSafepay Docs"
read_more: '.'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /tools/multisafepay-test-environment/refunds
---

Refunds work differently in the MultiSafepay [test](https://testmerchant.multisafepay.com/signup?_ga=2.239314307.1689046699.1579505297-896219683.1574159857) and live environments.

### Live environment
For refunds processed by [bank transfer](/payment-methods/banks/), the transaction status changes to **Reserved** and can be cancelled until midnight that day. At midnight, the status changes to **Completed**.

Refunds for credit cards, PayPal, and [billing suites](/payment-methods/billing-suite/) are processed immediately and cannot be reversed.

### Test environment
The transaction status remains **Reserved** until the refund is manually approved since there is no settlement with a bank.
