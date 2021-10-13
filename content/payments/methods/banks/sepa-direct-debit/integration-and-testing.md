---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "SEPA Direct Debit - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing SEPA Direct Debit in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
url: '/payment-methods/sepa-direct-debit/integration-testing/'
aliases:
    - /payment-methods/sepa-direct-debit/sepa-direct-debit-testing
    - /payments/methods/banks/sepa-direct-debit/integration-and-testing/
---

To process SEPA Direct Debit payments via our API, see API reference – [SEPA Direct Debit](/api/#sepa-direct-debit).

For the SEPA Direct Debit logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

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