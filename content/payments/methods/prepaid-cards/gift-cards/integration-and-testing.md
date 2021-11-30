---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Gift cards - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing gift cards in your ecommerce platform"
layout: 'child'
url: '/payment-methods/gift-cards/integration-testing/'
aliases:
    - /payment-methods/gift-cards/test-gift-cards
    - /payments/methods/prepaid-cards/gift-cards/integration-and-testing/
---

To process gift card payments via our API, see API reference – [Gift cards](/api/#gift-cards).

For support, email the Integration Team at <integration@multisafepay.com>

{{< details title="View credentials and testing process" >}}

You can test the following gift cards:

- Beauty Cadeau
- Boeken Voordeel
- Huis & Tuin Cadeau
- Klus Cadeau
- Nationale Bioscoopbon
- VVV Cadeaukaart
- Wijn Cadeaukaart

**Test a gift card order**

Test credentials: [API key](/account/site-id-api-key-secure-code/)

1. Make a [redirect](/api/#gift-cards) API request.
2. On the payment page:
    - In the **Card number** field, enter `111115`.
    - In the **Security code** field, enter any 4-digit number.
    - Click **Add discount**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different gift card balances.

| Card numbers     | Balance    |
| ------- | --------- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |

Any other card number receives an "Invalid card number" error.

**Other gift cards** 

You can't test other gift cards in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. You make a small payment and the amount is actually deducted from the gift card.

{{< /details >}}


