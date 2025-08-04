---
title: SmartPOS solutions
category:
  uri: Point-of-sale
slug: smartpos-solutions
parent:
  uri: smartpos-terminal
position: 0
privacy:
  view: public
---
We currently offer this product in the following countries:

<table>
  <tr>
    <td>Countries</td>
    <td>Netherlands, Belgium</td>
  </tr>

  <tr>
    <td>For partners</td>
    <td>Netherlands, Belgium, Italy, Spain</td>
  </tr>
</table>

If you are interested in our Point of Sale solutions, email \[mailto:[sales@multisafepay.com](mailto:sales@multisafepay.com)]

# Set up your SmartPOS flow

Our SmartPOS terminals support three different payment solutions, offering flexible integration options for your business needs.

<CardRow>
  <CardText title="Cloud POS Payments" href="/docs/bank-transfer/" icon="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Cloud_POS.svg" alt="Cloud POS Payments" description="Process payments from an external application. This lets your Point of Sale system process payments securely via a cloud connection." />

  <CardText title="On-same Device Applications" href="/docs/bank-transfer/" icon="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Transactions_ondevice.svg" alt="On-same Device Applications" description="Run your native or web based aplication on your terminal and initiate payments on the same device through the payment app." />

  <CardText title="Manual input" href="/docs/bank-transfer/" icon="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/img/In-person-payments.svg" alt="Manual input" description="Manually enter payment amounts in the app. The customer pays using a supported payment method." />
</CardRow>

***

Click on the options below for more information on how to further set up your terminal.

<style jsx>
  {`
    .steps {
      display: flex;
      flex-direction: column;
      align-items: stretch;
    }
    .step-item {
      display: flex;
      margin-bottom: 10px;
      align-items: center;
    }
    .step-info {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .step-number {
      background-color: #007bff;
      color: white;
      border-radius: 50%;
      width: 35px;
      height: 35px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      margin-left: 10px;
    }
    .step-description {
      margin-top: 5px;
      flex: 1;
      /* CORRECTED: The invalid 'align-items' was removed. */
      /* It's already being centered by its parent, .step-info. */
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .step-description p {
      margin-top: 10px !important;
      margin-bottom: 0 !important;
    }
    .configure-text {
      font-size: 22px;
      font-weight: lighter;
    }

    /* --- CARD STYLES (Cleaned Up) --- */
    .card-container-setup {
      display: flex;
      flex-direction: column;
      justify-content: center; /* Vertically centers content */
      align-items: center;     /* Horizontally centers content */
      padding: 1rem;
      margin: 0.125rem;
      box-sizing: border-box;
      border: 1px solid #d1d5db;
      border-radius: 0.375rem;
      box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      width: 250px;
      flex-shrink: 0;
      transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
      background-color: #fff;
    }
    .card-container-setup:hover {
      transform: scale(1.02);
      box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
      border-color: #60a5fa;
      cursor: pointer;
    }
    .card-container-setup a {
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 100%;
    }
    .card-container-setup img {
      width: 60px;
      height: 60px;
      margin-bottom: 0.75rem;
      object-fit: contain;
      pointer-events: none;
    }
    .card-container-setup h4 {
      font-size: 15px;
      font-weight: 550;
      color: #00bcd4;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      margin: 0;
      text-align: center;
    }
    .card-container-setup h4 b {
      color: inherit;
      font-weight: inherit;
    }
    
    /* --- RESPONSIVE STYLES --- */
    @media (max-width: 768px) {
      .step-item {
        flex-direction: column;
        align-items: stretch;
      }
      .step-info {
        order: -1;
        width: 100%;
        margin-bottom: 10px;
      }
      .card-container-setup {
        width: 100%;
        margin: 8px 0;
      }
      .step-number {
        margin-left: 0;
        margin-right: 10px;
      }
      .step-description {
        margin-left: 0;
      }
    }
  `}
</style>

<div className="steps-container">
  <div className="steps">
    <LargeCardPOS title="Hardware setup" href="/docs/hardware-setup" icon="https://cdn.jsdelivr.net/gh/MultiSafepay/docs@master/static/svgs/POS/Settings.svg" stepNumber="1">
      <p>
        Configure your terminal's hardware for first use
      </p>
    </LargeCardPOS>

    <LargeCardPOS title="Activation" href="/docs/smartpos-activation" icon="https://cdn.jsdelivr.net/gh/MultiSafepay/docs@master/static/svgs/POS/Activation.svg" stepNumber="2">
      Activate your terminal from your MultiSafepay dashboard
    </LargeCardPOS>

    <LargeCardPOS title="Event notifications" href="/docs/event-notifications" icon="https://cdn.jsdelivr.net/gh/MultiSafepay/docs@master/static/svgs/POS/Notifications.svg" stepNumber="3">
      Subscribe to event notifications to receive order status updates
    </LargeCardPOS>

    <LargeCardPOS title="SmartPOS features" href="/docs/smartpos-features" icon="https://cdn.jsdelivr.net/gh/MultiSafepay/docs@master/static/img/Omnichannel-payments.svg" stepNumber="4">
      Customize your payment flow with additional features
    </LargeCardPOS>
  </div>
</div>

***