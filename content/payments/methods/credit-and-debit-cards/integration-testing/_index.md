---
title: "Integrating and testing cards"
breadcrumb_title: 'Integration and testing'
weight: 3
meta_title: "Integrating and testing cards - MultiSafepay Docs"
short_description: "Options for integrating cards and testing payments"
layout: 'child'
url: '/payment-methods/credit-debit-cards/integration-testing/'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/american-express-testing
    - /payment-methods/credit-and-debit-cards/credit-card-payment-page
    - /payments/methods/credit-and-debit-cards/american-express/integration-and-testing/
    - /payment-methods/amex/integration-testing/
    - /payments/methods/credit-and-debit-cards/cartes-bancaires/integration-and-testing/
    - /payment-methods/cartes-bancaires/integration-testing/
---
## Integration

| | |
|---|---|
| **API** | **API reference** {{< br >}} - [American Express redirect](/api/#american-express) {{< br >}} - [Maestro redirect](/api/#maestro) {{< br >}} - [Mastercard redirect](/api/#mastercard) {{< br >}} - [Visa redirect](/api/#visa) {{< br >}} - [Co-branded credit cards](/api/#co-branded-credit-cards) {{< br >}} **Bundled credit cards** {{< br >}} You can also bundle multiple credit cards together on your MultiSafepay credit card payment page. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits. See API reference – [Credit cards](/api/#credit-cards). {{< br >}} To display on MultiSafepay credit card payment pages, set the [`locale`](/developer/api/using-locale-parameters) in transaction requests to: {{< br >}} - Dankort: `da_DK` (Denmark) {{< br >}} - Cartes Bancaires: `fr_FR` (France) {{< br >}} - Postepay: `it_IT` (Italy) |
| **Ready-made integrations** | Card payments are supported in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing
{{< details title="American Express" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an American Express order**  

1. Make a [redirect](/api/#american-express) API request.
2. On the payment page:
    - In the **Card number** field, enter `378282246310005`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 374200000000004| **Declined**  | Transaction was declined |
| 378734493671000| **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |

{{< /details >}}

{{< details title="Cartes Bancaires / Dankort / V Pay" >}}
You can test the following cards using the Visa test instructions. To display these cards on MultiSafepay payment pages, you must set the `locale` parameter in the redirect API request to a specific locale.

| Card             | `locale` |
|------------------|----------|
| Cartes Bancaires | `fr_FR`  |
| Dankort          | `da_DK`  |
| V Pay            | `it_IT`  |

{{< /details >}}

{{< details title="Maestro" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

Testing Maestro is similar to Visa. For extensive testing, see [Visa](#details-visa). 

**Test a Maestro order**  

1. Make a [redirect](/api/#maestro) API request.
2. On the payment page:
    - In the **Card number** field, enter `6759000000005`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Mastercard" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

Testing Mastercard is similar to Visa. For extensive testing, see [Visa](#details-visa). 

**Test a Mastercard order**  

1. Make a [redirect](/api/#mastercard) API request.
2. On the payment page:
    - In the **Card number** field, enter `5500000000000004`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**. 
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

{{< /details >}}

{{< details title="Visa" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a VISA order**  

1. Make a [redirect](/api/#visa) API request.
2. On the payment page:
    - In the **Card number** field, enter `4111111111111111`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
3. On the 3D payment page:
    - From the drop-down list, select **Authenticated (Y)**.
    - Click **Confirm**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Void**. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

---

**Note:** 
- You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.
- You can't test cancelling orders. 

{{< /details >}}

{{< details title="Refunding credit and debit card orders" >}}
**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test dashboard, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Make a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test dashboard, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}



