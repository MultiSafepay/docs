---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Bancontact - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Bancontact in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
url: '/payment-methods/bancontact/integration-testing/'
aliases:
    - /payment-methods/bancontact/bancontact-testing
    - /payments/methods/banks/bancontact/integration-and-testing/
    - /payments/methods/banks/bancontact-qr/integration-and-testing/
---

To process payments via our API, see API reference:

- [Bancontact](/api/#bancontact)
- [Bancontact QR](/api/#bancontact-qr)

For the Bancontact logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Testing" >}}

Test card numbers: See the table below.

Possible errors: Test QR codes can only be read with a general QR reader. If you scan the code using the Bancontact app, an error occurs.

Sample statuses:

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

{{< /details >}}

