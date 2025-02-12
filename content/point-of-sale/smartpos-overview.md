---
title: 'SmartPOS terminal'
category: 6477597e0e2961004638cd5d
order: 2
hidden: false
slug: 'smartpos-terminal'
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

If you are interested in our Point of Sale solutions, email <a href="mailto:sales@multisafepay.com" style="font-size: inherit;">sales@multisafepay.com</a>

# Set up your SmartPOS flow

Our SmartPOS terminals support three different payment solutions, offering flexible integration options for your business needs.

<div class="step-info">
      <div class="step-number">1</div>
      <p class="step-description configure-text">Choose your solution</p>
</div>
<style>
  
</style>

<div class="auto-grid-2">
  <div class="card-container-2">
    <a href="/docs/smartpos-solutions#cloud-pos-payment" style="text-decoration: none;">
    <div class="card-2">
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Cloud_POS.svg" alt="Cloud POS Payments">
      <h4>Cloud POS Payments</h4>
      <p class="text-flows">Process payments from an external application. This lets your Point of Sale system process payments securely via a cloud connection.</p>
     </a>
    </div>
  </div>

  <div class="card-container-2">
    <div class="card-2">
      <a href="/docs/smartpos-solutions#on-same-device-third-party-applications" style="text-decoration: none;">
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Transactions_ondevice.svg" alt="On-Same Device Third-Party Applications">
      <h4>On-Same Device Applications</h4>
      <p class="text-flows">Run your native or web based aplication on your terminal and initiate payments on the same device through the payment app.</p>
      </a>
    </div>
  </div>

  <div class="card-container-2">
    <div class="card-2">
      <a href="/docs/smartpos-solutions#manual-input" style="text-decoration: none;">
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/img/In-person-payments.svg" alt="On-Same Device Third-Party Applications">
      <h4>Manual input</h4>
      <p class="text-flows">Manually enter payment amounts in the app. The customer pays using a supported payment method.</p>
      </a>
    </div>
  </div>
</div>

***

Click on the options below for more information on how to further set up your terminal.

<style>
/* Overall Container */
.auto-grid-2 {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* Align items to the start for left alignment */
  align-items: stretch;       /* Make all cards the same height */
  gap: 20px;
  padding: 20px;
  width: 100%;
  box-sizing: border-box;
}

/* Card Container - Width for Larger Screens (Desktops) */
.card-container-2 {
  width: calc(33.33% - 20px); /* Three items per row on larger screens */
  max-width: 400px;           /* Limit card width */
  box-sizing: border-box;
  margin-bottom: 20px;        /* Spacing between rows */
}
<!--
/* Hover effect on the container */
.card-container-2:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  transform: translateY(-0.2rem);
  transition: all 0.2s;
  cursor: pointer;
  border-radius: 8px;
}
-->

/* Card Styling */
.card-2 {
  display: flex;
  flex-direction: column;
  padding: 20px;             /* Reduced padding */
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
  transition: all 0.2s ease-in-out;
  background-color: #fff;
  width: 100%;
  height: 100%; /* Add this line */
}

.card-2:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-2 img {
  max-width: 60%;            /* Reduced image size */
  max-height: 70px;           /* Reduced image height */
  margin-bottom: 10px;        /* Reduced spacing below image */
  pointer-events: none;
  object-fit: contain;
}

.card-2 h4 {
  color: #00bcd4;
  margin-top: 0;             /* Reset top margin */
  margin-bottom: 8px;         /* Reduced spacing below heading */
  font-size: 1.1em;          /* Slightly smaller heading */
  pointer-events: none;
}

.text-flows {
  color: #555;
  font-size: 0.9em;          /* Slightly smaller text */
  line-height: 1.4;          /* Reduced line height */
  margin-bottom: 0;          /* Reset bottom margin */
  flex-grow: 1; /* Allow the paragraph to take up remaining vertical space */
}

.card-2 a {
  text-decoration: none;
  color: inherit;
  display: block;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}

/* Mobile Media Query - One item per row */
@media (max-width: 768px) {
  .card-container-2 {
    width: 100%;             /* Full width on mobile */
    max-width: none;          /* Remove max width */
  }
}

/* Added for Smaller Mobile devices */
@media (max-width: 480px) {
  .card-2 img {
    width: 55px;             /* Smaller image width */
    height: 35px;            /* Smaller image height */
  }
}

/* Desktop Media Query - for larger screens */
@media (min-width: 769px) {
  .auto-grid-2 {
    justify-content: flex-start;
  }
    .card-container-2 {
    width: calc(33.33% - 20px); /* Three items per row */
    max-width: 400px;
  }
}

/* Desktop Media Query - for larger screens */
@media (min-width: 1200px) {
  .card-container-2 {
    width: calc(33.33% - 20px); /* Keep three items per row, even on very large screens */
  }
}

</style>

<style>
  b {
    color: #384248 !important;
  }
  .steps-container { /* Added container for the whole widget */
    /* You can add styles to this container like width, max-width, margin, etc. */
    /* For example: max-width: 800px; margin: 0 auto; */
  }

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
	.step-item img {
    pointer-events: none;
  }

  .step-item h4 {
    pointer-events: none;
  }
  .card-container-setup {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    padding: 16px;
    text-align: center;
    border-radius: 5px;
    margin: 8px;
    width: 250px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card-container-setup:hover {
    box-shadow: 0 8px 16px 0 rgb(0 0 0 / 20%);
    transform: translateY(-0.2rem);
    transition: all 0.2s;
    cursor: pointer;
  }
  .field-description blockquote, .field-description dl, .field-description ol, .field-description p, .field-description pre, .field-description table, .field-description ul, .markdown-body blockquote, .markdown-body dl, .markdown-body ol, .markdown-body p, .markdown-body pre, .markdown-body table, .markdown-body ul {
    margin-bottom: 12px !important;
    margin-top: 12px !important;
	}

  .step-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
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
    flex: 1;
    margin-left: 10px;
    display: flex;
    align-items: center;
    height: 100%;
    font-size: 1rem;
    margin-top: 0px;
    margin-bottom: 0px; /*Removing to reset*/
    width: 600px;
  }
   .step-description p {
      margin-bottom: 10;
  }
  .configure-text {
    font-size: 22px; /* Or whatever size you want */
    font-weight: lighter;
  }
     /* Mobile Styles (applied when screen width is 768px or less) */
  @media (max-width: 768px) {
    .step-item {
      flex-direction: column; /* Stack card and info */
      align-items: stretch; /* Stretch items to full width */
    }

    /* Order is specified using the order property */
    .step-info {
      order: -1;  /* Moves the step-info div to the top */
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

    /* Larger Screen (Desktop) Styles */
  @media (min-width: 769px) {
    .step-item {
      flex-direction: row; /* Restore horizontal layout on larger screens */
      align-items: center;    /* Restore vertical alignment */
    }

    .step-info {
      order: 0;        /* Reset order to default */
      width: auto;       /* Reset width */
      margin-bottom: 0; /* Reset margin */
    }

    .card-container-setup {
      width: 250px; /* Restore original width */
      margin: 8px;    /* Restore original margins */
    }

    .step-number {
        margin-left: 10px;
        margin-right: 0;
    }

    .step-description {
        margin-left: 10px;
    }
  }

</style>

<div class="steps-container">  <!-- Added the container div here -->
  <div class="steps">
    <div class="step-item">
      <div class="card-container-setup">
        <a href="/docs/hardware-setup" style="text-decoration: none;">
          <div>
            <img
              src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Settings.svg"
              style="margin: 5px; max-height: 100px; max-width: 100px;">
            <div class="container">
              <h4><b>Hardware setup</b></h4>
            </div>
          </div>
        </a>
      </div>
      <div class="step-info">
        <div class="step-number">2</div>
        <p class="step-description configure-text">Configure your terminal's hardware for first use</p>
      </div>
    </div>
<div class="step-item">
  <div class="card-container-setup">
    <a href="/docs/smartpos-activation" style="text-decoration: none;">
      <div>
        <img
          src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Activation.svg"
          style="margin: 5px; max-height: 100px; max-width: 100px;">
        <div class="container">
          <h4><b>Activation</b></h4>
        </div>
      </div>
    </a>
  </div>
  <div class="step-info">
    <div class="step-number">3</div>
    <p class="step-description configure-text">Activate your terminal from your MultiSafepay dashboard</p>
  </div>
</div>
<div class="step-item">
  <div class="card-container-setup">
    <a href="/docs/event-notifications" style="text-decoration: none;">
      <div>
        <img
          src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/svgs/POS/Notifications.svg"
          style="margin: 5px; max-height: 100px; max-width: 100px;">
        <div class="container">
          <h4><b>Event notifications</b></h4>
        </div>
      </div>
    </a>
  </div>
  <div class="step-info">
    <div class="step-number">4</div>
    <p class="step-description configure-text">Subscribe to event notifications to receive order status updates</p>
  </div>
	</div>
</div>
</div>

<div class="step-item">
  <div class="card-container-setup">
    <a href="/docs/smartpos-features" style="text-decoration: none;">
      <div>
        <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Omnichannel-payments.svg"
          style="margin: 5px; max-height: 100px; max-width: 100px;">
        <div class="container">
          <h4><b>SmartPOS features</b></h4>
        </div>
      </div>
    </a>
  </div>
  <div class="step-info">
    <div class="step-number">5</div>
    <p class="step-description configure-text" style="margin-top: 12px !important;">Customize your payment flow with additional features</p>
  </div>
</div>

***

If you encounter issues during the set-up of your terminal, visit our [POS troubleshooting](<>)  page for common solutions.

[Top of page](#)