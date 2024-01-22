from appium.options.common.base import AppiumOptions
import subprocess

def get_device_udid():
    udid = subprocess.check_output(["adb", "devices"]).decode("utf-8").split("\n")[1].split("\t")[0].strip()
    return udid

def android_get_desired_capabilities():
    android_capabilities = AppiumOptions()
    android_capabilities.load_capabilities({
        "appium:autoGrantPermissions": True,
        "appium:automationName": "uiautomator2",
        "appium:newCommandTimeout": 500,
        "appium:noSign": True,
        "platformName": "Android",
        "appium:platformVersion": "14",
        "appium:resetKeyboard": True,
        "appium:systemPort": 8301,
        "appium:takesScreenshot": True,
        "appium:udid": get_device_udid(),
        "appium:appPackage": "com.ajaxsystems",
        "appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:connectHardwareKeyboard": True
    })
    return android_capabilities
