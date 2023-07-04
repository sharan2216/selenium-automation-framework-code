import pytest

# @pytest.fixture(scope="session",autouse=True)---session scope will run the setup file ones# autouse=True----means no need to mention the setup function name as the arguments in any of the test cases..it will automatically will picup the setup n teardown methods
# then all theTestcases then teardown tescase--

# @pytest.fixture(scope="function",autouse=True)---function scope will run the setup file
# then the Testcases then teardown again it will repeat for next Test case.--
def tc_setUp():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("LogOff")
    print("Close Browse")

# <<<<<<< HEAD
    
# pytest --browser %browser% --url %url% --html=reportjenkins.html
# =======
# some lines added---
# >>>>>>> f669a945ffa90144a468b1eca1f0fbc8c51a399c
