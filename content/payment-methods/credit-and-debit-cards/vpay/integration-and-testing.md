---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "V Pay - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing V Pay in your ecommerce platform"
layout: 'child'
---

V Pay payments are processed as credit card payments.

To integrate V Pay using our API, see API Reference – [Credit cards](/api/#credit-cards).

For the V Pay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Credentials and testing process" >}}

Test card details: 

- Card number: See the table below.
- CVC code: 123
- Expiry date in the future

Sample statuses:

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

{{< /details >}}