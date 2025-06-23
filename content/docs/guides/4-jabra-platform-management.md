---
title: "Jabra+ platform management"
date: 2025-06-23T14:40:19.934Z
weight: 4
---

#### Jabra+ platform management

The Jabra+ platform offers a web interface for managing Jabra personal and meeting room devices remotely. This chapter is a general reference for understanding the capabilities of Jabra+ .

This chapter is divided into platform management, personal device management and meeting room device management. You can track assets, usage, access analytics, and perform mass firmware updates. Organizations such as a business, corporation, or subsidiary -are grouped under unique names, and devices are automatically added to inventories upon software client deployment.

You can customize configurations for specific Jabra personal and meeting room device models and view key metrics on the Dashboard , including Jabra device counts and activity.

## Dashboard

The Dashboard provides an overview of the key Jabra meeting room and personal device information, including the total number of managed Jabra meeting room and personal devices in each organization, Jabra device activity, room status, firmware status, and other variables.

You can access the dashboard from the main page after logging into the platform or click the Dashboard menu on the left-hand navigation bar.

---

## Organizations

An organization is a representation of your company/business in Jabra+ with a unique organization ID. When you log in to the platform for the first time, you are prompted to create your organization, in which you take up the owner role.

### Important note

When single sign-on (SSO) is enabled, admin users cannot leave an organization, invite other admin users or modify their Jabra+ profile. Be aware that granting access or changing access rights for admin users is performed exclusively in Microsoft® Entra, instead of within the platform.

See the Roles and Permissions chapter.

---

### When SSO is disabled

When your domain is not using SSO, owners can invite other admin users (additional owners or members), and set their respective permissions i.e. edit rights or read-only access for Meeting rooms or Personal devices in the platform.

When SSO is disabled, a member can leave an organization; however, an owner can only leave an organization if they first elevate another user to the owner role.

Whether SSO is enabled or not, any owner can delete an organization altogether.

## Deleting an organization

When an owner deletes an organization, it permanently removes all Jabra device data within the platform, and all Jabra devices in the device inventory and room inventory gradually stop sending device data.

Moreover, the connection to the platform that the relevant software client initially established is severed. However, the software client remains installed on end-user computers or meeting room computers/computing devices until it is uninstalled from the devices on which it was installed.

### Important note

Be aware that when an owner deletes an organization, Jabra personal and meeting room devices continue to operate, but the remote management of those devices within the platform is terminated.

The deletion process is not instantaneous and may take up to 24 hours to complete. All associated device data, usage data, and user data are then irrevocably deleted.

### To delete an organization:

- On the bottom left-hand side of the navigation bar, click the name of the organization you currently belong to, and then click Manage my organizations
- Within the Organization pane of the organization you want to delete, click the action menu (three-dot menu) and click Delete organization
- In the Revoke active PC Clients? dialog box, confirm with Yes, continue
- In the Delete organization? dialog box, check the I confirm to delete the organization checkbox, and click Yes, delete organization

After deleting an organization, the logged-in admin user is prompted to create a new one.

## Leaving an organization as a member

When SSO is enabled, members cannot leave organizations. This can only be done through Microsoft® Entra. Otherwise, when SSO is disabled, a member can leave an organization on their own.

### To leave an organization as a member:

- The member who wants to leave the organization must log in to the platform using their email address
- On the left-hand navigation bar, click the name of the organization you belong to, and then click Manage my organizations
- Within the Organization pane (of the organization you want to leave), click the action menu and click Leave organization

---

### In the Leave organization dialog box, click Leave to confirm

At this point, the owner of the organization receives an email informing them that a member has left the organization.

## Leaving an organization as an owner

When SSO is enabled, admin users cannot leave organizations. This can only be done through Microsoft® Entra. Otherwise, an admin user holding the owner role can leave an organization on their own provided that the organization has more than one admin user with the owner role.

In this case, the owner must first upgrade an admin user from member to owner . See the Changing roles, editing permissions, or removing a user as an owner procedure.

After the owner has elevated an admin user from member to owner , the owner can leave an organization as follows:

- The owner who wants to leave the organization must log in to the platform using their email address
- On the left-hand navigation bar, click the name of the organization you belong to, and then click Admin users
- On the Admin users page, on the list, find the row with your name and click the action menu (three-dot menu)
- Click Leave organization , and in the Leave organization dialog box, click Leave

At this point, the new owner of the organization receives an email informing them that another owner has left the organization.

## Roles and permissions

### Important note

When single sign-on is enabled, you cannot perform user management tasks within the platform, including keeping activity logs, as this is exclusively done via Microsoft® Entra. For details, see the Enabling single sign-on chapter.

In Jabra+, when an admin user creates an organization, the admin user becomes the owner of that organization. Admin users of the platform are system/IT administrators for Jabra devices in their organization, and fall into the following two roles:

- Owner : Elevated admin user who manages all Jabra devices and can perform Jabra device provisioning, user management tasks such as enabling SSO, managing Roles and permissions or deleting organizations.

### Note

If SSO is not enabled, an owner role can invite users individually, revoke invitations, change roles, or terminate or remove member(s) access to their organization from within the platform.

When SSO is enabled, the owner role appears as Jabra+ Organization Owner in Microsoft® Entra.

- Member : Subordinate to owners , a member can be classified as admin user with edit or readonly rights for either Meeting rooms Personal devices , , or both. When SSO is enabled, in Microsoft® Entra, the member with edit rights role appears as Jabra+ Personal Device Editor and Jabra+ Meeting Room Editor .
- Member with Edit Rights : Can manage all Jabra meeting room and/or personal devices in the organization, depending on the permission given (meeting rooms or personal devices) and can perform Jabra device provisioning
- Member with Read-Only Rights : Can only view Jabra meeting room and personal devices and associated data, with no user or Jabra device management capabilities. When SSO is enabled, in Microsoft® Entra, the default role for any admin user is readonly.

Members cannot perform any user management tasks or change organization settings, such as disabling metadata collection. Moreover, a member with edit rights to either Meeting rooms or Personal devices has read-only access to the other.

## Roles and permissions matrix

The following matrix shows interactions that an owner or member can or cannot perform within the Jabra+ platform.

| Interactions | Owner | Member ( edit rights ) | Member ( read only ) |
|----------------|--------|------------------------|---------------------|
| • Delete an organization  • Change organization settings (Metadata collection) | Yes | No | No |
| • Invite new admin users to the organization  • Change roles from owner to member (or vice versa)  • Change permissions for members with edit rights to read-only rights (or vice versa)  • Remove admin users ( owners or members ) | Yes | No | No |
| • Leave an organization | No | Yes | Yes |
| • View history (admin user activity log) | Yes | No | No |
| • Access the Meeting rooms menu item to view Jabra meeting room devices in the room inventory and associated data e.g.: created Meeting room software clients, created configurations, etc. | Yes | Yes | Yes |
| • Name Meeting rooms  • Change Jabra meeting room device settings  • Download meeting room software clients | Yes | Yes | No |

---

### In the table above, footnotes:

1 When SSO is enabled, these actions are performed in Microsoft® Entra or not at all. Refer to the Enabling SSO procedure.

2 An owner can only leave an organization if there is another owner in the organization. Refer to the Leaving an organization as an owner procedure.

3 Provided that the Member with edit rights has been given access to Meeting room management. See the Changing roles, editing permissions or removing a user as an owner for the procedure.

4 Provided that the Member with edit rights has been given access to Personal device management. See the Changing roles, editing permissions or removing a user as an owner for details.

## Changing roles, editing permissions or removing a user

When SSO is enabled, admin users cannot change roles, edit permissions or remove admin users from within the platform. You can only do this through Microsoft® Entra. For details, see the Enabling single sign-on chapter.

Otherwise, if SSO is not enabled, the owner of an organization can perform user management tasks within their organization. For example, an owner can change the role of a member , effectively making the member also an owner of the organization. An owner can also change their own role from owner to member , or downgrade other owner(s) to member(s) , provided that the organization has at least one owner .

Moreover, an owner can edit the permissions of a member to fine tune the access rights of the Member to either manage Jabra meeting room devices, personal devices or both.

In addition, all admin users are notified via email of any role changes or changes in permission scope. An owner can also remove or terminate access to their organization for a member .

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000023_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

### To change roles, edit permissions:

- On the left-hand navigation bar, click the name of the organization you are currently the owner of, and then click Admin users
- On the Admin users page, on the list, find the user that you want to manage access rights for or to remove, click the action menu (three-dot menu) and click Edit permissions
- a. To change the role of a member to owner or vice-versa, in the Role pane, click the relevant radio button for Member or Owner , and then click Save
- b. To edit the access rights or permissions for a member , in the Permissions pane, click the relevant radio button Edit or Read only for meeting rooms/personal devices, and click Save

For changes to apply, after changing the role of a user, they must log out and back in.

### To remove a user:

- On the Admin users page, on the list, find the user that you want to terminate access for, and click the action menu (three-dot menu)
- Click Remove admin user , and in the Remove admin user dialog box, click Remove

For changes to apply, after removing a user, the removed user must log out but cannot access the platform. If the removed member was also an admin user in other organizations, the removed user maintains their membership in the other organization(s); however, the removed member can also be reinvited.

## Viewing admin user activity or history

To enhance security and accountability in Jabra+ , the platform logs admin user activity to monitor, track, and manage user activities in an organization.

In the platform, the History tab in the Admin users menu keeps a log of any changes to access rights, user invitations, and access terminations for 30 days.

### Note

When SSO is enabled, user activity is logged and kept within Microsoft® Entra.

The admin user with the owner role can view admin user activity or history on a filterable list. The list contains details such as Time Impacted Entity, Event , , and User.

### To view admin user activity:

- On the left-hand navigation bar, click the name of the organization you are currently the owner of, and then click Admin users
- On the Admin users page, click the History tab

The history of admin user activity in the organization is now visible on a list that can be sorted by Time Impacted Entity Event , , , and User .

---

### In the table above, footnotes:

1 When SSO is enabled, user activity is logged and kept within Microsoft® Entra.

## Personal device management

In the Jabra+ platform, the Personal devices menu item lets you visualize, sort, and configure Jabra personal devices to effectively manage them in an organization.

Personal devices are audio devices such as headphones, headsets and speakerphones; Personal device management addresses the challenges of remote identification, management, and troubleshooting of Jabra personal devices.

You can perform bulk management of settings and firmware, inspect real-time Jabra personal device status, remotely adjust settings on behalf of end-users, and other functionalities.

Like meeting room devices, Jabra personal devices have a virtual inventory, or device inventory . The Personal devices menu item is made up of the Device inventory for personal devices, Configurations, Device groups, and Desktop clients.

Device groups act as the foundation to assign configurations, and custom firmware policies that takes effect on specific groups of Jabra personal devices.

This grouping mechanism is designed to give you an overview of all your Jabra personal devices, and help you group or classify the devices based on real or made-up variables, such as countries, cities, building or department names, etc.

To provision personal devices, you must install Jabra+ desktop on all end-user computers. After provisioning, Jabra personal devices appear in the device inventory and you can then adjust settings remotely of a single Jabra personal device and/or to Create device groups and sort Jabra devices into Device groups.

For guidance, see the Walkthrough: Suggested configuration of Jabra+ chapter.

## Device inventory for personal devices

The device inventory is a repository for all Jabra personal devices (including speakerphones) added to an organization. It is automatically populated when the Jabra+ desktop app is deployed and installed on your end-user 's computers and end user Jabra personal devices are paired (Bluetooth Jabra devices) or recognized by the app automatically (cabled or wired Jabra devices).

In a searchable and filterable list, the device inventory outlines information such as Device model , Connection status Firmware status , , any Device group(s) it may belong to, and others. In the device inventory , the collected metadata lets you search for keywords such as Computer Name or Windows Username .

For more information about device metadata, see the Disabling Metadata collection topic in the Appendix.

In addition, you can further sort Jabra personal devices in the device inventory into device groups , effectively creating a secondary grouping in the organization.

For example, an admin user may want to group Jabra devices in the organization into different departments, such as Marketing, Human Resources, etc. You may also want to classify Jabra personal devices in device groups based on the location of Jabra devices or another useful variable.

When Jabra personal devices are added to the device inventory , a default standard configuration is applied to all Jabra personal devices in the inventory.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000025_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

### Adding Jabra personal devices to the device inventory

For procedures, see the Device Provisioning and Onboarding Guide.

### Removing Jabra personal devices from the device inventory

You can also remove Jabra personal devices from the device inventory . When you do so, you permanently remove the Jabra personal devices from device groups .

To remove a Jabra personal device from the device inventory:

- On the left-hand navigation bar, click Devices > Device inventory
- On the Device inventory table, check the checkbox next to the device you would like to remove
- In the bottom ribbon, click Remove from inventory and confirm

### Note

Ensure that after you remove Jabra personal devices from the device inventory , you must also uninstall the Jabra+ desktop app from the end-user computer(s) it was installed on.

Failure to do so means when the end-user reconnects their Jabra personal device to their computer, the Jabra personal device is automatically re-added to the device inventory.

### Adjusting settings remotely of a single Jabra personal device

The Jabra+ platform lets you remotely manage the settings of Jabra personal devices individually or in bulk.

If the Jabra personal device has an admin user-created configuration assigned to it, you cannot change the settings of a single Jabra personal device. To adjust the settings on a single device, the admin user can do so via the device inventory .

To adjust the settings of many Jabra devices at the same time, it is recommended to use configurations and choose a suitable approach. Be aware that when adjusting individual settings, the Jabra personal device must be online.

### Tip

You can also use this procedure to test the settings of a single Jabra device before mass deployment and determine whether the changes are suitable or not.

To adjust the settings of one Jabra personal device:

- On the left-hand navigation bar, click Personal devices > Device inventory
- On the table of personal devices, find the Jabra device you would like to change settings for. You can search for the specific Jabra device using filtering based on Model Connection status , , Device group Firmware Status Inactive devices , , , or Firmware Stage .
- Click the Jabra device name, for example, Jabra Evolve2 75 MS
- Click the Settings tab
- Adjust the settings of your relevant device

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000026_916cd71bb2c716679c18c63daa4bc6e99494f723392260d94089a57e20c71fff.png)

- To apply the changes and deploy them to the end-user, in the bottom ribbon, click Publish changes

For changes to take effect, ensure you restart the computer that the personal device is connected to. Changes are applied when the end-user logs in to Windows® again.

### Exporting the device inventory table or list

To see a list of your Jabra personal devices on a comma-separated values list, you can export your device inventory as a *.csv file. The list contains details such as Firmware status Computer name , , Firmware version Electronic serial number , , and others.

After exporting the *.csv file you can import it into a spreadsheet, storage database or open it as a plain-text file.

To export the list:

- In the top-right of the Device inventory page, click the action menu and then click Export to CSV . The file is then downloaded to your default Downloads folder associated with your web browser.

### Viewing Jabra personal device details

When a Jabra personal device is added to the device inventory , you can see information such as Firmware status Operating system Computer name Client version Version Policy , , , , , and others. To do this:

- On the Device inventory page, click the device name on the list to see additional Jabra personal device details, such as Jabra Evolve2 65, Jabra Evolve2 75, etc. You can search for the specific Jabra personal device using filtering based on Model Device group Firmware status, , , or Connection status .

### Customizing the device inventory table

You can customize your view of the Device inventory and display or hide columns. Be aware that Device Connection status , , and Firmware Status remain selected and cannot be hidden or be removed from the table.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000027_c35274a7d926a4fce1939862a86cd131b59c9dc007f76ccb5f95b819a0fdadce.png)

To customize the device inventory table:

- On the Device inventory page, on the top-right of the table, click the action menu and then click Customize table . In the Customize device inventory table dialog box, check or uncheck the checkboxes you would like displayed or hidden, and to save your preference, click OK .

### Device groups for personal devices

To help admin users manage and organize Jabra personal devices in the device inventory, device groups let the admin user sort the collection of Jabra personal devices into different containers or buckets.

- Primary grouping: Organization (e.g., ABC Company )
- Secondary grouping: Device groups (e.g., Marketing, Human Resources , )

In this case, you can add Jabra personal devices from the device inventory into the individual device groups that were created and named. Device groups are essential for creating configurations, enabling the deployment of specific settings to select Jabra personal devices. See the Configurations chapter for details.

### Creating a device group for personal devices

Creating a device group can be helpful when you have a large number of Jabra personal devices in your device inventory because it helps you create a container or bucket for them.

You can also create a device group to test a specific firmware version you would like to use with your Jabra devices, before you perform a mass deployment.

To create a device group:

- On the left-hand navigation bar, click Personal devices > Device groups
- On the Device groups page, click Create device group
- In the Create device group dialog box, in the Name field, enter a name for your device group, for example, Marketing department . Optionally, in the Description field, enter a description of your device group.
- Click Create

You are now taken to the Device groups page.

### Sorting personal devices into a device group

After creating and giving a name to a device group , you can sort your Jabra personal devices into device groups.

A Jabra personal device can only be associated with one device group at a time. If the Jabra device is added to a different device group, the new one replaces the previous affiliation.

To sort Jabra personal device(s) from the device inventory to a device group:

- On the left-hand navigation bar, click Personal devices > Device inventory
- On the list, check the checkbox of the relevant Jabra device(s)
- In the bottom ribbon, click Add devices to device group
- In the Add devices to device group dialog box, select a device group, and click Add devices

You have now added Jabra personal devices to a device group.

---

### Meeting room device management

In the Jabra+ platform, the Meeting rooms menu item enables you to digitally visualize, sort, and manage Jabra meeting room devices, effectively mapping physical meeting rooms used for online meetings and creating an organizational structure.

Meeting rooms address the challenges of remote identification, management, and troubleshooting of Jabra meeting room devices. You can perform bulk management of settings and firmware, inspect realtime Jabra meeting room device status, reboot Jabra meeting room devices for troubleshooting, access activity logs for each meeting room, and other functionalities.

Like personal devices, Jabra meeting room devices have a virtual inventory, called room inventory . The Meeting rooms menu item is made up of the Room inventory, Room configurations, and Room clients.

During provisioning, you can name the virtual room where the Jabra meeting room device is located, aiding identification in the room inventory before moving it to a Location. The room name can also be renamed at any time.

After provisioning and naming your Jabra meeting room devices, they appear in the room inventory as an unassigned room. You can then drag and drop these rooms into predetermined locations, which serve as a grouping mechanism, similar to device groups (for personal devices). This is designed to hierarchically group or organize Jabra meeting room devices based on real or made-up locations e.g.: countries, cities, buildings, departments, rooms, or others.

The following is an example of a tree structure within locations.

Your organization ( root of tree structure )

- United States ( Parent )

- California ( Child )

- Cupertino office ( Child )

To keep Jabra meeting room devices updated with the latest firmware while minimizing disruptions for end users, you can modify scheduled device updates according to the organization's working hours. For example, updates can be scheduled to take place at night.

Clicking on a Jabra meeting room device in the room inventory opens the Room page, displaying details such as Room Type Location Software client , , , and if applicable, Room AV system Video Service , Provider , and Meeting room computer or computing device information, among others.

### Note

The Video Service Provider pane is displayed only in rooms with PanaCast 40/50 VBS meeting room devices. Changing the video service provider between Microsoft® Teams Rooms and Zoom Rooms requires re-provisioning the affected meeting room devices.

## Room inventory for meeting room devices

The room inventory is a repository or bucket for all Jabra meeting room devices added to a specific organization in the platform, like the device inventory for personal devices.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000030_916cd71bb2c716679c18c63daa4bc6e99494f723392260d94089a57e20c71fff.png)

The room inventory enables you to set up a structure to organize your meeting rooms and Jabra devices in your business organization, showing you a real-time overview of your meeting room devices. Be aware that you can only have one room inventory per organization. All Jabra meeting room devices connected to the Meeting room software client created by the same organization appear in the room inventory.

Through the room inventory , you can remove individual meeting room devices, or you can delete the entire room, removing any Jabra meeting room device within it.

### Note

There are different procedures to remove Jabra meeting room devices from the room inventory . See the Deleting a room or removing a meeting room device from a room topic for procedures.

In a searchable and filterable list -the inventory outlines information such as Room Room Status , , Location Devices Seat Count Configuration , , , , and Firmware Status , all in real time.

In the room inventory , Jabra meeting room devices are first automatically sorted into rooms (a primary grouping), and rooms can be further sorted into locations , enabling you to create a secondary grouping for your rooms. For example, you can group rooms into different regions, countries, offices, and others, effectively building a hierarchical structure based on geography.

When Jabra meeting room devices are added to the room inventory -and to mass manage meeting room devices with a shared firmware policy and settings -a default standard room configuration is applied across the board to all Jabra meeting room devices in the room inventory .

See standard room configuration for further details.

## Adding Jabra meeting room devices to the room inventory

For procedures, see the Device Provisioning and Onboarding Guide.

## Moving a room into a location

To perform this procedure, you must first have created one or more locations in your room inventory . See the Moving rooms into locations and adding room details topic.

## Adjusting settings remotely of a single Jabra meeting room device

The Jabra+ platform lets you remotely manage the settings of Jabra meeting room devices individually or in bulk. You can only change the settings of a single Jabra meeting room device, when you have not assigned a newly created configuration to the room that includes the specific Jabra meeting room device. You can, however, adjust the settings on a single device via the room inventory .

Moreover, it is recommended that you Create a Room Configuration to adjust the settings of many Jabra meeting room devices simultaneously. When adjusting individual settings, the Jabra meeting room device must be connected and online.

### Tip

You can also use this procedure to test the settings of a single Jabra meeting room device and determine whether the changes are suitable prior to mass deployment.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000031_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

To adjust the settings of one Jabra meeting room device:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory page, in your locations tree structure, click the name of your organization
- On the Room inventory table, click the room name where your Jabra meeting room device is located
- On the Room details page, click the relevant Jabra meeting room device pane
- On the Device details page, click the Settings tab and make the necessary changes to settings
- To apply the changes and deploy them to the end-user, in the bottom ribbon, click Publish changes

After you click Publish changes , the setting changes are published or applied, and Jabra meeting room devices may automatically reboot.

## Renaming a room

After provisioning a Jabra meeting room device, an admin user with the relevant permissions can rename the room.

### To rename a room:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory table, click the relevant room name
- On the Room page, on the top right-hand side of the page, click the action menu (three-dot menu) and click Edit room
- Rename the room as desired and click Save changes to confirm

## Deleting a room or removing a meeting room device from a room

In the Jabra+ platform, an owner or member with edit rights (for meeting rooms) can delete rooms from the room inventory as well as remove a Jabra meeting room device from within a room.

Be aware that when you remove a room from the room inventory, you delete all Jabra meeting room devices within the room.

Depending on the Jabra meeting room device -and to permanently delete the room -you must ensure that after deleting a room or meeting room device from the room inventory, that you also delete the software client from the meeting room computer it was installed on.

Failure to do so means when the meeting room computer is restarted, the Jabra meeting room device is automatically re-added to the room inventory as an unassigned room .

In the room inventory, when you remove a single meeting room device from the room (i.e.: the structure created when the meeting room device was added to the platform) the room itself remains empty within the room inventory, ready to have a meeting room device provisioned to the inventory.

### Note

An exception applies in the case of the PanaCast 50 BYOD, whereby if you delete the meeting room device from the room inventory , you also delete the associated room.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000032_916cd71bb2c716679c18c63daa4bc6e99494f723392260d94089a57e20c71fff.png)

To remove a Jabra meeting room device from the room inventory, you must first ensure the Device status appears as Offline before removing it.

To do this, ensure that you unplug the Jabra meeting room device from the power outlet and wait a few minutes for the Device status to appear Offline . You can then perform the following procedure:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory table, click the relevant room name
- On the Room page, click the action menu (three-dot menu) in the meeting room or personal device you want to remove and click Remove device
- To remove the room entirely, including all the Jabra devices within the room, on the top right-hand side of the page, click the action menu (three-dot menu) and click Delete room .

### Important note

To permanently delete a room or Jabra meeting room device from a room, ensure that after you delete the meeting room device, you also delete the meeting room software clients whenever possible.

Depending on the Jabra meeting room device, the client removal must be performed differently, and as follows:

- PanaCast 50 BYOD : After the meeting room device has been deleted from a room, or a room has been deleted, the PanaCast 50 BYOD is removed. To re-add the meeting room device to the platform, you must re-provision it.
- PanaCast 50 RS : After the meeting room device has been deleted from a room or a room has been deleted, you must switch the PanaCast 50 RS OFF , and the USB cable must be unplugged. To re-add the meeting room device to the platform, you must reinstall the meeting room software client.
- PanaCast 40/50 VBS : After the meeting room device has been deleted from a room or a room has been deleted, the PanaCast 40/50 VBS is removed. To re-add the meeting room device to the platform, you must factory reset it and then re-provision the meeting room device.

Failure to remove the clients can result in the Jabra meeting room device being detected by the platform again and reappearing in the room inventory .

## Activity logs -Device details and meeting room activity

Activity logs consist of device details and meeting room activities, allowing you to view information about Jabra meeting room devices and events in physical rooms.

From the room inventory , clicking a room name shows a timeline of activities related to that room and its associated meeting room devices. The Activity tab on each device's Room page lists events such as reboots, status changes, firmware updates, and errors.

Logs maintain a record of activities for the past 30 days, displayed in a searchable and filterable format, including Events in the room and their triggers (e.g., configuration changes or device additions/removals).

The Activity tab also shows the exact time of events, and the serial number of the device involved. For example, if an admin user renames a room, this action is logged.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000033_7638b45f5b0abde5776608dbd76f114f314b172bba94fe5f12e0fa5682fc3802.png)

### Viewing additional Details and Activity

aid troubleshooting by helping you identify the origin of issues, track actions, and resolve problems, such as rebooting the Jabra meeting room device.

## Viewing Jabra meeting room device details

When a Jabra meeting room device is added to the room inventory , you can see information such as Room name and Status Location Devices Seat Count Configuration , , , , , and Firmware Status .

You can also find additional details of your Jabra meeting room device by drilling down into the Device page.

On the Room page, the Room Details tab displays Room Information Room Configuration Room , , AV system / Meeting room computer Date and Time , for scheduled device updates, and more.

The Device Details page shows you more granular information specific to the Jabra meeting room device, which includes Installed Firmware (version), Firmware policy , when the device was Last Seen as Connected (online), and more.

To view additional Room or Device details:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory page, in your Locations tree structure, click the name of your organization
- On the Meeting room inventory table, click the relevant room name
- On the Room page, click the Details tab to see more information about the room
- To see more information about the Jabra meeting room device in the room, click the relevant pane on the Room page showing the Jabra meeting room device.

### Viewing room activity

In addition to Room Details and Device Details , the Activity tab is a source of information that helps you track events and their triggers in a room.

The Activity tab captures events that occurred in a room, e.g.: Firmware status reboot change of , , settings of a meeting room device, and others.

To view activity in a room:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory page, in your Locations tree structure, click the name of your organization
- On the Meeting room inventory table, click the relevant room name
- On the Room page, find and click the Activity tab

The activity log in a room (and the meeting room devices within) is now visible on a list that can be sorted by Time Impacted Entity Event , , , and User .

---

### In the table above, footnotes:

1 When SSO is enabled, user activity is logged and kept within Microsoft® Entra.

## Locations

Locations are a secondary grouping, designed as a hierarchical tree structure to sort and organize your organization´s virtual meeting rooms and meeting room devices. It is located within the Room inventory menu item.

It is suggested that you use locations as a geographical representation of your organization.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000034_88706fa68aa11d6c2936f18a49d13905e392951e1e5f3da7df0f2a3b9642e346.png)

If you have created a location-based hierarchy, be aware that you can drill down several levels in the hierarchical structure. A location consists of a name and a placement in the hierarchy that you choose. The following example illustrates an organization with a simple hierarchical structure:

- Your organization: ABC Company
- Secondary grouping: (location) United States
- Tertiary grouping: (location) California
- Additional grouping: (location) Cupertino office rooms

However, your organization may be simpler and not need many locations. For example, it could instead be divided as follows:

- Organization: ABC Company
- Secondary grouping (location): Cupertino office rooms

In both examples, your Jabra meeting room device appears as a room in the Cupertino office rooms location and all parent groupings, where Cupertino office rooms are grouped under.

### Adding, renaming, or deleting a location

You can also add, rename, or delete a location in the room inventory . Like a parent-child hierarchy, when you add a location starting from the top of the tree structure you can create as many locations as the organization may need.

Moreover, when you create more locations within the nested groups you can have up to six levels of hierarchy. You can also rename or delete a location.

### Adding a location :

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) and then click Add location
- In the Add location dialog box, in the Location name field, enter the name of the new location, and click Create . The new location appears beneath the location that you chose to group it under.

### Renaming a location :

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) of the relevant location you would like to rename, and then click Rename
- In the Rename location dialog box, in the Name field, enter the new location name
- Click Save . The location has now been renamed.

### Deleting a location :

Be aware that when you delete a location you also delete all the children locations beneath.

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the left-hand side of the screen, on the locations tree structure, click the action menu (three-dot menu) of the relevant location you would like to delete, and then click Delete
- In the dialog box that appears, click Delete to confirm. The location is now deleted.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000035_a8f92aec2efd322e45f0afef961018989d1452a564a5967dd621511816fd5ae2.png)

### Moving rooms into locations and adding room details

After provisioning meeting room devices, an unassigned room is created in the locations tree structure, within the room inventory . You can move the unassigned room into a predetermined location that you may have created in the tree structure.

Moreover, when you move a room into a location, an Add details dialog box appears, letting you add room information such as Room name Seat Count Description , , , and others.

### Tip

The following procedure is also helpful when you have already provisioned several Jabra meeting room devices into the platform as unassigned rooms , and you would also like to bulk assign a configuration that you have previously created or change the room name.

### To do this:

- On the left-hand navigation bar, click Meeting rooms > Room inventory
- On the Meeting room inventory page, and if you have already created a locations structure, click unassigned room
- On the list of unassigned rooms, drag and drop the room into the desired location in the hierarchical structure
- In the Add details dialog box, if necessary, enter the relevant information in the provided fields, and then click Save

### Scheduling firmware updates for meeting room devices

See the Scheduled device updates topic in the firmware management chapter.

![Image](Jabra+ platform - An Administrator´s Guide_artifacts\image_000036_916cd71bb2c716679c18c63daa4bc6e99494f723392260d94089a57e20c71fff.png)