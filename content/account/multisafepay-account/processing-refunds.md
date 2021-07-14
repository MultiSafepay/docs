---
title : "Processing refunds"
weight: 20
meta_title: "MultiSafepay account - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /faq/refunds
    - /faq/refunds/initiating-refunds/
    - /faq/refunds/initiating-refunds-in-batches/
    - /faq/refunds/cancelling-refunds/
    - /faq/refunds/refund-period-for-payment-methods/
    - /faq/refunds/refund-processing-time/
    - /faq/refunds/delays-in-processing-refunds/
    - /faq/refunds/using-the-refund-script
    - /faq/refunds/refund-an-order
    - /faq/finance/how-can-i-perform-a-refund
    - /faq/finance/paying-refunds
    - /faq/refunds/initiating-refunds
    - /faq/refunds/refund-period-payment-methods
    - /faq/refunds/
    - /faq/refunds/how-long-does-a-refund-take-to-process
     - /faq/refunds/can-i-cancel-an-initiated-refund
    - /faq/finance/paying-out-funds-from-your-multisafepay-control
    - /faq/finance/refund-more-than-original-amount
    - /tools/multisafepay-control/processing-refunds
---
## In your MultiSafepay account

{{< details title="Full refunds" >}}
  
To refund the full transaction, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

   The transaction is cancelled.

{{< /details >}}

{{< details title="Partial refunds" >}}

To refund part of the transaction in the checkout editor, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Select the item(s) you want to deduct from the order.
6. Click **Save**.

   The transaction shows the credited item(s) with the deducted amount added to the transaction.
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

{{< details title="Discounts" >}}

Discounts are processed as a **negative amount** instead of a **negative quantity**. This method of adding discounts only applies to successful transactions. 

Instead of deleting an item in the checkout editor, you may want to add a discount. Follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Add the discount as a new page in the checkout editor.  
  Example: quantity (1) > discount (item or name) > amount (as negative) > VAT
6. To deduct the amount of the discount, add a new line to the order.
7. Click **Save**.

   The discount is added to the transaction. 
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

For support, email the Integration Team at <integration@multisafepay.com>

## In your backend

You can process refunds in the backend of most ecommerce platforms. For more information, see the User guide in the integration manual for the relevant platform, e.g. Magento 2 – [Processing refunds](/payments/integrations/ecommerce-platforms/magento2/faq/processing-refunds/).

## Via our API

For post-payment methods, you can also refund via our API. Make a POST `/orders/{order_id}/refunds` request. 

See API Reference – [Refund with shopping cart](/api/#refund-with-shopping-cart).

## Refund rules

{{< details title="Refunding more than the original transaction amount" >}}

You can refund customers more than the amount of the original transaction, e.g. if you want to cover the customer's postage costs when returning an order. 

This option is only available for debit card transactions, and **not** for credit cards or post-payment methods. A maximum ammount limit applies. 

To enable this option, follow these steps:

1. Email your request to your account manager at <sales@multisafepay.com>
2. The Risk Team assesses your application. 
3. Once approved, the Risk Team enables the **allow more than original** function in your MultiSafepay account.
4. Activate the function in your MultiSafepay account account. 

{{< /details >}}

{{< details title="Processing times" >}}

The refund processing time depends on the payment method:

- Direct banking (e.g. KBC, Belfius, ING Homepay, Trustly, Direct Debit): 1 business day 
- Bank transfers: 2 to 3 business days, depending on the customer's bank
- Credit cards: Up to 4 weeks 

{{< /details >}}

{{< details title="Refund period per payment method" >}}

The refund period is the maximum number of days after a payment was completed that you can refund it through MultiSafepay. After this time, we recommend using a bank transfer.

This table lists the refund period for each payment method:

| Payment method   | Refund period  |
| --------- | ------------------------ |
| [AfterPay](/payments/methods/billing-suite/afterpay/) | 730 days |
| [Alipay](/payments/methods/wallet/alipay/) | 365 days |
| [American Express](/payments/methods/credit-and-debit-cards/american-express/) | 180 days |
| [Bancontact / Bancontact Mobile](/payments/methods/banks/bancontact/) | 180 days |
| [Bank transfer](/payments/methods/banks/bank-transfer/) | 730 days |
| [Belfius](/payments/methods/banks/belfius/) | 730 days |
| [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand/) | 730 days |
| [CBC](/payments/methods/banks/cbc/) | 730 days |
| [Dotpay](/payments/methods/banks/dotpay/) | 730 days |
| [E-invoicing](/payments/methods/billing-suite/e-invoicing/) | 730 days |
| [EPS](/payments/methods/banks/eps/) | 730 days |
| [Giropay](/payments/methods/banks/giropay/) | 730 days |
| [iDEAL](/payments/methods/banks/ideal/) | 730 days |
| [iDEAL QR](/payments/methods/banks/idealqr/) | 730 days |
| [in3](/payments/methods/billing-suite/in3/) | 730 days |
| [ING Home'Pay](/payments/methods/banks/ing-home-pay/) | 730 days |
| [KBC](/payments/methods/banks/kbc/) | 730 days |
| [Klarna](/payments/methods/billing-suite/klarna/) | 730 days |
| [Maestro](/payments/methods/credit-and-debit-cards/maestro/) | 180 days |
| [MasterCard](/payments/methods/credit-and-debit-cards/mastercard/) | 180 days |
| [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery/) | 730 days |
| [PayPal](/payments/methods/wallet/paypal/) | 180 days |
| [Paysafecard](/payments/methods/prepaid-cards/paysafecard/) | 180 days |
| [Request to Pay](/payments/methods/banks/request-to-pay/) | 730 days |
| [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit/) | 730 days |
| [SOFORT Banking](/payments/methods/banks/sofort-banking/) | 730 days |
| [Trustly](/payments/methods/banks/trustly/) | 365 days |
| [Visa](/payments/methods/credit-and-debit-cards/visa/) | 180 days |

{{< /details >}}

{{< details title="Reserved status" >}}

If the status of the refund  is **Reserved**, it may mean: 

- The refund hasn't been processed yet. Refunds are passed to the customer's bank at midnight on the day they are initiated, and then the status changes to **Completed**. The bank is now responsible for processing the payment. Refunds may be delayed by the issuing bank.
- The refund cannot be processed due to insufficient funds in your MultiSafepay account. To top up your balance, see [Adding funds to your MultiSafepay balance](https://docs.multisafepay.com/faq/finance/adding-funds-to-your-multisafepay-balance).

{{< /details >}}

{{< details title="Cancelling refunds" >}}

You can cancel a refund while the status is **Reserved**, and the refund won't be paid to the customer. 

The refund status is **Reserved** until midnight on the day the refund was initiated. At midnight, the transaction is passed to the customer's bank to process. You can no longer cancel it via MultiSafepay.

{{< /details >}}

{{< details title="Batching refunds" >}}

You can process refunds in batches using our refund script. The script requires 2 parameters: 

- A .csv file that specifies the order ID, amount, and a description of every transaction
- Your [API key](/faq/general/multisafepay-glossary/#api-key)

The script is written in PHP, so make sure you have a PHP interpreter installed.

For instructions on using the script and to download, see MultiSafepay GitHub - [Refund script](https://github.com/MultiSafepay/refund-script).

For questions, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}

For any questions, email the Support Team at <support@multisafepay.com>
