---
title: "Software clients"
date: 2025-06-23T13:19:26.375Z
weight: 7
---

#### 7 Software clients

A software client establishes a connection between an organization's Jabra devices and the platform. Installing and running a software or desktop client ( Jabra+ desktop app) on a computer is a prerequisite to remote manage Jabra personal or meeting room devices and adds them to virtual inventories.

On the one hand, you can generate and download from the Jabra+ platform, the specific software client for the relevant Jabra device type.

On the other hand, for Jabra devices using the Jabra+ for installers app and Jabra devices with a builtin client, you must generate a provisioning code, which is also generated from within the platform, and has an expiration date.

| Jabra+ desktop software  client  ▼   | Meeting room software  client  ▼    | Built-in software client   ▼                                                                                  | Jabra+ for installers  software client  ▼          |
|--------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Jabra personal devices               | Jabra PanaCast 50 Room  System (RS) | Jabra PanaCast 40/50  Video Bar System (VBS)  All-in-One & Jabra  PanaCast 40/50 Video  Bar System (bar only) | Jabra PanaCast 50  - Bring Your Own Device  (BYOD) |

#### Important note

You cannot install the Meeting room software client and the Desktop client (i.e.: the Jabra+ desktop app) on the same computer.

#### 7.1 Jabra+ desktop software client

Jabra+ desktop is both a software client (Desktop client) and an app that connects Jabra personal devices to the platform.

You can generate and download Jabra+ desktop from within the relevant organization in the Jabra+ platform. When you download the Jabra+ desktop app, it is recommended to save it with a meaningful name related to the organization. For example, My Company´s desktop application .

You or an AV Installer must then deploy or distribute Jabra+ desktop to the relevant organization's end-users as you best see fit.

#### 7.1.1 Creating and downloading Jabra+ desktop

This procedure is a prerequisite to manage Jabra personal devices in the Jabra+ platform. To do this, you must generate or create the software client, which is exclusive to an organization.

To create and download Jabra+ desktop:

- 1. On the left-hand navigation bar, click Personal devices &gt; Desktop clients
- 2. Click Create desktop client
- 3. In the Create desktop client dialog box, in the Name field, enter a name for your client for example, Human Resources, and click Next

#### Tip

When downloading Jabra+ desktop, ensure you give it a meaningful name. This lets you have a contingency plan in case security or other matters compromise the Jabra personal devices in the grouping.

Therefore, in the case that you must delete Jabra+ desktop (Desktop client) from a relevant organization, you can isolate and stop data transmission from Jabra personal devices in that grouping only and not the entire organization.

- 4. In the Download desktop client dialog box, click Download . The Jabra+ desktop app installation file is downloaded to your default Downloads folder associated with your Internet browser.

At this point, you can perform or delegate the installation procedure. For guidance, see the Device Provisioning and Onboarding Guide.

#### 7.2 Meeting room software client

There is an instance of a Jabra meeting room device that is connected to a meeting room computer (or ThinkSmart ™ Core) and is provisioned in a Microsoft® Teams Rooms or Zoom Rooms setup. This requires you to first create and download a Meeting room software client in the Jabra+ platform.

It is recommended that after creating the Meeting room software client , you save it with a meaningful name related to the organization, such as ABC Company Meeting room software client .

You, the admin user or an AV Installer, must then deploy or distribute this client, which adds the Jabra meeting room device to the organization's room inventory .

#### 7.2.1 Creating and downloading the Meeting room software client

To begin provisioning, you must create and deploy the Meeting room software client on all meeting room computers connected to your Jabra meeting room device, so they can connect to your organization.

To create and download the Meeting room software client:

- 1. On the left-hand navigation bar, click Meeting rooms &gt; Room clients
- 2. Click Create meeting room client
- 3. In the Create meeting room client dialog box, in the Name field, enter a name for your client for example, Meeting room 1 client, and click Next

#### Tip

You can give the Meeting room software client a meaningful name, allowing you to have a contingency plan in case security or other matter compromises the Jabra meeting room devices in the relevant grouping.

Therefore, if you must delete a Meeting room software client from a relevant organization, only the Jabra meeting room devices in that grouping stop sending data to the Jabra+ platform, and not the Jabra meeting room devices in the entire organization.

- 4. In the Download meeting room client dialog box, click Download . The installation file is downloaded to your default Downloads folder associated with your web browser.

At this point, you can perform or delegate the installation procedure. For details, see the Device Provisioning and Onboarding Guide.

#### 7.3 Jabra+ for installers software client or using a provisioning code

There are Jabra meeting room devices that require a provisioning code to add them to an organization´s room inventory .

On the one hand, some Jabra meeting room devices have a built-in software client, letting you, an admin user, or AV installer link the device in a physical meeting room to an organization in the platform.

On the other hand, another type of Jabra meeting room device that is provisioned in a BYOD setup requires Jabra+ for installers, a standalone app that helps provision this specific type of Jabra meeting room device. You or an AV Installer can download the app directly from the following link.

In both cases, to initiate the provisioning process, you must generate the provisioning code from within the platform and note it down before starting the relevant provisioning procedure described in the Device Provisioning and Onboarding Guide.

#### 7.3.1 Viewing or generating a provisioning code

A provisioning code is a 12-digit alphanumeric code that connects or links specific Jabra meeting room devices to the Jabra+ platform. You can view or generate the provisioning code from the Room inventory menu item.

#### Note

The provisioning code is valid for 14 days from the day it was generated. During provisioning, if you get a Code has expired error message, you must generate a new code before continuing.

To view or generate a provisioning code:

- 1. Log in to the Jabra+ platform as an owner or member with edit rights
- 2. On the left-hand navigation bar, click Meeting rooms &gt; Room inventory
- 3. On the left-hand Locations bar, at the top of the list, click the action menu (three-dot menu) next to the name of your organization
- 4. Click Provisioning code
- 5. In the Provisioning code dialog box, in the Provisioning code field, copy or note down the alphanumeric code
- o If you must generate a new code, in the Provisioning code dialog box, click Generate a new code

You can note down the organization´s 12-digit provisioning code in the spaces below for future reference:

At this point, you can perform or delegate the installation procedures, described in the Device Provisioning and Onboarding Guide.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000065_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

#### Appendix

The following procedures are complementary to the Jabra+ platform and can be performed ad-hoc.

#### ➢ Detailed whitelist domain requirements

If you cannot whitelist parent domains with a wildcard (*) as a prefix, the following table lists the specific subdomains, denoted with a ( ▶ ).

|              | Specific subdomain (prefix instead of  *wildcard)       | Outbound  TCP  port(s):   | Description                                                                                        |
|--------------|---------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------|
| Jabra+  core | https://*.cloud.jabra.com/*                             | 443                       | Used to access the  Jabra+ platform                                                                |
| Jabra+  core | ▶  https://cloud.jabra.com/*                            | 443                       | Used to access the  Jabra+ platform                                                                |
| Jabra+  core | ▶  https://signalr.cloud.jabra.com/*                    | 443                       | Used to establish real-time  connections of Jabra devices  to the platform and for  sending events |
| Jabra+  core | ▶  https://api.cloud.jabra.com/*                        | 443                       | The main API used by  Jabra+  software clients                                                     |
| Jabra+  core | ▶  https://file.cloud.jabra.com/*                       | 443                       | Used exclusively to  download Jabra+ for  installers  *.msi  files stored  in Azure blobs          |
| Jabra+  core | ▶  https://content.jabra.com/*                          | 443                       | Used by the Content  Delivery Network (CDN) for  translations                                      |
| Jabra+  core | wss://*.cloud.jabra.com/*                               | 443                       | Used by SignalR WebSocket  communication layer for  responsive UI                                  |
| Jabra+  core | ▶  wss://signalr.cloud.jabra.com/*                      | 443                       | Used by SignalR WebSocket  communication                                                           |
| Jabra+  core | https://*.azure-devices.net/*                           | 443, 5671                 | Used by Jabra devices, the  IoT Hub service facilitates  communication with Azure  Cloud services  |
| Jabra+  core | ▶  https://jabra-prd-westeu- iothub.azure-devices.net/* | 443, 5671                 | Used by Jabra devices, the  IoT Hub service facilitates  communication with Azure  Cloud services  |
| Jabra+  core | https://*.cookiebot.com/*                               | 443                       | Used for collecting consent.  If no consent is given, no  data is collected                        |
| Jabra+  core | ▶ https://consentcdn.cookiebot.com/*                    | 443                       | Used for collecting consent.  If no consent is given, no  data is collected                        |
| Jabra+  core | ▶  https://consent.cookiebot.com/*                      | 443                       | Used for collecting consent.  If no consent is given, no  data is collected                        |

| Jabra+  analytics  related   | https://*.hotjar.com/*  ▶  https://ws.hotjar.com/*  ▶  https://script.hotjar.com/*  ▶  https://static.hotjar.com/*   |   443 | Used for heatmaps, screen  recordings, and feedback   |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|-------|-------------------------------------------------------|
| Jabra+  analytics  related   | https://*.google-analytics.com/*  ▶  https://region1.google- analytics.com/*                                         |   443 | Used for in-app event  statistics collection.         |

#### ➢ Device Management System matrix

The following table informs you of known Jabra+ compatibility issues with other device management systems and offers recommendations when more than one system is used together at the same time with the platform.

| Device  Management  System   | Potential issues                                                                                                                                                                         | Recommendation                                                                                                                                                                                                                                                                                                                               |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Jabra Xpress                 | When using both systems at the same  time, duplicate device management can  cause a conflict.                                                                                            | Not recommended. Avoid using  the  Jabra+  platform and  Jabra  Xpress  at the same time.  For more information, see the  Migration from Jabra Xpress to  Jabra+ topic.                                                                                                                                                                      |
| Jabra Direct                 | Using both systems simultaneously can  cause device management conflicts,  except during initial setup for Jabra  meeting room devices or when using  older Jabra personal devices.      | Not recommended. Avoid using  the  Jabra+  platform and  Jabra  Direct  at the same time.                                                                                                                                                                                                                                                    |
| Jabra Direct                 | Exception for meeting room devices  Setting up  Whiteboard view  is not  supported natively in the  Jabra+ platform.                                                                     | Exception for meeting room  devices You can still use  Whiteboard view in the  Jabra+  platform after you  set it up in  Jabra Direct .   After setting up  Whiteboard view ,  you must close, exit, or uninstall  Jabra Direct  and continue using  Jabra+  platform only. For  guidance, see the Jabra meeting  room device documentation. |
| Jabra Direct                 | Exception for personal devices  You can use  Jabra Direct  or  Jabra  Xpress  to update the firmware of older  Jabra personal devices. To check  whether your Jabra device is compatible | Exception for personal devices  After updating the firmware using  Jabra Direct  or  Jabra Xpress ,  ensure you uninstall them.                                                                                                                                                                                                              |

|                                                      | with  Jabra+ , see Supported Jabra  devices.                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lenovo  ThinkSmart ™ Manager  (basic +  premium)     | When using both systems at the same  time, duplicate device management can  cause a conflict and settings can be  overwritten.                                                                                                                                                                                                                                                                                    | Not recommended. Avoid using  the  Jabra+  platform and Lenovo  ThinkSmart ™  Manager at the same  time.                                                                                                                                                                                                                           |
| Zoom Device  Management  (firmware  management only) | Managing device firmware on both  device management systems is not  recommended.                                                                                                                                                                                                                                                                                                                                  | Choose the  Jabra+  platform as the  primary firmware management  platform instead of Zoom Device  Management.  If firmware must be managed  using Zoom's Device Management  instead of the platform, ensure the  firmware policy is disabled in the  platform.  See the firmware policy chapter  for the procedure.               |
| Microsoft Teams  Pro Manager  Portal                 | Both device management systems can  run at the same time.  No known conflicts exist.                                                                                                                                                                                                                                                                                                                              | Ensure the  Jabra+  platform and  Microsoft® Teams Pro Manager  Portal are set up/configured to  avoid conflicts.                                                                                                                                                                                                                  |
| Windows Update  (firmware  management only)          | Firmware management can be handled  side by side only if one of the two  firmware management systems is  disabled. Either disable it in the  Jabra+ platform or pause Windows Updates.  Note  If the organization has Jabra meeting  room devices, an  owner  or  member with  edit rights  (for meeting rooms) must  choose whether to firmware manage  through Windows Update or through the  Jabra+  platform. | To keep a fixed firmware version  on Jabra meeting room devices,  then disable the  Always keep  devices updated  toggle switch in  the  Jabra+  platform and pause  Windows Updates.   To do this, see the modifying &  setting the firmware policy for  specific Jabra device models  procedure in the firmware policy  chapter. |
| Crestron XiO  Cloud                                  | When using both systems at the same  time, duplicate device management can  cause a conflict.                                                                                                                                                                                                                                                                                                                     | Not recommended. Avoid using  the  Jabra+  platform and XiO Cloud  at the same time.                                                                                                                                                                                                                             

#### Migrating from Jabra Xpress to Jabra+

The Jabra+ platform does not provide tools for automatic migration of settings and room information from Jabra Xpress to the platform. This must be done manually.

#### Important note

There can only be one instance of a Jabra software client running on one individual computer.

If you are a current user of Jabra Xpress and/or Jabra Direct client, you can optionally migrate settings and room information to the Jabra+ platform. To do so, complete the procedure that follows and perform the migration, and afterwards uninstall Jabra Xpress .

Be aware that the software clients in Jabra+ were designed for a ' clean install ', i.e., without other Jabra applications previously installed. Therefore, it is not recommended to use the Jabra+ platform's software clients simultaneously with other Jabra software or partner applications (e.g.: ThinkSmart ™ Manager, Jabra Integration Services, Jabra Xpress , or Jabra Direct client) on the same computer .

To prevent conflicts or unexpected behavior -and only after you perform the optional migration -you must uninstall other Jabra software or partner applications before continuing with provisioning Jabra devices into the platform. After migration, you can uninstall the Jabra Direct client and stop using Jabra Xpress to manage your Jabra devices.

#### Gradual migration

To reduce downtime, you can perform a gradual migration, as the Jabra Xpress solution (i.e.: Jabra Xpress Jabra Xpress , Cloud, Jabra Xpress Tenant, Jabra Xpress Packages) can work in parallel with the Jabra+ platform.

However, the Jabra Direct client must not be installed on the same computer, where the platform's software clients are also installed.

To perform the migration, ensure you follow procedures A and B.

#### A. Copy existing settings

To migrate your settings into the Jabra+ platform from Jabra Xpress :

- 1. Launch Jabra Xpress
- 2. On the left-hand navigation bar, click Devices &gt; Manage
- 3. Click on the relevant Jabra device and manually copy the settings using your preferred method. For example, you can copy the settings to a text or spreadsheet. After provisioning your Jabra device to the Jabra+ platform, ensure you create a configuration with the settings from Jabra Xpress .

At this point, you can continue with the next procedure Export room information . If you do not have to do this, to finish, ensure you uninstall Jabra Xpress .

#### B. Export room information

In Jabra Xpress , the Room Insights menu item contains analytics information about meeting room(s), room usage, capacity thresholds, Jabra device usage, and more.

You can export this data as a *.csv file and keep it for backup. To do this:

- 1. Launch Jabra Xpress
- 2. On the left-hand navigation bar, click Analytics &gt; Room Insights
- 3. In the Select Time Range ribbon, on the right-hand side of the screen, click Export
- 4. Enter a name for the file and click Save
- 5. Ensure you uninstall Jabra Xpress

#### ➢ Disabling Metadata collection

Metadata collection lets you gather end-user data such as Computer username, Computer information, and Location, among other information. Metadata collection is enabled by default when you create an organization. However, you can also disable it if necessary.

This metadata is necessary to identify and manage Jabra devices and meeting rooms. More specifically, when the Metadata collection checkboxes are checked, the following information is collected and sent to Jabra+ :

- · Computer Username : The username of the operating system where the software client is running
- · Computer Information : A set of values showing Computer name, Operating system name, Operating system version, List of IP addresses, Domain name, Computer manufacturer´s name, Computer serial number
- · Location : Information about computer location if available from the system. This information needs to be accessible to the software client first

#### Important note

Your organization may want to disable metadata collection due to legal concerns or privacy policies.

To disable metadata collection:

- 1. On the left-hand navigation bar, click the name of the organization you are currently the owner of or belong to, and then Organization settings
- 2. On the Organization Settings page, in the Metadata collection section, uncheck the checkboxes, i.e., Computer information, Location, and Username
- 3. To confirm your metadata collection choices, click Save

At this point, your Jabra personal and meeting room devices stop collecting metadata.

#### ➢ Firmware bundles and specific firmware versions

Firmware bundles are exclusive to PanaCast 40 and 50 VBS video bars, and they contain a package of firmware versions that ensure the touchscreen tablet/touch controller can work with the video bar, avoiding incompatibility issues. This is due to the tablet having its own firmware.

For example, Bundle 1.0.0 includes two firmware: one for the video bar (i.e. 6.5.0 PanaCast 50 VBS bar ) and another for the touchscreen tablet/touch controller (i.e. 6.5.0 PanaCast Control ).

#### Specific firmware versions for PanaCast 50 VBS

When you create a room configuration from scratch, or set exceptions in the standard room configuration , and you want to run an earlier firmware version than 6.5.0 , you must select the old card i.e.: PanaCast video bar system (Firmware release: February 2025 or older)

#### Important note

Before installing firmware version 6.5.0 or later, on your PanaCast 50 VBS with Microsoft® Teams as the video service provider, you must migrate the affected Jabra meeting room device to Android OpenSource Project (AOSP) and upgrade to the Microsoft® Device Ecosystem Platform (MDEP). The migration ensures that the connection to your current rooms is not severed by a firmware update to version 6.5.0 or later. For migration instructions, read the Android Migration Guide.

However, if you have updated the firmware of your PanaCast 50 VBS to version 6.5.0 or later, then you must select the PanaCast 50 VBS option together with the relevant video service provider i.e.: Microsoft Teams Zoom , or BYOD .

#### ➢ Duplicating a configuration for personal or meeting room devices

You can also duplicate a configuration or room configuration and assign it to many rooms or device groups .

Duplicating a configuration with custom Jabra device model settings, firmware policy, and locked enduser settings allows you to create multiple similar configurations/room configurations and make small changes if necessary.

To duplicate a configuration/room configuration:

- 1. On the left-hand navigation bar, click Meeting rooms &gt; Room configurations , or in the case of personal devices, click Devices &gt; Configurations
- 2. On the Room configurations/Configurations page, click the pane with the configuration name you would like to duplicate
- 3. On the configuration page you would like to duplicate, click the action menu (three-dot menu)
- 4. Click Duplicate configuration
- 5. In the Duplicate configuration dialog box, in the Configuration name field, enter a name. Optionally, in the Description field, enter a description for the duplicated room configuration/configuration.
- 6. Click Save Changes

For your duplicated configuration to take effect, you must assign a created configuration to a device group or a room.

#### ➢ Bulk assigning a previously created room configuration to many rooms

For a configuration to take effect on specific rooms with Jabra meeting room devices and replace the default standard room configuration for the specific rooms, you must change the assigned configuration of the room. When required, you can also select multiple rooms and bulk assign a room configuration that was created.

To bulk-assign a previously created room configuration to a room:

- 1. On the left-hand navigation bar, click Meeting rooms &gt; Room inventory
- 2. On the Meeting room inventory table, check the checkbox for the relevant room name(s)
- 3. In the bottom ribbon, click Assign configuration

- 4. In the Change room configuration dialog box, in the drop-down menu, select the configuration name you created, and click Apply to confirm. Now, you have bulk-assigned a Room configuration you created for one or many rooms.

#### ➢ Rebooting Jabra meeting room devices

The Jabra+ platform lets you remotely reboot Jabra meeting room devices. The reboot feature is the first step in troubleshooting any undesired behavior or errors and can be performed on all Jabra meeting room devices.

In the case of PanaCast 40/50 VBS, both the meeting room device and the Jabra PanaCast Control/Touchscreen tablet are simultaneously rebooted.

#### Important note

Rebooting Jabra devices from within the platform is only available when the Jabra meeting room device appears Online (connected) in the room inventory.

Also, the Jabra meeting room device must not be in an active meeting or call; otherwise, the Reboot device option is unavailable or greyed out.

To reboot a Jabra meeting room device:

- 1. On the left-hand navigation bar, click Meeting rooms &gt; Room inventory
- 2. On the Meeting room inventory page, in your Locations tree structure, click the name of your organization
- 3. On the Meeting room inventory table, click the relevant room name
- 4. On the Room page, click the action menu on the relevant pane that shows the Jabra meeting room device you would like to reboot and click Reboot device
- 5. In the Are you sure you want to reboot? dialog box, click Confirm

#### ➢ Pairing your Jabra Bluetooth adapter &amp; personal device in Jabra+

For the Jabra+ (desktop) app to work with your wireless (Bluetooth) Jabra personal device, you must install the Jabra Link Bluetooth adapter and pair it to your Jabra personal device.

As a prerequisite, ensure you have first installed the Jabra+ app (Desktop client) on the end user´s computer.

#### Note

For cabled or wired Jabra personal devices, you do not have to perform the procedure that follows.

To pair your Jabra Link Bluetooth adapter and Jabra personal device (Bluetooth device):

- 1. Insert the Jabra Link Bluetooth adapter into a USB port on your computer and ensure the Jabra personal device is switched ON and within range
- 2. Put your Jabra personal device in pairing mode
- 3. On your Windows system tray, right click the Jabra+ app icon and click Pairing
- 4. When the app detects your Jabra Link Bluetooth adapter it searches for your Jabra personal device. When detected, in the Available devices dialog box, click the Jabra device(s) you would like to pair. When pairing is successful, you see a Device connected message.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000076_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png)

#### ➢ Recovering your Jabra personal device after a failed firmware update

In the Jabra+ desktop app, if your firmware update fails, it is interrupted or did not complete, the end user is prompted to recover their Jabra personal device.

During the recovery process, Jabra+ retries installing the previously failed firmware update.

#### Note

The following procedure applies only to cabled or wired Jabra personal devices. Jabra wireless or Bluetooth personal devices do not need to be recovered.

To perform firmware recovery on wired or cabled Jabra personal device(s):

- 1. If your firmware update fails, a notification informs you, and you can begin the recovery process. In the Something went wrong dialog box, click Recover device

Note

You may be asked to unplug or undock all other Jabra devices to start the recovery.

- 2. Recovery in progress dialog box shows the duration of the recovery. When it is finished, in the Recovery complete dialog box, click OK

The recovery is now completed. The Jabra+ desktop app checks again whether your Jabra personal device requires a firmware update. Click OK to finish.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000077_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png)

#### Troubleshooting

| Problem                                                                                                                                                                                                       | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I have modified my Jabra account  profile information, but the changes  are not reflected in the  Jabra+ platform .  Note  If you have enabled SSO in your  organization, you cannot  perform this procedure. | 1. On the left-hand navigation bar, click your profile name  (user icon)  2. Click  Personal details 3. On the  Personal details  page, click the  Edit profile button. You are now taken to an external webpage  4. In the Account tab, under Display name, click  Edit 5. In the provided field, enter the new display name and  click  Save .  Now, you can close the web browser and return to the  Jabra+ platform. Ensure you log out of the platform and log back in to  see the reflected changes to your display name in the  Profile > Personal details  page.  6. At this point, on the  Personal details  page, click the  Sync profile  button.  You will get a notification that your profile on Jabra.com  has been synced with the  Jabra+  platform. |
| I created and installed a software  client, but my Jabra device (Meeting  room or Personal device) does not  appear in the  room inventory  or  device inventory .                                            | • If the Jabra meeting room or personal device is not  visible in the relevant inventory, the end user must  restart the computer that the Jabra device is connected  to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| I tried to update the firmware of my  Jabra meeting room device;  however, the process stopped  during the update, and I cannot  continue updating it.                                                        | • PanaCast 50 RS: If the firmware update fails, ensure you  reboot the Jabra meeting room device. The firmware  update resumes automatically, in the context of  scheduled device updates.  • PanaCast 50 BYOD: Ensure you unplug the Jabra meeting  room device from the power supply/outlet and plug it  back in. You can now retry the firmware installation.  • PanaCast 40/50 VBS: See the error message displayed in  the PanaCast Control/Touchscreen tablet.  Restart/reboot the Jabra meeting room device and retry  the firmware update.  Important note  For instructions on rebooting, ensure you read the                                                                                                                                                |
| As an end user, I tried to update the  firmware of my Jabra personal  device, but the process was  interrupted or did not complete,  and my device does not work, or the  firmware was not installed.         | relevant Jabra meeting room device documentation.  • You must perform a firmware recovery.   See the Recovering your Jabra personal device after a  failed firmware update topic.  Be aware that this procedure only applies to cabled or  wired Jabra personal devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000078_bbecf688b110ba1d6901c10a79565f159c169cf1eca9daebe330421c72efc123.png)

| When I want to perform a  procedure, some of the menus  appear greyed out or unavailable.                                                                                                                                                                                                                                | • The admin user performing the procedure may not have  the correct permission to do so. See the Roles and  permissions chapter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I tried to update the firmware of  certain Jabra personal devices in  the  Jabra+  platform , however, I see  a message  Firmware updates are  ' not supported in  Jabra+ , use  Jabra  Direct  or  Jabra Xpress  to update  the device when required' , how can  I update the firmware of my Jabra  personal device(s)? | • Jabra personal devices with older hardware must be  firmware updated using  Jabra Direct  or  Jabra Xpress .  Ensure that you first update the firmware using  Jabra  Direct  or  Jabra Xpress , and after the update is  completed, you must uninstall  Jabra Direct  (or stop  using  Jabra Xpress ) and continue using the  Jabra+ desktop app.  For the list of Jabra personal devices that may require a  firmware update using  Jabra Direct  or  Jabra Xpress ,  see the Supported Jabra devices list.  Be aware that some of the settings of your older personal  device(s) may not be available in the  Jabra+  platform.                                                                                       |
| There is a  Configuration warning message in a (room) configuration  (or configuration for personal  devices) that I created. How can I  address the warning?  I also see an  exclamation mark ( ) on some Jabra  ! devices in my  device inventory  (or  room inventory .                                               | • When a previously selected firmware version in a  configuration becomes unsupported, subsequent Jabra  devices added to the respective inventories keep their  existing firmware and cannot update to the unsupported  version.  • To remove the exclamation mark  (!)  and the  Configuration warning  message, you must select a  different firmware version and edit the firmware policy.  To do this, see the procedure Modifying & setting the  firmware policy for specific Jabra device models or if you  have configurations assigned to a specific room or Jabra  personal devices in a device group, see the Modifying &  setting an existing firmware policy for a specific room or  device group  procedure. |

If you require further assistance, would like to get in touch with Jabra, or consult other documents, ensure you visit the Jabra+ support page.