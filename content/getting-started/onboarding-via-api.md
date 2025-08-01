---
title: "Onboarding & affiliate management via API"
category: 627bbcf80c1c9c0050320b60
parentDoc: 62a2055be5b9db006a2545a7
order: 2
hidden: true
slug: 'onboarding-affiliates-via-api'
excerpt: ''
---

Partner account holders can manage and onboard affiliated merchant accounts via our API.

# Authentication

To authenticate requests, you must include a **partner account** API key.\
For more information, email your partner manager.

# Affiliate Onboarding

The table below lists our API references for onboarding an affiliate's account.

<table>
  <thead>
    <tr>
      <th>Onboard account</th>
      <th style={{ textAlign:'left' }}>API reference</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Create merchant account</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/createaffiliate" target="_blank">Create affiliate</a>

        <i class="fa fa-external-link" />
      </td>
    </tr>

    <tr>
      <td rowspan="3">Provide bank accounts</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/addaffiliatebankaccount" target="_blank">Add bank account</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/listaffiliatebankaccounts" target="_blank">List bank accounts</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/getbankaccount" target="_blank">Get bank account</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>Validate the ownership of a bank account</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/validatebankaccount" target="_blank">Validate bank account</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td rowspan="3">Provide bank statement</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/addbankstatement" target="_blank">Add bank statement</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/listbankstatements" target="_blank">List bank statements</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/getbankstatement" target="_blank">Get bank statement</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td rowspan="2">Manage merchant account</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/addaffiliatesite" target="_blank">Add site</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/listaffiliatesites" target="_blank">List sites</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td rowspan="4">Provide UBO details</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/addaffiliateubo" target="_blank">Add UBO</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/listaffiliateubos" target="_blank">List UBOs</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/updateubo" target="_blank">Update UBO</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/getubo" target="_blank">Get UBO</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td rowspan="3">Provide identity document</td>

      <td>
        <a href="https://docs.multisafepay.com/reference/addidentitydoc" target="_blank">Add identity document</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/listidentitydocs" target="_blank">List identity documents</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>

    <tr>
      <td>
        <a href="https://docs.multisafepay.com/reference/getidentitydoc" target="_blank">Get identity document</a>

        <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
      </td>
    </tr>
  </tbody>
</table>

# Affiliate management

The table below lists our API references for managing an affiliate's account.

<table style={{ textAlign:'left' }}>
  <tr>
    <th>Manage account</th>
    <th style={{ textAlign:'left' }}>API reference</th>
  </tr>

  <tr>
    <td rowspan="5">Access affiliated accounts</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/listaffiliates" target="_blank">List affiliates</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/reference/getaffiliate" target="_blank">Get affiliate</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/docs/generate-login-url-1" target="_blank">Create login URL</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/reference/updateaffiliate" target="_blank">Update affiliate</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/reference/listaffiliatebalances" target="_blank">List affiliate's balances</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>Charge fees to affiliates</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/chargeaffiliate" target="_blank">Charge affiliate</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>Fund affiliates</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/partnercreatefundforsubaccount" target="_blank">Fund affiliate</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td rowspan="2">Payout affiliates</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/payoutaffiliate" target="_blank">Payout affiliate</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/docs/auto-payouts" target="_blank">Auto payouts</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td rowspan="2">Access requests made to affiliates</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/partnerlistaccountinquiries" target="_blank">List inquiries</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/reference/partnergetaccountinquiry" target="_blank">Get inquiry</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td rowspan="2">Access messages sent to affiliates</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/partnerlistaccountmessages" target="_blank">List message</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://docs.multisafepay.com/reference/partnergetaccountmessage" target="_blank">Get message</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>List all UBOs</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/listaffiliateubos" target="_blank">List UBOs</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>Get closing balances</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/partnerlistaccountclosingbalances" target="_blank">List affiliate's closing balances</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>Adjust fees</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/partnerupdatefee" target="_blank">Adjust fees for an affiliate account</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>

  <tr>
    <td>Get website categories</td>

    <td>
      <a href="https://docs.multisafepay.com/reference/listsitecategories" target="_blank">List website categories</a>

      <i class="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }} />
    </td>
  </tr>
</table>

***

<HTMLBlock>{`
<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>
`}</HTMLBlock>

[Top of page](#)