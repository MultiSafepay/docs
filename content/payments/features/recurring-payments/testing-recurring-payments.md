---
title : "Testing recurring payments"
weight: 55
meta_title: "Testing recurring payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/how-to-test-recurring-payments
---
To enable testing recurring payments in your [MultiSafepay test account](https://testmerchant.multisafepay.com), email the Integration Team at <integration@multisafepay.com> 

#### SEPA Direct Debit

For testing SEPA Direct Debit transactions, use the following test IBANs:

| IBAN | Status | Description |
---|---|---
NL87ABNA0000000001 | **Initialized/Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**.|
NL87ABNA0000000002 | **Initialized/Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**.|
NL87ABNA0000000003 | **Initialized/Uncleared/Completed** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**, and after another minute to **Completed**.|
NL87ABNA0000000004 | **Initialized/Uncleared/Declined** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**, and after another minute to **Declined**.|
