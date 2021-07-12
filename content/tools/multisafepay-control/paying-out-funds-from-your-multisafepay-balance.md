---
title : "Paying out funds from your MultiSafepay balance"
weight: 9
meta_title: "MultiSafepay account - Paying out funds from your MultiSafepay balance - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/getting-started/how-do-i-pay-out-the-balance-on-my-multisafepay-account-to-my-business-bank-account
    - /faq/getting-started/when-can-i-pay-out-the-balance-on-my-multisafepay-account-to-my-business-bank-account
    - /faq/getting-started/paying-out-your-multisafepay-control-balance-to-your-business-bank-account
    - faq/getting-started/paying-our-your-balance
    - /faq/general/how-can-i-pay-out-the-funds-on-my-multisafepay-account-
    - /faq/finance/paying-out-funds-from-your-multisafepay-control
    - /tools/multisafepay-control/paying-out-your-balance/
    - /faq/general/bank-holidays
---

You can pay out funds from your MultiSafepay account to your business bank account any time for 0,50 EUR each, except if:

{{< details title="Your MultiSafepay account is not yet fully activated" >}}

You can process payments immediately after creating a MultiSafepay test account and adding your website. But MultiSafepay holds your funds in your MultiSafepay balance until your account is fully activated.

To check if your account is fully activated, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Finance** > **Payouts**.
3. If your account is not fully activated, a red bar appears at the top of the screen with a link to the page where you can upload the documents required to approve your account.

The Risk Team then checks and approves your account details and the information on your website. Once approved, we will send you an email that your account is fully activated. 

{{< /details >}}

{{< details title="Your MultiSafepay balance is negative" >}}
&nbsp;  
If your MultiSafepay balance is negative (e.g. due to refunds, chargebacks, or fees), payouts are paused until enough funds are available. Always set a "reserved balance" in your payout settings to prevent payout and/or refund delays.

{{< /details >}}

{{< details title="The Risk Team has deactivated this feature for any reason" >}}
&nbsp;  
Email the Risk Team at <risk@multisafepay.com>

{{< /details >}}

## Automatic payouts

To schedule automatic payouts, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Finance** > **Balance**.
3. Select the IBAN number you want to pay out to.
4. Schedule your payouts using the payout scheduler.

{{< details title="About the payout scheduler" >}}

The payout scheduler lets you:

- Schedule automatic payouts on specific days of the week.
- Schedule payments only when your MultiSafepay balance exceeds a specific amount.
- Reserve a specific amount in your MultiSafepay balance, e.g. for refunds.

{{< /details >}}

## Manual payouts

To make manual payouts, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Finance** > **Balance**.
3. Select an amount to pay out, the currency, and the IBAN number.

## Payout currency
The standard currency for automatic payouts is euros (EUR). For manual payouts, you can process other currencies if you specify a business bank account that can receive funds in that currency.

## Payout processing times 
The time taken to process payouts is determined by the Risk Team. The default payout delay is 1 day. Payouts may take up to three business days to arrive in your business bank account.

Payment batches are not processed on weekends. That is, payouts initiated on Fridays are processed on Monday morning.

Not all banks have instant payments and therefore may take extra time to process payments.

{{< details title="Bank holidays" >}}

On some bank holidays, banks don't process outgoing payments. For example, see the [Deutsche Bank schedule for the Netherlands](https://www.deutschebank.nl/nl/content/producten_en_services_services_international_holidays_2017.html).

MultiSafepay pays out every business day of the year, but not on bank holidays. Delayed payouts are made the next business day. The dates of bank holidays change each year.

### Bank holidays 2021

| Date   | Occasion     | Payouts made |
|----------------|-------------------|-----------|
|  Friday, April 2, 2021 | Good Friday     | No  |
|  Monday, April 5, 2021 | Easter Monday     | No  |
|  Tuesday, April 27, 2021 | King's Day     | Yes  |
|  Thursday, May 13, 2021 | Ascension Day     | Yes  |
|  Monday, May 24, 2021 | Pentecost     | Yes  |

For more information, email the Support Team at <support@multisafepay.com>

{{< /details >}}

{{< details title="Processing time for automatic payouts" >}}

Assuming default settings, if you schedule a payout on Monday, the payout batch includes all payments up to 23:59 hours on the Monday night. The payout batch is sent to MultiSafepay's bank on Tuesday morning. Our bank processes the batch and transfers the pay out to your business bank account. You should receive the payout on Tuesday afternoon.

{{< /details >}}

{{< details title="Processing time for manual payouts" >}}

The status of the pay out is **Reserved** for 24 hours before it is added to our bank’s payout batch in the morning. Then, the payout is transferred to your business bank account. Manual payouts usually take longer to process than automatic ones.

{{< /details >}}

## Paying out to a different bank account

To pay out to a different bank account than the one activated in your MultiSafepay account, you must first add it under **Business documents**.
