---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Bank Transfer - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Bank Transfer in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
url: '/payment-methods/bank-transfer/integration-testing/'
aliases:
    - /payment-methods/bancontact/bank-transfer-testing
    - /payments/methods/banks/bank-transfer/integration-and-testing/
---

To process Bank Transfer payments via our API, see API reference - [Bank Transfer](/api/#bank-transfer).

For the Bank Transfer logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test IBANs: See the table below.

Sample statuses:

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000002| **Initialized**/ **Declined** | Transaction is initialized. After 1 minute, this changes to declined. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | Transaction is initialized. After 1 minute, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | Transaction is initialized. After 1 minute, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

{{< /details >}}