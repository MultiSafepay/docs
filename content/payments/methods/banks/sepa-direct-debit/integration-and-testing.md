---
title: "Integrating and testing SEPA Direct Debit"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing SEPA Direct Debit - MultiSafepay Docs"
short_description: "Options for integrating SEPA Direct Debit and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
url: '/payment-methods/sepa-direct-debit/integration-testing/'
aliases:
    - /payment-methods/sepa-direct-debit/sepa-direct-debit-testing
    - /payments/methods/banks/sepa-direct-debit/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#sepa-direct-debit---direct) and [redirect](/api/#sepa-direct-debit---redirect) |
| **Ready-made integrations** | EPA Direct Debit (direct) is supported in all our [ready-made integrations](/integrations/ready-made/). |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test a SEPA Direct Debit order

1. To test a SEPA Direct Debit order, make a [direct](/api/#sepa-direct-debit---direct) or [redirect](/api/#sepa-direct-debit---redirect) API request.
2. If you make a redirect API request, enter in the:
    - **Account holder** field the account holder name.
    - **IBAN** field the IBAN.
4. Click **Confirm**.

Use the following IBANs to test different transaction statuses.

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | The transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Declined** | The transaction is initialized. After 2 minutes, this changes to **Declined**. |
| NL87ABNA0000000003| **Initialized**/ **Uncleared**/ **Completed** | The transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Completed**. |
| NL87ABNA0000000004| **Initialized**/ **Uncleared**/ **Declined** | The transaction is initialized. After 2 minutes, this changes to **Uncleared**. After 1 more minute, it changes to **Declined**. |

### Test refunding an order

To test refunding an order:

1. Create an order with IBAN `NL87ABNA0000000001`. 
2. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

### Test an API refund

To test refunding an order via the API:

1. Create an order with IBAN `NL87ABNA0000000001`. 
2. Make a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Notes:** 

- You can't test cancelling orders.
- In the live environment, you can't accept refund orders. These are done automatically.
