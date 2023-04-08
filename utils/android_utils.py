import subprocess

CMD_ADB_DEVICES = "adb devices"
ADB_PLATFORM_VERSION_CMD = 'adb -s {} shell getprop ro.build.version.release'
APP_PACKAGE = 'com.ajaxsystems'
APP_ACTIVITY = 'com.ajaxsystems.ui.activity.LauncherActivity'


def get_udid() -> str:
    """Returns the UDID of the first active Android device connected via ADB."""
    with subprocess.Popen(CMD_ADB_DEVICES, stdout=subprocess.PIPE, shell=True) as proc:
        next(proc.stdout)
        device = next(proc.stdout).decode().strip()
        if device:
            return device.split()[0]
        else:
            raise Exception("No active devices")


def get_platform_version(udid: str) -> str:
    """Returns the Android platform version of the device with the given UDID."""
    with subprocess.Popen(ADB_PLATFORM_VERSION_CMD.format(udid), stdout=subprocess.PIPE,
                          shell=True) as proc:
        return proc.communicate()[0].decode().strip()


def android_get_desired_capabilities() -> dict:
    """Returns the desired capabilities for Appium to automate an Android app."""
    udid = get_udid()
    platform_version = get_platform_version(udid)
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': platform_version,
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': udid,
        'appPackage': APP_PACKAGE,
        'appActivity': APP_ACTIVITY,
    }
