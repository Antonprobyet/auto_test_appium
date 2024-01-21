from appium.options.common.base import AppiumOptions

android_get_desired_capabilities = AppiumOptions()
android_get_desired_capabilities.load_capabilities({
	"appium:autoGrantPermissions": True,
	"appium:automationName": "uiautomator2",
	"appium:newCommandTimeout": 500,
	"appium:noSign": True,
	"platformName": "Android",
	"appium:platformVersion": "14",
	"appium:resetKeyboard": True,
	"appium:systemPort": 8301,
	"appium:takesScreenshot": True,
	"appium:udid": "0C211FDD4003L7",
	"appium:appPackage": "com.ajaxsystems",
	"appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:connectHardwareKeyboard": True
})
