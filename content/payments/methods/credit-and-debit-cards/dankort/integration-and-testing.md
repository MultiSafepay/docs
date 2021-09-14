---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Dankort - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Testing Dankort transactions in your ecommerce platform"
layout: 'child'
---

To process Dankort payments via our API, see API reference – [Credit cards](/api/#credit-cards).

For the Dankort logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Credentials and testing process" >}}

Test credentials: MultiSafepay provides Visa test credentials for Dankort.

Payment page: Dankort only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` is set to `da_DK` (Denmark) in the transaction request sent to MultiSafepay.

{{< /details >}}