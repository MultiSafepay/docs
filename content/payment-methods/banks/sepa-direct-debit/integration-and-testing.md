---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "SEPA Direct Debit - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing SEPA Direct Debit in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
aliases:
    - /payment-methods/sepa-direct-debit/sepa-direct-debit-testing
---

To integrate SEPA Direct Debit using our API, see API Reference – [SEPA Direct Debit](/api/#sepa-direct-debit).

{{< details title="View test credentials and process" >}}

Test IBANs: See the table below.

Sample statuses:

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

{{< /details >}}