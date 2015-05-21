Channel removal hook
====================

This hook removes all the channel stuff from the libvirt xml together with it's serial controller

Install as a before_vm_start hook. Configure ovirt for channel_remove:

engine-config -s "UserDefinedVMProperties=channel_remove=(true|false)"


License
=======

All code contained here is under GPLv2.
