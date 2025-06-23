---
title: "Firmware management"
date: 2025-06-23T13:17:11.588Z
weight: 6
---

#### 6 Firmware management

You can remotely manage firmware and policies for Jabra personal and meeting room devices via the platform.

- · For Jabra personal devices : Firmware updates are performed through the Jabra+ desktop app. Admin users can select specific firmware versions for device models, applying them across inventories or device groups, as well as in exceptional cases downgrading firmware. If a firmware update fails, a recovery process is available for wired devices via the app. End-users receive prompts to update firmware based on organizational policies or can postpone them.
- · For Jabra meeting room devices : Firmware is managed directly on the platform, allowing updates or downgrades per organizational policies. Updates are pushed directly to the meeting room devices and follow a schedule update plan. Without a defined schedule, updates may interrupt meetings, as devices must reboot.

#### Important note

Jabra may cease support for certain firmware versions due to compatibility issues, security vulnerabilities, or regulatory changes. When a previously selected firmware version becomes unsupported, the affected Jabra devices continue to operate normally. However, subsequent Jabra devices added to the respective inventories keep their existing firmware and cannot update to the unsupported version.

When a specific firmware is no longer supported by Jabra, in the device inventory or room inventory an exclamation mark (!) indicates the affected Jabra devices. Additionally, a Configuration warning appears in the affected configuration or room configuration. For details, see the Troubleshooting section.

The end-user may continue to use the Jabra device with the unsupported firmware; however, the Jabra device´s settings can no longer be changed, and it is therefore not recommended.

To resolve this, an admin user in the platform with the relevant permissions must edit the configuration to either select a different firmware version or switch the toggle to Always use latest ON , automatically updating the Jabra device to the latest firmware.

To select a different firmware version, see the procedure Modifying &amp; setting the firmware policy for specific Jabra device models. If you have configurations assigned to a specific room or Jabra personal devices in a device group, see the Modifying &amp; setting an existing firmware policy for a specific Room or device group procedure.

#### 6.1.1 Firmware policy &amp; updates

The firmware policy -contained within Configurations -enables you to manage firmware for Jabra devices in the Jabra+ platform, giving end-users access to the latest updates and features for their Jabra device.

| Shown in Device or Room inventories | Description |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Postponed update 1 | The firmware update installation of the Jabra device has been delayed or postponed to a later time or date by the end-user. |
| Failed update | The firmware update installation of the Jabra device has failed on the end-user computer. The end-user can recover the Jabra device and retry the firmware update. Depending on the error code, the failed update can retry the update on its own. |
| Pending update | Waiting for the end-user to perform the firmware update. Can also occur if Jabra device is offline. |
| Latest installed | The installed firmware version being the most recent release which includes the latest improvements, features and bug fixes. This message is also displayed when firmware management is disabled. |
| Update available 1 | A new firmware version is available but has not yet been configured by you, the admin user. |

- · For personal devices

To modify the firmware policy and set it for all Jabra personal devices of a specific model:

1. On the left-hand navigation bar, click Personal devices &gt; Configurations
2. On the Configurations page, click the Standard Configuration pane
3. On the Standard Configuration page, in the Firmware Policy tab, switch OFF the Always keep devices updated toggle
4. In the bottom ribbon, when you click Publish changes and confirm, all Jabra personal devices continue using their current firmware version.
5. To choose a specific firmware version for a specific Jabra device model, click the Model Configurations tab
6. On the top right-hand side of the page, click Add model and select the Jabra devices that you want to set exceptions for, and on the bottom ribbon, click Continue
7. On the Manage settings page, in the Firmware pane, click the drop-down menu and select the firmware you want to use for the relevant configuration or toggle the Always use latest firmware switch
   - a. If you choose an older firmware than the one you are currently using, in the Downgrade firmware? dialog box, click Confirm
8. To apply the changes, in the bottom ribbon, click Publish, and in the Publish model settings? dialog box, click Publish again to confirm.

Next, ensure you assign a firmware policy to a device group that you have previously created; otherwise, your firmware policy is not applied.

For the custom firmware policy to take effect, perform the assigning a created configuration to a device group or a room procedure.

#### 6.1.5 Modifying &amp; setting an existing firmware policy for a specific room or device group

For a specific Jabra meeting room device model, an admin user can create a custom firmware policy in a room configuration that you created, which lets you set a specific firmware version for a Jabra meeting room device model which you can assign to a room.

For Jabra personal devices, you can create a firmware policy for a device group and apply the specific firmware version to all personal device models within the group.

For example, there may be a group of Jabra Evolve2 65 headsets within a specific device group, and the admin user wants a specific firmware policy to apply to that specific device group. In the case of meeting room devices, the admin user may have a specific firmware policy that was created and would like it applied to a specific room (with a meeting room device within the room).

- · For Meeting room devices

**Important note**

Before installing firmware version 6.5.0 or later, on your PanaCast 50 VBS with Microsoft® Teams as the video service provider, you must migrate the affected Jabra meeting room device to Android OpenSource Project (AOSP) and upgrade to the Microsoft® Device Ecosystem Platform (MDEP). The migration ensures that the connection to your current rooms is not severed by a firmware update to version 6.5.0 or later. For migration instructions, read the Android Migration Guide.

To modify the firmware policy and set it for all Jabra meeting room devices of a specific model:

1. On the left-hand navigation bar, click Meeting rooms &gt; Room configurations
2. On the Room configurations page, click the Standard Room pane
3. On the Standard Room page, in the Firmware Policy tab, in the Update devices using Jabra+ for Admins pane, toggle the switch ON to enable firmware management for all Jabra meeting room devices in the room inventory .

**Note**

When you switch OFF the toggle Update devices using Jabra+ for Admins , you manage firmware through a third-party platform.

4. In the Always keep devices updated pane, keep the toggle switch OFF
5. In the bottom ribbon, when you click Publish changes and confirm, all Jabra meeting room devices continue using their current firmware version
6. To select a specific firmware version or to Always use latest firmware for a specific Jabra device model, click Add model and on the list, select the relevant Jabra meeting room device model

- · For personal devices

To modify &amp; set an existing firmware policy for a specific Jabra personal device model in a device group:

1. On the left-hand navigation bar, click Personal devices &gt; Configurations
2. Click the pane with the relevant configuration where you would like to set a custom firmware policy
3. In the Firmware Policy tab, in the Update devices using Jabra+ for Admins pane, toggle the switch ON
4. In the Always keep devices updated pane, toggle the switch OFF
5. At the bottom of the page, on the ribbon, click Publish changes , and in the Publish changes? dialog box, click Publish changes
6. On the top right-hand side of the page, click Add model
7. Select the Jabra device model(s) to which the custom firmware policy applies, and at the bottom of the page, on the ribbon, click Continue
8. On the Manage settings page, in the Firmware pane, click the drop-down menu and select the firmware you want to use for the relevant configuration or toggle the Always use latest firmware switch
   - a. If you choose an older firmware than the one you are currently using, in the Downgrade firmware? dialog box, click Confirm
9. At the bottom of the page, on the ribbon, click Publish and click Publish again to confirm.

#### 6.1.6 Firmware recovery for personal devices

See the Recovering your Jabra personal device after a failed firmware update topic.