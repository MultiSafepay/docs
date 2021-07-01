---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Dankort - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Testing Dankort transactions in your ecommerce platform"
layout: 'child'
---

To integrate Dankort using our API, see API Reference – [Credit cards](/api/#credit-cards).

{{< details title="Credentials and testing process" >}}

Test credentials: MultiSafepay provides Visa test credentials for Dankort.

Payment page: Dankort only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` is set to `da_DK` (Denmark) in the transaction request sent to MultiSafepay.

{{< /details >}}