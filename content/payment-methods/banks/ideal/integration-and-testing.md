---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "iDEAL - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing iDEAL in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/iDEAL.svg'
aliases:
    - /payment-methods/ideal/ideal-testing
---

To integrate Klarna using our API, see API Reference - [iDEAL](/api/#ideal).

{{< details title="View test statuses" >}}

| Status                | Description              |
| --------------------- | ------------------------ |
| **Completed**             | Transaction was completed |
| **Declined**              | Transaction was declined |
| **Cancelled**             | Transaction was cancelled |
| **Initialized**/ **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Initialized**/ **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

{{< /details >}}
