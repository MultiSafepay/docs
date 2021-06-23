---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Bancontact - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing Bancontact in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
aliases:
    - /payment-methods/bancontact/bancontact-testing
---

To integrate Bancontact using our API, see API Reference - [Bancontact](/api/#bancontact).

{{< details title="View credentials and testing process" >}}

Test card number: See the table below.

Possible errors: The test QR codes can only be read with a general QR code application. If you scan the code using the Bancontact app, an error occurs.

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

{{< /details >}}