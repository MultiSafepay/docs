---
title: 'Unreferenced refunds'
category: 6477597e0e2961004638cd5d
order: 3
hidden: true
slug: 'unreferenced-refunds'
---

Alternatively to regular refunds, you can process unreferenced refunds. This allows you to return funds to a customer without referring to the original transaction.

## Activation

To enable unreferenced refunds for your MultiSafepay account, email [sales@multisafepay.com](mailto:sales@multisafepay.com).

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/unref-refunds-pos.svg" alt="cloud-POS" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;"/>


***

## SmartPOS

### Prerequisites

On your terminal:

- Enable the **unreferenced refunds** feature.
- For Cloud POS payments, additionally enable **Cloud mode**. 

Check the general flow below:

1. You create an unreferenced refund via 
   - **Cloud POS**: See <a href="https://docs.multisafepay.com/recipes/smartpos-unreferenced-refunds" target="_blank">Unreferenced refunds</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> OR
   - **Manual Input** OR
   - **App-to-app** (this will soon be available). 
2. The customer presents their card.
3. The card details are sent to MultiSafepay.
4. The details are forwarded to the card scheme for authorization which can be accepted or declined.
5. Once we receive an authorization response, we forward it to the terminal. The result will be displayed on the screen.

***

## Traditional (CTAP) terminals

The steps to process an unreferenced refund may vary from one terminal model to another. Check the general flow below:

1. You initiate the refund by introducing the amount on the CTAP terminal.
2. The customer presents their card.
3. The card details are sent to MultiSafepay.
4. The details are forwarded to the card scheme for authorization which can be accepted or declined.
5. Once we receive an authorization response, we forward it to the terminal. The result will be displayed on the screen. 

## Updates

Once created, the `status` of the order will be `initialized`. While the transaction is processed, the `status` will change to `reserved`, then to  `completed`.

Check how to receive updates for unreferenced refunds in the table below:

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="text-align: left;">Terminal</th>
      <th style="text-align: left;">How to handle notifications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;"><strong>SmartPOS</strong></td>
      <td style="text-align: left;">
        To receive order updates, use a <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">webhook</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.<br>
        <strong>⚠️Note:</strong> Event notifications are not supported for unreferenced refunds.
      </td>
    </tr>
    <tr>
      <td style="text-align: left;"><strong>CTAP</strong></td>
      <td style="text-align: left;">
        Make a <a href="/reference/getorder/">Get order</a> request. Retrieve the details from the response.
      </td>
    </tr>
  </tbody>
</table>

***

[Top of page](#)