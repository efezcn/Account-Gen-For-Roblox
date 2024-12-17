config = {
    "FunCaptchaSolvers": {
        "//capbypass_link": "https://capbypass.com/",
        "capbypass": "your_api_key_here",
    },
    "CookieChecker": {
        "delete_invalid_cookies": False,
        "use_proxy": True,
        "check_premium": False,
        "max_workers": None
    },
    "CookieGenerator": {
        "vanity": None,
        "custom_password": None,
        "max_generations": 1000,
        "captcha_solver": "capbypass",
        "use_proxy": True,
        "max_workers": 50
    },
    "CookieRefresher": {
        "use_proxy": True,
        "max_workers": None
    },
    "CookieRegionUnlocker": {
        "use_proxy": True,
        "max_workers": None
    },
    "CookieVerifier": {
        "use_proxy": True,
        "max_workers": None
    }
}
