---
title: "Firmware management"
date: 2025-06-23T14:40:21.245Z
weight: 6
---

#### 6 Firmware management

You can remotely manage firmware and policies for Jabra personal and meeting room devices via the platform.

- - For Jabra personal devices : Firmware updates are performed through the Jabra+ desktop app. Admin users can select specific firmware versions for device models, applying them across inventories or device groups, as well as in exceptional cases downgrading firmware. If a firmware update fails, a recovery process is available for wired devices via the app. End-users receive prompts to update firmware based on organizational policies or can postpone them.
- - For Jabra meeting room devices : Firmware is managed directly on the platform, allowing updates or downgrades per organizational policies. Updates are pushed directly to the meeting room devices and follow a schedule update plan. Without a defined schedule, updates may interrupt meetings, as devices must reboot.

## Important note

Jabra may cease support for certain firmware versions due to compatibility issues, security vulnerabilities, or regulatory changes. When a previously selected firmware version becomes unsupported, the affected Jabra devices continue to operate normally. However, subsequent Jabra devices added to the respective inventories keep their existing firmware and cannot update to the unsupported version.

When a specific firmware is no longer supported by Jabra, in the device inventory or room inventory an exclamation mark (!) indicates the affected Jabra devices. Additionally, a Configuration warning appears in the affected configuration or room configuration. For details, see the Troubleshooting section.

The end-user may continue to use the Jabra device with the unsupported firmware; however, the Jabra device´s settings can no longer be changed, and it is therefore not recommended.

To resolve this, an admin user in the platform with the relevant permissions must edit the configuration to either select a different firmware version or switch the toggle to Always use latest ON , automatically updating the Jabra device to the latest firmware.

To select a different firmware version, see the procedure Modifying &amp; setting the firmware policy for specific Jabra device models. If you have configurations assigned to a specific room or Jabra personal devices in a device group, see the Modifying &amp; setting an existing firmware policy for a specific Room or device group procedure.

## Firmware policy &amp; updates

The firmware policy -contained within Configurations -enables you to manage firmware for Jabra devices in the Jabra+ platform, giving end-users access to the latest updates and features for their Jabra device.

## Note

Certain older Jabra devices' firmware cannot be updated via Jabra+ . Instead, they must be updated using Jabra Direct or Jabra Xpress .

You can still use the older Jabra devices in Jabra+ and change settings, however, depending on the firmware version you are running, the list of settings that you can modify in Jabra+ can change.

To find out whether your device can be firmware updated or not, see the list of supported Jabra devices.

Governed by a firmware policy, you can control and enforce firmware deployment of the latest firmware updates on all Jabra devices (in their organization) or set exceptions for specific Jabra device models, for example, preventing updates to all Jabra Evolve2 75 personal devices or restricting all PanaCast 50 to use a particular firmware version.

The default firmware policy is part of the standard configuration or standard room configuration as well as any created configuration . The default firmware policy applies in both cases, however, the default works differently for Jabra meeting room and for personal devices.

Modifying the default firmware policy effectively creates a custom policy, but these cannot be named as they are contained within configurations.

Therefore, to have different firmware policies for various Jabra device models, an admin user must first create a configuration or create a room configuration and then modify the firmware policy accordingly.

For both Jabra meeting room and personal devices, a firmware policy consists of the following toggle switches:

- - Update devices using Jabra+ for Admins : primary toggle switch that enables or disables Jabra device firmware management in the platform
- - Always keep devices updated : secondary toggle switch that updates all Jabra devices to the latest firmware version when available

## Note

The default firmware policy acts differently according to the type of Jabra device, and as follows:

- - Personal devices : the default setting for both toggle switches is ON , which means firmware is managed automatically, and end-users are notified of updates. However, you can disable the

- - firmware policy, preventing updates and keeping the currently installed firmware version.

- - Meeting room devices : the default setting for the firmware management toggle is OFF , meaning firmware is not managed through the platform. Consequently, updates are not automatically applied.

## Note

When you enable firmware updates in the Jabra+ platform, you must disable firmware updates from other platforms, such as Windows ® Update .

This means whenever a Jabra Meeting room device is added to the room inventory , you can manage the firmware exclusively within the Jabra+ platform.

You can modify &amp; set the firmware policy for specific Jabra device models in the standard configuration for all personal devices in the device inventory . You can also set a specific firmware version for a Jabra meeting room device model in the standard room configuration that is automatically assigned to all your meeting room devices in the room inventory .

Moreover, in any created configuration that was saved and assigned to specific device groups , as well as any created room configuration that was saved and assigned to specific rooms, you can modify &amp; set an existing firmware policy for a specific room or device group . You can also restrict the Always use latest firmware feature only to a specific Jabra device model.

Both inventories show Firmware status for all rooms and personal devices. See the Firmware Statuses topic for guidance.

## Firmware Statuses

In the platform, the status of the firmware updates is located within the device inventory or room inventory and the statuses are different depending on personal or meeting room devices.

| Shown in Device or Room inventories | Description |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Postponed update | The firmware update installation of the Jabra device has been delayed or postponed to a later time or date by the end-user. |
| Failed update | The firmware update installation of the Jabra device has failed on the end-user computer. The end-user can recover the Jabra device and retry the firmware update. Depending on the error code, the failed update can retry the update on its own. |
| Pending update | Waiting for the end-user to perform the firmware update. Can also occur if Jabra device is offline. |
| Latest installed | The installed firmware version being the most recent release which includes the latest improvements, features and bug fixes. This message is also displayed when firmware management is disabled. |
| Update available | A new firmware version is available but has not yet been configured by you, the admin user. |

## Note

On the end-user side, they are notified of an update to their Jabra device in the Jabra+ desktop app.

Can also be shown when the Update devices using Jabra+ for Admins Toggle is switched OFF

## Scheduled device updates

Specific date and time set in the Jabra+ platform when the update takes place.

See the Scheduled device updates topic.

## Note

Currently, for meeting room devices, firmware management is turned OFF by default. To switch it ON , see the Enabling or disabling firmware management for Jabra meeting room and personal devices topic.

This default schedule cascades to all locations and follows the local time zone of the Jabra meeting room device. You can use the default schedule or set a custom weekly schedule for the entire organization.

## Note

For Jabra meeting room devices to follow the schedule, they must have a time zone that was set during provisioning.

- - PanaCast 50 BYOD or PanaCast 40/50 VBS : If the time zone was incorrectly set or the meeting room device was moved to a location with a different time zone, you must reprovision the device(s)
- - PanaCast 50 RS : To set the correct time zone an admin user must change the Windows® settings for the time zone on the meeting room computer/ThinkSmart ™ Core, included in the bundle

Firmware updates take place when following your organization's firmware policy, which governs whether you can update the firmware of Jabra meeting room devices and keep them regularly updated to the latest firmware version.

Unless you have a defined schedule for when updates can be installed, end-users may be interrupted during their online meetings. This is due to meeting room devices having to reboot to have the updates applied.

Therefore, updating the firmware of meeting room devices only occurs during the time previously set in the maintenance schedule. If you experience any issues while updating your firmware, see the Troubleshooting section.

## Custom schedule for device updates

Defining and setting a custom schedule for device updates ensures you that Jabra meeting room device downtime in your entire organization only occurs during non-office hours.

This is based on the local time zone of where the device is physically located, therefore minimizing potential interruptions for end-users.

## Note

Be aware that the custom schedule that you defined and set, overwrites the default schedule for all Jabra meeting room device updates in the organization.

## To do this:

- - On the left-hand navigation bar, click Meeting rooms &gt; Room inventory
- - On the left-hand Locations bar, at the top of the list, click the action menu (three-dot menu) next to the name of the organization, and click Scheduled device updates
- - In the Scheduled device updates dialog box, on the Select time range drop-down menu, choose a timeframe
- - In the Scheduled device updates dialog box, in the Repeats on section, check or click to select at least one weekday, for example, M for Monday, S for Saturday, etc.
- - To uncheck, click on the first letter of the weekday, for example, F for Friday
- - To save click Apply

## Viewing the schedule for meeting room device updates

All Jabra meeting room devices in your organization follow an automated schedule that recurs on a weekly basis, on specific days in a specific one-hour timeframe. In the Jabra+ platform, you can view the schedule for updates that apply to your entire organization.

To view the schedule for device updates in the room:

- - On the left-hand navigation bar, click Meeting rooms &gt; Room inventory
- - On the Meeting room inventory page, to view the schedule for device updates, on the list of rooms, click the relevant room name
- - On the Room page, on the Details tab, on the Date and time pane, you can see the Scheduled Device Updates timeframe

## Modifying &amp; setting the firmware policy for specific Jabra device models

You can edit the standard configuration and set exceptions for managing firmware for specific Jabra meeting room and personal device models that apply to all Jabra meeting room devices in the room inventory and device inventory .

You can also choose a specific firmware version for a Jabra device model variant, with an exception that applies to all Jabra meeting room and personal devices of the model variants specified.

For example, there may be an organization where you would like to apply a specific firmware version to a model range of e.g. Jabra Evolve2 75 personal devices. With this approach, all Jabra Evolve2 75 personal devices in the organization would have the (exception) setting, in this case, a specific firmware version applied automatically.

## Note

Be aware that a firmware version may become unsupported by Jabra. See the firmware management topic for details.

## For Meeting room devices

To modify &amp; set an existing firmware policy for a specific Jabra meeting room device model in a room, you must follow the procedure and then assign the firmware policy to a room.

## Note

If you would like to use a specific firmware version with your PanaCast 40/50 VBS, be aware that there is an exception. See the Firmware bundles and specific firmware versions topic.

- - On the left-hand navigation bar, click Meeting rooms &gt; Room configurations
- - Click the pane with the configuration that you previously created where you would like to set a custom firmware policy
- - In the Firmware Policy tab, in the Update devices using Jabra+ for Admins pane, toggle the switch ON and in the Always keep devices updated pane, toggle the switch OFF
- - Click Publish changes , and in the Publish changes? dialog box, click Publish changes
- - On the top right-hand side of the page, click Add model and select the Jabra device model(s), for example, PanaCast 50 , to which the custom firmware policy applies
- - Click Continue
- - On the Manage settings page, in the Firmware pane, select a specific firmware version or switch ON the toggle Always use latest firmware for a specific Jabra device model in the relevant configuration
- - If you choose an older firmware than the one you are currently using, in the Downgrade firmware? dialog box, click Confirm
- - If instead you toggled the Always use latest firmware switch, at the bottom of the page, on the ribbon, click Publish and click Publish again to confirm.

At this point, for the custom firmware policy to take effect, perform the assigning a created configuration to a device group or a room procedure.

## For personal devices

To modify &amp; set an existing firmware policy for a specific Jabra personal device model in a device group:

- - On the left-hand navigation bar, click Personal devices &gt; Configurations
- - Click the pane with the relevant configuration where you would like to set a custom firmware policy
- - In the Firmware Policy tab, in the Update devices using Jabra+ for Admins pane, toggle the switch ON
- - In the Always keep devices updated pane, toggle the switch OFF
- - At the bottom of the page, on the ribbon, click Publish changes , and in the Publish changes? dialog box, click Publish changes
- - On the top right-hand side of the page, click Add model
- - Select the Jabra device model(s) to which the custom firmware policy applies, and at the bottom of the page, on the ribbon, click Continue
- - On the Manage settings page, in the Firmware pane, click the drop-down menu and select the firmware you want to use for the relevant configuration or toggle the Always use latest firmware switch
- - If you choose an older firmware than the one you are currently using, in the Downgrade firmware? dialog box, click Confirm
- - At the bottom of the page, on the ribbon, click Publish and click Publish again to confirm.

Next, ensure you assign a firmware policy to a device group that you have previously created; otherwise, your firmware policy is not applied.

For the custom firmware policy to take effect, perform the assigning a created configuration to a device group or a room procedure.

## Firmware recovery for personal devices

See the Recovering your Jabra personal device after a failed firmware update topic.