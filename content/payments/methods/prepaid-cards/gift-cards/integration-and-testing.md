---
title: "Integrating and testing gift cards"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing gift cards - MultiSafepay Docs"
short_description: "Options for integrating gift cards and testing payments"
layout: 'child'
url: '/payment-methods/gift-cards/integration-testing/'
aliases:
    - /payment-methods/gift-cards/test-gift-cards
    - /payments/methods/prepaid-cards/gift-cards/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Redirect](/api/#gift-cards)  |
| **Ready-made integrations** | We don’t support all open-loop gift cards in our [ready-made integrations](/integrations/ready-made/) and no closed-loop gift cards. Therefore in some integrations, we use [generic gateways](/developer/general/generic-gateways/). {{< br >}} To check if a specific gift card is supported in your ready-made integration, email the Integration Team at integration@multisafepay.com   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |

## Testing 

### Intersolve gift cards

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

### Other gift cards

You can't test other gift cards in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account. You make a small payment and the amount is actually deducted from the gift card.



