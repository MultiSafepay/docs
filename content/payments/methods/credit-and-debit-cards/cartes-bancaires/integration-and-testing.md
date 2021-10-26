---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Cartes Bancaires - Integration and testing - MultiSafepay Docs"
short_description: "Testing Cartes Bancaires in your ecommerce platform"
layout: 'child'
---

To process Cartes Bancaires payments via our API, see API reference – [Credit cards](/api/#credit-cards).

{{< details title="Credentials and testing process" >}}

Test credentials: MultiSafepay provides Visa test credentials to test Cartes Bancaires.

Payment page: Cartes Bancaires only appears on the MultiSafepay payment page if:

- The Visa gateway is enabled, and
- The `locale` parameter is set to `fr_FR` (France) in the transaction API request.

{{< /details >}}