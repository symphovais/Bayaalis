---
title: "Quick Start Guide"
date: 2025-06-23T11:31:49.941Z
weight: 2
---

## 2 Quick Start Guide

All procedures in this chapter are mandatory unless stated otherwise.

## Step 1

To quickly get started with the Jabra+ platform, you must perform both of the following procedures:

- Creating a Jabra+ account
- Creating an organization

After creating an account, you must log in and you are prompted to create an organization (such as a business or corporation), which is a representation of the company/business in the platform and has a unique organization ID.

When creating an organization, data tracking and metadata collection are enabled by default. Although you can disable metadata collection at a later time, it is recommended that you review and decide on the Metadata collection settings before provisioning Jabra devices to the platform.

After creating the organization, you become the owner (of the organization) and can then choose how to grant access to subsequent admin users. This is done by either enabling single sign-on (SSO) and using Microsoft® Entra for user management or you, the owner, can manually invite additional admin users to the platform.

## Step 2 (Optional)

After account and organization creation, you can enable SSO and invite additional admin users to the platform. Both of the following procedures are optional. If you do not wish to do so, you may continue to End of QSG -Next steps.

- Enabling single sign-on (SSO)
- Inviting additional admin users

Only owners and members with edit rights in the Jabra+ platform can download organization-specific software clients, manage Jabra devices remotely, set the settings for one or a group of Jabra devices, manage the firmware, and more. For conceptual information on the different components of the platform, read the Jabra+ platform chapter.
 
## 2.1 Creating a Jabra+ account

In the Jabra+ platform, you must first create a Jabra+ account.

To create an account:
 
- 1. In a web browser, enter the following URL: https://cloud.jabra.com
- o Alternatively: On the public product page for Jabra+, on the upper right-hand side of the screen, click the account icon.
- 2. In the Log in to Jabra+ pane, click Create account.
- 3. On the Jabra Login page, click Sign up now.
- 4. On the Create Account page, enter your business email address, and click Send verification code.
- 5. At this point, you receive a confirmation email with a verification code. Ensure you copy the verification code, and then return to https://cloud.jabra.com.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts/image_000012_fa1e155445bfc8bc513c5e792919a9c310eda864d6f00f8b8fd6b360b0fa2f5b.png)

- 6. On the Create Account page, ensure you enter the code, click Verify code and then click Continue on the next screen.
- 7. On the Create Account page, you must choose your Country/Region and on the Display name field you must enter a name or alias, as this is your username within the Jabra+ platform. Ensure you also create a password following the guidelines, accept the terms of service and click Next.

After your initial sign-in to the platform, the owner is prompted to create an organization.

## 2.2 Creating an organization

After you complete the sign-up (first-time registration) process for an account and log in to the platform with your email domain, you, the admin user (now the owner), are prompted to create an organization, for example, ABC Company.

For conceptual information and guidance, see the Organizations topic.

To create an organization upon first-time login:

- 1. In the Create organization dialog box, in the field provided, enter a name for your organization. Ensure you provide a meaningful name, as there may be a need to invite additional admin users to the organization.

**Note**

The platform supports ASCII and non-ASCII characters, such as accented letters, non-Latin alphabets, and symbols, however an organization cannot be renamed, so ensure the naming of the organization is correct.

- 2. In the Create organization dialog box, click Continue.
- 3. In the Set up device metadata dialog box, check the relevant device metadata checkboxes, and to save your selections, click Continue. For more information about device metadata, see the Disabling Metadata collection topic in the Appendix.
- 4. In the Organization created dialog box, ensure you read the Privacy Policy and License Agreement, and then click Get started.

You are now the owner of the organization you created and are directed to the Dashboard.

At this point, you can enable SSO to grant additional admin users access to the organization. Otherwise, if SSO is disabled, you can follow the Inviting additional admin users procedure.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts/image_000013_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

## 2.3 Enabling single sign-on (SSO)

An organization owner can enable SSO in the platform. This ensures that only admin users from preapproved domain(s) can log in and access the organization.

**Note**

Due to an update in the SSO process, Early Adopters Program (EAP) customers can migrate their admin user accounts to the new SSO setup. If you have multiple organizations under the old SSO, you can only associate the new setup with one organization. For more details, request the SSO Optional Migration Guide from your Jabra representative.

When SSO is enabled, all admin users authenticate using Microsoft® Entra and can only access the one organization. Be aware that by default, all admin users are given read-only access. Access rights, i.e., granting owner or edit permissions for meeting rooms and/or personal devices, is assigned exclusively in Microsoft® Entra.

If the organization does not want to use SSO, an owner can invite other admin users individually. If needed, you can also disable SSO and after two hours, admin users can no longer log in to the organization using SSO.

## Important note

When SSO is enabled, certain functionalities are not available in the Jabra+ platform, for example, admin users cannot invite additional admin users, edit permissions, change their Jabra+ profile or leave an organization.

Additionally, be aware that when SSO is enabled, admin user activity or history is not logged. See the Viewing admin user activity or history section.

To enable SSO for all admin users in the organization:

- 1. In a web browser, enter the following URL: https://cloud.jabra.com
- o Alternatively: On the public product page for Jabra+, on the upper right-hand side of the screen, click the account icon.
- 2. In the Log in to Jabra+ pane, in the Email field, enter your business email address and click Continue with email.
- 3. On the left-hand navigation bar, at the bottom of the page, click the name of the organization you are currently the owner of, and then click Organization settings.
- 4. On the Organization Settings page, in the Single sign-on (SSO) pane, click Enable.

At this point, you are prompted to log in to Microsoft® Entra and then verify and accept the permissions requested. In the Jabra+ platform, in the Single sign-on enabled dialog box, click OK.

To continue, return to Microsoft® Entra and grant additional admin users access to the platform. For details on the scope of roles, refer to the Roles and permissions chapter.

After enabling SSO and granting access to other users, the admin user can continue with the End of QSG -Next Steps.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts/image_000014_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png)

## 2.4 Inviting additional admin users

If SSO is disabled, the owner can invite other admin users (i.e., additional owner roles and/or members with either edit rights or read-only rights) to grant them access to the organization.

Adding a second owner to the organization is advisable, as it can be helpful if access to the platform is lost. Only an owner can invite a new admin user, send, resend or revoke invitations, and edit permissions on behalf of all admin users in the organization.

After inviting additional admin users (SSO is disabled), be aware that user management takes place exclusively within the platform. For procedures, refer to the Changing roles, editing permissions or removing a user as an owner section.

An owner can invite multiple admin users, and invitations sent to additional admin users are valid for seven days.

To invite one or more admin users to the organization:

- 1. On the bottom left-hand side of the navigation bar, click the name of the organization you are currently the owner of, and then click Admin users.
- 2. On the Admin users page, on the top-right hand side of the screen, click Invite new user.
- 3. In the Invite new user dialog box, in the Email field, enter the new admin user's business email address.
- o To invite multiple members with the same permissions or additional owners, separate the email addresses with a comma (,) or semicolon (;).
- 4. In the Role section, click the relevant radio button for Member or Owner.
- o When selecting the Member role, in the Permissions section, for Meeting rooms and/or Personal devices management, click Edit or Read only.
- 5. Click Invite.

The Jabra+ platform sends an email prompting the recipient to create a Jabra+ account using a unique sign-up link. After creating an account, the added admin user can log in to the platform.

At this point, you can continue with the End of QSG -Next Steps.

## 2.5 End of QSG -Next Steps

At this point, you are now the owner of an organization, and you may or may not have invited additional admin users to the Jabra+ platform.

The next step is to provision Jabra devices to the newly created organization. You can refer to the Device Provisioning and Onboarding Guide for procedures.

When you have finished provisioning Jabra devices to Jabra+, you can return to Chapter 3 of this guide to continue configuring the platform.

## Device provisioning strategy

When adding Jabra devices to the platform, you, as an admin user, can perform the software client installation or the generating of the provisioning code.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts/image_000015_916cd71bb2c716679c18c63daa4bc6e99494f723392260d94089a57e20c71fff.png)

Alternatively, you can delegate the installation/provisioning to an AV Installer or third-party. If so, the organization's owner must provide the AV Installer or third-party with the software client(s) and/or provisioning code.

The following table outlines the types of Jabra devices and their respective software client.

| Type of Jabra device | Software client | Description | Pre-requisite step performed by an admin user |
|------------------------|-------------------|--------------|----------------------------------------------|
| Jabra personal devices (e.g., Evolve2 75, Engage 50, etc.)<br>Note: Includes Jabra speakerphones (e.g., Speak2 75, etc.) | Jabra+ desktop app 1 | A Windows® application and software client installed on all end-user computers | Create and download Jabra+ desktop |
| Jabra meeting room device Jabra PanaCast 50 Room System (RS) | Meeting room software client 1 | A client software file installed on the meeting room computer (or ThinkSmart™ Core) of the PanaCast 50 RS | Create and download Meeting room software client |
| Jabra meeting room device Jabra PanaCast 40/50 Video Bar System (VBS) | Built-in client | The software client is native on all variants of the PanaCast 40/50 VBS | View or generate provisioning code |
| Jabra meeting room device Jabra PanaCast 50 - Bring Your Own Device (BYOD) | Jabra+ for installers app | An application to exclusively provision PanaCast 50 in a BYOD setup | View or generate provisioning code |

1 Mass deployment option: An admin user or AV Installer can perform the software client installation in a mass deployment context. For details, options, and guidance, see the Mass deployment section in the Jabra+ Device Provisioning and Onboarding Guide.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts/image_000016_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png)